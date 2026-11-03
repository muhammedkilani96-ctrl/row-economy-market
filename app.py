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

# LOGIN
if "user" not in st.session_state:
    st.title("ROW ECONOMY SUPER")
    st.info("Login: 08116911722 / Kilani247")
    phone = st.text_input("Phone Number")
    pwd = st.text_input("Password", type="password")
    if st.button("LOGIN"):
        if phone.strip() == "08116911722" and pwd.strip().lower() == "kilani247":
            st.session_state.user = phone.strip()
            st.rerun()
        else:
            st.error("Wrong - Use 08116911722 / Kilani247")
    st.stop()

products = load_file("products.json", [])
lives = load_file("lives.json", [])

st.title("ROW ECONOMY SUPER")
st.success(f"Welcome {st.session_state.user} | Bal N500000")

tab1, tab2, tab3, tab4 = st.tabs(["LIVE MARKET", "POST PRODUCT", "GO LIVE", "MAP"])

with tab1:
    st.header("LIVE MARKETPLACE")
    st.write("People posting + going live now")
    if lives:
        st.subheader("🔴 LIVE NOW")
        for lv in lives[::-1][:5]:
            st.error(f"🔴 {lv['user']} LIVE: {lv['title']}")
            st.write(lv.get('desc',''))
    st.divider()
    if len(products) == 0:
        st.write("No products yet - Be first to post!")
    else:
        for p in products[::-1]:
            st.subheader(f"{p['name']} - N{p['price']}")
            st.write(f"Seller: {p['user']} | {p['phone']}")
            st.write(p['desc'])
            if p.get('img'):
                try:
                    st.image(p['img'])
                except:
                    pass
            st.link_button("Chat on WhatsApp", f"https://wa.me/{p['phone']}")
            st.divider()

with tab2:
    st.header("POST PRODUCT")
    st.write("Fill form to sell")
    pname = st.text_input("Product Name")
    pprice = st.number_input("Price in Naira", min_value=
