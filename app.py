import streamlit as st
import urllib.parse
from datetime import datetime

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="centered")

if 'ads_today' not in st.session_state:
    st.session_state.ads_today = 0
if 'ads_date' not in st.session_state:
    st.session_state.ads_date = datetime.now().date()
if st.session_state.ads_date != datetime.now().date():
    st.session_state.ads_today = 0
    st.session_state.ads_date = datetime.now().date()

WHATSAPP = "2348116911722"
DISPLAY_NUM = "08116911722"
PAYSTACK_EMAIL = "muhammedkilani96@gmail.com"

PRICES = {
    "Spaghetti 500g": 1000,
    "Rice 1kg (Parboiled)": 1500,
    "Indomie (1 pack)": 350,
    "Groundnut Oil 1L": 1500,
    "Tomatoes 1kg": 1200,
    "Chicken 1kg": 4000,
    "Maggi (1 pack)": 50
}

st.title("Row Economy Market")
st.write(f"How many people? We calculate, you order via WhatsApp {DISPLAY_NUM}")
st.info(f"Abuja Seller: Wuse/Garki - Delivery N500-N1500 - Verified - FREE Ads: {st.session_state.ads_today}/10")

people = st.number_input("Number of people", min_value=1, max_value=500, value=10, step=1)
meal_type = st.selectbox("Wetin you wan cook?", ["Spaghetti Jollof", "Rice & Stew", "Indomie Special", "Full Package (Rice+Spag+Oil)"])

def calc():
    if meal_type == "Spaghetti Jollof":
        packs = max(1, (people + 3)//4)
        return {"Spaghetti 500g": packs, "Groundnut Oil 1L": max(1, packs//2), "Tomatoes 1kg": max(1, packs//2), "Maggi (1 pack)": packs*2}
    elif meal_type == "Rice & Stew":
        return {"Rice 1kg (Parboiled)": max(1, (people+4)//5), "Groundnut Oil 1L": 1, "Tomatoes 1kg": 1, "Chicken 1kg": max(1, people//5)}
    elif meal_type == "Indomie Special":
        return {"Indomie (1 pack)": people, "Groundnut Oil 1L": 1}
    else:
        return {"Rice 1kg (Parboiled)": max(1, (people+4)//5), "Spaghetti 500g
