import streamlit as st
import pandas as pd
from supabase import create_client

# CONNECT TO SUPABASE
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Row Market - Permanent", layout="wide")
st.title("🛒 Row Economy Market - PERMANENT")

# TABS
tab1, tab2, tab3 = st.tabs(["🏠 Market", "➕ Sell Product", "🔴 Go Live"])

# LOAD PRODUCTS FROM SUPABASE
def load_products():
    res = supabase.table("products").select("*").order("created_at", desc=True).execute()
    return res.data

# TAB 1 - MARKET
with tab1:
    st.subheader("Products wey dey")
    products = load_products()
    if not products:
        st.info("No products yet. Be first to sell!")
    else:
        cols = st.columns(3)
        for i, p in enumerate(products):
            with cols[i % 3]:
                if p.get("image_link"):
                    st.image(p["image_link"], use_container_width=True)
                st.write(f"**{p['name']}**")
                st.write(f"₦{p['price']:,}")
                st.caption(p.get("description",""))
                st.caption(f"📞 {p.get('phone','')} | Seller: {p.get('seller','')}")
                if st.button(f"WhatsApp {p['name']}", key=f"wa_{p['id']}"):
                    st.markdown(f"[Chat on WhatsApp](https://wa.me/{p['phone']})")

# TAB 2 - SELL
with tab2:
    st.subheader("Add Your Product")
    with st.form("sell_form"):
        name = st.text_input("Product Name")
        price = st.number_input("Price (₦)", min_value=0)
        desc = st.text_area("Description")
        phone = st.text_input("WhatsApp Number (e.g 2348012345678)")
        image = st.text_input("Image Link (from imgur, etc)")
        seller = st.text_input("Your Name / Shop Name")
        submit = st.form_submit_button("Post Product")
        if submit:
            if name and price:
                supabase.table("products").insert({
                    "name": name, "price": price, "description": desc,
                    "phone": phone, "image_link": image, "seller": seller
                }).execute()
                st.success("✅ Product posted permanently! Go check Market tab!")
                st.balloons()
            else:
                st.error("Name and Price required")

# TAB 3 - LIVE
with tab3:
    st.subheader("Live Selling")
    lives_res = supabase.table("lives").select("*").order("created_at", desc=True).execute()
    lives = lives_res.data
    if lives:
        for l in lives:
            st.write(f"🔴 LIVE: {l['title']} by {l['seller']}")
    st.divider()
    with st.form("live_form"):
        title = st.text_input("Live Title (e.g Selling Shoes)")
        seller_live = st.text_input("Your Name")
        go_live = st.form_submit_button("Start Live")
        if go_live and title:
            supabase.table("lives").insert({"title": title, "seller": seller_live}).execute()
            st.success("You are LIVE now!")
