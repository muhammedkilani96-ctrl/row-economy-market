import streamlit as st
from database import get_adverts
def show(area, state):
    st.subheader(f"Explore {area}")
    st.link_button("View Map",f"https://maps.google.com/?q={area}")
    ads=get_adverts()
    if not ads:
        st.write("No adverts yet")
        return
    for i,ad in enumerate(reversed(ads)):
        st.write(f"{ad['business']} - {ad['what']} - N{ad['price']}")
        st.link_button("WhatsApp",f"https://wa.me/{ad['whatsapp']}",key=f"w{i}")
        st.divider()
