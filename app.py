import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy", layout="wide")

# STYLE - MAKE IT LOOK LIKE K&K
st.markdown("<style>header{visibility:hidden} .block-container{padding:0px !important} div[data-testid='stVerticalBlock']{gap:0px}</style>", unsafe_allow_html=True)

# DATA
if "goods" not in st.session_state:
    st.session_state.goods = []
    st.session_state.goods.append("Horlance Auto Cooling Ltd|Car AC Repair|25000|Osun & Oyo State|09046044472|Car Mart|YES")
    st.session_state.goods.append("Mama T|Bag of Rice|45000|Abuja|09046044472|Food|YES")

if "cat" not in st.session_state:
    st.session_state.cat = "All"

# HEADER - GREEN
st.markdown("<div style='background:#00A651;padding:14px 14px 28px 14px;border-radius:0 0 24px 24px'><div style='display:flex;justify-content:space-between;align-items:center;color:white'><span style='font-size:24px'>☰</span><b style='font-size:24px'>ROW ECONOMY</b><span style='background:#FF8A00;width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:20px'>👤</span></div></div>", unsafe_allow_html=True)

# SEARCH BAR
search = st.text_input("S", placeholder="Ask Mama Oloja - What are you looking for today? 🎤", label_visibility="collapsed")
st.markdown("<style>input{border-radius:14px !important}</style>", unsafe_allow_html=True)

# CATEGORIES TITLE
st.markdown("<div style='display:flex;justify-content:space-between;padding:12px 14px 6px'><b style='font-size:20px'>Categories</b><span style='color:#00A651'>See all ></span></div>", unsafe_allow_html=True)

# CATEGORIES - 4x2 GRID
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("🧴\nPerfume"):
        st.session_state.cat = "Perfume"
with c2:
    if st.button("👕\nClothes"):
        st.session_state.cat = "Clothes"
with c3:
    if st.button("📱\nPhones"):
        st.session_state.cat = "Phones"
with c4:
    if st.button("🍲\nFood"):
        st.session_state.cat = "Food"

c5, c6, c7, c8 = st.columns(4)
with c5:
    if st.button("🚗\nCar Mart"):
        st.session_state.cat = "Car Mart"
with c6:
    if st.button("💼\nServices"):
        st.session_state.cat = "Services"
with c7:
    if st.button("🎟️\nTickets"):
        st.session_state.cat = "Tickets"
with c8:
    if st.button("💬\nChat Rooms"):
        st.session_state.cat = "Chat Rooms"

st.write("Showing: " + st.session_state.cat)
if st.button("Show All"):
    st.session_state.cat = "All"
    st.rerun()

# FEATURED LISTING
st.markdown("<div style='display:flex;justify-content:space-between;padding:10px 14px'><b style='font-size:20px'>Featured Listing</b><span style='color:#00A651'>See all ></span></div>", unsafe_allow_html=True)

for line in st.session_state.goods:
    p = line.split("|")
    seller = p[0]
    name = p[1]
    price = p[2]
    loc = p[3]
    wa = p[4]
    cat = p[5]
    ver = p[6]
    if st.session_state.cat != "All":
