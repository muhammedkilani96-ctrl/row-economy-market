import streamlit as st
from database import add_advert

def show(area, state):
    st.subheader("Advertise Here")
    b = st.text_input("Business Name")
    w = st.text_input("What you sell")
    p = st.number_input("Price (N)", 100, 10000000, 2000)
    wa = st.text_input("WhatsApp Number", "08116911722")
    img = st.file_uploader("Upload Product Image", type=["jpg","png","jpeg"])
    
    if st.button("Post Now"):
        if not b or not w:
            st.error("Fill business and product")
            return
        num = wa.replace("0","234",1) if wa.startswith("0") else wa
        add_advert(b,w,p,num,area,state,img)
        st.success("Posted with image!")
        st.balloons()
