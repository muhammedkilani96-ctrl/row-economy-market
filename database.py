import streamlit as st
import base64

def get_adverts():
    if "adverts" not in st.session_state:
        st.session_state.adverts = []
    return st.session_state.adverts

def add_advert(business, what, price, whatsapp, area, state, image=None):
    ads = get_adverts()
    img_str = None
    if image:
        img_str = base64.b64encode(image.getvalue()).decode()
    ads.append({
        "business": business,
        "what": what,
        "price": price,
        "whatsapp": whatsapp,
        "area": area,
        "state": state,
        "image": img_str
    })

def count_adverts():
    return len(get_adverts())
