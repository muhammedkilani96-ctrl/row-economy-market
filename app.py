import streamlit as st
import pandas as pd
import uuid, qrcode, io, datetime

st.set_page_config(page_title="Ilorin Game Fiesta 4.0", page_icon="🎲", layout="wide")

# --- CONFIG ---
EVENT_NAME = "ILORIN GAME FIESTA 4.0 - The Legacy Continues"
EVENT_DATE = "Sunday, 15th Nov, 2026 - 2PM"
VENUE = "Succoth Valley Garden, GRA, Ilorin, Kwara State"
CONTACT = "+234 703 364 2277"
INSTAGRAM = "@ilorin_game_fiesta"
ORGANIZER = "KK_EVENTS"

TICKETS = {
    "Early Bird - ₦1,500": {"price": 1500, "limit": 100, "desc": "Entry + All games. First 100 only."},
    "Regular - ₦2,500": {"price": 2500, "limit": 500, "desc": "Entry + Access to all games."},
    "VIP - ₦5,000": {"price": 5000, "limit": 50, "desc": "Front row + Free drink + Priority for games."},
    "Squad of 4 - ₦8,000": {"price": 8000, "limit": 100, "desc": "4 Regular tickets. Save ₦2,000. For friends."},
    "Vendor Stand - ₦10,000": {"price": 10000, "limit": 20, "desc": "Entry + 1 table to sell food, drinks, merch."},
}

# --- AI AUTO RESPONDER KNOWLEDGE ---
FAQ = {
    "date": f"The event is on {EVENT_DATE}.",
    "venue": f"Venue is {VENUE}.",
    "price": "Early Bird 1500, Regular 2500, VIP 5000, Squad of 4 is 8000, Vendor Stand 10000.",
    "ticket": "Pick a ticket below, login, pay with Paystack, you get QR ticket instantly.",
    "game": "Games are Chess, Cards, Snooker / Pool, PlayStation, Monopoly.",
    "contact": f"Call or WhatsApp {CONTACT}, Instagram {INSTAGRAM}.",
    "vendor": "Vendors pay 10000 for a stand. Upload your product image, we approve before it goes live.",
    "refund": "Tickets are non-refundable but transferable. You can give your QR to a friend.",
}

def ai_reply(question):
    q = question.lower()
    if "date" in q or "when" in q or "day" in q:
        return FAQ["date"]
    if "where" in q or "venue" in q or "location" in q or "address" in q:
        return FAQ["venue"]
    if "price" in q or "cost" in q or "how much" in q or "ticket" in q:
        return FAQ["price"] + " " + FAQ["ticket"]
    if "game" in q or "play" in q:
        return FAQ["game"]
    if "vendor" in q or "seller" in q or "sell" in q or "stand" in q:
        return FAQ["vendor"]
    if "refund" in q or "return" in q:
        return FAQ["refund"]
    if "contact" in q or "phone" in q or "whatsapp" in q:
        return FAQ["contact"]
    return f"Great question! {EVENT_NAME} is on {EVENT_DATE} at {VENUE}. Tickets start at ₦1,500 Early Bird. Regular is ₦2,500, VIP ₦5,000, Squad of 4 ₦8,000. Want me to help you pick a ticket?"

# --- SESSION STATE ---
if "user" not in st.session_state:
    st.session_state.user = None
if "tickets_sold" not in st.session_state:
    st.session_state.tickets_sold = []
if "vendor_products" not in st.session_state:
    st.session_state.vendor_products = []
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- HEADER ---
st.markdown(f"# 🎲 {EVENT_NAME}")
st.markdown(f"**{EVENT_DATE} | {VENUE} | By {ORGANIZER}**")
st.markdown("Chess | Cards | Snooker | PlayStation | Monopoly | Music | Food")
st.info("Login is required to buy tickets or sell. AI Assistant answers you instantly below.")

# --- LOGIN GATE ---
if not st.session_state.user:
    st.subheader("🔐 Login To Continue")
    tab1, tab2 = st.tabs(["Login", "Create Account"])
    with tab1:
        email = st.text_input("Email", key="login_email")
        pwd = st.text_input("Password", type="password", key="login_pwd")
        if st.button("Login"):
            if email and pwd:
                st.session_state.user = {"email": email, "role": "buyer"}
                st.success(f"Welcome {email}! You can now buy tickets.")
                st.rerun()
            else:
                st.error("Enter email and password.")
    with tab2:
        name = st.text_input("Full Name")
        email2 = st.text_input("Email", key="signup_email")
        pwd2 = st.text_input("Password", type="password", key="signup_pwd")
        role = st.selectbox("I am a:", ["Buyer", "Seller / Vendor"])
        if st.button("Create Account"):
            if name and email2 and pwd2:
                st.session_state.user = {"email": email2, "name": name, "role": role}
                st.success("Account created! You are logged in.")
                st.rerun()
    st.markdown("---")
    st.markdown("### 🤖 Ask AI About The Event - No Login Needed")
    q = st.text_input("Ask anything: e.g. How much is VIP? Where is venue?", key="public_q")
    if st.button("Ask AI"):
        if q:
            st.success(ai_reply(q))
    st.stop()

