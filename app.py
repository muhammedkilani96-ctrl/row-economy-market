import streamlit as st

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="wide")

if "ad_count" not in st.session_state:
    st.session_state.ad_count = 0

st.title("🛒 Naija Market AI - Row Economy")
st.write("Type wetin you wan cook, we calculate how much you need!")

people = st.number_input("How many people you wan cook for?", min_value=1, value=10)

if people:
    spaghetti_packs = (people + 3) // 4
    oil_bottles = 1 if people <= 10 else 2
    rice_kg = people * 0.15
    
    st.success(f"For {people} people:")
    st.write(f"🍝 Spaghetti: {spaghetti_packs} packs @ N1000 = N{spaghetti_packs*1000}")
    st.write(f"🛢️ Groundnut Oil: {oil_bottles} bottle @ N4500")
    st.write(f"🍚 Rice: {rice_kg:.1f}kg")
    
    # YOUR REAL NUMBER - 08116911722
    wa_link = f"https://wa.me/2348116911722?text=Hello%20Row%20Economy!%20I%20want%20to%20order%20for%20{people}%20people:%20{spaghetti_packs}%20spaghetti%20packs"
    st.link_button("💬 Order via WhatsApp - 08116911722", wa_link)

st.divider()

st.title("Advert Room - 10 Ads Free Per Day")

if st.session_state.ad_count < 10:
    st.write(f"Ads seen today: {st.session_state.ad_count}/10 FREE")
    if st.button("View Advert"):
        st.session_state.ad_count += 1
        st.balloons()
        st.success("Ad watched! Thanks!")
        st.rerun()
else:
    st.error(f"Ads seen today: {st.session_state.ad_count}/10 - FREE FINISHED!")
   
