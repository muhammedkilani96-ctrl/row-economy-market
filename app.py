import streamlit as st
import pandas as pd
import requests
import re

st.set_page_config(page_title="ROW ECONOMY MARKET - Abuja", layout="wide")

SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxD0TcnR6NayT4pCYslMDaH8dXvFrQhmxDLANC1wqcOs006OmF8frhUOCY_m34CHqfv/exec"
SHEET_ID = "1DMODScWNcjddoxARnCFQIp3jIrqLZ0EI770GaLuYXVA"
SHEET_CSV = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=Sheet1"

def send_to_sheet(payload):
    try:
        r = requests.post(SCRIPT_URL, json=payload, timeout=15)
        return r.status_code == 200
    except:
        return False

def load_products():
    try:
        df = pd.read_csv(SHEET_CSV)
        df.columns = [c.strip().lower() for c in df.columns]
        return df
    except:
        return pd.DataFrame()

def clean_phone(phone):
    if pd.isna(phone) or str(phone) == "":
        return ""
    s = str(phone).strip()
    if s.endswith(".0"):
        s = s[:-2]
    c = re.sub(r'\D', '', s)
    if c.startswith("0"):
        c = "234" + c[1:]
    return c

def fmt_phone(phone):
    c = clean_phone(phone)
    if c.startswith("234"):
        c = "0" + c[3:]
    return c

def fmt_price(price):
    try:
        return f"{int(float(price)):,}"
    except:
        return str(price)

if "ai_query" not in st.session_state:
    st.session_state.ai_query = ""
if "ai_not_found" not in st.session_state:
    st.session_state.ai_not_found = False

st.title("ROW ECONOMY MARKET - Abuja")
st.write("Buy and Sell Near You. Chat Seller Direct on WhatsApp.")
st.write("Help: 08116911722")

df = load_products()
products = pd.DataFrame()
waitlist = pd.DataFrame()
if not df.empty:
    if 'location' in df.columns:
        products = df[df['location'].astype(str).str.upper() != "WAITLIST"].copy()
        waitlist = df[df['location'].astype(str).str.upper() == "WAITLIST"].copy()
        products = products.drop_duplicates(subset=['name','price','location'], keep='last')
    else:
        products = df.copy()

st.header("LIVE MAP - Abuja")
if not products.empty and 'lat' in products.columns and 'lon' in products.columns:
    map_df = products.copy()
    map_df['lat'] = pd.to_numeric(map_df['lat'], errors='coerce')
    map_df['lon'] = pd.to_numeric(map_df['lon'], errors='coerce')
    map_df = map_df.dropna(subset=['lat', 'lon'])
    if not map_df.empty:
        st.map(map_df[['lat', 'lon']])
    else:
        st.map(pd.DataFrame({'lat': [9.066], 'lon': [7.483]}))
else:
    st.map(pd.DataFrame({'lat': [9.066], 'lon': [7.483]}))

if products.empty:
    st.info("No products yet. Be the first to post!")
else:
    for _, row in products.iloc[::-1].iterrows():
        name = row.get('name', '')
        price = row.get('price', '')
        location = row.get('location', '')
        phone = row.get('phone
