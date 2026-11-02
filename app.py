import streamlit as st
import streamlit.components.v1 as comp
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Row Economy - Wuse 2 Abuja Market", layout="centered")

st.markdown("<style>.stApp{background:#000000;}h1,h2,h3{color:#00FF66;}p,div,label,span{color:white;} .stButton>button{background:#006600;color:white;border:1px solid #00FF66; border-radius:10px;} .stTabs [data-baseweb=\"tab\"]{color:white;} .advert-card{background:#111111; border:1px solid #00FF66; border-radius:12px; padding:12px; margin-bottom:10px;}</style>", unsafe_allow_html=True)

st.title("Row Economy")

# --- REAL GPS ---
try:
    with open("location.html", "r") as f:
        gps = f.read()
    comp.html(gps, height=180)
except:
    st.info("Add location.html file for Real GPS - Use My Real Location")

# --- STATE & AREA ---
state = st.selectbox("State", ["Abuja","Lagos","Kano","Rivers","Kaduna"])
area = st.text_input("Area / Market", "Wuse 2 Abuja")

# --- DATABASE FILE ---
CSV_FILE = "adverts.csv"
if not os.path.exists(CSV_FILE):
    df_init = pd.DataFrame(columns=["date","state","area","business","what","price","whatsapp"])
    df_init.to_csv(CSV_FILE, index=False)

t1, t2, t3, t4, t5 = st.tabs(["Home","Advertise Here","Explore","Chats","Profile"])

with t1:
    st.subheader(f"Food | Cloth | Cars | Events for {area}")
    st.write(f"Welcome to {area}, {state} market - Real Location enabled")
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        df_area = df[df["area"].str.contains(area, case=False, na=False) | df["state"].str.contains(state, case=False, na=False)]
        st.write(f"**{len(df_area)} adverts live for {area}**")
        st.link_button("📍 View on Google Maps", "https://maps.google.com/?q=" + area.replace(" ", "+"))

with t2:
    st.subheader("Advertise Here - Post Your Business")
    biz = st.text_input("Business Name", placeholder="e.g. Mama Food Wuse 2")
    what = st.text_input("What you sell", placeholder="e.g. Jollof Rice, iPhone 14")
    price = st.number_input("Price N", 100, 10000000, 2000)
    whatsapp = st.text_input("WhatsApp Number", placeholder="e.g. 08012345678")
    st.caption
