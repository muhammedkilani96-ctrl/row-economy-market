import streamlit as st
import urllib.parse
from datetime import datetime

st.set_page_config(page_title="Row Economy", layout="centered")

if 'ads' not in st.session_state:
    st.session_state.ads = 0

WHATSAPP = "2348116911722"
NUM = "08116911722"

st.title("Row Economy Market")
st.write(f"Abuja Seller - Order via {NUM}")
st.info(f"FREE Ads Today: {st.session_state.ads}/10")

people = st.number_input("Number of people", 1, 500, 10)
meal = st.selectbox("Wetin you cook?", ["Spaghetti", "Rice", "Indomie", "Full Package"])

# Simple calc
spag = (people + 3)//4
rice = (people + 4)//5
oil = 1
tom = 1
chick = people//5
indo = people

needs = {}
if meal == "Spaghetti":
    needs = {"Spaghetti": spag, "Oil": oil, "Tomatoes": tom}
elif meal == "Rice":
    needs = {"Rice": rice, "Oil": oil, "Chicken": chick}
elif meal == "Indomie":
    needs = {"Indomie": indo, "Oil": oil}
else:
    needs = {"Rice": rice, "Spaghetti": spag, "Oil": 2}

# Prices
prices = {"Spaghetti": 1000, "Rice": 1500, "Indomie": 350, "Oil": 1500, "Tomatoes": 1200, "Chicken": 4000}

total = 0
for k,v in needs.items():
    total += prices[k]*v

st.subheader(f"For {people} people - {meal}")
for k,v in needs.items():
    st.metric(f"{k} x {v}", f"N{prices[k]*v}")

st.write(f"### Total: N{total}")
st.caption("Wuse N500, Garki N1000, Other N1500")

msg = f"Hello I want order for {people} people {meal} total N{total} location:"
link = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg)}"
st.link_button(f"Order via WhatsApp {NUM}", link, use_container_width=True)

st.divider()
st.subheader("Advertise (10 FREE)")
with st.form("ad"):
    name = st.text_input("Shop Name")
    area = st.selectbox("Area", ["Wuse","Garki","Kubwa","Other"])
    item = st.text_area("Wetin you sell?")
    ok = st.form_submit_button("Post Ad")
    if ok:
        if st.session_state.ads < 10:
            st.session_state.ads += 1
            st.success(f"Posted! Left: {10-st.session_state.ads}")
        else:
            st.error("Pay N200 for more ads")
