import streamlit as st
import json
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="centered")

def load_file(name, default):
    try:
        with open(name, "r") as f:
            return json.load(f)
    except:
        return default

def save_file(name, data):
    with open(name, "w") as f:
        json.dump(data, f)

if "user" not in st.session_state:
    st.title("ROW ECONOMY SUPER")
    st.info("Login: 08116911722 / Kilani247")
    phone = st.text_input("Phone")
    pwd = st.text_input("Password", type="password")
    if st.button("LOGIN"):
        if phone.strip() == "08116911722" and pwd.strip().lower() == "kilani247":
            st.session_state.user = phone.strip()
            st.rerun()
        else:
            st.error("Wrong login")
    st.stop()

products = load_file("products.json", [])
lives = load_file("lives.json", [])

st.title("ROW ECONOMY SUPER")
st.success("Welcome 08116911722 | Bal N500000")

tab1, tab2, tab3, tab4 = st.tabs(["LIVE MARKET", "POST PRODUCT", "GO LIVE", "MAP"])

with tab1:
    st.header("LIVE MARKETPLACE")
    if lives:
        for lv in lives[::-1][:5]:
            st.error(f"LIVE {lv['user']}: {lv['title']}")
    st.divider()
    if len(products) == 0:
        st.write("No products yet - Be first to post!")
    else:
        for p in products[::-1]:
            st.write(f"{p['name']} - N{p['price']}")
            st.write(f"Seller: {p['phone']}")
            st.write(p['desc'])
            if p.get('img'):
                st.image(p['img'])
            st.link_button("Chat Seller", f"https://wa.me/{p['phone']}")
            st.divider()

with tab2:
    st.header("POST PRODUCT")
    pname = st.text_input("Product Name")
    pprice = st.number_input("Price", min_value=100, value=1000)
    pdesc = st.text_area("Description")
    pphone = st.text_input("WhatsApp", value="08116911722")
    pimg = st.text_input("Image Link")
    if st.button("POST PRODUCT NOW"):
        if pname:
            new_product = {}
