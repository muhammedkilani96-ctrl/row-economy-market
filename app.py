import streamlit as st
from supabase import create_client
import time

st.set_page_config(page_title="Row Economy Market", layout="wide")
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

st.markdown("### Row Economy Market")
st.caption("Wuse Market - Abuja - Live Shopping")
st.markdown("LIVE - 128 watching")
st.markdown("**@WuseSeller** - 5.0 stars | Wuse Market")
st.markdown("### Fresh Rice Available Now - Ask Me Price!")
st.caption("Fresh stock from Wuse Market. Delivery available in Abuja.")

st.subheader("Your Live Camera")
photo = st.camera_input("Take Photo", label_visibility="collapsed")
live_title = st.text_input("Live Title", value="Fresh Rice Available Now")

if st.button("Start Live", use_container_width=True):
    try:
        supabase.table("live_sessions").insert({"title": live_title, "is_live": True}).execute()
        st.success("You are LIVE now!")
    except:
        st.error("Could not start live")
if st.button("End Live", use_container_width=True):
    try:
        supabase.table("live_sessions").update({"is_live": False}).eq("is_live", True).execute()
        st.info("Live ended.")
    except:
        st.error("Error")

st.markdown("### Support Seller")
c1, c2 = st.columns(2)
with c1:
    if st.button("Rose - N100", use_container_width=True):
        st.success("Thank you! Rose sent!")
    if st.button("Lion - N1000", use_container_width=True):
        st.success("Thank you! Lion sent!")
with c2:
    if st.button("Fire - N500", use_container_width=True):
        st.success("Thank you! Fire sent!")
    if st.button("Diamond - N5000", use_container_width=True):
        st.success("Thank you! Diamond sent!")

st.markdown("### Live Comments")
cname = st.text_input("Your Name", placeholder="e.g. Amina")
ctext = st.text_input("Ask a question", placeholder="e.g. How much is delivery to Garki?")
if st.button("Send Comment"):
    if cname and ctext:
        st.success("Comment sent!")
    else:
        st.error("Please enter name and question")

st.markdown("---")
st.markdown("## LIVE MARKETPLACE")
search = st.text_input("Search", placeholder="Search rice, yam, oil...")

try:
    res = supabase.table("products").select("*").order("created_at", desc=True).execute()
    products = res.data or []
except:
    st.error("Could not load products")
    products = []

if search:
    products = [p for p in products if search.lower() in str(p.get("name", "")).lower()]

if not products:
    st.info("No products yet. Post your first product below.")
else:
    for p in products:
        name = p.get("name", "No name")
        price = p.get("price", 0) or 0
        desc = p.get("description") or ""
        img = p.get("image_url") or ""
        unit = p.get("unit", "") or ""
        if img and img.startswith("http"):
            st.image(img, use_container_width=True)
        st.markdown("### " + str(name))
        st.markdown("## N" + f"{price:,.0f}" + " / " + str(unit))
        if desc:
            st.write(desc)
        st.caption("5.0 stars | Wuse Market | Delivery in Abuja")
        if st.button("Buy Now", key="buy_" + str(p.get("id"))):
            st.success("Order started! Tap WhatsApp below.")
        wa = "https://wa.me/2348116911722"
        st.link_button("Chat on WhatsApp", wa)
        st.markdown("---")

st.markdown("## Post Product")
with st.form("post_form"):
    pname = st.text_input("Product Name", placeholder="Rice 50kg")
    pprice = st.number_input("Price (N)", min_value=0, value=85000)
    punit = st.selectbox("Unit", ["bag", "pcs", "kg", "litre", "basket"])
    pdesc = st.text_area("Description", placeholder="Fresh 50kg bag of rice from Wuse Market.")
    pimage = st.text_input("Product Image Link", placeholder="Paste image link here")
    submit = st.form_submit_button("Post Product", use_container_width=True)
    if submit:
        if not pname or not pdesc:
            st.error("Name + Desc needed!")
        else:
            try:
                supabase.table("products").insert({"name": pname, "price": pprice, "unit": punit, "description": pdesc, "image_url": pimage}).execute()
                st.success("Posted! Refresh to see it.")
                time.sleep(1)
                st.rerun()
            except:
                st.error("Error posting")

st.caption("Row Economy Market - Wuse Market sellers")
