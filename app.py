import streamlit as st
import streamlit.components.v1 as comp
st.set_page_config(page_title="Row Economy")
st.markdown("<style>.stApp{background:#000000;}h1{color:#00FF66;}h2,h3{color:white;}p,div{color:white;}.stButton>button{background:#006600;color:white;}</style>", unsafe_allow_html=True)
st.title("Row Economy")
comp.html('<button onclick="getLoc()" style="background:#006600;color:white;padding:10px;border-radius:8px;border:none;width:100%;">Use My Real Location</button><p id="loc" style="color:white;"></p><script>function getLoc(){if(navigator.geolocation){navigator.geolocation.getCurrentPosition(function(p){document.getElementById("loc").innerHTML="GPS: "+p.coords.latitude.toFixed(5)+","+p.coords.longitude.toFixed(5);},function(e){document.getElementById("loc").innerHTML="Allow location in browser";});}}</script>', height=100)
a=st.text_input("Area","Wuse 2")
s=st.selectbox("State",["Abuja","Lagos","Kano","Rivers","Kaduna"])
t1,t2,t3=st.tabs(["Home","Advertise Here","Profile"])
with t1:
 st.write("Welcome to "+a+", "+s)
 st.write("Food | Cloth | Cars | Events")
with t2:
 st.header("Advertise Here - People will advertise here")
 biz=st.text_input("Business Name","Baba")
 what=st.text_input("What you sell","Jollof rice")
 price=st.number_input("Price N",100,10000000,2000)
 if st.button("Post Advert Now"):
  st.success("Posted: "+biz+" - "+what+" - "+s)
  st.balloons()
with t3:
 st.link_button("CMRIS Verify","https://cmris.npf.gov.ng")
 st.link_button("WhatsApp","https://wa.me/2348116911722")
