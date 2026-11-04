import streamlit as st
import pandas as pd
import urllib.parse

st.set_page_config(page_title="ROW Economy Market - Abuja", layout="wide")
st.title("🛒 ROW ECONOMY MARKET - Abuja")
st.write("No more waka waka for market. Find am, Chat Seller, Buy am.")

# --- Keep products + waitlist in memory ---
if "products" not in st.session_state:
    st.session_state.products = [
        {"name": "Fresh Rice 50kg", "price": 85000, "location": "Wuse Market, Abuja", "whatsapp": "2348116911722", "lat": 9.066, "lon": 7.483}
    ]
if "waitlist" not in st.session_state:
    st.session_state.waitlist = []
if "show_wait" not in st.session_state:
    st.session_state.show_wait = False
if "last_search" not in st.session_state:
    st.session_state.last_search = ""

# --- MAP ---
st.subheader("📍 Live Map - Abuja")
df = pd.DataFrame(st.session_state.products)
st.map(df, latitude="lat", longitude="lon", zoom=11)

# --- SHOW PRODUCTS ---
st.subheader("Available Products")
for p in st.session_state.products:
    st.write(f"**{p['name']} - N{p['price']:,} - {p['location']}**")
    msg = f"Hello, I see your {p['name']} for N{p['price']} for {p['location']}. Is it still available?"
    link = f"https://wa.me/{p['whatsapp']}?text={urllib.parse.quote(msg)}"
    st.link_button(f"Chat Seller - {p['name']}", link)

# --- ASK AI ---
st.divider()
st.subheader("🤖 Ask AI - Find Product Fast")
st.write("Example: I need Rice for Wuse")
query = st.text_input("What do you need?", key="ai_input")
if st.button("Ask AI"):
    st.session_state.last_search = query
    q = query.lower()
    found = [p for p in st.session_state.products if p['name'].split()[0].lower() in q or p['name'].lower() in q or any(w in q for w in p['name'].lower().split())]
    # simple check: if product name word appears in query
    found = []
    for p in st.session_state.products:
        for word in p['name'].lower().split():
            if word in q and word not in ["50kg", "fresh"]:
                found.append(p)
                break

    if found:
        st.success(f"AI found {len(found)} for you:")
        for p in found:
            st.write(f"✅ **{p['name']} - N{p['price']:,} - {p['location']}**")
            msg = f"Hello, I see your {p['name']} for N{p['price']} for {p['location']}. Is it still available?"
            link = f"https://wa.me/{p['whatsapp']}?text={urllib.parse.quote(msg)}"
            st.link_button(f"Chat Seller - {p['name']}", link)
        st.session_state.show_wait = False
    else:
        # --- THE NEW SORRY + WAIT FEATURE ---
        st.warning(f"Sorry, we have no {query} available right now.")
        st.write("Do you want to **Post a Product** or **Wait** till we have an order of your request?")
        st.write("If you wait, **I'll text you directly on your WhatsApp** once we have what you requested.")
        st.session_state.show_wait = True

# --- WAITLIST FORM - shows only when AI says sorry ---
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
    if st.button("I Want To Post A Product Instead"):
        st.info("Scroll down small - Post Product dey below. Post am, buyers go find am.")

# --- POST PRODUCT ---
st.divider()
st.subheader("📦 Post Product - Show on Map")
with st.form("post_form"):
    name = st.text_input("Product Name (e.g Beans 50kg)")
    price = st.number_input("Price (Naira)", min_value=0, step=100)
    location = st.text_input("Location (e.g Garki Market, Abuja)")
    whatsapp = st.text_input("Your WhatsApp Number (e.g 08116911722)")
    submit = st.form_submit_button("Post Product")
    if submit and name and price and location and whatsapp:
        wa_clean = whatsapp.replace(" ", "").replace("+", "")
        if wa_clean.startswith("0"):
            wa_clean = "234" + wa_clean[1:]
        new_p = {"name": name, "price": price, "location": location, "whatsapp": wa_clean, "lat": 9.066, "lon": 7.483}
        st.session_state.products.append(new_p)
        st.success(f"Posted! {name} don show for Map now.")
        # Check waitlist - tell seller someone is waiting
        for w in st.session_state.waitlist:
            if any(word.lower() in name.lower() for word in w["request"].lower().split() if len(word) > 2):
                st.info(f"🔔 Good news! Somebody dey wait for this: {w['request']} - WhatsApp: {w['whatsapp']}. Text them now!")

st.write("---")
st.write("📲 ROW Economy Market | Abuja | 08116911722")
