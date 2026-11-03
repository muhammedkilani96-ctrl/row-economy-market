import streamlit as st
import uuid
from supabase import create_client

# --- SUPABASE SETUP ---
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Row Economy Market", layout="wide")
st.title("Row Economy Market - PERMANENT")

tab1, tab2, tab3 = st.tabs(["🏠 Market", "➕ Sell Product", "🔴 Go Live"])

# TAB 1 - MARKET
with tab1:
    st.subheader("Available Products")
    try:
        res = supabase.table("products").select("*").order("id", desc=True).execute()
        products = res.data
        if not products:
            st.info("No products yet. Be first to sell!")
        else:
            cols = st.columns(3)
            for i, p in enumerate(products):
                with cols[i % 3]:
                    # Show image or video
                    if p.get("image_url"):
                        if p["image_url"].endswith(('.mp4','.mov','.webm')):
                            st.video(p["image_url"])
                        else:
                           
