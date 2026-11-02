import streamlit as st
import urllib.parse
from datetime import datetime

st.set_page_config(page_title="Row Economy", layout="centered")

if 'ads' not in st.session_state:
    st.session_state.ads = 0

WHATSAPP = "2348116911722"
NUM = "08116911722"

st.title("Row Economy Market")
st.write(f"Abuja - Food & Events - WhatsApp {NUM}")

tab1, tab2 = st.tabs(["Food Market", "Event Tickets"])

with tab1:
    people = st.number_input("Number of people", 1, 500, 10, key="p1")
    meal = st.selectbox("Wetin you cook?", ["Spaghetti","Rice","Indomie","Full Package"])
    spag = (people + 3)//4
    rice = (people + 4)//5
    needs = {}
    if meal == "Spaghetti":
        needs = {"Spaghetti": spag, "Oil": 1}
    elif meal == "Rice":
        needs = {"Rice": rice, "Oil": 1}
    elif meal == "Indomie":
        needs = {"Indomie": people, "Oil": 1}
    else:
        needs = {"Rice": rice, "Spaghetti": spag, "Oil": 2}
    prices = {"Spaghetti":1000,"Rice":1500,"Indomie":350,"Oil":1500}
    total = sum(prices[k]*v for k,v in needs.items())
    for k,v in needs.items():
        st.metric(f"{k} x {v}", f"N{prices[k]*v}")
    st.write(f"### Total: N{total}")
    msg = f"Hello I want food for {people} people {meal} total N{total}"
    link = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg)}"
    st.link_button(f"Order Food {NUM}", link, use_container_width=True)

with tab2:
    st.subheader("Sell Your Event Ticket")
    st.write("Anybody fit sell ticket here")
    event = st.text_input("Event Name", "e.g. Abuja Music Concert")
    date = st.date_input("Event Date")
    venue = st.text_input("Venue", "e.g. Wuse Park")
    price = st.number_input("Ticket Price N", 500, 100000, 2000)
    qty = st.number_input("How many tickets you want?", 1, 20, 1)
    total_t = price * qty
    st.write(f"### Total for {qty} tickets: N{total_t}")
    msg2 = f"Hello I want {qty} tickets for {event} on {date} at {venue} total N{total_t}"
    link2 = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg2)}"
    st.link_button(f"Buy Tickets via {NUM}", link2, use_container_width=True)
    st.divider()
    st.caption("Sellers: Post your event below - 10 FREE ads daily")

st.divider()
st.subheader("Advertise (10 FREE per day)")
with st.form("ad"):
    name = st.text_input("Shop or Event Name")
    area = st.selectbox("Area", ["Wuse","Garki","Maitama","Kubwa","Lugbe","Other"])
    cat = st.selectbox("Category", ["Food","Event Ticket","Other"])
    item = st.text_area("Wetin you dey sell?")
    ok = st.form_submit_button("Post Ad FREE")
    if ok:
        if st.session_state.ads < 10:
            st.session_state.ads += 1
            st.success(f"{cat} Ad Posted! Left: {10-st.session_state.ads}")
        else:
            st.error("Pay N200 for more ads - muhammedkilani96@gmail.com")
