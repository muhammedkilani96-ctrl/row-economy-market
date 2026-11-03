import streamlit as st
import requests
import uuid
import urllib.parse

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
HEADERS = {"apikey": KEY, "Authorization": "Bearer " + KEY, "Content-Type": "application/json"}

USDT_TRC20 = st.secrets.get("USDT_WALLET", "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb")
BTC_ADDRESS = st.secrets.get("BTC_WALLET", "bc1qxy2kgy6jxc4ccklm3v3r7h5a")

st.set_page_config(page_title="Row Economy Market", layout="wide")
st.title("Row Economy Market - PERMANENT")
st.info("We accept Naira, USDT, BTC")
