import streamlit as st
import requests
import uuid
import urllib.parse

# --- SECRETS ---
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
HEADERS = {"apikey": KEY, "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

# --- YOUR CRYPTO WALLETS - EDIT HERE OR ADD TO STREAMLIT SECRETS ---
# Go to Streamlit Cloud > Your App > Settings > Secrets and add these two lines:
# USDT_WALLET = "TXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# BTC_WALLET = "bc1qXXXXXXXXXXXXXXXXXXXXXXXX"
USDT_TRC20 = st.secrets.get("USDT_WALLET", "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb")  # <-- REPLACE WITH YOURS
BTC_ADDRESS = st.secrets.get("BTC_WALLET", "bc1qxy2kgy6jxc4ccklm3v3r7h5a")  # <-- REPLACE WITH YOURS

st.set_page_config(page_title="Row Economy Market", layout="wide", page_icon="🛒")
st.title("Row Economy Market - PERMANENT")
st.caption("Naira + Crypto Marketplace | Lagos, Nigeria")

# --- LIVE CRYPTO TICKER ---
try:
   
