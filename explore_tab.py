import streamlit as st
from database import get_adverts
import base64

def show(area, state):
    st.subheader(f"Explore {area}")
    ads = get_adverts()
    if not ads:
        st.info("No adverts yet. Be first to post!")
        return
    for i, ad in enumerate(reversed(ads)):
        if ad.get("image"):
            st.image(base64.b64decode(ad["image"]), width=300)
        st.write(f"**{ad['business']}** - {ad['what']} - N{ad['price']}")
        st.link_button(f"Chat {ad['business']} on WhatsApp", f"https://wa.me/{ad['whatsapp']}?text=Hi, I saw {ad['what']} on Row Economy", key=f"wa{i}")
        st.divider()
