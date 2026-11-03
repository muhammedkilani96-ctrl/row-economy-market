import streamlit as st
import requests
import time

st.set_page_config(page_title="Row Economy Market", layout="wide")

# Try get secrets, if not exist use placeholder
try:
    SUPABASE_URL = st.secrets.get("SUPABASE_URL", "https://your-project-id.supabase.co")
    SUPABASE_KEY = st.secrets.get("SUPABASE_KEY", "your-anon-key")
    BTC_WALLET = st.secrets.get("BTC_WALLET", "bc1q...")
    USDT_WALLET = st.secrets.get("USDT_WALLET", "T...")
except:
    SUPABASE_URL = "https://your-project-id.supabase.co"
    SUPABASE_KEY = "demo"
    BTC_WALLET = "bc1q..."
    USDT_WALLET = "T..."

st.info("We accept Naira, USDT, BTC")

tab1, tab2, tab3 = st.tabs(["Market", "Sell", "My Shop"])

with tab1:
    st.subheader("Search product")
    q = st.text_input("", label_visibility="collapsed")
    try:
        # If SUPABASE_URL still placeholder, show demo
        if "your-project-id" in SUPABASE_URL:
            st.warning("Add your real Supabase URL in Secrets to see real products")
            st.write("Demo: Your market is working! Add secrets to make it permanent.")
        else:
            headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
            url = f"{SUPABASE_URL}/rest/v1/products?select=*&order=id.desc"
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                products = r.json()
                for p in products:
                    if q.lower() in p.get('name','').lower() or not q:
                        with st.container(border=True):
                            st.write(f"**{p.get('name')}** - ₦{p.get('price')}")
                            if p.get('image_url'):
                                st.image(p.get('image_url'), width=200)
                            with st.expander("Wallets & Pay"):
                                st.code(f"BTC: {BTC_WALLET}")
                                st.code(f"USDT: {USDT_WALLET}")
            else:
                st.error(f"Supabase error: {r.text[:200]}")
    except Exception as e:
        st.error(f"Error: {e}")

with tab2:
    st.subheader("Post Product")
    name = st.text_input("Product Name")
    price = st.number_input("Price (₦)", min_value=0)
    desc = st.text_area("Description")
    img = st.file_uploader("Image", type=['jpg','png','jpeg'])
    if st.button("Post Product"):
        if "your-project-id" in SUPABASE_URL:
            st.error("Please add real Supabase URL in Streamlit Secrets first!")
        else:
            st.success("Product posting logic here - add your Supabase insert code")
            
with tab3:
   
