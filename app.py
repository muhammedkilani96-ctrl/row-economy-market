import streamlit as st
import streamlit.components.v1 as comp
import urllib.parse as u

W="2348116911722"
st.set_page_config(page_title="Row Economy")

st.markdown("<style>.stApp{background:white;}h1{color:#006600;}</style>",unsafe_allow_html=True)

st.title("Row Economy")
st.caption("Naija Green White Green + Real Location")

# --- REAL LOCATION PERMISSION ---
st.subheader("📍 Real Location")
st.write("Click to allow GPS - like Police CMRIS")

loc_html="""
<button onclick="getLoc()" style="background:#006600;color:white;padding:10px;border-radius:8px;border:none;width:100%;">Use My Real Location</button>
<p id="loc" style="color:black;margin-top:10px;"></p>
<script>
function getLoc(){
  if(navigator.geolocation){
    navigator.geolocation.getCurrentPosition(function(pos){
      var lat=pos.coords.latitude;
      var lon=pos.coords.longitude;
      document.getElementById("loc").innerHTML="✅ Real GPS: "+lat.toFixed(5)+", "+lon.toFixed(5)+"<br><a href='https://maps.google.com/?q="+lat+","+lon+"' target='_blank'>Open in Google Maps</a><br>Permission Granted!";
    }, function(err){
      document.getElementById("loc").innerHTML="❌ Denied: "+err.message;
    });
  } else {
    document.getElementById("loc").innerHTML="Geolocation not supported";
  }
}
</script>
"""
comp.html(loc_html, height=180)

# Fallback manual
S=["Abuja","Lagos","Kano","Rivers","Kaduna"]
s=st.selectbox("State (auto from GPS)",S)
a=st.text_input("Area / Street","Wuse 2 - Real location verified")
st.caption("TIP: Allow location above, then copy lat/long to Area for verification like CMRIS")

# --- REST OF APP ---
nav=st.tabs(["Home","Explore","Sell","Chats","Profile"])
with nav[0]:
  name=st.text_input("Your name","Chinedu")
  st.success(f"Welcome {name}! Location: {a}, {s}")
  st.text_input("Search",placeholder="Search food, fabrics, cars...")
  st.success("Empowering Local Trade")
  c1,c2,c3,c4,c5=st.columns(5)
  c1.button("Food")
  c2.button("Event")
  c3.button("Cloth")
  c4.button("Cars")
  c5.button("Square")
  f1,f2=st.columns(2)
  with f1:
    st.write("Fresh Yam - Kano")
    st.link_button("View","https://wa.me/"+W+"?text="+u.quote("Yam"))
  with f2:
    st.write("Ankara GWG - Lagos")
    st.link_button("View","https://wa.me/"+W+"?text="+u.quote("Ankara"))

with nav[1]:
  st.subheader("Explore Near Me")
  st.write(f"Showing items near {s} - {a}")
  st.slider("Distance km",1,50,5)

with nav[2]:
  st.subheader("Sell with Real Location")
  pname=st.text_input("Product")
  pprice=st.number_input("Price",100,1000000,2000)
  st.checkbox(f"Verify I am really in {a}, {s} - Real GPS")
  if st.button("Post with Location"):
    st.success(f"Posted! Buyers see you are in {a} - Real location ON")

with nav[3]:
  st.link_button("WhatsApp","https://wa.me/"+W)

with nav[4]:
  st.subheader("CMRIS Verification")
  st.write("For cars, verify at Police CMRIS")
  st.link_button("Open CMRIS - cmris.npf.gov.ng","https://cmris.npf.gov.ng")
  st.write("Your real location helps Police verify ownership")

st.caption("Row Economy - Real GPS + CMRIS Link")
