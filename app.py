import streamlit as st
import urllib.parse
import pandas as pd

st.set_page_config(page_title="Row Economy Market", page_icon="🛒")
st.title("ROW ECONOMY MARKET - Abuja")
st.markdown("Buy and Sell Near You. Chat Seller Direct on WhatsApp.")
st.markdown("Help: 08116911722")

if 'products' not in st.session_state:
    st.session_state.products = [
        {"name": "Fresh Rice 50kg", "price": 85000, "location": "Wuse Market, Abuja", "whatsapp": "2348116911722", "lat": 9.0667, "lon": 7.4833}
    ]

products = st.session_state.products

st.subheader("LIVE MAP - Abuja")
if products:
    df = pd.DataFrame(products)
    st.map(df, latitude="lat", longitude="lon", zoom=11)
    for p in products:
        st.markdown(f"**{p['name']} - N{p['price']:,} - {p['location']}**")
        wa = str(p['whatsapp']).replace("+", "").replace(" ", "")
        if wa.startswith("0"):
            wa = "234" + wa[1:]
        msg = f"Hello, I see your {p['name']} for N{p['price']} for {p['location']}. Is it still available?"
        link = f"https://wa.me/{wa}?text={urllib.parse.quote(msg)}"
        st.link_button(f"Chat Seller - {p['name']}", link)

st.subheader("Ask AI - Find Product Fast")
need_input = st.text_input("Example: I need Rice for Wuse")
if st.button("Ask AI"):
    if not need_input:
        st.warning("Type wetin you need first")
    else:
        need = need_input.lower()
        found = []
        for p in products:
            nm = p['name'].lower()
            lc = p['location'].lower()
            match = False
            for w in ["rice", "beans", "garri", "oil", "yam"]:
                if w in need and w in nm:
                    match = True
            for loc in ["wuse", "garki", "kubwa", "nyanya", "lugbe"]:
                if loc in need and loc in lc:
                    match = True
            if match:
                found.append(p)
        if found:
            st.success(f"AI found {len(found)} for you:")
           
