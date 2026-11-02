import streamlit as st
import streamlit.components.v1 as comp
import os

st.set_page_config(page_title="Row Economy", layout="centered")
st.markdown("<style>.stApp{background:#000000;}h1,h2,h3{color:#00FF66;}p,div,label,span{color:white;} .stButton>button{background:#006600;color:white;border:1px solid #00FF66; border-radius:10px;}</style>", unsafe_allow_html=True)

st.title("Row Economy")

# GPS
try:
    with open("location.html", "r") as f:
        comp.html(f.read(), height=180)
except:
    st.write("Real GPS Ready")

state = st.selectbox("State", ["Abuja","Lagos","Kano","Rivers","Kaduna"])
area = st.text_input("Area / Market", "Wuse 2 Abuja")

# SESSION DATABASE - This one must work
if "adverts" not in st.session_state:
    st.session_state.adverts = []

t1, t2, t3, t4, t5 = st.tabs(["Home","Advertise Here","Explore","Chats","Profile"])

with t1:
    st.write(f"Welcome to {area}, {state} - {len(st.session_state.adverts)} adverts live")
    st.link_button("📍 View on Google Maps", f"https://maps.google.com/?q={area}")

with t2:
    st.subheader("Advertise Here")
    biz = st.text_input("Business Name", key="biz")
    what = st.text_input("What you sell", key="what")
    price = st.number_input("Price N", 100, 10000000, 2006)
    whatsapp = st.text_input("WhatsApp Number", value="08116911722", key="wa")
    st.write("Use format 080... we auto convert")

    if st.button("Post Advert Now"):
        st.write("Button clicked! Checking...") # DEBUG - you must see this
        if biz and what and whatsapp:
            wa = whatsapp.replace(" ", "").replace("+", "")
            if wa.startswith("0"):
                wa = "234" + wa[1:]
            
            new_ad = {
                "business": biz,
                "what": what,
                "price": price,
                "whatsapp": wa,
                "area": area,
                "state": state
            }
            st.session_state.adverts.append(new_ad)
            st.success(f"Posted! {biz} - {what} N{price}")
            st.balloons()
            st.write(f"Go to Explore now - you have {len(st.session_state.adverts)} adverts")
        else:
            st.error("Please fill Business Name and What you sell and WhatsApp")

with t3:
    st.subheader(f"Explore {area}")
    st.link_button("📍 View on Google Maps", f"https://maps.google.com/?q={area}")
    
    if len(st.session_state.adverts) == 0:
        st.write("No adverts yet. Post first one in Advertise Here!")
    else:
        for i, ad in enumerate(reversed(st.session_state.adverts)):
            st.markdown(f"""
            <div style="background:#111;border:1px solid #00FF66;border-radius:12px;padding:12px;margin-bottom:10px;">
            <b style="color:#00FF66;">{ad['business']}</b><br>
            {ad['what']} - <b>N{ad['price']}</b><br>
            <small>{ad['area']}, {ad['state']}</small>
            </div>
            """, unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.link_button("💬 WhatsApp", f"https://wa.me/{ad['whatsapp']}?text=Hi I saw {ad['what']} on Row Economy", key=f"wa_btn_{i}")
            with c2:
                st.link_button("📍 Map", f"https://maps.google.com/?q={ad['area']}", key=f"map_btn_{i}")

with t4:
    st.write("Chats - via
