import streamlit as st
import json
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="centered")

if "products" not in st.session_state:
    st.session_state.products = []
if "lives" not in st.session_state:
    st.session_state.lives = []

if "user" not in st.session_state:
    st.title("ROW ECONOMY SUPER")
    phone = st.text_input("Phone")
    pwd = st.text_input("Password", type="password")
    if st.button("LOGIN"):
        if phone.strip() == "08116911722" and pwd.strip().lower() == "kilani247":
            st.session_state.user = phone.strip()
            st.rerun()
        else:
            st.error("Wrong")
    st.stop()

st.title("ROW ECONOMY SUPER")
st.success(f"Welcome {st.session_state.user} | Bal N500000")

tab1, tab2, tab3, tab4 = st.tabs(["LIVE MARKET", "POST PRODUCT", "GO LIVE", "MAP"])

with tab1:
    st.header("LIVE MARKETPLACE")
    if st.session_state.lives:
        for lv in st.session_state.lives[::-1]:
            st.warning(f"LIVE: {lv['title']} by {lv['user']}")
    st.divider()
    if len(st.session_state.products) == 0:
        st.write("No products yet - Be first to post!")
    else:
        for p in st.session_state.products[::-1]:
            st.subheader(f"{p['name']} - N{p['price']}")
            st.write(f"Seller: {p['phone']} | {p['time']}")
            st.write(p['desc'])
            st.link_button("Chat Seller on WhatsApp", f"https://wa.me/{p['phone']}")
            st.divider()

with tab2:
    st.header("POST PRODUCT - LEAVE IMAGE EMPTY!")
    pname = st.text_input("Product Name *", key="pn")
    pprice = st.number_input("Price *", min_value=100, value=1000, key="pp")
    pdesc = st.text_area("Description", key="pd")
    pphone = st.text_input("WhatsApp Number", value="08116911722", key="ph")
    if st.button("POST PRODUCT NOW", type="primary", key="postbtn"):
        if pname.strip() == "":
            st.error("Type Product Name first!")
        else:
            new_product = {
                "name": pname.strip(),
                "price": pprice,
                "desc": pdesc,
                "phone": pphone,
                "user": st.session_state.user,
                "time": datetime.now().strftime("%H:%M")
            }
            st.session_state.products.append(new_product)
            st.success("POSTED! Check LIVE MARKET now!")
            st.balloons()
            st.snow()

with tab3:
    st.header("GO LIVE - SCROLL DOWN IF BLANK!")
    st.write("If you see black, swipe UP to see form")
    ltitle = st.text_input("Live Title *", key="lt")
    ldesc = st.text_input("What are you selling?", key="ld")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("START LIVE", type="primary"):
            if ltitle:
                st.session_state.lives.append({"user": st.session_state.user, "title
