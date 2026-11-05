import streamlit as st
import requests
import uuid
from supabase import create_client

st.set_page_config(page_title="K&K Market - Mama Oloja", page_icon="🛍️", layout="centered")

# --- CONNECT ---
try:
    supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
    PAYSTACK_SECRET = st.secrets["PAYSTACK_SECRET_KEY"]
except Exception as e:
    st.warning("Add SUPABASE_URL, SUPABASE_KEY and PAYSTACK_SECRET_KEY in Streamlit Secrets.")
    supabase = None
    PAYSTACK_SECRET = None

def init_paystack(email, amount_naira, ref):
    url = "https://api.paystack.co/transaction/initialize"
    headers = {"Authorization": f"Bearer {PAYSTACK_SECRET}", "Content-Type": "application/json"}
    data = {
        "email": email,
        "amount": int(amount_naira * 100), # Paystack uses kobo
        "reference": ref,
        "callback_url": "https://row-economy-market.streamlit.app",
        "metadata": {"app": "K&K Market", "product": "Seller Listing 30 days"}
    }
    r = requests.post(url, json=data, headers=headers, timeout=20)
    return r.json()

def verify_paystack(ref):
    url = f"https://api.paystack.co/transaction/verify/{ref}"
    headers = {"Authorization": f"Bearer {PAYSTACK_SECRET}"}
    r = requests.get(url, headers=headers, timeout=20)
    return r.json()

# --- CHECK IF USER RETURNED FROM PAYSTACK ---
query = st.query_params
if "reference" in query:
    ref = query["reference"]
    with st.spinner("Verifying your ₦200 payment with Paystack..."):
        v = verify_paystack(ref)
        if v.get("data", {}).get("status") == "success":
            st.success("Payment verified! ✅ Your listing is now LIVE.")
            # Mark seller as paid in Supabase
            if supabase:
                try:
                    supabase.table("sellers").update({"paid": True, "status": "live"}).eq("payment_ref", ref).execute()
                except: pass
            st.query_params.clear()
        else:
            st.error("Payment not verified yet. Please try again or contact K&K Market.")

st.markdown("<h1 style='text-align:center;color:#0BA360'>K&K Market</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Powered by <b>Mama Oloja</b> - She Knows All Prices</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🏠 Home", "💬 Chat Rooms", "🛍️ Sell - ₦200"])

with tab1:
    st.subheader("Ask Mama Oloja - What are you looking for today?")
    q = st.text_input("Ask Mama Oloja", placeholder="e.g. I need perfume under 15000, or Car AC in Osun")
    if q:
        ql = q.lower()
        if "perfume" in ql:
            st.success("Mama Oloja: For perfume, tell me your budget - under ₦15,000 or above? Sweet or strong fragrance? I will find the best seller for you.")
        elif "ac" in ql or "car" in ql:
            st.success("Mama Oloja: For Car AC, go to Horlance Auto Cooling Ltd - Verified Seller in Osun & Oyo. WhatsApp 09046044472. Tell them Mama Oloja sent you.")
        elif "ticket" in ql:
            st.success("Mama Oloja: For tickets, I will verify the seller before you pay. Never pay without verification. Which event?")
        else:
            st.success(f"Mama Oloja: Good choice my dear. I am searching the market for '{q}'. Tell me your budget and location and I will recommend the best seller.")

    st.divider()
    st.subheader("Featured Listing - Verified ✅")
    st.markdown("### Horlance Auto Cooling Ltd")
    st.write("🔧 Car AC Repair")
    st.write("📍 Osun & Oyo State")
    st.write("📞 WhatsApp: 09046044472")
    st.write("Slot 1 of 10 - First Verified Seller")
    st.link_button("💬 Chat on WhatsApp", "https://wa.me/2349046044472?text=Hello%20Horlance%2C%20Mama%20Oloja%20sent%20me%20from%20K%26K%20Market")

    st.divider()
    st.subheader("All Sellers in Market")
    if supabase:
        try:
            res = supabase.table("sellers").select("*").order("created_at", desc=True).execute()
            live = [s for s in (res.data or []) if s.get("status") in ["live", "pending"] or s.get("paid") or True]
            # Show all for launch, paid badge if paid
            if live:
                for s in live:
                    badge = "✅ PAID & LIVE" if s.get("paid") else "🆓 FREE SLOT"
                    with st.container(border=True):
                        st.write(f"**{s.get('name')}** - {s.get('product')} - ₦{s.get('price')} - {badge}")
                        st.write(s.get('description',''))
                        st.write(f"WhatsApp: {s.get('phone')}")
            else:
                st.info("No sellers yet. Be Seller #2 - Go to Sell tab.")
        except Exception as e:
            st.error(f"Could not load sellers: {e}")

