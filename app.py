import streamlit as st
import requests
import uuid
import urllib.parse

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
HEADERS = {"apikey": KEY, "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

# --- PUT YOUR WALLET ADDRESSES HERE (or in Streamlit Secrets) ---
USDT_TRC20 = st.secrets.get("USDT_WALLET", "TYourUSDTAddressHere")  # Replace with your real TRC20 address
BTC_ADDRESS = st.secrets.get("BTC_WALLET", "bc1qYourBTCAddressHere") # Replace
# You can also put for .env: USDT_WALLET = "T..."

st.set_page_config(page_title="Row Economy Market", layout="wide")
st.title("Row Economy Market - PERMANENT")

# --- NEW: Live Crypto Ticker ---
try:
    cg = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd,
