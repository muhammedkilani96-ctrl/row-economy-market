import streamlit as st
from database import add_advert
def show(area, state):
    st.subheader("Advertise Here")
    b=st.text_input("Business")
    w=st.text_input("What you sell")
    p=st.number_input("Price",100,10000000,2000)
    wa=st.text_input("WhatsApp","08116911722")
    if st.button("Post Now"):
        num=wa.replace("0","234",1) if wa.startswith("0") else wa
        add_advert(b,w,p,num,area,state)
        st.success("Posted!")
        st.balloons()
