import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy", layout="centered")

if 'ads' not in st.session_state:
    st.session_state.ads = 0

WHATSAPP = "2348116911722"
NUM = "08116911722"

st.title("Row Economy Market")
st.write(f"Abuja Super Market - {NUM}")
st.caption("Food | Event Tickets | Clothes - 10 FREE Ads Daily")

tab1, tab2, tab3 = st.tabs(["Food", "Events", "Cloth Store"])

with tab1:
    people = st.number_input("Number of people", 1, 500, 10, key="f1")
    meal = st.selectbox("Food", ["Spaghetti","Rice","Indomie","Full Package"], key="f2")
    spag = (people + 3)//4
    rice = (people + 4)//5
    needs = {"Spaghetti": spag} if meal=="Spaghetti" else {"Rice": rice} if meal=="Rice" else {"Indomie": people} if meal=="Indomie" else {"Rice": rice, "Spaghetti": spag}
    prices = {"Spaghetti":1000,"Rice":1500,"Indomie":350}
    total = sum(prices[k]*v for k,v in needs.items())
    for k,v in needs.items():
        st.metric(f"{k} x {v}", f"N{prices[k]*v}")
    st.write(f"Total: N{total}")
    msg = f"Food order for {people} people {meal} total N{total}"
    st.link_button(f"Order Food {NUM}", f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg)}", use_container_width=True)

with tab2:
    event = st.text_input("Event Name", "Abuja Concert")
    venue = st.text_input("Venue", "Wuse Park")
    price = st.number_input("Ticket Price", 500, 100000, 2000, key="e1")
    qty = st.number_input("Qty", 1, 20, 1, key="e2")
    total_t = price*qty
    st.write(f"Total: N{total_t}")
    msg2 = f"I want {qty} tickets for {event} at {venue} total N{total_t}"
    st.link_button(f"Buy Tickets {NUM}", f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg2)}", use_container_width=True)

with tab3:
    st.subheader("Cloth Store - Abuja")
    cloth = st.selectbox("Wetin you want?", ["Men
