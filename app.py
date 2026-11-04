import streamlit as st
import pandas as pd
import requests
import re

st.set_page_config(page_title="ROW ECONOMY MARKET", layout="wide")

SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxD0TcnR6NayT4pCYslMDaH8dXvFrQhmxDLANC1wqcOs006OmF8frhUOCY_m34CHqfv/exec"
SHEET_ID = "1DMODScWNcjddoxARnCFQIp3jIrqLZ0EI770GaLuYXVA"
SHEET_CSV = "https://docs.google.com/spreadsheets/d/" + SHEET_ID + "/gviz/tq?tqx=out:csv&sheet=Sheet1"

def send_to_sheet(payload):
    try:
        r = requests.post(SCRIPT_URL, json=payload, timeout=15)
        return r.status_code == 200
    except:
        return False

def load_data():
    try:
        df = pd.read_csv(SHEET_CSV)
        df.columns = [c.strip().lower() for c in df.columns]
        return df
    except:
        return pd.DataFrame()

def clean_phone(p):
    if pd.isna(p) or str(p) == "":
        return ""
    s = str(p).strip()
    if s.endswith(".0"):
        s = s[:-2]
    c = re.sub(r"\D", "", s)
    if c.startswith("0"):
        c = "234" + c[1:]
    return c

def show_phone(p):
    c = clean_phone(p)
    if c.startswith("234"):
        c = "0" + c[3:]
    return c

def show_price(p):
    try:
        return str(int(float(p)))
    except:
        return str(p)

if "q" not in st.session_state:
    st.session_state.q = ""
if "notfound" not in st.session_state:
    st.session_state.notfound = False

st.title("ROW ECONOMY MARKET - Abuja")
st.write("Buy and Sell Near You. Chat Seller Direct on WhatsApp.")
st.write("Help: 08116911722")
df = load_data()
products = pd.DataFrame()
waitlist = pd.DataFrame()
if not df.empty and "location" in df.columns:
    products = df[df["location"].astype(str).str.upper() != "WAITLIST"].copy()
    waitlist = df[df["location"].astype(str).str.upper() == "WAITLIST"].copy()
    products = products.drop_duplicates(subset=["name", "price", "location"], keep="last")

st.header("LIVE MAP - Abuja")
st.map(pd.DataFrame({"lat": [9.066], "lon": [7.483]}))

if products.empty:
    st.info("No products yet. Be the first to post!")
else:
    for _, row in products.iloc[::-1].iterrows():
        nm = row.get("name", "")
        pr = row.get("price", "")
        loc = row.get("location", "")
        ph = row.get("phone", "")
        if pd.isna(ph) or str(ph) == "":
            ph = row.get("whatsapp", "")
        st.write("**" + str(nm) + " - N" + show_price(pr) + " - " + str(loc) + "**")
        st.write(str(loc))
        cl = clean_phone(ph)
        if cl:
            st.link_button("WhatsApp " + show_phone(ph), "https://wa.me/" + cl + "?text=Hi, I want " + str(nm))
        st.divider()
