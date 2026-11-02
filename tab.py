import streamlit as st
from database import add_advert

def show(area, state):
    st.subheader("Advertise Here")
    biz = st.text_input("Business Name", key="biz_name")
    what = st.text_input("What you sell", key="what_sell")
    price = st.number_input("Price N", 100, 10000000, 2006, key="price")
    whatsapp = st.text_input("WhatsApp Number", value="08116911722", key="wa_num")
    st.write("Use 080 format, we auto convert")

    if st.button("Post Advert Now"):
        if biz and what and whatsapp:
            wa = whatsapp.strip().replace(" ", "").replace("+", "")
            if wa.startswith("0"):
                wa = "234" + wa[1:]
            add_advert(biz, what, price, wa, area, state)
            st.success(f"Posted: {biz} - {what}")
            st.balloons()
            st.write("Go to Explore tab now!")
        else:
            st.error("Fill all fields")
