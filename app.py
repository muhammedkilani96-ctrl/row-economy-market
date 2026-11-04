import streamlit as st
from supabase import create_client
import pandas as pd

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="wide")

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

if 'logged' not in st.session_state:
    st.session_state.logged = False

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
            st.error("Wrong login")
    st.stop()

phone = st.session_state.phone
st.markdown(f"<div style='background:#0a2a15;padding:14px;border-radius:10px;color:#4ade80;font-weight:bold'>Welcome {phone} | Bal N500000</div>", unsafe_allow_html=True)

# Safe load
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

tab_home, tab_market, tab_post, tab_live, tab_map, tab_sec, tab_sos, tab_chat, tab_wallet = st.tabs(
    ["Home","LIVE MARKET","POST PRODUCT","GO LIVE","MAP","SECURITY","SOS","CHAT","Wallet"]
)

with tab_home:
    st.title("ROW ECONOMY SUPER")
    st.subheader("Food Calculator")
    people = st.number_input("People", 1, 1000, 10)
    st.success(f"Total: ₦{people*1000}")
    st.link_button("Order WA", f"https://wa.me/2348116911722?text=Order for {people}")

with tab_market:
    st.markdown("# 🔴 LIVE MARKETPLACE")
    if not products:
        st.info("No products yet")
    for p in products:
        with st.container(border=True):
            st.write(f"**{p.get('name')}** - ₦{p.get('price',0)}")
            st.caption(p.get('description',''))

with tab_post:
    st.title("Post Your Product")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("Product Name")
        price = st.number_input("Price N", value=1000, min_value=0)
        desc = st.text_area("Description")
        if st.form_submit_button("Post", type="primary") and name:
            supabase.table("products").insert({"name":name,"price":price,"description":desc}).execute()
            st.success("Posted!"); st.rerun()

with tab_live:
    st.title("🔴 GO LIVE")
    if lives:
        for lv in lives:
            st.write(f"🔴 {lv['phone']} - {lv['title']}")
    title = st.text_input("Live Title", "Selling in Wuse")
    cam = st.camera_input("Camera")
    if st.button("Start Live", type="primary"):
        supabase.table("live_sessions").insert({"phone":phone,"title":title,"is_live":True}).execute()
        st.success("LIVE!"); st.rerun()
    if st.button("End Live"):
        supabase.table("live_sessions").delete().eq("phone",phone).execute()
        st.warning("Ended"); st.rerun()

with tab_map:
    st.title("SNAP MAP - Abuja")
    st.caption("Red dots = People selling live around you")
    df = pd.DataFrame({
        'lat': [9.0765, 9.08, 9.09, 9.065, 9.06, 9.10],
        'lon': [7.3986, 7.40, 7.42, 7.45, 7.39, 7.43],
    })
    st.map(df, zoom=12, color="#FF0000", size=100)
    st.dataframe(df, use_container_width=True)
    st.info("📍 Wuse, Maitama, Katampe, Gwarimpa live now")

with tab_sec:
    st.title("SECURITY MAP")
    st.caption("Lagos, Ibadan, Abuja, Cotonou")
    df2 = pd.DataFrame({
        'lat': [6.5244, 7.3775, 9.0765, 6.37, 6.12],
        'lon': [3.3792, 3.9470, 7.3986, 2.42, 1.22],
        'city': ["Lagos","Ibadan","Abuja","Cotonou","Lome"]
    })
    st.map(df2, zoom=5)
    st.dataframe(df2)

with tab_sos:
    st.title("SOS")
    if st.button("SEND SOS", type="primary", use_container_width=True):
        st.error("🚨 SOS SENT!")
    st.link_button("Call 112", "tel:112", use_container_width=True)

with tab_chat:
    st.title("CHAT")
    msg = st.text_input("Message")
    if st.button("Send"):
        st.toast("Sent!")

with tab_wallet:
    st.title("Wallet")
    st.metric("Balance", "₦500,000")
    amt = st.number_input("Amount", value=1000)
    c1,c2 = st.columns(2)
    if c1.button("Deposit"):
        supabase.table("wallet_transactions").insert({"phone":phone,"type":"credit","amount":amt,"description":"Deposit"}).execute()
        st.success("Deposited"); st.rerun()
    if c2.button("Withdraw"):
        supabase.table("wallet_transactions").insert({"phone":phone,"type":"debit","amount":amt,"description":"Withdraw"}).execute()
        st.success("Withdrew"); st.rerun()
    for w in wallet[:10]:
        st.write(f"{w['type']} ₦{w['amount']} {w['description']}")

if st.button("Logout"):
    st.session_state.logged = False
    st.rerun()
