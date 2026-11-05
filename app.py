import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="wide")

st.markdown("""
<style>
.topbar { background:#00A651; padding:18px 14px 20px 14px; border-radius:0 0 20px 20px; color:white; text-align:center; }
.topbar h1 { color:white; margin:0; font-size:28px; }
.featured { background:white; border-radius:16px; padding:16px; border:1px solid #eee; }
.verified { background:#00A651; color:white; padding:4px 10px; border-radius:20px; font-size:12px; font-weight:bold; }
.mama { background:#D5F5E3; border-radius:16px; padding:12px; }
</style>
""", unsafe_allow_html=True)

if "all_products" not in st.session_state:
    st.session_state.all_products = [
        {"seller": "Horlance Auto Cooling Ltd", "name": "Car AC Repair", "price": "₦25,000", "location": "Osun & Oyo State", "whatsapp": "09046044472", "cat": "Car Mart", "verified": True},
        {"seller": "Mama T
