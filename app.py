import streamlit as st
import json
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="centered")

def load_file(name, default):
    try:
        with open(name, "r") as f:
            return json.load(f)
    except:
        return default

def save_file(name, data):
    with open(name, "w") as f:
        json.dump(f, data)

# LOGIN
if "user" not in st.session_state:
    st.title("ROW ECONOMY SUPER")
    st.info("Login: 08116911722 / Kilani247")
    phone = st.text_input("Phone Number")
    pwd = st.text_input("Password", type="password")
    if st.button("LOGIN"):
        if phone.strip() == "08116911722" and pwd.strip().lower() == "kilani247":
            st.session_state.user = phone.strip()
            st.rerun()
        else:
            st.error("Wrong - Use 08116911722 / Kilani247")
    st.stop()

# LOAD DATA
products = load_file("products.json", [])
lives = load_file("lives.json", [])

st.title("ROW ECONOMY SUPER")
st.success(f"Welcome {st.session_state.user} | Bal N500000")

tab1, tab2, tab3, tab4 = st.tabs(["LIVE MARKET", "POST PRODUCT", "GO LIVE", "MAP"])

with tab1:
    st.header("LIVE MARKETPLACE")
    st.write("People posting + going live now")
    
    if lives:
        st.subheader("🔴 LIVE NOW")
        for lv in lives[::-1][:5]:
            st.error(f"🔴 {lv['user']} LIVE: {lv['title']}")
            st.write(lv.get('desc',''))
    
    st.divider()
    
    if len(products) == 0:
        st.write("No products yet - Be first to post!")
    else:
        for p in products[::-1]:
            st.subheader(f"{p['name']} - N{p['price']}")
            st.write(f"Seller: {p['user']} | {p['phone']}")
            st.write(p['desc'])
            if p.get('img'):
                try:
                    st.image(p['img'])
                except:
                    pass
            st.link_button("Chat on WhatsApp", f"https://wa.me/{p['phone']}")
            st.divider()

with tab2:
    st.header("POST PRODUCT")
    st.write("Fill form to sell")
    pname = st.text_input("Product Name", key="pname")
    pprice = st.number_input("Price in Naira", min_value=100, value=1000, key="pprice")
    pdesc = st.text_area("Description", key="pdesc")
    pphone = st.text_input("Your WhatsApp Number", value="08116911722", key="pphone")
    pimg = st.text_input("Image Link (optional)", key="pimg")
    
    if st.button("POST MY PRODUCT NOW", key="postbtn"):
        if pname:
            new_product = {
                "name": pname,
                "price": pprice,
                "desc": pdesc,
                "phone": pphone,
                "user": st.session_state.user,
                "img": pimg,
                "time": datetime.now().strftime("%H:%M")
            }
            products.append(new_product)
            save_file("products.json", products)
            st.success("Product Posted Successfully!")
            st.balloons()
        else:
            st.error("Please enter product name")

with tab3:
    st.header("GO LIVE")
    st.write("Start live to sell")
    ltitle = st.text_input("Live Title", key="ltitle")
    ldesc = st.text_input("What are you selling?", key="ldesc")
    
    if st.button("🔴 START LIVE NOW", key="startlive"):
        if ltitle:
            new_live = {
                "user": st.session_state.user,
                "title": ltitle,
                "desc": ldesc,
                "time": datetime.now().strftime("%H:%M:%S")
            }
            lives.append(new_live)
            save_file("lives.json", lives)
            st.success("YOU ARE LIVE NOW!")
            st.balloons()
        else:
            st.error("Enter Live Title")
    
    if st.button("END LIVE", key="endlive"):
        lives = [x for x in lives if x['user'] != st.session_state.user]
        save_file("lives.json", lives)
        st.warning("Live Ended")

with tab4:
    st.header("SNAP MAP")
    st.write("Live locations")
    lats = [9.06 + random.uniform(-0.03,0.03) for _ in range(20)]
    lons = [7.48 + random.uniform(-0.03,0.03) for _ in range(20)]
    df = pd.DataFrame({"lat": lats, "lon": lons})
    st.map(df)
    if st.button("Logout"):
        del st.session_state.user
        st.rerun()
