import streamlit as st
import urllib.parse as u

W="2348116911722"

st.set_page_config(page_title="Row Economy")

st.markdown("""
<style>
.stApp{background:#FFFFFF !important;}
h1{color:#006600 !important; font-weight:900 !important;}
h2,h3{color:#006600 !important;}
p, label, div, span{color:#111111 !important;}
input{color:#000000 !important; background:#FFFFFF !important;}
div[data-baseweb="tab"]{color:#006600 !important;}
.stButton>button{background:#006600 !important; color:white !important; border:none !important;}
</style>
""",unsafe_allow_html=True)

st.title("Row Economy")
st.write("Naija Green White Green - Made in Nigeria")

nav=st.tabs(["Home","Explore","Sell","Chats","Profile"])

with nav[0]:
  name=st.text_input("Your name", "Chinedu")
  st.success(f"Welcome back, {name}! Find products made in Nigeria 🇳🇬")
  
  search=st.text_input("Search", placeholder="Search food, fabrics, cars, events")
  
  st.markdown("### Empowering Local Trade")
  st.caption("Buy • Sell • Connect with your community")
  
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
    st.write("Fresh Yam")
    st.caption("Kano - N5,500")
    st.link_button("View","https://wa.me/"+W+"?text="+u.quote("Yam"))
  with f2:
    st.write("Ankara Green White")
    st.caption("Lagos - N12,000")
    st.link_button("View","https://wa.me/"+W+"?text="+u.quote("Ankara"))

with nav[1]:
  st.subheader("Explore")
  st.slider("Price",500,50000,2000)

with nav[2]:
  st.subheader("Sell")
  pname=st.text_input("Product name")
  pprice=st.number_input("Price",100,1000000,2000)
  if st.button("Post"):
    st.success("Posted!")

with nav[3]:
  st.subheader("Chats")
  st.link_button("WhatsApp","https://wa.me/"+W)

with nav[4]:
  st.subheader("Profile")
  st.write("Name: "+name)
  st.link_button("Police CMR","https://cmris.npf.gov.ng")
