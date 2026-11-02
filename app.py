import streamlit as st

st.set_page_config(page_title="Row Economy Market", layout="wide")

# Initialize counter
if "ad_count" not in st.session_state:
    st.session_state.ad_count = 0

st.title("Advert Room - 10 Ads Free Per Day")

if st.session_state.ad_count < 10:
    st.write(f"Ads seen today: {st.session_state.ad_count}/10 FREE")
    if st.button("View Advert"):
        st.session_state.ad_count += 1
        st.success("Ad watched!")
        st.rerun()
else:
    st.error(f"Ads seen today: {st.session_state.ad_count}/10 - FREE FINISHED!")
    st.write("Pay N200 to continue")
    st.button("Pay N200 with Paystack")

st.divider()
st.header("Ranking")
st.table({
    "name": ["Indomie Carton", "Rice 50kg", "Groundnut Oil", "Spaghetti"],
    "price": [12000, 65000, 4500, 1000],
    "sold": [50, 45, 30, 12],
    "stock": [100, 20, 40, 50]
})
