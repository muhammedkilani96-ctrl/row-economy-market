import streamlit as st
import urllib.parse as u

W="2348116911722"

st.markdown("""
<style>
.stApp{background:#fdf6e3;}
h1,h2,h3,p,label{color:#3b1f0b !important;}
.stButton>button{border-radius:12px;font-weight:bold;}
</style>
""", unsafe_allow_html=True)

st.title("Row Economy")
st.markdown("**Ankara • Drum • Calabash • Hut • Garage**")

# --- ADINKRA CATEGORY BUTTONS ---
st.subheader("Browse Categories - Adinkra")
c1,c2,c3,c4=st.columns(4)

with c1:
  st.markdown("### 🪘")
  st.markdown("**Food**")
  st.caption("Adinkra: Gye Nyame\nExcept God")
  st.markdown("♻️")

with c2:
  st.markdown("### 🛖")
  st.markdown("**Event**")
  st.caption("Adinkra: Sankofa\nGo Back & Get It")
  st.markdown("🔄")

with c3:
  st.markdown("### 🏺")
  st.markdown("**Cloth**")
  st.caption("Adinkra: Duafe\nBeauty Love")
  st.markdown("🌸")

with c4:
  st.markdown("### 🚗")
  st.markdown("**Car**")
  st.caption("Adinkra: Ese Ne Tekrema\nFriends Help")
  st.markdown("🤝")

st.divider()
s=st.selectbox("State",["Abuja","
