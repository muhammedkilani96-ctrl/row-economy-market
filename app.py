import streamlit as st
import urllib.parse as u

W="2348116911722"

st.set_page_config(page_title="Row Economy")

st.markdown("<style>.stApp{background:white;}h1{color:#006600;}</style>",unsafe_allow_html=True)

st.title("Row Economy")
st.caption("Naija Green White Green")

nav=st.tabs(["Home","Explore","Sell","Chats","Profile"])

with nav[0]:
  name=st.text_input("Your name","Chinedu")
  st.success(f"Welcome back, {name}! Find products made in Nigeria")
  
  search=st.text_input("Search food, fabrics, cars, events")
  
  st.success("Empowering Local Trade - Buy Sell Connect")
  
  st.subheader("Explore Categories")
  c1,c2,c3,c4,c5=st.columns(5)
  c1.button("Food")
  c2.button("Event")
  c3.button("Cloth")
  c4.button("Cars")
  c5.button("Square")

  st.subheader("Featured Near You")
  f1,f2=st.columns(2)
  with f1:
    st.write("**Fresh Yam & Vegetables**")
    st.caption("Kano Market - N5,500")
    st.link_button("View","https://wa.me/"+W+"?text="+u.quote("Yam"))
  with f2:
    st.write("**Ankara Green White**")
    st.caption("Lagos - N12,000")
    st.link_button("View","https://wa.me/"+W+"?text="+u.quote("Ankara"))

  st.divider()
  S=["Abuja","Lagos","Kano"]
  s=st.selectbox("State",S)
  a=st.text_input("Area","Wuse")

with nav[1]:
  st.subheader("Explore")
  st.slider("Price",500,50000,2000)

with nav[2]:
  st.subheader("Sell - Post Product")
  pname=st.text_input("Product name")
  pprice=st.number_input("Price",100,1000000,2000)
  pimg=st.file_uploader("Upload photo")
  if st.button("Post"):
    st.success("Posted to Village Square")

with nav[3]:
  st.subheader("Chats")
  st.link_button("Open WhatsApp","https://wa.me/"+W)

with nav[4]:
  st.subheader
