import streamlit as st
from supabase import create_client
import pandas as pd
import uuid

st.set_page_config(page_title="ROW ECONOMY", layout="wide")
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

if 'logged' not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    st.title("ROW ECONOMY")
    st.caption("Abuja's Live Marketplace")
    phone = st.text_input("Phone", value="08116911722")
    pwd = st.text_input("Password", type="password", value="Kilani247")
    if st.button("Login", type="primary", use_container_width=True):
        if phone.strip() == "08116911722" and pwd.strip().lower() == "kilani247":
            st.session_state.logged = True
            st.session_state.phone = phone
            st.rerun()
        else:
            st.error("Wrong login")
    st.stop()

phone = st.session_state.phone
# CLEAN BANNER - no battery text
st.markdown(f"""
<div style='background:#0a2a15;padding:14px;border-radius:12px;color:white'>
<b style='color:#4ade80'>● ROW ECONOMY</b> &nbsp; Welcome {phone} &nbsp; | &nbsp; 🪙 5000 Coins &nbsp; | &nbsp; 📍 Abuja
</div>
""", unsafe_allow_html=True)

try: products = supabase.table("products").select("*").order("created_at", desc=True).execute().data
except: products = []
try: lives = supabase.table("live_sessions").select("*").eq("is_live", True).execute().data
except: lives = []

tabs = st.tabs(["LIVE MARKET","POST PRODUCT","GO LIVE","MAP","Wallet"])

with tabs[0]:
    st.markdown("# 🔴 LIVE MARKETPLACE")
    st.caption("Fresh from Wuse, Garki, Utako")
    
    # SEARCH + FILTER - NEW SIMPLE WIN
    search = st.text_input("🔍 Search rice, yam, oil...", "")
    cat = st.selectbox("Category", ["All","Food","Fashion","Electronics","Other"])
    
    filtered = products
    if search:
        filtered = [p for p in filtered if search.lower() in str(p.get('name','')).lower() or search.lower() in str(p.get('description','')).lower()]
    
    if not filtered:
        st.info("No product found. Be the first to post!")
    
    cols = st.columns(2)
    for i, p in enumerate(filtered):
        with cols[i%2]:
            with st.container(border=True):
                if p.get('image_url'):
                    st.image(p['image_url'], use_container_width=True)
                else:
                    st.write("📦")
                st.markdown(f"**{p.get('name','No name')}**")
                st.markdown(f"### ₦{p.get('price',0):,}")
                st.caption(p.get('description','No description'))
                st.markdown(f"⭐ {p.get('rating',5.0)} | 📍 Wuse Market")
                c1,c2 = st.columns(2)
                if c1.button("Buy Now", key=f"buy{p['id']}", type="primary", use_container_width=True):
                    st.toast("Order placed! Seller will call you")
                    st.balloons()
                # WhatsApp Buy
                msg = f"Hello I want to buy {p.get('name')} for N{p.get('price')} on ROW ECONOMY"
                st.link_button("💬 WhatsApp Seller", f"https://wa.me/2348116911722?text={msg}", use_container_width=True)

with tabs[1]:
    st.title("Post Product")
    st.info("Pic + Description compulsory")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("Product Name*")
        price = st.number_input("Price*", value=1000)
        desc = st.text_area("Description*")
        pic = st.file_uploader("Product Picture* - COMPULSORY", type=['jpg','png','jpeg'])
        if st.form_submit_button("Post Product", type="primary", use_container_width=True):
            if not name or not desc or not pic:
                st.error("❌ Name + Description + Pic are COMPULSORY!")
            else:
                try:
                    fname = f"{uuid.uuid4()}_{pic.name}"
                    supabase.storage.from_("product_images").upload(fname, pic.getvalue())
                    image_url = supabase.storage.from_("product_images").get_public_url(fname)
                    supabase.table("products").insert({"name":name,"price":price,"description":desc,"image_url":image_url}).execute()
                    st.success("✅ Posted! Check LIVE MARKET")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")

with tabs[2]:
    st.title("🔴 GO LIVE - Earn Coins")
    if lives:
        for lv in lives:
            st.success(f"🔴 LIVE NOW: {lv['title']} - 👁️ 124 watching")
    st.divider()
    st.subheader("Send Coin Gift 🎁")
    g1,g2,g3,g4 = st.columns(4)
    if g1.button("🌹 Rose 10"): st.balloons()
    if g2.button("🔥 Fire 50"): st.balloons()
    if g3.button("🦁 Lion 100"): st.balloons()
    if g4.button("💎 Diamond 500"): st.balloons()
    st.divider()
    cam = st.camera_input("Your Live Camera")
    title = st.text_input("Live Title", "Selling in Wuse - Send Coins!")
    if st.button("Start Live", type="primary", use_container_width=True):
        supabase.table("live_sessions").insert({"phone":phone,"title":title,"is_live":True}).execute()
        st.rerun()
    if st.button("End Live"):
        supabase.table("live_sessions").delete().eq("phone",phone).execute()
        st.rerun()

with tabs[3]:
    st.title("SNAP MAP - Abuja")
    st.map(pd.DataFrame({'lat':[9.0765,9.08,9.09],'lon':[7.3986,7.40,7.42]}), zoom=12)

with tabs[4]:
    st.title("Wallet")
    st.metric("Naira Balance","₦500,000")
    st.metric("Coins","5000")
    st.info("Coins from gifts can be converted to Naira soon")

if st.button("Logout"):
    st.session_state.logged = False
    st.rerun()
