import streamlit as st
import streamlit.components.v1 as comp

st.set_page_config(page_title="Row Economy - Naija Market", layout="wide", initial_sidebar_state="collapsed")

# === BLACK + GREEN WHITE GREEN THEME ===
st.markdown("<style>.stApp{background:#000000 !important;}h1,h2,h3{color:#00FF66 !important;}h1{font-weight:900;}p,div,label,span{color:#FFFFFF !important;}.stButton>button{background:#006600 !important;color:white !important;border:1px solid #00FF66 !important;border-radius:10px;padding:10px;font-weight:bold;width:100%;}.stTabs [data-baseweb=tab]{color:white !important;}.stTextInput>div>div>input,.stNumberInput>div>div>input,.stTextArea>div>textarea{background:#111111 !important;color:white !important;border:1px solid #00FF66 !important;}</style>", unsafe_allow_html=True)

st.title("Row Economy")
st.markdown("**Naija Market • Black Background • Green White Green • Advertise Here • Real Location**")

# === REAL LOCATION LIKE GOOGLE ===
comp.html('<div style="text-align:center;padding:10px;"><button onclick="getLoc()" style="background:#006600;color:white;padding:14px 20px;border-radius:12px;border:1.5px solid #00FF66;width:100%;font-weight:bold;font-size:16
