import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy", layout="wide")

# DATA - short lines only
if "items" not in st.session_state:
    st.session_state.items = []
    st.session_state.items.append("Horlance|Car AC Repair|25000|Osun & Oyo|09046044472|Car Mart")
    st.session_state.items.append("Mama T|Bag of Rice|45000|Abuja|09046044472|Food")

if "cat" not in st.session_state:
    st.session_state.cat = "All"

# HEADER
st.markdown("<h1 style='background:#00A651;color:white;text-align:center;padding:15px;border-radius:0 0 20px 20px'>ROW ECONOMY</h1>", unsafe_allow_html=True)
search = st.text_input("Search", placeholder="Ask Mama Oloja - What are you looking for today?")

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

st.write("Showing:")
st.write(st.session_state.cat)
if st.button("Show All"):
    st.session_state.cat = "All"
    st.rerun()

# LISTINGS
st.write("### Featured Listing")
for line in st.session_state.items:
    parts = line.split("|")
    seller = parts[0]
    name = parts[1]
    price = parts[2]
    loc = parts[3]
    wa = parts[4]
    cat = parts[5]
    if st.session_state.cat != "All":
        if cat != st.session_state.cat:
            continue
    if search:
        if search.lower() not in name.lower():
            continue
    st.write("**" + seller + "**")
    st.write(name)
    st.write("Location: " + loc)
    st.write("WhatsApp: " + wa)
    st.write("Price: N" + price)
    msg = urllib.parse.quote("Hello " + seller)
    link = "https://wa.me/234" + wa[1:] + "?text=" + msg
    st.link_button("Chat on WhatsApp", link)
    st.write("---")

# MAMA OLOJA
st.write("### Mama Oloja AI")
st.write("Welcome my dear, I can help you find the best price.")
q = st.text_input("Ask Mama Oloja", placeholder="e.g. rice")
if q:
    st.success("Mama Oloja: I found " + q + " for you above. Chat seller now.")

# SELLER FORM
st.write("### Sell - FREE for First 10")
st.write("1 Name  2 WhatsApp  3 Location  4 Pictures  5 Price")
with st.form("f"):
    n1 = st.text_input("1. Your Name")
    n
