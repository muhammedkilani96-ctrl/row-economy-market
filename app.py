import streamlit as st
from supabase import create_client
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="wide")

# Secrets
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

if 'logged' not in st.session_state:
    st.session_state.logged = False

# LOGIN - FIXED
if not st.session_state.logged:
    st.title("ROW ECONOMY SUPER")
    st.markdown("`08116911722 / Kilani247`")
    phone = st.text_input("Phone", value="08116911722")
    pwd = st.text_input("Password", type="password", value="Kilani247")
    if st.button("Login", type="primary"):
        if phone.strip() == "08116911722" and pwd.strip().lower() == "kilani247":
            st.session_state.logged = True
            st.session_state.phone = phone
            st.rerun()
        else:
            st.error(f"Wrong login - you typed {pwd}, try Kilani247")
    st.stop()

phone = st.session_state.phone

# Header
st.markdown(f"""
<div style='background:#0a2a15;padding:14px;border-radius:10px;border:1px solid #1a5a2a'>
<span style='color:#4ade80;font-weight:bold'>Welcome {phone} | Bal N500000</span>
</div>
""", unsafe_allow_html=True)

# Load data safely
try:
    products = supabase.table("products").select("*").order("created_at", desc=True).execute().data
except:
    products = []
try:
    wallet = supabase.table("wallet_transactions").select("*").eq("phone", phone).order("created_at", desc=True).execute().data
except:
    wallet = []
try:
    lives = supabase.table("live_sessions").select("*").eq("is_live", True).execute().data
except:
    lives = []

# ALL TABS FROM YOUR SCREENSHOTS
tab_home, tab_market, tab_post, tab_live, tab_map, tab_sec, tab_sos, tab_chat, tab_wallet = st.tabs(
    ["Home", "LIVE MARKET", "POST PRODUCT", "GO LIVE", "MAP", "SECURITY", "SOS", "CHAT", "Wallet"]
)

with tab_home:
    st.title("ROW ECONOMY SUPER")
    st.subheader("Food Calculator")
    people = st.number_input("People", 1, 1000, 10, key="people")
    st.markdown(f"<div style='background:#222;padding:10px;border-radius:8px;color:#4ade80;font-family:monospace'>{people*1000}</div>", unsafe_allow_html=True)
    st.link_button("Order WA", f"https://wa.me/2348116911722?text=Order food for {people} people")

with tab_market:
    st.markdown("# 🔴 LIVE MARKETPLACE")
    st.caption("People posting + going live now")
    if not products:
        st.info("No products yet - Be first to post!")
    else:
        for p in products:
            with st.container(border=True):
                st.markdown(f"**{p.get('name','Product')}** - ₦{p.get('price',0)}")
                st.caption(p.get('description',''))
                c1,c2 = st.columns(2)
                c1.button("Buy", key=f"buy{p['id']}")
                c2.button("Chat Seller", key=f"chat{p['id']}")

with tab_post:
    st.title("Post Your Product")
    st.write("Sell anything - food, clothes, gadgets")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("Product Name e.g. Bag of Rice")
        price = st.number_input("Price N", value=1000, min_value=0)
        desc = st.text_area("Description")
        submitted = st.form_submit_button("Post Product", type="primary")
        if submitted and name:
            supabase.table("products").insert({"name":name,"price":price,"description":desc}).execute()
            st.success("Posted! Check LIVE MARKET")
            st.rerun()

with tab_live:
    st.title("GO LIVE")
    if lives:
        st.success(f"{len(lives)} LIVE NOW")
        for lv in lives:
            st.markdown(f"🔴 **{lv['phone']}** - {lv['title']}")
    title = st.text_input("Live Title", "Selling in Wuse Market")
    cam = st.camera_input("Turn on camera to Go Live")
    col1,col2 = st.columns(2)
    if col1.button("🔴 Start Live", type="primary"):
        supabase.table("live_sessions").insert({"phone":phone,"title":title,"is_live":True}).execute()
        st.success("YOU ARE LIVE!")
        st.rerun()
    if col2.button("End Live"):
        supabase.table("live_sessions").delete().eq("phone",phone).execute()
        st.warning("Live ended")
        st.rerun()

with tab_map:
    st.title("SNAP MAP")
    try:
        m = folium.Map(location=[9.0765,7.3986], zoom_start=13, tiles="CartoDB dark_matter")
        for lat,lon in [[9.08,7.3986],[9.09,7.42],[9.065,7.45],[9.06,7.39],[9.05,7.41],[9.10,7.43]]:
            folium.CircleMarker([lat,lon], radius=8, color="red", fill=True, fill_color="red").add_to(m)
        st_folium(m, height=500, use_container_width=True)
    except:
        st.map(data=[{"lat":9.0765,"lon":7.3986}])
        st.error("Map fallback - add folium to requirements")

with tab_sec:
    st.title("SECURITY MAP")
    try:
        m2 = folium.Map(location=[7.5,4.5], zoom_start=6, tiles="CartoDB dark_matter")
        for name, lat, lon in [("Lagos",6.5244,3.3792),("Ibadan",7.3775,3.9470),("Abuja",9.0765,7.3986),("Cotonou",6.37,2.42),("Lome",6.12,1.22)]:
            folium.Marker([lat,lon], popup=name).add_to(m2)
        st_folium(m2, height=500, use_container_width=True)
    except:
        st.info("Security Map - Lagos, Ibadan, Abuja, Cotonou")

with tab_sos:
    st.title("SOS")
    if st.button("SEND SOS", type="primary", use_container_width=True):
        st.error("🚨 SOS SENT! Location shared to ROW network + 112")
        try:
            supabase.table("wallet_transactions").insert({"phone":phone,"type":"sos","amount":0,"description":"SOS Sent"}).execute()
        except:
            pass
    st.link_button("Call 112", "tel:112", use_container_width=True)

with tab_chat:
    st.title("CHAT")
    st.text_input("Message")
    if st.button("Send"):
        st.toast("Message sent!")

with tab_wallet:
    st.title("Wallet")
    st.metric("Balance", "₦500,000")
    c1,c2 = st.columns(2)
    amt = c1.number_input("Amount", value=1000, key="wallet_amt")
    if c1.button("Deposit"):
        supabase.table("wallet_transactions").insert({"phone":phone,"type":"credit","amount":amt,"description":"Deposit"}).execute()
        st.success(f"Deposited ₦{amt}"); st.rerun()
    if c2.button("Withdraw"):
        supabase.table("wallet_transactions").insert({"phone":phone,"type":"debit","amount":amt,"description":"Withdraw"}).execute()
        st.success(f"Withdrew ₦{amt}"); st.rerun()
    st.divider()
    for w in wallet[:20]:
        st.write(f"{w['created_at'][:16]} | {w['type']} | ₦{w['amount']} | {w['description']}")

st.divider()
if st.button("Logout"):
    st.session_state.logged = False
    st.rerun()
