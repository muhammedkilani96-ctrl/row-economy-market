import streamlit as st
import urllib.parse
st.set_page_config(page_title="Row Economy", layout="wide")
st.markdown("<style>header{visibility:hidden} .block-container{padding:0px !important} .stApp{background:#F8F8F8}</style>", unsafe_allow_html=True)
if "goods" not in st.session_state:
    st.session_state.goods = []
    st.session_state.goods.append("Horlance Auto Cooling Ltd|Car AC Repair|Osun & Oyo State|09046044472|Car Mart|YES|https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=400")
    st.session_state.goods.append("Mama T|Bag of Rice|Abuja|09046044472|Food|YES|https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400")
qp = st.query_params
cat_now = qp.get("cat", "All")
st.markdown("<div style='background:#00A651;padding:16px 14px 26px 14px;border-radius:0 0 28px 28px;color:white'><div style='display:flex;justify-content:space-between;align-items:center'><span style='font-size:26px'>☰</span><b style='font-size:26px'>ROW ECONOMY</b><span style='background:#FF8A00;width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px'>👤</span></div></div>", unsafe_allow_html=True)
search = st.text_input("S", placeholder="Ask Mama Oloja - What are you looking for today?", label_visibility="collapsed")
st.markdown("<div style='display:flex;justify-content:space-between;padding:14px 14px 8px'><b style='font-size:21px;color:#111'>Categories</b><a href='?cat=All' style='color:#00A651;font-weight:bold;text-decoration:none'>See all ></a></div>", unsafe_allow_html=True)
st.markdown("<div style='display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px;padding:0 14px'>
