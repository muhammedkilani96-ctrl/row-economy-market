import streamlit as st
import streamlit.components.v1 as comp

st.set_page_config(page_title="Row Economy", layout="centered")

# Load black style
try:
    with open("style.html", "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)
except:
    st.markdown("<style>.stApp{background:#000} h1{color:#00FF66} p{color:white}</style>", unsafe_allow_html=True)

st.title("Row Economy")

# Real GPS
try:
    with open("location.html", "r") as f:
        comp.html(f.read(), height=180)
except:
    st.write("Real GPS Ready")

import database
database.init_db()

state = st.selectbox("State", ["Abuja", "Lagos", "Kano", "Rivers", "Kaduna"])
area = st.text_input("Area / Market", "Wuse 2 Abuja")

t1, t2, t3, t4, t5 = st.tabs(["Home", "Advertise Here", "Explore", "Chats", "Profile"])

with t1:
    st.subheader(f"Food | Cloth | Cars for {area}")
    st.write(f"{database.count_adverts()} adverts live in {state}")
    st.link_button("View on Google Maps", f"https://maps.google.com/?q={area}")

with t2:
    try:
        import advertise_tab
        advertise_tab.show(area, state)
    except:
        st.subheader("Advertise Here")
        biz = st.text_input("Business Name", key="b1")
        what = st.text_input("What you sell", key="w1")
        price = st.number_input("Price N", 100, 10000000, 2006, key="p1")
        wa = st.text_input("WhatsApp Number", "08116911722", key="wa1")
        if st.button("Post Advert Now"):
            num = wa.replace("0", "234", 1) if wa.startswith("0") else wa
            database.add_advert(biz, what, price, num, area, state)
            st.success("Posted!")
            st.balloons()

with t3:
    st.subheader(f"Explore {area}")
    st.link_button("View on Google Maps", f"https://maps.google.com/?q={area}")
    ads = database.get_adverts()
    if not ads:
        st.write("No adverts yet. Post in Advertise Here!")
    else:
        for i, ad in enumerate(reversed(ads)):
            st.write(f"{ad['business']} - {ad['what']} - N{ad['price']}")
            st.write(f"{ad['area']}, {ad['state']}")
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("WhatsApp", f"https://wa.me/{ad['whatsapp']}", key=f"wa_{i}")
            with c2:
                st.link_button("Map", f"https://maps.google.com/?q={ad['area']}", key=f"map_{i}")
            st.divider()

with t4:
    st.subheader("Chats")
    st.write("Chats via WhatsApp")

with t5:
    st.subheader("Profile")
    st.write(f"Total Adverts: {database.count_adverts()}")
