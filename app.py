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
