import streamlit as st
if "cat" not in st.session_state:
    st.session_state.cat="All"
if "goods" not in st.session_state:
    st.session_state.goods=[]
if "photos" not in st.session_state:
    st.session_state.photos=[]
if "orders" not in st.session_state:
    st.session_state.orders=[]
if "msgs" not in st.session_state:
    st.session_state.msgs=[]
if "page" not in st.session_state:
    st.session_state.page="Home"
css="<style>"
css+="[data-testid='stHorizontalBlock']"
css+="{flex-wrap:nowrap !important}"
css+="</style>"
st.markdown(css,unsafe_allow_html=True)
head="<div style='background:#16a34a;"
head+="padding:20px 10px;"
head+="border-radius:0 0 20px 20px;"
head+="text-align:center'>"
head+="<h1 style='color:white;margin:0'>"
head+="Row Market</h1>"
head+="<p style='color:white'>"
head+="Row Market Abuja - FREE</p></div>"
st.markdown(head,unsafe_allow_html=True)
s=st.text_input("Ask Mama Oloja")
q=s
st.markdown('<h3>Categories</h3>',unsafe_allow_html=True)
a,b=st.columns(2)
if a.button("Perfume",key="c1"):
    st.session_state.cat="Perfume"
if b.button("Clothes",key="c2"):
    st.session_state.cat="Clothes"
c,d=st.columns(2)
if c.button("Phones",key="c3"):
    st.session_state.cat="Phones"
if d.button("Food",key="c4"):
    st.session_state.cat="Food"
e,f=st.columns(2)
if e.button("Car Mart",key="c5"):
    st.session_state.cat="Car"
if f.button("Services",key="c6"):
    st.session_state.cat="Services"
g,h=st.columns(2)
if g.button("Tickets",key="c7"):
    st.session_state.cat="Tickets"
if h.button("Chat Rooms",key="c8"):
    st.session_state.cat="Chat"
st.write("Category:")
st.write(st.session_state.cat)
card="<div style='background:white;"
card+="padding:14px;border-radius:16px'>"
card+="<h4>Horlance Auto Cooling Ltd</h4>"
card+="<p>Car AC Repair</p>"
card+="<p>Osun & Oyo State</p>"
card+="<p>WhatsApp 09046044472</p></div>"
st.markdown(card,unsafe_allow_html=True)
u="https://wa.me/2349046044472"
st.link_button("Chat on WhatsApp",u)
mama="<div style='background:#dcfce7;"
mama+="padding:12px;border-radius:16px'>"
mama+="Mama Oloja AI: Welcome my dear"
mama+="</div>"
st.markdown(mama,unsafe_allow_html=True)
st.subheader("Sell FREE")
nm=st.text_input("Your Name",key="nm1")
pd=st.text_input("Product Name",key="pd1")
pr=st.text_input("Price",key="pr1")
ct1=["Perfume","Clothes","Phones","Food"]
ct2=["Car
