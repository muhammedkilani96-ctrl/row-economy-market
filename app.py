import streamlit as st
from supabase import create_client
import folium
from streamlit_folium import st_folium
from datetime import date

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="wide", page_icon="🛒")

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

# --- LOGIN ---
if 'logged' not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    st.title("ROW ECONOMY SUPER")
    st.info("08116911722 / Kilani247")
    phone = st.text_input("Phone", value="08116911722")
    pwd = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Fix: accept both kilani247 and Kilani247
        if phone == "08116911722" and pwd.lower() == "kilani247":
            st.session_state.logged = True
            st.session_state.phone = phone
            st.rerun()
        else:
            st.error("Wrong login")
    st.stop()

# --- AFTER LOGIN ---
st.markdown(f"<div style='background:#0f3d1f;padding:15px;border-radius:10px;color:#4ade80'>Welcome {st.session_state.phone} | Bal N500000</div>", unsafe_allow_html=True)

# Load products for LIVE MARKET
def load_products():
    try:
        return supabase.table("products").select("*").order("created_at", desc=True).execute().data
    except:
        return []

products = load_products()

tabs = st.tabs(["Home", "LIVE MARKET", "POST PRODUCT", "GO LIVE", "MAP", "SECURITY", "SOS", "CHAT", "Wallet"])

with tabs[0]: # HOME
    st.title("ROW ECONOMY SUPER")
    st.subheader("Food Calculator")
    people = st.number_input("People", min_value=1, value=10, step=1)
    price_per = 1000
    total = people * price_per
    st.markdown(f"<span style='color:#4ade80;background:#1a1a1a;padding:5px 10px;border-radius:5px'>{total}</span>", unsafe_allow_html=True)
    if st.button("Order WA"):
        st.link_button("Chat on WhatsApp", f"https://wa.me/234{st.session_state.phone[1:]}?text=I want to order food for {people} people - Total N{total}")

with tabs[1]: # LIVE MARKET
    st.markdown("## 🔴 LIVE MARKETPLACE")
    st.caption("People posting + going live now")
    if not products:
        st.write("No products yet - Be first to post!")
    else:
        for p in products:
            with st.container(border=True):
                st.write(f"**{p['name']}** - ₦{p.get('price', 'N/A')}")
                st.caption(p.get('description',''))

with tabs[2]: # POST PRODUCT
    st.title("Post Your Product")
    st.write("Sell anything - food, clothes, gadgets")
    with st.form("post_product", clear_on_submit=True):
        name = st.text_input("Product Name e.g. Bag of Rice")
        price = st.number_input("Price N", value=1000, min_value=0)
        desc = st.text_area("Description")
        if st.form_submit_button("Post"):
            supabase.table("products").insert({"name": name, "price": price, "description": desc}).execute()
            st.success("Product Posted!")
            st.rerun()

with tabs[3]: # GO LIVE
    st.title("GO LIVE")
    st.button("🔴 Start Live Stream")

with tabs[4]: # MAP - SNAP MAP
    st.title("SNAP MAP")
    m = folium.Map(location=[9.0765, 7.3986], zoom_start=13, tiles="CartoDB dark_matter")
    # Red dots around Wuse, Katampe, Maitama
    points = [[9.08,7.40],[9.09,7.42],[9.07,7.45],[9.06,7.39],[9.05,7.41]]
    for lat,lon in points:
        folium.CircleMarker([lat,lon], radius=8, color="red", fill=True).add_to(m)
    st_folium(m, height=500, use_container_width=True)

with tabs[5]: # SECURITY
    st.title("SECURITY MAP")
    m2 = folium.Map(location=[6.5, 3.5], zoom_start=7, tiles="CartoDB dark_matter")
    folium.Marker([6.5244, 3.3792], popup="Lagos").add_to(m2)
    folium.Marker([7.3775, 3.9470], popup="Ibadan").add_to(m2)
    folium.Marker([6.3350, 2.4245], popup="Cotonou").add_to(m2)
    st_folium(m2, height=500, use_container_width=True)

with tabs[6]: # SOS
    st.title("SOS")
    if st.button("SEND SOS"):
        st.error("SOS Sent! Location shared.")
    st.link_button("Call 112", "tel:112")

with tabs[7]: # CHAT
    st.title("CHAT")
    st.text_input("Type message...")
    st.button("Send")

with tabs[8]: # Wallet
    st.title("Wallet")
    st.metric("Balance", "₦500,000")
    st.write(f"User: {st.session_state.phone}")

if st.button("Logout"):
    st.session_state.logged = False
    st.rerun()
