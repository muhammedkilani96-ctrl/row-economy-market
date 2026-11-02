import streamlit as st
def init_db():
    if "adverts" not in st.session_state:
        st.session_state.adverts = []
def add_advert(biz, what, price, wa, area, state):
    init_db()
    st.session_state.adverts.append({"business":biz,"what":what,"price":price,"whatsapp":wa,"area":area,"state":state})
def get_adverts():
    init_db()
    return st.session_state.adverts
def count_adverts():
    init_db()
    return len(st.session_state.adverts)
