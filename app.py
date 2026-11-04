import streamlit as st
import urllib.parse
import pandas as pd

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="wide")

st.title("🛒 ROW ECONOMY MARKET - Live Map for Abuja")
st.markdown("Buy and Sell Near You. No Middleman. Chat Seller Direct on WhatsApp.")
st.markdown("👉 Help: 08116911722")

# ===== PRODUCTS STORAGE =====
if 'products' not in st.session_state:
    st.session_state.products = [
        {"name": "Fresh Rice 50kg", "price": 85000, "location": "Wuse Market, Abuja", "whatsapp": "2348116911722", "lat": 9.0667, "lon": 7.4833},
    ]

products = st.session_state.products

# ===== LIVE MAP =====
st.subheader("📍 LIVE MAP - Abuja")
st.markdown("See products near you on map.")

if products:
    map_data = pd.DataFrame(products)
    # Streamlit map needs lat / lon columns
    st.map(map_data, latitude="lat", longitude="lon", zoom=11)
    for p in products:
        st.markdown(f"**{p['name']} - N{p['price']:,} - {p['location']}**")
        wa_clean = str(p['whatsapp']).replace("+", "").replace(" ", "")
        if wa_clean.startswith("0"):
            wa_clean = "234" + wa_clean[1:]
        msg = f"Hello, I see your {p['name']} for N{p['price']} for {p['location']} on Row Economy Market. Is it still available?"
        wa_link = f"https://wa.me/{wa_clean}?text={urllib.parse.quote(msg)}"
        st.link_button(f"💬 Chat Seller - {p['name']}", wa_link)
else:
    st.info("No products yet. Be the first to post.")

# ===== STEP 4: AI ASSISTANT =====
st.subheader("🤖 Ask AI - Find Product Fast")
st.markdown("Type wetin you need, AI go find am for you.")

user_need = st.text_input("Example: I need Rice for Wuse, budget 85000", key="ai_input")

if st.button("Ask AI 🔍"):
    if not user_need:
        st.warning("Abeg type wetin you need first, e.g: I need Rice for Wuse")
    else:
        need = user_need.lower()
        found = []
        for p in products:
            name_low = p['name'].lower()
            loc_low = p['location'].lower()
            # check product word
            match = False
            for word in ["rice", "beans", "garri", "oil", "yam", "tomato", "onion", "pepper"]:
                if word in need and word in name_low:
                    match = True
            if "wuse" in need and "wuse" in loc_low:
                match = True
            if "garki" in need and "garki" in loc_low:
                match = True
            if "kubwa" in need and "kubwa" in loc_low