# --- LOGGED IN ---
user = st.session_state.user
st.success(f"Logged in as {user.get('email')} | Role: {user.get('role', 'Buyer')}")
if st.button("Logout"):
    st.session_state.user = None
    st.rerun()

tab_market, tab_sell, tab_mytickets, tab_ai, tab_admin = st.tabs([
    "🎟️ Buy Tickets", "🛍️ Sell / Vendor Post", "🎫 My Tickets", "🤖 AI Assistant", "📊 Admin"
])

with tab_market:
    st.subheader("Choose Your Ticket")
    for t_name, info in TICKETS.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{t_name}**")
            st.caption(info["desc"])
        with col2:
            qty = st.number_input(f"Qty for {t_name}", min_value=0, max_value=10, key=f"qty_{t_name}")
            if qty > 0:
                total = qty * info["price"]
                st.write(f"Total: ₦{total:,}")
                if st.button(f"Pay ₦{total:,} - {t_name}", key=f"pay_{t_name}"):
                    # Connect Paystack here - for now generate ticket
                    code = str(uuid.uuid4())[:8].upper()
                    st.session_state.tickets_sold.append({
                        "code": code, "ticket": t_name, "qty": qty,
                        "total": total, "buyer": user.get("email"),
                        "date": str(datetime.datetime.now())
                    })
                    st.success(f"Payment Successful! Your Ticket Code: {code}")
                    st.info("Screenshot this code. Show QR at gate.")
                    # QR
                    qr = qrcode.make(f"ILORIN-GAME-FIESTA-{code}-{user.get('email')}")
                    buf = io.BytesIO()
                    qr.save(buf, format="PNG")
                    st.image(buf.getvalue(), width=200, caption=f"Ticket {code}")

with tab_sell:
    st.subheader("Seller - Post Product Before Publishing")
    st.caption("Upload image. Admin must approve before buyers see it. Nothing goes live without approval.")
    pname = st.text_input("Product Name - e.g. Shawarma, Merch, Game Pad")
    pprice = st.number_input("Price (₦)", min_value=0)
    pdesc = st.text_area("Description")
    pimg = st.file_uploader("Upload Product Image", type=["jpg", "png", "jpeg"])
    if st.button("Submit For Review"):
        if pname and pprice and pimg:
            st.session_state.vendor_products.append({
                "name": pname, "price": pprice, "desc": pdesc,
                "seller": user.get("email"), "status": "Pending", "image": pimg
            })
            st.success("Submitted! Waiting for Admin approval. You will not lose it, it is saved as Pending.")
        else:
            st.error("Add name, price and image.")

    st.markdown("### Approved Products For Event")
    approved = [p for p in st.session_state.vendor_products if p["status"] == "Approved"]
    if not approved:
        st.info("No approved products yet. Once Admin approves, they show here.")
    for p in approved:
        st.image(p["image"], width=200)
        st.write(f"**{p['name']}** - ₦{p['price']:,} - by {p['seller']}")
        st.caption(p["desc"])

with tab_mytickets:
    st.subheader("My Tickets")
    mine = [t for t in st.session_state.tickets_sold if t["buyer"] == user.get("email")]
    if not mine:
        st.info("You have no tickets yet. Buy one above.")
    else:
        st.dataframe(pd.DataFrame(mine))

with tab_ai:
    st.subheader("🤖 AI Auto Responder - Answers Instantly")
    st.caption("Ask about date, venue, price, games, vendor, refund. AI replies automatically so you never lose a customer.")
    for msg in st.session_state.chat:
        st.write(f"**You:** {msg['q']}")
        st.write(f"**AI:** {msg['a']}")
    user_q = st.text_input("Ask AI anything about Ilorin Game Fiesta", key="ai_q")
    if st.button("Send to AI"):
        if user_q:
            ans = ai_reply(user_q)
            st.session_state.chat.append({"q": user_q, "a": ans})
            st.rerun()

with tab_admin:
    st.subheader("Admin - You Control Everything")
    st.write("Only you should open this tab. Use password to protect it in production.")
    admin_pass = st.text_input("Admin Password", type="password")
    if admin_pass == "KK2026":  # Change this in Secrets
        st.markdown("### Pending Vendor Products")
        for i, p in enumerate(st.session_state.vendor_products):
            if p["status"] == "Pending":
                st.image(p["image"], width=150)
                st.write(f"{p['name']} - ₦{p['price']:,} by {p['seller']}")
                col1, col2 = st.columns(2)
                if col1.button(f"Approve {i}"):
                    st.session_state.vendor_products[i]["status"] = "Approved"
                    st.rerun()
                if col2.button(f"Reject {i}"):
                    st.session_state.vendor_products[i]["status"] = "Rejected"
                    st.rerun()
        st.markdown("### All Tickets Sold")
        if st.session_state.tickets_sold:
            df = pd.DataFrame(st.session_state.tickets_sold)
            st.dataframe(df)
            st.metric("Total Revenue", f"₦{df['total'].sum():,}")
            st.metric("Tickets Sold", len(df))
        else:
            st.info("No tickets sold yet.")
    elif admin_pass:
        st.error("Wrong password.")
