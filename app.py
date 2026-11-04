import streamlit as st
from supabase import create_client
import pandas as pd
import uuid

st.set_page_config(page_title="ROW ECONOMY", layout="wide", initial_sidebar_state="collapsed")

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

# PROFESSIONAL CSS - ALIGNMENT
st.markdown("""
<style>
    .block-container {padding-top: 0.8rem; padding-bottom: 1rem; padding-left: 0.8rem; padding-right: 0.8rem; max-width: 700px; margin: auto;}
    .stButton > button {width: 100%; height: 48px; border-radius: 12px; font-weight: 600; font-size: 15px;}
    .stLinkButton > a {width: 100%; height: 48px; border-radius: 12px; font-weight: 600; display:flex; align-items:center; justify-content:center;}
    div[data-testid="column"] .stButton > button {height: 56px; font-size: 14px;}
    [data-testid="stCameraInput"] {display:flex; justify-content:center;}
    [data-testid="stCameraInput"] > div {width: 100%; max-width: 420px; margin: auto; border-radius: 16px; overflow:hidden;}
    img {border-radius: 16px; object-fit: cover;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'logged' not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    st.markdown("<h1 style='text-align:center; margin-top:40px;'>ROW ECONOMY</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>Abuja Live Marketplace - Wuse - Garki - Utako</p>", unsafe_allow_html=True)
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

# TOP BAR - ALIGNED
c_top1, c_top2, c_top3 = st.columns([1, 2, 1])
with c_top1:
    st.markdown("**ROW**")
with c_top2:
    st.markdown(f"<p style='text-align:center; font-size:13px;'>Welcome {phone}</p>", unsafe_allow_html=True)
with c_top3:
    st.markdown("<p style='text-align:right; font-size:13px;'>Coins 5000 | Abuja</p>", unsafe_allow_html=True)
st.divider()

try:
    products = supabase.table("products").select("*").order("created_at", desc=True).execute().data
except Exception:
    products = []
try:
    lives = supabase.table("live_sessions").select("*").eq("is_live", True).execute().data
except Exception:
    lives = []

tabs = st.tabs(["LIVE MARKET", "POST PRODUCT", "GO LIVE", "MAP", "Wallet"])

# 1. LIVE MARKET
with tabs[0]:
    st.markdown("## LIVE MARKETPLACE")
    st.caption("Fresh from Wuse, Garki, Utako - Updated live")
    col_s, col_c = st.columns([3, 1])
    with col_s:
        search = st.text_input("Search", placeholder="Search rice, yam, oil...", label_visibility="collapsed")
    with col_c:
        cat = st.selectbox("Category",
