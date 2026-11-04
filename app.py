import streamlit as st
from supabase import create_client
import time

st.set_page_config(page_title="Row Economy Market - LIVE", page_icon="🛒", layout="wide")

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

# PUT YOUR WHATSAPP NUMBER HERE - e.g. 2348031234567 (234 + number without 0)
SELLER_WHATSAPP = "2348031234567"

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
st.markdown("### Fresh Rice Available Now - Ask Me Price!")
st.caption("Fresh stock from Wuse Market. Delivery available in Abuja. Tap WhatsApp to order.")

st.subheader("Your Live Camera")
photo = st.camera_input("Take Photo", label_visibility="collapsed")
live_title = st.text_input("Live Title", value="Fresh Rice Available Now - Wuse Market")

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

st.markdown("### Support Seller")
g1, g2, g3, g4 = st.columns(4)
with g1:
    if st.button("Rose - N100"):
        st.success("Thank you! Rose sent!")
with g2:
    if st.button("Fire - N500"):
        st.success("Thank you! Fire sent!")
with g3:
    if st.button("Lion - N1000"):
        st.success("Thank you! Lion sent!")
with g4:
    if st.button("Diamond - N5000"):
        st.success("Thank you! Diamond sent!")

st.markdown("### Live Comments")
comment_name = st.text_input("Your Name", placeholder="e.g. Amina")
comment_text = st.text_input("Ask a question", placeholder="e.g. How much is delivery to Garki?")
if st.button("Send Comment"):
    if comment_name and comment_text:
        st.success(f"{comment_name}: {comment_text} - Sent!")
    else:
        st.error("Please enter name and question")

st.markdown("---")
st.markdown("## LIVE MARKETPLACE")
search = st.text_input("Search", placeholder="Search rice, yam, oil...")
category = st.selectbox("Category", ["All", "Food", "Rice", "Oil", "Vegetables", "Others"])

try:
    res = supabase.table("products").select("*").order("created_at", desc=True).execute()
    products = res.data or []
except Exception as e:
    st.error(f"Could not load products: {e}")
    products = []

if search:
    products = [p for p in products if search.lower() in str(p.get("name", "")).lower()]
if category != "All":
    products = [p for p in products if category.lower() in str(p.get("category", "") or "").lower() + str(p.get("name", "")).lower()]

if not products:
    st.info("No products yet. Post your first product below.")
else:
    for p in products:
        name = p.get("name", "No name")
        price = p.get("price", 0) or 0
        desc = p.get("description") or ""
        img = p.get("image_url") or ""
        unit
