import streamlit as st
import uuid
from supabase import create_client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Row Economy Market", layout="wide")
st.title("Row Economy Market - PERMANENT")

tab1, tab2 = st.tabs(["Market", "Sell Product"])

with tab1:
    st.subheader("Available Products")
    try:
        res = supabase.table("products").select("*").order("id", desc=True).execute()
        products = res.data
        if not products:
            st.info("No products yet")
        else:
            cols = st.columns(3)
            for i, p in enumerate(products):
                with cols[i % 3]:
                    url = p.get("image_url","")
                    if url:
                        if url.endswith((".mp4",".mov",".webm")):
                            st.video(url)
                        else:
                            st.image(url, use_container_width=True)
                    st.write(f"**{p.get('name','')}**")
                    st.write(f"₦{p.get('price','')}")
                    st.write(p.get("description",""))
                    wa = p.get("whatsapp","")
                    if wa:
                        st.link_button("Chat Seller", f"https://wa.me/{wa}")
                    st.divider()
    except Exception as e:
        st.error(f"Error: {e}")

with tab2:
    st.subheader("Post Product With Picture/Video")
    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0)
    desc = st.text_area("Description")
    whatsapp = st.text_input("WhatsApp e.g 2348012345678")
    seller = st.text_input("Shop Name")
    up
