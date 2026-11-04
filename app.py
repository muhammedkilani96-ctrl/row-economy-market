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
    c = re.sub(r'\D', '', str(phone))
    if c.startswith("0"):
        c = "234" + c[1:]
    return c

# ===== HEADER =====
st.title("ROW ECONOMY MARKET - Abuja")
st.write("Buy and Sell Near You. Chat Seller Direct on WhatsApp.")
st.write("Help: 08116911722")

df = load_products()
# Remove waitlist rows from marketplace view
products = pd.DataFrame()
if not df.empty:
    if 'location' in df.columns:
        products = df[df['location'].astype(str).str.upper() != "WAITLIST"].copy()
    else:
        products = df.copy()

# ===== LIVE MAP =====
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

# ===== PRODUCT LIST =====
if products.empty:
    st.info("No products yet. Be the first to post!")
else:
    for _, row in products.iloc[::-1].iterrows():
        name = row.get('name', '')
        price = row.get('price', '')
        location = row.get('location', '')
        phone = row.get('phone', '')
        if pd.isna(phone) or str(phone) == "":
            phone = row.get('whatsapp', '')
        st.write(f"**{name} - ₦{price} - {location}**")
        clean = clean_phone(phone)
        if clean:
            st.link_button(f"Chat Seller - {name}", f"https://wa.me/{clean}?text=Hi, I want {name} from ROW Economy Market")
        st.divider()

# ===== ASK AI =====
st.header("🤖 Ask AI - Find Product Fast")
st.write("Example: I need Rice for Wuse")
ai_q = st.text_input("What do you need?", key="ai_q", placeholder="I need rice")
if st.button("Ask AI"):
    if not ai_q:
        st.warning("Type wetin you need")
    elif products.empty:
        st.info("No products yet")
    else:
        # Simple AI: remove stop words, match keywords
        stop = {"i", "need", "want", "for", "in", "a", "an", "the", "please", "buy", "get", "find", "me"}
        words = [w.lower() for w in re.findall(r'\w+', ai_q) if w.lower() not in stop]
        mask = pd.Series([False]*len(products))
        for w in words:
            mask = mask | products.astype(str).apply(lambda x: x.str.contains(w, case=False, na=False)).any(axis=1)
        found = products[mask]
        if not found.empty:
            st
