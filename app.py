import streamlit as st
import streamlit.components.v1 as comp

st.set_page_config(page_title="Row Economy")

st.markdown("<style>.stApp{background:#000000;}h1{color:#00FF66;}p,div,label{color:white;}.stButton>button{background:#006600;color:white;}</style>", unsafe_allow_html=True)

st.title("Row Economy")

# Load real GPS from location.html
try:
    with open("location.html", "r") as f:
        gps = f.read()
    comp.html(gps, height=180)
except:
    st.write("Add location.html file for Real GPS")

state = st.selectbox("State", ["Abuja","Lagos","Kano","Rivers","Kaduna"])
area = st.text_input("Area / Market", "Wuse 2 Abuja")

t1, t2, t3, t4, t5 = st.tabs(["Home","Advertise Here","Explore","Chats","Profile"])

with t1:
    st.write("Food | Cloth | Cars | Events for " + area)
with t2:
    biz = st.text_input("Business Name")
    what = st.text_input("What you sell")
    price = st.number_input("Price N", 100, 10000000, 2000)
    if st.button("Post Advert Now"):
        st.success("Posted: " + biz + " - " + what)
        st.balloons()
with t3:
    st.link_button("View on Google Maps", "https://maps.google.com/?q=" + area)
with t4:
    st.write("Chats")
with t5:
    st.link_button("Verify Car CMRIS", "https://cmris.npf.gov.ng")
    st.link_button("WhatsApp", "https://wa.me/2348116911722")

st.caption("Row Economy - Black + GWG + Real Location + Advertise")
