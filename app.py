import streamlit as st
import urllib.parse as u
st.set_page_config(page_title="Row Economy")
h1="<div style='background:#00A651;"
h1+="padding:16px;border-radius:0 0 20px 20px;"
h1+="color:white;text-align:center'>"
h1+="<b style='font-size:25px'>ROW ECONOMY</b>"
h1+="<p>Nigeria Sweetest Market</p></div>"
st.markdown(h1, unsafe_allow_html=True)
st.markdown("### Mama Oloja")
q=st.text_input("Ask Mama", placeholder="Rice, AC...")
st.markdown("### Featured")
c1="<div style='background:white;"
c1+="padding:16px;border-radius:20px;"
c1+="box-shadow:0 4px 16px #EDEDED'>"
c1+="<b>Horlance Auto Cooling Ltd</b>"
c1+="<p>Car AC Repair - <b>N25000</b></p>"
c1+="<p>Osun & Oyo - 09046044472</p>"
c1+="<p>Payment: <b>Pay on Delivery</b></p>"
c1+="<p>Delivery: <b>Delivery Available</b></p></div>"
st.markdown(c1, unsafe_allow_html=True)
link="https://wa.me/2349046044472"
st.link_button("Chat on WhatsApp", link)
c2="<div style='background:white;"
c2+="padding:16px;border-radius:20px;"
c2+="box-shadow:0 4px 16px #EDEDED'>"
c2+="<b>Mama T</b>"
c2+="<p>Bag of Rice - <b>N45000</b></p>"
c2+="<p>Abuja - 09046044472</p>"
c2+="<p>Payment: <b>Transfer Before Delivery</b></p>"
c2+="<p>Delivery: <b>Pickup Only</b></p></div>"
st.markdown(c2, unsafe_allow_html=True)
st.link_button("Chat Mama T", link)
st.markdown("### Sell - FREE for First 10")
n1=st.text_input("Your Name")
n2=st.text_input("WhatsApp")
n5=st.text_input("Product Name")
n6=st.text_input("Price")
n7=st.selectbox("Payment", ["Pay on Delivery","Transfer Before Delivery","Cash on Pickup"])
n8=st.selectbox("Delivery", ["Pickup Only","Delivery Available","Delivery + Pickup"])
if st.button("POST MY GOODS FOR FREE"):
    st.success("Done! "+n1+" - "+n5)
    st.success("Pay: "+n7)
    st.success("Delivery: "+n8)
    st.balloons()
b1="<div style='background:#00A651;"
b1+="padding:14px;border-radius:20px 20px 0 0;"
b1+="color:white;text-align:center'>"
b1+="<b>Home</b> &nbsp; | &nbsp; "
b1+="<b>Shop</b> &nbsp; | &nbsp; "
b1+="<b>Orders</b> &nbsp; | &nbsp; <b>Profile</b></div>"
st.markdown(b1, unsafe_allow_html=True)
