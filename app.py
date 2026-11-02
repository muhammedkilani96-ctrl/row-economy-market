import streamlit as st
import urllib.parse as u

W="2348116911722"

st.set_page_config(page_title="Row Economy",layout="wide")

st.markdown("""
<style>
.stApp{background:white;}
header{visibility:hidden;}
.main-green{background:#006600;color:white;padding:15px;border-radius:0 0 20px 20px;}
.welcome{background:#e6f4ea;padding:15px;border-radius:12px;}
.banner{background:#006600;color:white;padding:15px;border-radius:12px;}
.card{border:1px solid #00660033;padding:10px;border-radius:12px;}
.stButton>button{background:#006600;color:white;border-radius:8px;width:100%;}
</style>
""",unsafe_allow_html=True)

# --- TOP GREEN HEADER ---
st.markdown('<div class="main-green"><h1 style="color:white !important;">Row Economy</h1></div>',unsafe_allow_html=True)

# --- BOTTOM NAV LIKE IMAGE ---
nav=st.tabs(["Home","Explore","Sell","Chats","Profile"])

with nav[0]:
  # Welcome
  name=st.text_input("Your name","Chinedu")
  st.markdown(f'<div class="welcome"><h3>Welcome back, {name}!</h3><p>Find products, events, services near you - made in Nigeria 🇳🇬</p></div>',unsafe_allow_html=True)
  
  st.write("")
  search=st.text_input("Search","",placeholder="Search for food, fabrics, cars, events...")
  
  st.write("")
  st.markdown('<div class="banner"><h3>🪘 Empowering Local Trade</h3><p>Buy • Sell • Connect with your community</p></div>',unsafe_allow_html=True)
  
  st.write("")
  st.subheader("Explore Categories")
  c1,c2,c3,c4,c5=st.columns(5)
  with c1:
    st.button("🍲\nFood")
  with c2:
    st.button("🗓️\nEvent")
  with c3:
    st.button("👗\nCloth")
  with c4:
    st.button("🚗\nCars")
  with c5:
    st.button("🏘️\nSquare")

  st.subheader("Featured Near You")
  f1,f2=st.columns(2)
  with f1:
    st.markdown('<div class="card">',
