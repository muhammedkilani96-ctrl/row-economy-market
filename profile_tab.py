import streamlit as st
def show(area,state):
    st.subheader("Profile")
    st.write("CEO: Muhammed"); st.write(f"Location: {area}, {state}")
    st.write(f"Ads Today: {st.session_state.ads_today}/10 Free + {st.session_state.paid_unlock} Paid")
    st.write(f"Live Gifts: {st.session_state.live_gifts} Cowries = N{st.session_state.live_gifts*10}")
    st.link_button("Contact CEO WhatsApp", "https://wa.me/2348116911722", use_container_width=True)
