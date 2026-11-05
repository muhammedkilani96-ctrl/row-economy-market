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
st.markdown("**Horlance Auto**")
st.markdown("Car AC Repair - N25000")
st.markdown("Osun & Oyo - 09046044472")
st.markdown("Payment: Pay on Delivery")
st.markdown("Delivery: Delivery Available")
link="https://wa.me/2349046044472"
st.link_button("Chat on WhatsApp", link)
st.markdown("**Mama T**")
st.markdown("Bag of Rice - N45000")
st.markdown("Abuja - 09046044472")
st.markdown("Payment: Transfer Before Delivery")
st.markdown("Delivery: Pickup Only")
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
st.markdown("### Bottom")
st.markdown("Home | Shop | Orders | Profile")
