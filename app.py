import streamlit as st
import requests

st.set_page_config(page_title="Row Economy Market", layout="wide")

try:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
    BTC_WALLET = st.secrets.get("BTC_WALLET", "bc1q...")
    USDT_WALLET = st.secrets.get("USDT_WALLET", "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb")
    has_secrets = True
except:
    has_secrets = False
    SUPABASE_URL = ""
    SUPABASE_KEY = ""
    BTC_WALLET = "bc1q..."
    USDT_WALLET = "T..."

st.markdown("### We accept Naira, USDT, BTC")
tab1, tab2, tab3 = st.tabs(["Market", "Sell", "My Shop"])

with tab1:
    st.subheader("Search product")
    q = st.text_input("Search", placeholder="rice, shoe...")
    if not has_secrets:
        st.warning("Secrets not loaded")
    else:
        headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
        url = f"{SUPABASE_URL}/rest/v1/products?select=*&order=id.desc"
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            products = r.json()
            for p in products:
                if q.lower() in str(p.get('name','')).lower() or not q:
                    with st.container(border=True):
                        st.write(f"**{p.get('name')}** - ₦{p.get('price')}")
                        if p.get('image_url'):
                            st.image(p.get('image_url'), width=200)
                        with st.expander("Pay with Crypto / Naira"):
                            st.code(f"BTC: {BTC_WALLET}")
                            st.code(f"USDT: {USDT_WALLET}")
        else:
            st.error(r.text[:300])

with tab2:
    st.subheader("Post Product")
    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0)
    desc = st.text_area("Description")
    whatsapp = st.text_input("WhatsApp")
    img_url = st.text_input("Image URL")
    if st.button("Post Product", type="primary"):
        headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}", "Content-Type": "application/json", "Prefer": "return=representation"}
        data = {"name": name, "price": price, "description": desc, "whatsapp": whatsapp, "image_url": img_url}
        r = requests.post(f"{SUPABASE_URL}/rest/v1/products", headers=headers, json=data, timeout=15)
        if r.status_code in [200,201]:
            st.success("Posted! Check Market tab")
        else:
            st.error(r.text[:400])

with tab3:
    st.write("My Shop")
