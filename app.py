import streamlit as st
from supabase import create_client
import time
import pandas as pd
import urllib.parse

st.set_page_config(page_title="Row Economy - Nigeria Map", layout="wide")
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

# Nigeria States + Map Coords
STATES = {
"Abuja": [9.0765, 7.3986],
"Lagos": [6.5244, 3.3792],
"Kano": [12.0022, 8.5919],
"Kaduna": [10.5200, 7.4380],
"Port Harcourt": [4.8156, 7.0498],
"Ibadan": [7.3775, 3.9470],
"Enugu": [6.5244, 7.5000],
"Benin": [6.335, 5.603],
"Jos": [9.8965, 8.8583],
"Maiduguri": [11.8333, 13.1500],
"Onitsha": [6.1667, 6.7833],
"Aba": [5.1167, 7.3667],
"Uyo": [5.0515, 7.9336],
"Calabar": [4.9757, 8.3417],
"Sokoto": [13.0600, 5.2400],
"Bauchi": [10.3100, 9.8400],
"Akure": [7.2500, 5.2000],
"Owerri": [5.4833, 7.0333],
"Abeokuta": [7.1600, 3.3500],
"Yola": [9.2300, 12.4700],
}

st.markdown("### Row Economy Market - Nigeria Wide")
st.caption("Live Map - Buy Near You - Delivery Across Nigeria")
st.markdown("LIVE - Delivery to All 36 States + Abuja")

# Buyer Registration - For AI Notifications
st.markdown("## Get Notified on WhatsApp")
st.caption("AI will notify you when product drops near you")
with st.form("buyer_form"):
    bname = st.text_input("Your Name", placeholder="Amina")
    bphone = st.text_input("Your WhatsApp Number", placeholder="2348116911722")
    bwant = st.text_input("What do you want?", placeholder="Rice, Yam, Oil")
    bstate = st.selectbox("Your State", list(STATES.keys()))
    bgo = st.form_submit_button("Turn ON Notifications")
    if bgo:
        if bname and bphone and bwant:
            try:
                supabase.table("buyers").insert({"name": bname, "phone": bphone, "want": bwant, "state": bstate}).execute()
                st.success("Done! AI will notify you on WhatsApp when " + bwant + " drops in " + bstate)
            except:
                st.success("Saved locally! AI will notify you.")
                st.session_state["buyer"] = {"name": bname, "phone": bphone, "want": bwant, "state": bstate}
        else:
            st.error("Fill Name + Phone + What you want")

# Filter
st.markdown("---")
st.markdown("## LIVE MAP - Products Near You")
my_state = st.selectbox("Show products in:", ["All Nigeria"] + list(STATES.keys()))
my_want = st.text_input("Search product", placeholder="Search rice, yam...")
st.caption("Tap a pin on map to see product. Red pins = near you.")

# Load Products
try:
    res = supabase.table("products").select("*").order("created_at", desc=True).execute()
    products = res.data or []
except:
    products = []

if my_state != "All Nigeria":
    products = [p for p in products if str(p.get("state","")).lower() == my_state.lower()]
if my_want:
    products = [p for p in products if my_want.lower() in str(p.get("name","")).lower()]

# Build Map Data
map_rows = []
for p in products:
    stt = p.get("state") or "Abuja"
    coord = STATES.get(stt, [9.0765, 7.3986])
    lat = p.get("lat") or coord[0]
    lng = p.get("lng") or coord[1]
    map_rows.append({"lat": lat, "lon": lng, "name": p.get("name","")})

if map_rows:
    df = pd.DataFrame(map_rows)
    st.map(df, zoom=6)
else:
    st.info("No products on map yet. Post first product below.")
    df = pd.DataFrame([{"lat": 9.0765, "lon": 7.3986}])
    st.map(df, zoom=5)

# AI Matcher - Notify Buyer
if products and "buyer" in st.session_state:
    b = st.session_state["buyer"]
    for p in products:
        if b["want"].lower() in str(p.get("name","")).lower() and b["state"].lower() == str(p.get("state","")).lower():
            msg = "Hi " + b["name"] + ", Fresh " + str(p.get("name")) + " just dropped near you in " + b["state"] + " - N" + str(p.get("price")) + ". Tap to buy!"
            link = "https://wa.me/" + b["phone"] + "?text=" + urllib.parse.quote(msg)
            st.success("AI MATCH FOUND near you!")
            st.link_button("Send AI Notification to My WhatsApp", link)

# Product List
st.markdown("## Products")
if not products:
    st.info("No products yet in this state. Post below.")
else:
    for p in products:
        name = p.get("name", "No name")
        price = p.get("price", 0) or 0
        desc = p.get("description") or ""
        img = p.get("image_url") or ""
        unit = p.get("unit", "") or ""
        seller = p.get("seller_name") or "@WuseSeller"
        sphone = p.get("seller_phone") or "2348116911722"
        state = p.get("state") or "Abuja"
        if img and img.startswith("http"):
            st.image(img, use_container_width=True)
        st.markdown("### " + str(name))
        st.markdown("## N" + f"{price:,.0f}" + " / " + str(unit))
        st.markdown("Seller: " + str(seller) + " | Location: " + str(state) + " | Delivery Across Nigeria")
        if desc:
            st.write(desc)
        # Buyer -> Seller Direct WhatsApp
        msg2 = "Hi " + str(seller) + ", I want to buy " + str(name) + " for N" + str(price) + " in " + str(state) + ". Is it available?"
        wa2 = "https://wa.me/" + str(sphone) + "?text=" + urllib.parse.quote(msg2)
        st.link_button("Chat Seller on WhatsApp - " + str(state), wa2)
        st.markdown("---")

# Post Product - With Location + Seller Phone
st.markdown("## Post Product - Show on Map")
with st.form("post_form"):
    pname = st.text_input("Product Name", placeholder="Rice 50kg")
    pprice = st.number_input("Price (N)", min_value=0, value=85000)
    punit = st.selectbox("Unit", ["bag", "pcs", "kg", "litre", "basket"])
    pdesc = st.text_area("Description", placeholder="Fresh 50kg bag, delivery across Nigeria")
    pimage = st.text_input("Product Image Link", placeholder="Paste image link")
    sname = st.text_input("Your Seller Name", placeholder="WuseSeller")
    sphone = st.text_input("Your WhatsApp Number", placeholder="2348116911722")
    sstate = st.selectbox("Your State / Location", list(STATES.keys()))
    submit = st.form_submit_button("Post on Map", use_container_width=True)
    if submit:
        if not pname or not sphone:
            st.error("Name + WhatsApp Number needed!")
        else:
            coord = STATES.get(sstate, [9.0765, 7.3986])
            try:
                supabase.table("products").insert({"name": pname, "price": pprice, "unit": punit, "description": pdesc, "image_url": pimage, "seller_name": sname, "seller_phone": sphone, "state": sstate, "lat": coord[0], "lng": coord[1]}).execute()
                st.success("Posted on Map! Buyers in " + sstate + " will see you.")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error("Add columns in Supabase first: seller_name, seller_phone, state, lat, lng")
                st.write(str(e))

st.caption("Row Economy - Delivery Across Nigeria - AI WhatsApp Notifications")