with tab2:
    st.subheader("Market Square - Chat Rooms")
    room = st.selectbox("Choose Room", ["General Chat - Abuja / Osun / Lagos", "Marketplace Talk", "Car Talk", "Perfume Talk", "Tickets & Events"])
    username = st.text_input("Your username", placeholder="@YourName", key="chat_user")
    msg = st.text_input("Type your message", key="chat_msg")
    if st.button("Send Message"):
        if supabase and username and msg:
            supabase.table("chat_messages").insert({"room": room, "username": username, "message": msg}).execute()
            st.rerun()
        else:
            st.warning("Enter username and message")
    if supabase:
        try:
            chats = supabase.table("chat_messages").select("*").eq("room", room).order("created_at", desc=True).limit(30).execute()
            for c in reversed(chats.data or []):
                st.write(f"**{c['username']}**: {c['message']}")
        except:
            st.info("Mama Oloja: Welcome my dear, please be kind. Do not share phone numbers in public chat.")

with tab3:
    st.subheader("Sell On K&K Market - ₦200 / 30 Days")
    # Count sellers to know if free slots remain
    seller_count = 1 # Horlance
    if supabase:
        try:
            cnt = supabase.table("sellers").select("id", count="exact").execute()
            seller_count = (cnt.count or 0) + 1 # +1 for Horlance
        except: pass

    free_left = max(0, 10 - seller_count)
    if free_left > 0:
        st.info(f"🎉 FREE SLOTS LEFT: {free_left} of 10. After that, ₦200 per product for 30 days.")
    else:
        st.warning("Free slots finished. Listing fee is ₦200 for 30 days via Paystack.")

    with st.form("sell_form"):
        name = st.text_input("Name / Business Name")
        product = st.text_input("Product e.g. Perfume, Clothes, Car AC Service")
        price = st.number_input("Price (₦)", min_value=0)
        phone = st.text_input("WhatsApp Number e.g. 090...")
        email = st.text_input("Email for Paystack receipt (required for payment)")
        desc = st.text_area("Describe your product")
        submit = st.form_submit_button("Continue")

    if submit:
        if not name or not product or not email:
            st.error("Please enter Name, Product and Email.")
        else:
            if free_left > 0:
                # FREE - Save directly
                if supabase:
                    supabase.table("sellers").insert({"name": name, "product": product, "price": int(price), "phone": phone, "email": email, "description": desc, "paid": False, "status": "live"}).execute()
                    st.success(f"Thank you {name}! Your FREE listing for {product} is LIVE. Mama Oloja will review it.")
                    st.balloons()
            else:
                # PAID - Create Paystack payment
                ref = f"KK-{uuid.uuid4().hex[:8].upper()}"
                # Save as pending first
                if supabase:
                    supabase.table("sellers").insert({"name": name, "product": product, "price": int(price), "phone": phone, "email": email, "description": desc, "paid": False, "status": "pending", "payment_ref": ref}).execute()
                if PAYSTACK_SECRET:
                    res = init_paystack(email, 200, ref)
                    if res.get("status"):
                        pay_url = res["data"]["authorization_url"]
                        st.success(f"Listing saved as pending. Pay ₦200 to activate it. Reference: {ref}")
                        st.link_button("💳 Pay ₦200 Now With Paystack", pay_url)
                        st.write("After payment, you will return here and your listing will go live automatically.")
                    else:
                        st.error(f"Paystack error: {res.get('message')}")
                else:
                    st.error("PAYSTACK_SECRET_KEY not found in Secrets.")

    st.divider()
    st.write("**Already paid?** Enter your Paystack reference to verify:")
    ref_check = st.text_input("Payment Reference e.g. KK-AB12CD34", key="ref_check")
    if st.button("Verify My Payment"):
        if ref_check:
            v = verify_paystack(ref_check)
            if v.get("data", {}).get("status") == "success":
                if supabase:
                    supabase.table("sellers").update({"paid": True, "status": "live"}).eq("payment_ref", ref_check).execute()
                st.success("Payment verified! Your listing is LIVE ✅")
            else:
                st.error("Payment not found or not successful yet.")
