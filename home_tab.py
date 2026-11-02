import streamlit as st
from database import count_adverts
def show(area, state):
    st.subheader(f"For {area}")
    st.write(f"{count_adverts()} adverts in {state}")
    st.link_button("View Map",f"https://maps.google.com/?q={area}")
