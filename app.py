import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy", layout="wide")

# DATA
if "goods" not in st.session_state:
    st.session_state.goods = []
    st.session_state.goods.append("Horlance|Car AC Repair|25000|Osun & Oyo|09046044472|Car Mart|YES")
    st.session_state.goods.append("Mama T|Bag of Rice|45000|Abuja|09046044472|Food|YES")

if "cat" not in st.session_state:
    st.session_state.cat = "All"

# HEADER - GREEN LIKE K&K
st.markdown("<h1 style='background:#00A651;color:white;text-align:center;padding:15px;border-radius:0 0 20px 20px'>ROW ECONOMY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Ask Mama Oloja - What are you looking for today?</p>", unsafe_allow_html=True)
search = st.text_input("Search", placeholder="Ask Mama Oloja...")

# CATEGORIES
st.write("### Categories")
a1, a2, a3, a4 = st.columns(4)
with a1:
    if st.button("Perfume"):
        st.session_state.cat = "Perfume"
    if st.button("Car Mart"):
        st.session_state.cat = "Car Mart"
with a2:
    if st.button("Clothes"):
        st.session_state.cat = "Clothes"
    if st.button("Services"):
        st.session_state.cat = "Services"
with a3:
    if st.button("Phones"):
        st.session_state.cat = "Phones"
    if st.button("Tickets"):
        st.session_state.cat = "Tickets"
with a4:
    if st.button("Food"):
        st.session_state.cat = "Food"
    if st.button("Chat Rooms"):
        st.session_state.cat = "Chat Rooms"

st.write("Showing: " + st.session_state.cat)
if st.button("Show All"):
    st.session_state.cat = "All"
    st.rerun()

# FEATURED LISTING - CARD STYLE LIKE K&K
st.write("### Featured Listing")
for line in st.session_state.goods:
    parts = line.split("|")
    seller = parts[0]
    name = parts[1]
    price = parts[2]
    loc = parts[3]
    wa = parts[4]
    cat = parts[5]
    ver = parts[6]
    if st.session_state.cat != "All":
        if cat != st.session_state.cat:
            continue
    if search:
        if search.lower() not in name.lower():
            continue
    # CARD
    st.markdown("<div style='background:white;border:1px solid #eee;border-radius:16px;padding:16
