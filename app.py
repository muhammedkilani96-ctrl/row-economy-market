import streamlit as st

st.set_page_config(page_title="Row Economy")

st.markdown("<style>.stApp{background:#000000;}h1{color:#00FF66;}h2,h3{color:white;}p,div,label{color:white;}.stButton>button{background:#006600;color:white;}</style>", unsafe_allow_html=True)

st.title("Row Economy")
st.write("Black - Green White Green - Advertise Here")

state = st.selectbox("State", ["Abuja","Lagos","Kano","Rivers","Kaduna"])
area = st.text_input("Area / Market", "Wuse 2 Abuja")

t1, t2, t3, t4, t5 = st.tabs(["Home","Advertise Here","Explore","Chats","Profile"])

with t1:
    st.subheader("Home")
    st.write("Location: " + area + ", " + state)
    st.write("Food | Cloth | Cars | Events")

with t2:
    st.header("Advertise Here")
    st.write("People will advertise here")
    biz = st.text_input("Business Name", "Mama Food")
    what = st.text_input("What you sell", "Jollof rice")
    price = st.number_input("Price N", 100, 10000000, 2000)
    phone = st.text_input("WhatsApp", "2348116911722")
    if st.button("Post Advert Now"):
        st.success("Posted: " + biz)
        st.balloons()

with t3:
    st.subheader("Explore")
    st.write("Yam - Kano - 5500")
    st.write("Ankara - Lagos - 12000")
    st.link_button("View on Google Maps", "https://maps.google.com/?q=" + area)

with t4:
    st.write("Chats")

with t5:
    st.link_button("Verify Car CMRIS", "https://cmris.npf.gov.ng")
    st.link_button("WhatsApp", "https://wa.me/2348116911722")

st.caption("Row Economy")
