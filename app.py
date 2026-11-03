import streamlit as st
import requests

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

st.set_page_config(page_title="Row Market Permanent", layout="wide")
st.title("🛒 Row Economy Market - PERMANENT")

def load_products():
    url = f"{SUPABASE_URL}/rest/v1/products?select=*&order=created_at.desc"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return []

def load_lives():
    url = f"{SUPABASE_URL}/rest/v1/lives?select=*&order=created_at.desc"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return []

tab1, tab2, tab3 = st.tabs(["🏠 Market", "➕ Sell Product", "🔴 Go Live"])

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
                st.write(f"**{p.get('name')}**")
                st.write(f"₦{p.get('price',0):,}")
                st.caption(p.get("description",""))
                st.caption(f"📞 {p.get('phone','')} | {p.get('seller','')}")
                if p.get('phone'):
                    st.link_button(f"WhatsApp {p.get('name')}", f"https://wa.me/{p.get('phone')}")

with tab2:
    st.subheader("Add Your Product")
    with st.form("sell_form"):
        name = st.text_input("Product Name")
        price = st.number_input("Price (₦)", min_value=0)
        desc = st.text_area("Description")
        phone = st.text_input("WhatsApp Number e.g 2348012345678")
        image = st.text_input("Image Link")
        seller = st.text_input("Your Name / Shop Name")
        submit = st.form_submit_button("Post Product")
        if submit:
            if name and price:
                data = {"name": name, "price": int(price), "description": desc, "phone": phone, "image_link": image, "seller": seller}
                url = f"{SUPABASE_URL}/rest/v1/products"
                r = requests.post(url, headers=HEADERS, json=data)
                if r.status_code in [200,201]:
                    st.success("✅ Product posted permanently!")
                    st.balloons()
                else:
                    st.error(f"Error: {r.text}")
            else:
                st.error("Name and Price needed")

with tab3:
    st.subheader("Live Selling")
    lives = load_lives()
    for l in lives:
        st.write(f"🔴 LIVE: {l.get('title')} by {l.get('seller')}")
    st.divider()
    with st.form("live_form"):
        title = st.text_input("Live Title")
        seller_live = st.text_input("Your Name")
        go_live = st.form_submit_button("Start Live")
        if go_live and title:
            data = {"title": title, "seller": seller_live}
            url = f"{SUPABASE_URL}/rest/v1/lives"
            r = requests.post(url, headers=HEADERS, json=data)
            if r.status_code in [200,201]:
                st.success("You are LIVE!")
