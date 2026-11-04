import streamlit as st
import pandas as pd
import requests
import re

st.set_page_config(page_title="Abuja Market", layout="wide")

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

st.title("🛒 Abuja Market - Buy & Sell Near You")

tab1, tab2, tab3 = st.tabs(["🏠 Marketplace", "➕ Post Product", "📋 Waitlist"])

with tab1:
    df = load_products()
    if df.empty:
        st.info("No products yet. Be the first to post!")
    else:
        # Filter out waitlist rows
        if 'location' in df.columns:
            df = df[df['location'].astype(str).str.upper() != "WAITLIST"]
        search = st.text_input("🔍 Search product, e.g. Yam, Rice")
        if search:
            df = df[df.astype(str).apply(lambda x: x.str.contains(search, case=False, na=False)).any(axis=1)]
        for _, row in df.iloc[::-1].iterrows():
            with st.container(border=True):
                name = row.get('name', '')
                price = row.get('price', '')
                location = row.get('location', '')
                phone = row.get('phone', '')
                if pd.isna(phone) or str(phone) == "":
                    phone = row.get('whatsapp', '')
                st.subheader(f"{name} - ₦{price}")
                st.write(f"📍 {location}")
                if phone and str(phone) != "nan":
                    clean = re.sub(r'\D', '', str(phone))
                    if clean.startswith("0"):
                        clean = "234" + clean[1:]
                    st.link_button(f"💬 WhatsApp {phone}", f"https://wa.me/{clean}")
                else:
                    st.write("No phone")

with tab2:
    st.subheader("Post Your Product")
    with st.form("post_form"):
        name = st.text_input("Product Name *", placeholder="e.g. Test Yam")
        price = st.text_input("Price *", placeholder="e.g. 5000")
        location = st.text_input("Location *", placeholder="e.g. Garki")
        whatsapp = st.text_input("WhatsApp Number *", placeholder="e.g. 08116911722")
        submit = st.form_submit_button("Post Product", type="primary")
        if submit:
            if not name or not price or not location or not whatsapp:
                st.error("Fill all fields")
            else:
                wa_clean = re.sub(r'\D', '', whatsapp)
                ok = send_to_sheet({"type": "product", "name": name, "price": price, "location": location, "phone": wa_clean, "whatsapp": wa_clean, "lat": 9.066, "lon": 7.483})
                if ok:
                    st.success("✅ Posted! Refresh Marketplace tab to see am.")
                    st.balloons()
                else:
                    st.error("Failed to post. Try again.")

with tab3:
    st.subheader("Join Waitlist - Tell us wetin you want")
    with st.form("wait_form"):
        request = st.text_input("What do you want to buy?", placeholder="e.g. Fresh Catfish")
        phone2 = st.text_input("Your WhatsApp Number", placeholder="e.g. 08116911722")
        submit2 = st.form_submit_button("Join Waitlist")
        if submit2:
            if not request or not phone2:
                st.error("Fill request and phone")
            else:
                ok = send_to_sheet({"type": "waitlist", "request": request, "phone": phone2, "whatsapp": phone2})
                if ok:
                    st.success("✅ You don join waitlist!")
                else:
                    st.error("Failed. Try again.")
