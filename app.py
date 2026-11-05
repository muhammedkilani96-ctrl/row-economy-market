import streamlit as st
import urllib.parse
st.set_page_config(page_title="Row Economy", layout="wide")
st.markdown("<style>header{visibility:hidden} .block-container{padding:0px !important}</style>", unsafe_allow_html=True)
if "goods" not in st.session_state:
    st.session_state.goods = []
    st.session_state.goods.append("Horlance Auto Cooling Ltd|Car AC Repair|25000|Osun & Oyo State|09046044472|Car Mart|YES")
    st.session_state.goods.append("Mama T|Bag of Rice|45000|Abuja|09046044472|Food|YES")
if "cat" not in st.session_state:
    st.session_state.cat = "All"
st.markdown("<div style='background:#00A651;padding:14px 14px 28px 14px;border-radius:0 0 24px 24px'><div style='display:flex;justify-content:space-between;align-items:center;color:white'><span style='font-size:24px'>☰</span><b style='font-size:24px'>ROW ECONOMY</b><span style='background:#FF8A00;width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:20px'>👤</span></div></div>", unsafe_allow_html=True)
search = st.text_input("S", placeholder="Ask Mama Oloja - What are you looking for today?", label_visibility="collapsed")
st.markdown("<div style='display:flex;justify-content:space-between;padding:12px 14px 6px'><b style='font-size:20px'>Categories</b><span style='color:#00A651'>See all ></span></div>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("Perfume"):
        st.session_state.cat = "Perfume"
with c2:
    if st.button("Clothes"):
        st.session_state.cat = "Clothes"
with c3:
    if st.button("Phones"):
        st.session_state.cat = "Phones"
with c4:
    if st.button("Food"):
        st.session_state.cat = "Food"
c5, c6, c7, c8 = st.columns(4)
with c5:
    if st.button("Car Mart"):
        st.session_state.cat = "Car Mart"
with c6:
    if st.button("Services"):
        st.session_state.cat = "Services"
with c7:
    if st.button("Tickets"):
        st.session_state.cat = "Tickets"
with c8:
    if st.button("Chat Rooms"):
        st.session_state.cat = "Chat Rooms"
st.write("Showing: " + st.session_state.cat)
if st.button("Show All"):
    st.session_state.cat = "All"
    st.rerun()
st.markdown("<div style='display:flex;justify-content:space-between;padding:10px 14px'><b style='font-size:20px'>Featured Listing</b><span style='color:#00A651'>See all ></span></div>", unsafe_allow_html=True)
for line in st.session_state.goods:
    p = line.split("|")
    seller = p[0]
    name = p[1]
    price = p[2]
    loc = p[3]
    wa = p[4]
    cat = p[5]
    ver = p[6]
    skip = False
    if st.session_state.cat != "All" and cat != st.session_state.cat:
        skip = True
    if search and search.lower() not in name.lower() and search.lower() not in seller.lower():
        skip = True
    if skip:
        continue
    st.markdown("<div style='background:white;margin:0 14px 14px 14px;padding:14px;border-radius:18px;box-shadow:0 2px 10px #eee'>", unsafe_allow_html=True)
    if ver == "YES":
        st.markdown("<div style='text-align:right'><span style='background:#00A651;color:white;padding:4px 10px;border-radius:20px;font-size:12px'>VERIFIED</span></div>", unsafe_allow_html=True)
    st.markdown("<b style='font-size:17px'>" + seller + "</b>", unsafe_allow_html=True)
    st.write("Product: " + name + " - N" + price)
    st.write("Location: " + loc)
    st.write("WhatsApp: " + wa)
    if "AC" in name:
        st.image("https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=600", use_container_width=True)
    else:
        st.image("https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600", use_container_width=True)
    msg = urllib.parse.quote("Hello " + seller + ", I saw your " + name)
    link = "https://wa.me/234" + wa[1:] + "?text=" + msg
    st.link_button("Chat on WhatsApp", link, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div style='display:flex;gap:8px;padding:0 14px'><div style='text-align:center'><div style='font-size:30px'>Mama</div><span style='background:#00A651;color:white;font-size:10px;padding:2px 6px;border-radius:10px'>Mama Oloja AI</span></div><div style='background:#D5F5E3;border-radius:16px;padding:10px;flex:1'>Welcome my dear, I can help you find the best price in the market.</div></div>", unsafe_allow_html=True)
q = st.text_input("Ask Mama", placeholder="Ask Mama Oloja...", label_visibility="collapsed")
if q:
    st.success("Mama Oloja: I found " + q + " for you above.")
st.markdown("<div style='padding:14px'><b style='font-size:18px'>Sell - FREE for First 10</b><br>1 Name  2 WhatsApp  3 Location  4 Pictures  5 Price</div>", unsafe_allow_html=True)
with st.form("f"):
    n1 = st.text_input("1. Your Name")
    n2 = st.text_input("2. WhatsApp")
    n3 = st.selectbox("3. Location", ["Abuja", "Osun & Oyo State", "Ogbomoso", "Ilorin", "Lagos"])
    n4 = st.selectbox("Category", ["Food", "Phones", "Clothes", "Perfume", "Car Mart", "Services", "Tickets", "Chat Rooms"])
    n5 = st.text_input("5. Product Name")
    n6 = st.text_input("5. Price - e.g. 25000")
    pic = st.file_uploader("4. Upload Picture", type=["jpg", "png"])
    if pic:
        st.image(pic)
    go = st.form_submit_button("POST MY GOODS FOR FREE")
    if go:
        if n1 == "" or n2 == "":
            st.error("Fill Name and WhatsApp")
        elif n5 == "":
            st.error("Fill Product Name")
        else:
            new = n1 + "|" + n5 + "|" + n6 + "|" + n3 + "|" + n2 + "|" + n4 + "|NO"
            st.session_state.goods.append(new)
            st.success
