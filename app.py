import streamlit as st
st.set_page_config(page_title="Row Economy")
if "goods" not in st.session_state:
    st.session_state.goods=[]
h1="<div style='background:#00A651;"
h1+="padding:18px;border-radius:0 0 25px 25px;"
h1+="color:white;text-align:center'>"
h1+="<b style='font-size:28px'>ROW ECONOMY</b>"
h1+="<p>Nigeria Sweetest Market</p></div>"
st.markdown(h1, unsafe_allow_html=True)
q=st.text_input("Ask", placeholder="Ask Mama Oloja - What are you looking for?")
if q:
    st.info("Mama dey find: "+q)
st.markdown("### Categories")
a,b,c,d=st.columns(4)
with a:
    st.markdown("<div style='background:#FDE7F3;padding:14px;border-radius:18px;text-align:center'>🧴</div>", unsafe_allow_html=True)
    st.markdown("<center>Perfume</center>")
with b:
    st.markdown("<div style='background:#E0F2FE;padding:14px;border-radius:18px;text-align:center'>👕</div>", unsafe_allow_html=True)
    st.markdown("<center>Clothes</center>")
with c:
    st.markdown("<div style='background:#DBEAFE;padding:14px;border-radius:18px;text-align:center'>📱</div>", unsafe_allow_html=True)
    st.markdown("<center>Phones</center>")
with d:
    st.markdown("<div style='background:#FEF3C7;padding:14px;border-radius:18px;text-align:center'>🍲</div>", unsafe_allow_html=True)
    st.markdown("<center>Food</center>")
e,f,g,h=st.columns(4)
with e:
    st.markdown("<div style='background:#FFEDD5;padding:14px;border-radius:18px;text-align:center'>🚗</div>", unsafe_allow_html=True)
    st.markdown("<center>Car Mart</center>")
with f:
    st.markdown("<div style='background:#DCFCE7;padding:14px;border-radius:18px;text-align:center'>💼</div>", unsafe_allow_html=True)
    st.markdown("<center>Services</center>")
with g:
    st.markdown("<div style='background:#FCE7F3;padding:14px;border-radius:18px;text-align:center'>🎟️</div>", unsafe_allow_html=True)
    st.markdown("<center>Tickets</center>")
with h:
    st.markdown("<div style='background:#DCFCE7;padding:14px;border-radius:18px;text-align:center'>💬</div>", unsafe_allow_html=True)
    st.markdown("<center>Chat Rooms</center>")
st.markdown("### Featured Listing")
m1="<div style='background:#D1FAE5;"
m1+="padding:14px;border-radius:18px'>"
m1+="<b>Mama Oloja AI</b><br>"
m1+="Welcome my dear, I can help you "
m1+="find the best price in the market.</div>"
st.markdown(m1, unsafe_allow_html=True)
st.markdown("### Horlance Auto Cooling Ltd")
c1="<div style='background:white;"
c1+="padding:16px;border-radius:20px;"
c1+="box-shadow:0 4px 16px #EDEDED'>"
c1+="<span style='background:#00A651;color:white;"
c1+="padding:4px 10px;border-radius:20px;float:right'>VERIFIED</span>"
c1+="<b>Horlance Auto Cooling Ltd</b>"
c1+="<p>Car AC Repair - <b>N25000</b></p>"
c1+="<p>Osun & Oyo - 09046044472</p>"
c1+="<p>Pay: <b>Pay on Delivery</b></p>"
c1+="<p>Delivery: <b>Delivery Available</b></p></div>"
st.markdown(c1, unsafe_allow_html=True)
st.link_button("Chat Horlance", "https://wa.me/2349046044472")
st.markdown("### Mama T")
c2="<div style='background:white;"
c2+="padding:16px;border-radius:20px;"
c2+="box-shadow:0 4px 16px #EDEDED'>"
c2+="<b>Mama T</b>"
c2+="<p>Bag of Rice - <b>N45000</b></p>"
c2+="<p>Abuja - 09046044472</p>"
c2+="<p>Pay: <b>Transfer Before Delivery</b></p>"
c2+="<p>Delivery: <b>Pickup Only</b></p></div>"
st.markdown(c2, unsafe_allow_html=True)
st.link_button("Chat Mama T", "https://wa.me/2349046044472")
st.markdown("### New Goods")
for g in st.session_state.goods:
    st.success(g)
st.markdown("### Sell - FREE")
n1=st.text_input("Your Name")
n5=st.text_input("Product Name")
n6=st.text_input("Price")
n7=st.selectbox("Payment", ["Pay on Delivery","Transfer Before Delivery"])
n8=st.selectbox("Delivery", ["Pickup Only","Delivery Available"])
if st.button("POST MY GOODS FOR FREE"):
    txt=n1+" - "+n5+" - N"+n6
    st.session_state.goods.append(txt)
    st.success("Posted! "+txt)
    st.balloons()
b1="<div style='background:#00A651;"
b1+="padding:14px;border-radius:20px 20px 0 0;"
b1+="color:white;text-align:center'>"
b1+="<b>Home</b> &nbsp; | &nbsp; "
b1+="<b>Shop</b> &nbsp; | &nbsp; "
b1+="<b>Orders</b> &nbsp; | &nbsp; <b>Profile</b></div>"
st.markdown(b1, unsafe_allow_html=True)
