import streamlit as st
from database import count_adverts
import advertise_tab
import home_tab
import explore_tab
import chats_tab
import profile_tab

st.set_page_config(page_title="Row Economy Market", layout="wide")

try:
    with open("style.html", "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)
except:
    pass

if "area" not in st.session_state:
    st.session_state.area = "Wuse 2 Abuja"
    st.session_state.state = "Abuja"

if "chats" not in st.session_state:
    st.session_state.chats = []

area = st.session_state.area
state = st.session_state.state

st.markdown(f"<h1 style='color:#00FF88;'>Row Economy - {area}</h1>", unsafe_allow_html=True)
st.write(f"{count_adverts()} adverts in {state}")

t1, t2, t3, t4, t5 = st.tabs(["Home", "Explore", "Advertise Here", "Chats", "Profile"])

with t1:
    home_tab.show(area, state)
with t2:
    explore_tab.show(area, state)
with t3:
    advertise_tab.show(area, state)
with t4:
    chats_tab.show(area, state)
with t5:
    profile_tab.show(area, state)
