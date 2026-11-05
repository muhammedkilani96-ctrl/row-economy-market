import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="wide")

# --- K&K STYLE CSS ---
st.markdown("""
<style>
.topbar { background:#00A651; padding:16px 14px 20px 14px; border-radius:0 0 20px 20px; color:white; text-align:center; }
.topbar h1 { color:white; margin:0; font-size:28px; }
.searchbox { background:white; border-radius:25px; padding:10px 14px; color:#555; margin-top:10px; text-align:left; }
.cat-card { background:#FFE8F0; border-radius:14px; padding:14px 6px; text-align:center; }
.cat-card2 { background:#D6EAF8; border-radius:14px; padding:14px 6px; text-align:center; }
.cat-card3 { background:#FDEBD0; border-radius:14px; padding:14px 6px; text-align:center; }
.cat-card4 { background:#D5F5E3; border-radius:14px; padding:14px 6px; text-align:center; }
.featured { background:white; border-radius:16px; padding:16px; border:1px solid #eee; box-shadow:0 2px 10px rgba(0,0,0,0.05); }
.verified { background:#00A651; color:white; padding:4px 10px; border-radius:20px; font-size:12px; font-weight:bold; }
.wa-btn { background:#00A651; color:white; padding:12px; border-radius:10px; text-align:center; font-weight:bold; display:block; text-decoration:none; }
.mama { background:#D5F5E3; border-radius:16px; padding:12px; }
.bottomnav { position:fixed; bottom:0; left:0; right:0; background:white; display:flex; justify-content:space-around; padding:10px; border-top:1px solid #eee; }
</style>
""", unsafe_allow_html=True)

if "all_products" not in st.session_state:
    st.session_state.all_products = [
        {"seller": "Horlance Auto Cooling Ltd", "name": "Car AC Repair", "price": "₦25,000", "location": "Osun & Oyo State", "whatsapp": "09046044472", "cat": "Car Mart", "verified": True, "image": None},
        {"seller": "Mama T Rice", "name": "Bag of Rice", "price": "₦45,000", "location": "Abuja", "whatsapp": "09046044472", "cat": "Food", "verified": True, "image": None},
    ]

# --- TOP BAR ---
st.markdown("""
<div class="topbar">
<h1>☰ &nbsp; ROW ECONOMY &nbsp; 👤</h1>
<div class="searchbox">🔍 &nbsp; Ask Mama Oloja - What are you looking for today? &nbsp; 🎤</div>
</div>
""", unsafe_allow_html=True)

search = st.text_input("", placeholder="Ask Mama Oloja - What are you looking for today?", label_visibility="collapsed")

# --- CATEGORIES ---
st.markdown("### Categories &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style='color:#00A651;font-size:14px'>See all ></span>", unsafe_allow_html=True)
cats = [
    ("💐", "Perfume", "#FFE8F0"),
    ("👕", "Clothes", "#D6EAF8"),
    ("📱", "Phones", "#D6EAF8"),
    ("🍲", "Food", "#FDEBD0"),
    ("🚗", "Car Mart", "#FDEBD0"),
    ("🧰", "Services", "#D5F5E3"),
    ("🎟️", "Tickets", "#FADBD8"),
    ("💬", "Chat Rooms", "#D5F5E3"),
]
cols
