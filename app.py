import streamlit as st
import streamlit.components.v1 as comp

st.set_page_config(page_title="Row Economy")

st.markdown("""
<style>
.stApp{background:#000000 !important;}
h1{color:#00FF66 !important;}
h2,h3{color:#FFFFFF !important;}
p, label, div{color:#FFFFFF !important;}
.stButton>button{background:#006600 !important; color:white !important;}
</style>
""", unsafe_allow_html=True)

st.title("Row Economy")
st.write("Black Background - Green White Green")

# REAL LOCATION - safe single line
comp.html('<button onclick="getLoc()" style="background:#006600;color:white;padding:10px;border-radius:8px;border:none;width:100%;">Use My Real Location</button><p id="loc" style="color:white;margin-top:10px;"></p><script>function getLoc(){if(navigator.geolocation){navigator.geolocation.getCurrentPosition(function(p){document.getElementById("loc").innerHTML="Real GPS: "+p.coords.latitude.toFixed(5)+", "+
