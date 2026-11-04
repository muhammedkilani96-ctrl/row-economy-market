import streamlit as st
import pandas as pd
import urllib.parse
import re

# --- YOUR REAL SHEET - ALREADY PUT ---
SHEET_ID = "1DMODScWNcjddoxARnCFQIp3jIrqLZ0EI770GaLuYXVA"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

st.set_page_config(page_title="ROW Economy Market - Abuja", layout="wide")
st.title("🛒 ROW ECONOMY MARKET - Abuja")
st.write("No more waka waka for market. Find am, Chat Seller, Buy am.")

@st.cache_data(ttl=30)
def load_products():
    try:
        df = pd.read_csv(CSV_URL)
        # Make headers small - so WhatsApp / whatsapp both work
        df.columns = [c.strip().lower() for c in df.columns]
        df = df.dropna(subset=["name"])
        # Clean lat/lon - remove "E2 =" if e still dey
        def clean_num(x):
            m = re.search(r"(\d+\.\d+|\d+)", str(x))
            return float(m.group(1)) if m else 9.066
        df["lat"] = df["lat"].apply(clean_num)
        df["lon"] = df["lon"].apply(clean_num)
        df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)
        # Clean whatsapp
        df["whatsapp"] = df["whatsapp"].astype(str).str.replace(r"\.0", "", regex=True)
        return df.to_dict("records")
    except Exception as e:
        return [
            {"name": "Fresh Rice 50kg", "price": 85000, "location": "Wuse Market, Abuja", "whatsapp": "2348116911722", "lat": 9.066, "lon": 7.483}
        ]

if "waitlist" not in st.session_state:
    st.session_state.waitlist = []
if "show_wait" not in st.session_state:
    st.session_state.show_wait = False
if "last_search" not in st.session_state:
    st.session_state.last_search = ""
if "new_products" not in st.session_state:
    st.session_state.new_products = []

all_products = load_products() + st.session_state.new_products

st.subheader("📍 Live Map - Abuja")
df_map = pd.DataFrame(all_products)
st.map(df_map, latitude="lat", longitude="lon", zoom=11)

st.subheader("Available Products")
for p in all_products:
    st.write(f"**{p['name']} - N{int(float(p['price'])):,} - {p['location']}**")
    msg = f"Hello, I see your {p['name']} for N{int(float(p['price']))} for {p['location']}. Is it still available?"
    link = f"https://wa.me/{p['whatsapp']}?text={urllib.parse.quote(msg)}"
    st.link_button(f"Chat Seller - {p['name']}", link)

st.divider()
st.subheader("🤖 Ask AI - Find Product Fast")
query = st.text_input("What do you need?", key="ai_input")
if st.button("Ask AI"):
    st.session_state.last_search = query
    q = query.lower()
    found = []
    for p in all_products:
        for word in str(p['name']).lower().split():
            if word in q and word not in ["50kg", "fresh"]:
                found.append(p)
                break
    if found:
        st.success(f"AI found {len(found)} for you:")
        for p in found:
            st.write(f"✅ **{p['name']} - N{int(float(p['price'])):,} - {p['location']}**")
            msg = f"Hello, I see your {p['name']} for N{int(float(p['price']))} for {p['location']}. Is it still available?"
            link = f"https://wa.me/{p['whatsapp']}?text={urllib.parse.quote(msg)}"
            st.link_button(f"Chat Seller - {p['name']}", link)
        st.session_state.show_wait = False
    else:
        st.warning(f"Sorry, we have no {query} available right now.")
        st.write("Do you want to **Post a Product** or **Wait** till we have an order of your request?")
        st.write("If you wait, **I'll text you directly on your WhatsApp** once we have what you requested.")
        st.session_state.show_wait = True

if st.session_state.show_wait:
    st.subheader("⏳ Wait For It - We Go Text You")
    st.write(f"You are waiting for: **{st.session_state.last_search}**")
    wa = st.text_input("Your WhatsApp Number (e.g 08116911722)", key="wait_wa")
    if st.button("Notify Me on WhatsApp"):
        if wa:
            st.session_state.waitlist.append({"request": st.session_state.last_search, "whatsapp": wa})
            st.success(f"Done! We don save your request for '{st.session_state.last_search}'. Once we have am, we go text you directly on WhatsApp {wa}. No need to dey check everyday.")
            st.session_state.show_wait = False
        else:
            st.error("Abeg put your WhatsApp number first.")

st.divider()
st.subheader("📦 Post Product - Show on Map")
st.info("New products go show instantly. To make am permanent for everybody, also add am as new row for your Google Sheet.")
with st.form("post_form"):
    name = st.text_input("Product Name (e.g Yam 10 tubers)")
    price = st.number_input("Price (Naira)", min_value=0, step=100)
    location = st.text_input("Location (e.g Garki Market, Abuja)")
    whatsapp = st.text_input("Your WhatsApp Number (e.g 08116911722)")
    submit = st.form_submit_button("Post Product")
    if submit and name and price and location and whatsapp:
        wa_clean = whatsapp.replace(" ", "").replace("+", "")
        if wa_clean.startswith("0"):
            wa_clean = "234" + wa_clean[1:]
        new_p = {"name": name, "price": price, "location": location, "whatsapp": wa_clean, "lat": 9.066, "lon": 7.483}
        st.session_state.new_products.append(new_p)
        st.success(f"Posted! {name} don show for Map now.")
        for w in st.session_state.waitlist:
            if any(word.lower() in name.lower() for word in w["request"].lower().split() if len(word) > 2):
                st.info(f"🔔 Somebody dey wait for this: {w['request']} - WhatsApp: {w['whatsapp']}. Text them now!")

st.write("---")
st.write("📲 ROW Economy Market | Abuja | 08116911722")
