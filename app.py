import streamlit as st
from supabase import create_client
import time

st.set_page_config(page_title="Row Economy Market - LIVE", page_icon="🛒", layout="wide")

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

st.markdown("""
<style>
.main {background-color:#0a0a0a; color:white;}
.live-badge {background:#ff2d55; color:white; padding:4px 12px; border-radius:20px; font-weight:800; font-size:14px;}
.host-box {background:#1a1a1a; padding:12px; border-radius:16px;}
.product-card {background:#171717; border-radius:18px; padding:14px; border:1px solid #2a2a2a;}
</style>
""", unsafe_allow_html=True)

c1, c2 = st.columns([3,1])
with c1:
    st.markdown("### Row Economy Market")
    st.caption("Wuse Market - Abuja - Live Shopping")
with c2:
    st.markdown('<span class="live-badge">LIVE</span> - 128 watching', unsafe_allow_html=True)

st.markdown('<div class="host-box"><b>@WuseSeller</b> - 5.0 stars | 1.2k followers - Wuse Market</div>', unsafe_allow_html=True)
st.markdown("### Selling Fresh Rice in Wuse Market - Ask Me Price!")
st.caption("Tap Take Photo to go LIVE. Buyers can send gifts and buy below.")

st.subheader("Your Live Camera")
photo = st.camera_input("Take Photo", label_visibility="collapsed")
live_title = st.text_input("Live Title", value="Selling in Wuse - Send Coins!")

col_a, col_b = st.columns(2)
with col_a:
    if st.button("Start Live", use_container_width=True):
        try:
            supabase.table("live_sessions").insert({"title": live_title, "is_live": True}).execute()
            st.success("You are LIVE now!")
        except Exception as e:
            st.error(f"Could not start live: {e}")
with col_b:
    if st.button("End Live", use_container_width=True):
        try:
            supabase.table("live_sessions").update({"is_live": False}).eq("is_live", True).execute()
            st.info("Live ended.")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("### Send Coin Gift")
g1, g2, g3, g4 = st.columns(4)
with g1:
    if st.button("Rose - 10"):
        st.success("Rose sent!")
with g2:
    if st.button("Fire - 50"):
        st.success("Fire sent!")
with g3:
    if st.button("Lion - 100"):
        st
