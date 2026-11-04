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
    products = products.reset_index(drop=True)
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
st.header("LIVE MAP - Abuja")


st.subheader("Search by Location")
loc_search = st.text_input("Type location e.g Wuse, Garki, Lagos, Ibadan", key="loc_search")
show_products = products
if loc_search and not products.empty:
    show_products = products[products["location"].astype(str).str.contains(loc_search, case=False, na=False)]
    if show_products.empty:
        st.warning("No product for " + loc_search + " yet.")
    else:
        st.success("Found " + str(len(show_products)) + " for " + loc_search)
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
st.header("Ask AI - Find Product Fast")
st.write("Example: I need Rice for Wuse")
ai_q = st.text_input("What do you need?", value=st.session_state.q, placeholder="I need rice", key="ai_input")
if st.button("Ask AI"):
    st.session_state.q = ai_q
    if not ai_q:
        st.warning("Type wetin you need")
        st.session_state.notfound = False
    elif products.empty:
        st.session_state.notfound = True
    else:
        stop = {"i", "need", "want", "for", "in", "a", "an", "the", "please", "buy", "get", "find", "me"}
        words = [w.lower() for w in re.findall(r"\w+", ai_q) if w.lower() not in stop]
        mask = pd.Series([False]*len(products))
        for w in words:
            mask = mask | products.astype(str).apply(lambda x: x.str.contains(w, case=False, na=False)).any(axis=1)
        found = products[mask]
        if not found.empty:
            st.session_state.notfound = False
            st.success("AI found " + str(len(found)) + " for you:")
            for _, row in found.iterrows():
                nm = row.get("name", "")
                pr = row.get("price", "")
                loc = row.get("location", "")
                ph = row.get("phone", "")
                if pd.isna(ph) or str(ph) == "":
                    ph = row.get("whatsapp", "")
                st.write("**" + str(nm) + " - N" + show_price(pr) + " - " + str(loc) + "**")
                cl = clean_phone(ph)
                if cl:
                    st.link_button("WhatsApp " + show_phone(ph), "https://wa.me/" + cl + "?text=Hi, I want " + str(nm))
        else:
            st.session_state.notfound = True

if st.session_state.notfound and st.session_state.q:
    qq = st.session_state.q
    st.warning("Sorry, we have no " + qq + " available right now.")
    st.write("Do you want to Post a Product or Wait till we have an order of your request?")
    st.header("Wait For It - We Go Text You")
    st.write("You are waiting for: " + qq)
    wphone = st.text_input("Your WhatsApp Number (e.g 08116911722)", key="wait_phone")
    if st.button("Notify Me on WhatsApp"):
        if not wphone:
            st.error("Put your WhatsApp number")
        else:
            wc = re.sub(r"\D", "", wphone)
            ok = send_to_sheet({"type": "waitlist", "request": qq, "name": qq, "phone": wc, "whatsapp": wc, "location": "WAITLIST"})
            if ok:
                st.success("Done! We don save your request. Once we have am, we go text you on WhatsApp " + wphone)
            else:
                st.error("Failed. Try again.")
    if st.button("I Want To Post A Product Instead"):
        st.session_state.notfound = False
        st.rerun()

st.divider()
st.header("Post Product - Show on Map")
with st.form("post_form"):
    pname = st.text_input("Product Name (e.g Beans 50kg)")
    pprice = st.number_input("Price (Naira)", min_value=0, value=0, step=100)
    ploc = st.text_input("Location (e.g Garki Market, Abuja)")
    pwa = st.text_input("Your WhatsApp Number (e.g 08116911722)")
    psubmit = st.form_submit_button("Post Product")
    if psubmit:
        if not pname or not ploc or not pwa or pprice == 0:
            st.error("Fill all fields")
        else:
            wac = re.sub(r"\D", "", pwa)
            ok = send_to_sheet({"type": "product", "name": pname, "price": pprice, "location": ploc, "phone": wac, "whatsapp": wac, "lat": 9.066, "lon": 7.483})
            if ok:
                st.success("Posted! " + pname + " don show for Map now.")
                st.balloons()
            else:
                st.error("Failed to post. Try again.")

st.divider()
st.write("ROW Economy Market | Abuja | 08116911722")
