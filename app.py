import streamlit as st
from supabase import create_client
import pandas as pd
import uuid

st.set_page_config(page_title="ROW ECONOMY", layout="wide", initial_sidebar_state="collapsed")

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

# --- PROFESSIONAL CSS - ALIGNMENT FIX ---
st.markdown("""
<style>
    .block-container {padding-top: 0.8rem; padding-bottom: 1rem; padding-left: 0.8rem; padding-right: 0.8rem; max-width: 700px; margin: auto;}
    h1, h2, h3 {letter-spacing: -0.5px !important;}
    /* Make all buttons same height + rounded */
    .stButton > button {width: 100%; height: 48px; border-radius: 12px; font-weight: 600; font-size: 15px;}
    .stLinkButton > a {width: 100%; height: 48px; border-radius: 12px; font-weight: 600; display:flex; align-items:center; justify-content:center;}
    /* Gift buttons smaller */
    div[data-testid="column"] .stButton > button {height: 56px; font-size: 14px;}
    /* Camera center */
    [data-testid="stCameraInput"] {display:flex; justify-content:center;}
    [data-testid="stCameraInput"] > div {width: 100%; max-width: 420px; margin: auto; border-radius: 16px; overflow:hidden;}
    /* Product image */
    img {border-radius: 16px; object-fit: cover;}
    /* Hide streamlit footer */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'logged' not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    st.markdown("<h1 style='text-align:center; margin-top:40px;'>🟢 ROW ECONOMY</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>Abuja's Live Marketplace • Wuse • Garki • Utako</p>", unsafe_allow_html=True)
    with st.container(border=True):
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

# --- TOP BAR - ALIGNED ---
c_top1, c_top2, c_top3 = st.columns([1, 2, 1])
with c_top1:
    st.markdown("**🟢 ROW**")
with c_top2:
    st.markdown(f"<p style='text-align:center; font-size:13px;'>Welcome {phone}</p>", unsafe_allow_html=True)
with c_top3:
    st.markdown("<p style='text-align:right; font-size:13px;'>🪙 5000 • 📍 Abuja</p>", unsafe_allow_html=True)
st.divider()

try: products = supabase.table("products").select("*").order("created_at", desc=True).execute().data
except: products = []
try: lives = supabase.table("live_sessions").select("*").eq("is_live", True).execute().data
except: lives = []

tabs = st.tabs(["LIVE MARKET","POST PRODUCT","GO LIVE","MAP","Wallet"])

# --- 1. LIVE MARKET - ALIGNED GRID ---
with tabs[0]:
    st.markdown("## 🔴 LIVE MARKETPLACE")
    st.caption("Fresh from Wuse, Garki, Utako • Updated live")
    
    col_s, col_c = st.columns([3, 1])
    with col_s:
        search = st.text_input("Search", placeholder="🔍 Search rice, yam, oil...", label_visibility="collapsed")
    with col_c:
        cat = st.selectbox("Category", ["All","Food","Fashion","Electronics","Other"], label_visibility="collapsed")
    
    filtered = products
    if search:
        filtered = [p for p in filtered if search.lower() in str(p.get('name','')).lower() or search.lower() in str(p.get('description','')).lower()]
    
    if not filtered:
        st.info("No product yet. Be first to post!")
    
    cols = st.columns(2)
    for i, p in enumerate(filtered):
        with cols[i%2]:
            with st.container(border=True):
                if p.get('image_url'):
                    st.image(p['image_url'], use_container_width=True)
                st.markdown(f"**{p.get('name','No name')}**")
                st.markdown(f"### ₦{p.get('price',0):,}")
                st.caption(p.get('description','No description')[:80])
                st.markdown("⭐ 5.0 &nbsp;|&nbsp; 📍 Wuse Market")
                b1, b2 = st.columns(2)
                with b1:
                    if st.button("Buy Now", key=f"buy{p['id']}", type="primary"):
                        st.balloons()
                with b2:
                    msg = f"Hello I want {p.get('name')} for N{p.get('price')} on ROW ECONOMY"
                    st.link_button("WhatsApp", f"https://wa.me/2348116911722?text={msg}")

# --- 2. POST PRODUCT - ALIGNED ---
with tabs[1]:
    st.markdown("## Post Product")
    st.info("Pic + Description compulsory — to build trust")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("Product Name*")
        c1, c2 = st.columns(2)
        with c1:
            price = st.number_input("Price (₦)*", value=1000, min_value=0)
        with c2:
            category = st.selectbox("Category", ["Food","Fashion","Electronics","Other"])
        desc = st.text_area("Description*", placeholder="e.g. Fresh 50kg rice, delivered today in Wuse...")
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

# --- 3. GO LIVE - PROFESSIONAL ALIGNED - THIS IS THE FIX ---
with tabs[2]:
    st.markdown("## 🔴 GO LIVE - Earn Coins")
    
    if lives:
        st.success(f"🔴 LIVE NOW: {lives[0]['title']} • 👁️ 124 watching")
    
    st.markdown("### 🎁 Send Coin Gift")
    # 2x2 GRID - ALIGNED TOGETHER
    g1, g2 = st.columns(2)
    with g1:
        if st.button("🌹 Rose • 10"): st.balloons()
    with g2:
        if st.button("🔥 Fire • 50"): st.balloons()
    g3, g4 = st.columns(2)
    with g3:
        if st.button("🦁 Lion • 100"): st.balloons()
    with g4:
        if st.button("💎 Diamond • 500"): st.balloons()
    
    st.divider()
    
    st.markdown("### 📷 Your Live Camera")
    cam = st.camera_input("Take Photo", label_visibility="collapsed")
    
    st.markdown("### Live Title")
    title = st.text_input("Live Title", "Selling in Wuse - Send Coins!", label_visibility="collapsed")
    
    # START / END SIDE BY SIDE - ALIGNED
    s1, s2 = st.columns(2)
    with s1:
        if st.button("▶️ Start Live", type="primary"):
            supabase.table("live_sessions").insert({"phone":phone,"title":title,"is_live":True}).execute()
            st.rerun()
    with s2:
        if st.button("⏹️ End Live"):
            supabase.table("live_sessions").delete().eq("phone",phone).execute()
            st.rerun()

with tabs[3]:
    st.markdown("## SNAP MAP - Abuja")
    st.caption("Live sellers • SOS • Safe zones")
    st.map(pd.DataFrame({'lat':[9.0765,9.08,9.09],'lon':[7.3986,7.40,7.42]}), zoom=12)
    st.markdown("#### 🆘 SOS")
    if st.button("🚨 SEND SOS - I NEED HELP", type="primary", use
