import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="ROW Economy Market - Abuja", layout="wide")
st.header("ROW Economy Market - Abuja")

# --- YOUR LINKS: Change these 2 if yours are different ---
SHEET_CSV = st.secrets.get("SHEET_CSV", "")
WEBAPP_URL = st.secrets.get("WEBAPP_URL", "")

def clean_phone(p):
    if p is None:
        return ""
    s = str(p).strip().replace(" ", "").replace("-", "").replace("+", "")
    if s.endswith(".0"):
        s = s[:-2]
    if s.startswith("0"):
        s = "234" + s[1:]
    if s.startswith("234") is False and len(s) == 10:
        s = "234" + s
    return "".join([c for c in s if c.isdigit()])

def show_price(p):
    try:
        f = float(str(p).replace(",", ""))
        if f == int(f):
            return str(int(f))
        return str(f)
    except:
        return str(p)

def show_phone(p):
    s = str(p).strip()
    if s.endswith(".0"):
        s = s[:-2]
    return s

def load_products():
    try:
        if not SHEET_CSV:
            return pd.DataFrame()
        df = pd.read_csv(SHEET_CSV, dtype=str).fillna("")
        df.columns = [c.strip().lower() for c in df.columns]
        df = df[df.get("location", "") != "WAITLIST"]
        if "name" not in df.columns:
            return pd.DataFrame()
        df = df[df["name"].astype(str).str.strip() != ""]
        df = df.drop_duplicates(subset=["name", "price", "location"], keep="last")
        df = df.reset_index(drop=True)
        return df
    except Exception as e:
        st.error("Could not load products: " + str(e))
        return pd.DataFrame()

products = load_products()

# --- MAP ---
st.subheader("LIVE MAP")
if not products.empty and "lat" in products.columns and "lon" in products.columns:
    mdf = products.copy()
    mdf["lat"] = pd.to_numeric(mdf["lat"], errors="coerce")
    mdf["lon"] = pd.to_numeric(mdf["lon"], errors="coerce")
    mdf = mdf.dropna(subset=["lat", "lon"])
    if not mdf.empty:
        st.map(mdf[["lat", "lon"]])
    else:
        st.map(pd.DataFrame({"lat": [9.066], "lon": [7.483]}))
else:
    st.map(pd.DataFrame({"lat": [9.066], "lon": [7.483]}))

# --- SEARCH BY LOCATION ---
st.subheader("Search by Location")
loc_search = st.text_input("Type location e.g Wuse, Garki, Lagos, Ibadan", key="loc_search")
show_products = products
if loc_search and not products.empty:
    show_products = products[products["location"].astype(str).str.contains(loc_search, case=False, na=False)]
    if show_products.empty:
        st.warning("No product for " + loc_search + " yet.")
    else:
        st.success("Found " + str(len(show_products)) + " for " + loc_search)

if show_products.empty:
    st.info("No products yet. Be the first to post!")
else:
    rev = show_products.iloc[::-1]
for _, row in rev.iterrows():
