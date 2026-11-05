import streamlit as st
import urllib.parse
st.set_page_config(page_title="Row Economy", layout="wide")
st.markdown("<style>header{visibility:hidden} .block-container{padding:0px !important} .stApp{background:white}</style>", unsafe_allow_html=True)
if "goods" not in st.session_state:
    st.session_state.goods = []
    st.session_state.goods.append("Horlance Auto Cooling Ltd|Car AC Repair|25000|Osun & Oyo State|09046044472|Car Mart|YES")
    st.session_state.goods.append("Mama T|Bag of Rice|45000|Abuja|09046044472|Food|YES")
# READ CATEGORY FROM LINK
qp = st.query_params
cat_now = qp.get("cat", "All")
st.markdown("<div style='background:linear-gradient(90deg,#00A651,#00C853);padding:16px 14px 30px 14px;border-radius:0 0 28px 28px;color:white'><div style='display:flex;justify-content:space-between;align-items:center'><span style='font-size:26px'>☰</span><b style='font-size:26px'>ROW ECONOMY</b><span style='background:#FF8A00;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px'>👤</span></div><p style='text-align:center;font-size:13px;margin:6px 0 0 0'>Nigeria Sweetest Market</p></div>", unsafe_allow_html=True)
search = st.text_input("S", placeholder="Ask Mama Oloja - What are you looking for today?", label_visibility="collapsed")
st.markdown("<div style='display:flex;justify-content:space-between;padding:14px 14px 6px'><b style='font-size:21px;color:#111'>Categories</b><a href='?cat=All' style='color:#00A651;font-weight:bold;text-decoration:none'>See all ></a></div>", unsafe_allow_html=True)
st.markdown("<div style='display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px;padding:0 14px'><a href='?cat=Perfume' style='text-decoration:none'><div style='background:#FFE4F1;border-radius:16px;padding:14px;text-align:center;font-size:28px'>🧴</div><p style='text-align:center;color:#111;font-size:13px;margin:4px 0'>Perfume</p></a><a href='?cat=Clothes' style='text-decoration:none'><div style='background:#D6EAF8;border-radius:16px;padding:14px;text-align:center;font-size:28px'>👕</div><p style='text-align:center;color:#111;font-size:13px;margin:4px 0'>Clothes</p></a><a href='?cat=Phones' style='text-decoration:none'><div style='background:#D6EAF8;border-radius:16px;padding:14px;text-align:center;font-size:28px'>📱</div><p style='text-align:center;color:#111;font-size:13px;margin:4px 0'>Phones</p></a><a href='?cat=Food' style='text-decoration:none'><div style='background:#FFE8CC;border-radius:16px;padding:14px;text-align:center;font-size:28px'>🍲</div><p style='text-align:center;color:#111;font-size:13px;margin:4px 0'>Food</p></a></div>", unsafe_allow_html=True)
st.markdown("<div style='display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px;padding:10px 14px'><a href='?cat=Car Mart' style='text-decoration:none'><div style='background:#FFE8CC;border-radius:16px;padding:14px;text-align:center;font-size:28px'>🚗</div><p style='text-align:center;color:#111;font-size:13px;margin:4px 0'>Car Mart</p></a><a href='?cat=Services' style='text-decoration:none'><div style='background:#D5F5E3;border-radius:16px;padding:14px;text-align:center;font-size:28px'>💼</div><p style='text-align:center;color:#111;font-size:13px;margin:4px 0'>Services</p></a><a href='?cat=Tickets' style='text-decoration:none'><div style='background:#FADBD8;border-radius:16px;padding:14px;text-align:center;font-size:28px'>🎟️</div><p style='text-align:center;color:#111;font-size:13px;margin:4px 0'>Tickets</p></a><a href='?cat=Chat Rooms' style='text-decoration:none'><div style='background:#D5F5E3;border-radius:16px;padding:14px;text-align:center;font-size:28px'>💬</div><p style='text-align:center;color:#111;font-size:13px;margin:4px 0'>Chat Rooms</p></a></div>", unsafe_allow_html=True)
st.markdown("<div style='padding:0 14px;color:#111'>Showing: <b>" + cat_now + "</b></div>", unsafe_allow_html=True)
st.markdown("<div style='display:flex;justify-content:space-between;padding:10px 14px'><b style='font-size:21px;color:#111'>Featured Listing</b><span style='color:#00A651;font-weight:bold'>See all ></span></div>", unsafe_allow_html=True)
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
    if cat_now != "All" and cat != cat_now:
        skip = True
    if search and search.lower() not in name.lower() and search.lower() not in seller.lower():
        skip = True
    if skip:
        continue
    st.markdown("<div style='background:white;margin:0 14px 16px 14px;padding:16px;border-radius:20px;box-shadow:0 4px 20px #E8E8E8;border:1px solid #F0F0F0'>", unsafe_allow_html=True)
    if ver == "YES":
        st.markdown("<div style='text-align:right'><span style='background:#00A651;color:white;padding:5px 12px;border-radius:20px;font-size:12px;font-weight:bold'>VERIFIED</span></div>", unsafe_allow_html=True)
    st.markdown("<b style='font-size:19px;color:#111'>" + seller + "</b>", unsafe_allow_html=True)
    st.markdown("<p style='color:#333;font-size:16px'>Product: " + name + " - <b style='color:#00A651'>N" + price + "</b></p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#666'>Location: " + loc + "</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#666'>WhatsApp: " + wa + "</p>", unsafe_allow_html=True)
    if "AC" in name:
        st.image("https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=600", use_container_width=True)
    else:
        st.image("https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600", use_container_width=True)
    msg = urllib.parse.quote("Hello " + seller + ", I saw your " + name)
    link = "https://wa.me/234" + wa[1:] + "?text=" + msg
    st.link_button("Chat on WhatsApp", link, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div style='display:flex;gap:8px;padding:0 14px'><div style='text-align:center'><div style='font-size:36px'>👩🏾</div><span style='background:#00A651;color:white;font-size:10px;padding:3px 7px;border-radius:10px'>Mama Oloja AI</span></div><div style='background:#D5F5E3;border-radius:18px;padding:12px;flex:1;color:#111'>Welcome my dear, I can help you find the best price in the market.</div></div>", unsafe_allow_html=True)
q = st.text_input("Ask Mama", placeholder="Ask Mama Oloja...", label_visibility="collapsed")
if q:
    st.success("Mama Oloja: I found " + q + " for you above.")
st.markdown("<div style='padding:16px'><b style='font-size:19px;color:#111'>Sell - FREE for First 10</b><br><span style='color:#555'>1 Name  2 WhatsApp  3 Location  4 Pictures  5 Price</span></div>", unsafe_allow_html=True)
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
            st.success("Done! Your goods are LIVE!")
            st.balloons()
            st.rerun()
st.markdown("<div style='background:white;display:flex;justify-content:space-around;padding:12px;border-top:1px solid #eee;color:#111'><span>Home</span><span>Shop</span><span>Orders</span><span>Profile</span></div>", unsafe_allow_html=True)
