import streamlit as st
from database import get_adverts
def show(area,state):
    st.subheader("Chats")
    st.write("Your advert buyers will chat you on WhatsApp 08116911722")
    for a in get_adverts()[:5]:
        st.write(f"📩 {a['business']} - {a['what'][:30]}...")
