import streamlit as st
import streamlit.components.v1 as comp

st.set_page_config(page_title="Row Economy", layout="wide")

st.markdown("<style>.stApp{background:#000000;}h1,h2{color:#00FF66;}p,div,label{color:white;}.stButton>button{background:#006600;color:white;border:1px solid #00FF66;border-radius:10px;width:100%;}</style>", unsafe_allow_html=True)

st.title("Row Economy")
st.write("Black Background - Green White Green - Real Location - Advertise Here")

# FIXED REAL LOCATION - triple quote safe
location_html = """
<div style="text-align:center;">
<button onclick="getLoc()" style="background:#006600;color:white;padding:12px;border-radius:10px;border:1px solid #00FF66;width:100%;font-weight:bold;">
Use My Real Location
</button>
<p id="loc" style="color:#00FF66;margin-top:10
