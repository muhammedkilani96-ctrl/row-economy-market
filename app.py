import streamlit as st
from supabase import create_client
import pandas as pd
import uuid

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="wide")

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

if 'logged' not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    st.title("ROW ECONOMY SUPER")
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
st.markdown(f"<div style='background:#0a2a15;padding:12px;border-radius:10px;color:#4ade80;font-weight:bold'>Welcome {phone} | Bal N500000 | Coins: 5000</div>", unsafe_allow_html=True)

# Load
try:
    products = supabase.table("products").select("*").order("created_at", desc=True).execute().data
except: products = []
try:
    wallet = supabase.table("wallet_transactions").select("*").eq("phone", phone).order("created_at", desc=True).execute().data
except: wallet = []
try:
    lives = supabase.table("live_sessions").select("*").eq("is_live", True).execute().data
except: lives = []
try:
    gifts = supabase.table("live_gifts").select("*").order("created_at", desc=True).limit(20).execute().data
except: gifts = []

tabs = st.tabs(["Home","LIVE MARKET","POST PRODUCT","GO LIVE","MAP","SECURITY","SOS","CHAT","Wallet"])

with tabs[0]:
    st.title("ROW ECONOMY SUPER")
    people = st.number_input("People", 1, 1000, 10)
    st.success(f"Total: ₦{people*1000}")

with tabs[1]:
    st.markdown("# 🔴 LIVE MARKETPLACE")
    st.caption("Products with pic + description")
    if not products:
        st.info("No products yet")
    cols = st.columns(2)
    for i, p in enumerate(products):
        with cols[i%2]:
            with st.container(border=True):
                if p.get('image_url'):
                    st.image(p['image_url'], use_container_width=True)
                else:
                    st.write("📦 No image")
                st.markdown(f"**{p.get('name')}** - ₦{p.get('price',0)}")
                st.caption(p.get('description','No description'))
                st.button(f"Buy {p.get('name')}", key=f"buy{p['id']}")

with tabs[2]:
    st.title("Post Your Product")
    st.warning("COMPULSORY: Pic + Description required")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("Product Name*")
        price = st.number_input("Price N*", value=1000, min_value=0)
        desc = st.text_area("Description* - Tell buyers about product")
        pic = st.file_uploader("Product Picture* - COMPULSORY", type=['jpg','jpeg','png'])
        submitted = st.form_submit_button("Post Product", type="primary")
        if submitted:
            if not name or not desc or not pic:
                st.error("❌ Product Name, Pic, and Description are COMPULSORY!")
            else:
                # Upload pic
                file_name = f"{uuid.uuid4()}_{pic.name}"
                try:
                    supabase.storage.from_("product_images").upload(file_name, pic.getvalue(), {"content-type": pic.type})
                    image_url = supabase.storage.from_("product_images").get_public_url(file_name)
                except Exception as e:
                    st.error(f"Upload failed: {e}")
                    st.stop()
                supabase.table("products").insert({"name":name,"price":price,"description":desc,"image_url":image_url}).execute()
                st.success("✅ Product posted with pic!"); st.rerun()

with tabs[3]:
    st.title("🔴 GO LIVE - Earn Coins")
    if lives:
        for lv in lives:
            st.markdown(f"🔴 **{lv['phone']}** LIVE: {lv['title']}")
    
    st.divider()
    st.subheader("Send Coin Gift 🎁")
    gift_cols = st.columns(4)
    gifts_list = [("🌹 Rose",10),("🔥 Fire",50),("🦁 Lion",100),("💎 Diamond",500)]
    for idx, (gift_name, coins) in enumerate(gifts_list):
        with gift_cols[idx]:
            if st.button(f"{gift_name}\n{coins} coins", key=f"gift{gift_name}"):
                # Send gift to first live
                if lives:
                    target = lives[0]['phone']
                    supabase.table("live_gifts").insert({"live_phone":target,"sender_phone":phone,"gift":gift_name,"coins":coins}).execute()
                    supabase.table("wallet_transactions").insert({"phone":phone,"type":"debit","amount":coins,"description":f"Gift {gift_name} to {target}"}).execute()
                    st.toast(f"Sent {gift_name}!")
                    st.balloons()
                else:
                    st.warning("No one live now")
    
    st.divider()
    st.subheader("Recent Gifts")
    for g in gifts:
        st.write(f"{g['sender_phone']} sent {g['gift']} ({g['coins']} coins) to {g['live_phone']}")

    st.divider()
    cam = st.camera_input("Your Live Camera")
    title = st.text_input("Live Title", "Selling Rice - Send me coins!")
    c1,c2 = st.columns(2)
    if c1.button("🔴 Start Live", type="primary"):
        supabase.table("live_sessions").insert({"phone":phone,"title":title,"is_live":True}).execute()
        st.success("YOU ARE LIVE - People can send you coins!"); st.rerun()
    if c2.button("End Live"):
        supabase.table("live_sessions").delete().eq("phone",phone).execute()
        st.warning("Ended"); st.rerun()

with tabs[4]:
    st.title("SNAP MAP")
    df = pd.DataFrame({'lat':[9.0765,9.08,9.09],'lon':[7.3986,7.40,7.42]})
    st.map(df, zoom=12)

with tabs[5]:
    st.title("SECURITY MAP")
    df2 = pd.DataFrame({'lat':[6.5244,7.3775,9.0765],'lon':[3.3792,3.9470,7.3986]})
    st.map(df2, zoom=5)

with tabs[6]:
    st.title("SOS")
    if st.button("SEND SOS", type="primary", use_container_width=True):
        st.error("SOS SENT!")

with tabs[7]:
    st.title("CHAT")

with tabs[8]:
    st.title("Wallet & Coins")
    st.metric("Coins", "5000")
    for w in wallet[:10]:
        st.write(f"{w['type']} ₦{w['amount']} - {w['description']}")

if st.button("Logout"):
    st.session_state.logged = False
    st.rerun()
