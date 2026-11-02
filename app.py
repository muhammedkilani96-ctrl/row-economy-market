import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy", layout="centered")

if 'ads' not in st.session_state:
    st.session_state.ads = 0

WHATSAPP = "2348116911722"
NUM = "08116911722"

st.title("Row Economy Market")
st.write("Abuja - Food, Events, Clothes")
st.caption(f"WhatsApp {NUM} - Free Ads {st.session_state.ads}/10")

tab1, tab2, tab3 = st.tabs(["Food", "Events", "Clothes"])

with tab1:
    people = st.number_input("People", 1, 500, 10, key="f1")
    meal = st.selectbox("Meal", ["Spaghetti","Rice","Indomie","Full"], key="f2")
    spag = (people + 3)//4
    rice = (people + 4)//5
    if meal == "Spaghetti":
        needs = {"Spaghetti": spag}
    elif meal == "Rice":
        needs = {"Rice": rice}
    elif meal == "Indomie":
        needs = {"Indomie": people}
    else:
        needs = {"Rice": rice, "Spaghetti": spag}
    prices = {"Spaghetti": 1000, "Rice": 1500, "Indomie": 350}
    total = 0
    for k,v in needs.items():
        total += prices[k]*v
        st.metric(f"{k} x {v}", f"N{prices[k]*v}")
    st.write(f"Total N{total}")
    msg = f"Food order for {people} {meal} total N{total}"
    link = "https://wa.me/" + WHATSAPP + "?text=" + urllib.parse.quote(msg)
    st.link_button("Order Food", link, use_container_width=True)

with tab2:
    event = st.text_input("Event Name", "Concert")
    venue = st.text_input("Venue", "Wuse")
    price = st.number_input("Ticket Price", 500, 100000, 2000, key="e1")
    qty = st.number_input("Qty", 1, 20, 1, key="e2")
    total_t = price*qty
    st.write(f"Total N{total_t}")
    msg2 = f"Tickets {qty} for {event} at {venue} total N{total_t}"
    link2 = "https://wa.me/" + WHATSAPP + "?text=" + urllib.parse.quote(msg2)
    st.link_button("Buy Ticket", link2, use_container_width=True)

with tab3:
    cloth = st.selectbox("Item", ["Shirt","Native","Hijab","Trouser","Shoe","Cap"], key="c0")
    size = st.selectbox("Size", ["S","M","L","XL","XXL"], key="c1")
    c_price = st.number_input("Price", 1000, 100000, 5000, key="c2")
    c_qty = st.number_input("How many", 1, 20, 1, key="c3")
    total_c = c_price*c_qty
    st.write(f"{cloth} {size} x {c_qty}")
    st.write(f"Total N{total_c}")
    msg3 = f"Cloth {cloth} {size} x {c_qty} total N{total_c}"
    link3 = "https://wa.me/" + WHATSAPP + "?text=" + urllib.parse.quote(msg3)
    st.link_button("Buy Cloth", link3, use_container_width=True)

st.divider()
with st.form("ad"):
    name = st.text_input("Shop Name")
    cat = st.selectbox("Category", ["Food","Event","Cloth"])
    area = st.selectbox("Area", ["Wuse","Garki","Kubwa","Other"])
    item = st.text_area("What you sell")
    ok = st.form_submit_button("Post Ad")
    if ok:
        if st.session_state.ads < 10:
            st.session_state.ads += 1
            st.success(f"Posted Left {10-st.session_state.ads}")
        else:
            st.error("Pay N200 for more")
