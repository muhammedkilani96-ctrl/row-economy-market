import streamlit as st
if "cat" not in st.session_state:
    st.session_state.cat="All"
if "goods" not in st.session_state:
    st.session_state.goods=[]
st.title("Row Market")
st.write("Row Market Abuja - FREE")
q=st.text_input("Ask Mama Oloja")
s=st.text_input("Type here to search")
st.subheader("Categories")
a,b,c,d=st.columns(4)
if a.button("Perfume"):
    st.session_state.cat="Perfume"
if b.button("Clothes"):
    st.session_state.cat="Clothes"
if c.button("Phones"):
    st.session_state.cat="Phones"
if d.button("Food"):
    st.session_state.cat="Food"
a2,b2,c2,d2=st.columns(4)
if a2.button("Car Mart"):
    st.session_state.cat="Car"
if b2.button("Services"):
    st.session_state.cat="Services"
if c2.button("Tickets"):
    st.session_state.cat="Tickets"
if d2.button("Chat Rooms"):
    st.session_state.cat="Chat"
st.write("Category:")
st.write(st.session_state.cat)
st.subheader("Featured Listing")
st.write("Horlance Auto Cooling Ltd")
st.write("VERIFIED")
st.write("Car AC Repair")
st.write("Osun & Oyo State")
st.write("WhatsApp 09046044472")
u="https://wa.me/2349046044472"
st.link_button("Chat on WhatsApp",u)
st.write("Mama Oloja AI:")
st.write("Welcome my dear, I can help")
st.write("you find best price.")
