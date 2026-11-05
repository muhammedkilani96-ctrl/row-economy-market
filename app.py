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
cat1="<div style='display:flex;"
cat1+="flex-wrap:wrap;gap:8px'>"
cat1+="<div style='width:23%;text-align:center;font-size:13px'>"
cat1+="<div style='background:#FDE7F3;"
cat1+="padding:14px;border-radius:18px'>🧴</div>"
cat1+="Perfume</div>"
cat1+="<div style='width:23%;text-align:center;font-size:13px'>"
cat1+="<div style='background:#E0F2FE;"
cat1+="padding:14px;border-radius:18px'>👕</div>"
cat1+="Clothes</div>"
cat1+="<div style='width:23%;text-align:center;font-size:13px'>"
cat1+="<div style='background:#DBEAFE;"
cat1+="padding:14px;border-radius:18px'>📱</div>"
cat1+="Phones</div>"
cat1+="<div style='width:23%;text-align:center;font-size:13px'>"
cat1+="<div style='background:#FEF3C7;"
cat1+="padding:14px;border-radius:18px'>🍲</div>"
cat1+="Food</div>"
cat1+="<div style='width:23%;text-align:center;font-size:13px'>"
cat1+="<div style='background:#FFEDD5;"
cat1+="padding:14px;border-radius:18px'>🚗</div>"
cat1+="Car Mart</div>"
cat1+="<div style='width:23%;text-align:center;font-size:13px'>"
cat1+="<div style='background:#DCFCE7;"
cat1+="padding:14px;border-radius:18px'>💼</div>"
cat1+="Services</div>"
cat1+="<div style='width:23%;text-align:center;font-size:13px'>"
cat1+="<div style='background:#FCE7F3;"
cat1+="padding:14px;border-radius:18px'>🎟️</div>"
cat1+="Tickets</div>"
cat1+="
