import streamlit as st
import requests
import uuid
import urllib.parse

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
HEADERS = {"apikey": KEY, "Authorization": "Bearer " + KEY, "Content-Type": "application/json"}

USDT_TRC20 = st.secrets.get("USDT_WALLET", "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb")
BTC_ADDRESS = st.secrets.get("BTC_WALLET", "bc1qxy2kgy6jxc4ccklm3v3r7h5a")

st.set_page_config(page_title="Row Economy Market", layout="wide")
st.title("Row Economy Market - PERMANENT")
st.info("We accept Naira, USDT, BTC")
tab1, tab2, tab3 = st.tabs(["Market", "Sell", "My Shop"])

with tab1:
    search = st.text_input("Search product", "")
    try:
        r = requests.get(URL + "/rest/v1/products?select=*&order=id.desc", headers=HEADERS, timeout=20)
        if r.status_code == 200:
            products = r.json()
            if search:
                products = [p for p in products if search.lower() in p.get('name','').lower()]
            cols = st.columns(3)
            for i, p in enumerate(products):
                with cols[i % 3]:
                    img = p.get("image_url", "")
                    if img:
                        if img.lower().endswith((".mp4", ".mov", ".webm")):
                            st.video(img)
                        else:
                            st.image(img, use_container_width=True)
                    st.write(p.get('name',''))
                    st.write("N" + str(p.get('price','')))
                    st.caption(p.get("description",""))
                    wa = p.get("whatsapp","")
                    if wa:
                        msg = "Hi I want to buy " + p.get('name','')
                        enc = urllib.parse.quote(msg)
                        st.link_button("Chat Seller", "https://wa.me/" + wa + "?text=" + enc)
                        st.link_button("Pay with Crypto", "https://wa.me/" + wa + "?text=" + enc)
                    with st.expander("Wallets"):
                        st.write("USDT TRC20:")
                        st.code(USDT_TRC20)
                        st.write("BTC:")
                        st.code(BTC_ADDRESS)
                    if st.button("Delete", key="del_" + str(p.get('id'))):
                        del_r = requests.delete(URL + "/rest/v1/products?id=eq." + str(p.get('id')), headers=HEADERS)
                        if del_r.status_code in [200, 204]:
                            st.success("Deleted")
                            st.rerun()
                    st.divider()
    except Exception as e:
        st.error(str(e))
with tab2:
    st.subheader("Post Product")
    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0)
    desc = st.text_area("Description")
    whatsapp = st.text_input("WhatsApp 234...")
    seller = st.text_input("Shop Name")
    up_file = st.file_uploader("Upload Pic/Video", type=["jpg","jpeg","png","mp4","mov","webm"])
    if st.button("Post Product"):
        image_url = ""
        if up_file is not None:
            ext = up_file.name.split(".")[-1]
            fname = str(uuid.uuid4()) + "." + ext
            sh = {"apikey": KEY, "Authorization": "Bearer " + KEY, "Content-Type": up_file.type}
            up_res = requests.post(URL + "/storage/v1/object/product-images/" + fname, headers=sh, data=up_file.getvalue(), timeout=30)
            if up_res.status_code in [200, 201]:
                image_url = URL + "/storage/v1/object/public/product-images/" + fname
        data = {"name": name, "price": price, "description": desc, "whatsapp": whatsapp, "seller_name": seller, "image_url": image_url}
        post_r = requests.post(URL + "/rest/v1/products", headers=HEADERS, json=data, timeout=20)
        if post_r.status_code in [200, 201]:
            st.success("Posted!")
            st.balloons()
