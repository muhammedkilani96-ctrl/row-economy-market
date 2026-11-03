import streamlit as st
import requests
import uuid
import urllib.parse

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
HEADERS = {"apikey": KEY, "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

USDT_TRC20 = st.secrets.get("USDT_WALLET", "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb")
BTC_ADDRESS = st.secrets.get("BTC_WALLET", "bc1qxy2kgy6jxc4ccklm3v3r7h5a")

st.set_page_config(page_title="Row Economy Market", layout="wide")
st.title("Row Economy Market - PERMANENT")

try:
    cg = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd,ngn", timeout=10).json()
    btc = cg.get('bitcoin', {}).get('usd', '-')
    eth = cg.get('ethereum', {}).get('usd', '-')
    usdt = cg.get('tether', {}).get('ngn', '-')
    st.success(f"LIVE: BTC ${btc} | ETH ${eth} | USDT N{usdt} - Naira & Crypto accepted!")
except:
    st.info("We accept: Naira, USDT, BTC")

tab1, tab2, tab3 = st.tabs(["Market", "Sell", "My Shop"])

with tab1:
    st.subheader("Products")
    search = st.text_input("Search product", "")
    min_price = st.number_input("Min Price", min_value=0, value=0)
    try:
        r = requests.get(f"{URL}/rest/v1/products?select=*&order=id.desc", headers=HEADERS, timeout=20)
        if r.status_code == 200:
            products = r.json()
            if search:
                products = [p for p in products if search.lower() in p.get('name','').lower() or search.lower() in p.get('description','').lower()]
            if min_price > 0:
                products = [p for p in products if float(p.get('price') or 0) >= min_price]
            if not products:
                st.info("No products yet")
            else:
                cols = st.columns(3)
                for i, p in enumerate(products):
                    with cols[i % 3]:
                        img = p.get("image_url", "")
                        if img:
                            if img.lower().endswith((".mp4", ".mov", ".webm")):
                                st.video(img)
                            else:
                                st.image(img, use_container_width=True)
                        st.write(f"**{p.get('name','')}** - N{p.get('price','')}")
                        st.caption(p.get("description",""))
                        wa = p.get("whatsapp","")
                        if wa:
                            msg = f"Hi! I want to buy Product: {p.get('name','')} Price: N{p.get('price','')} Shop: {p.get('seller_name','')} Image: {img}"
                            enc = urllib.parse.quote(msg)
                            st.link_button("Chat Seller", f"https://wa.me/{wa}?text={enc}")
                            cmsg = f"Hi! I want to PAY WITH CRYPTO for {p.get('name','')} N{p.get('price','')} TX ID: "
                            cenc = urllib.parse.quote(cmsg)
                            st.link_button("Pay with USDT/BTC", f"https://wa.me/{wa}?text={cenc}")
                        with st.expander("Wallets"):
                            st.code(f"USDT TRC20: {USDT_TRC20}\nBTC: {BTC_ADDRESS}")
                        if st.button("Delete", key=f"
