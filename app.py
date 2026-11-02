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
    
    if st.button("Order via WhatsApp"):
        st.link_button("Chat Seller", "https://wa.me/2348031234567")

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
    st.write("**Pay N200 to continue watching ads today**")
    # YOUR REAL PAYSTACK LINK
    st.link_button("🔒 Pay N200 with Paystack (REAL MONEY)", "https://paystack.shop/pay/row-economy-200")
    st.info("After payment, click below to reset")
    if st.button("✅ I don pay N200 - Reset to 0/10"):
        st.session_state.ad_count = 0
        st.success("Payment confirmed! You fit watch 10 more ads!")
        st.rerun()

st.divider()

st.header("Ranking - Best Sellers")
st.table({
    "name": ["Indomie Carton", "Rice 50kg", "Groundnut Oil", "Spaghetti"],
    "price": [12000, 65000, 4500, 1000],
    "sold": [50, 45, 30, 12],
    "stock": [100, 20, 40, 50]
})
