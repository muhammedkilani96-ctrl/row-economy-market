import streamlit as st
import urllib.parse as u

W="2348116911722"

# --- HIGH QUALITY AFRICAN THEME ---
st.markdown("""
<style>
.stApp{background:#fdf6e3;}
h1,h2,h3,p,label{color:#3b1f0b !important;}
div[data-baseweb="select"]{background:#fff;}
.stTabs [data-baseweb="tab"]{color:#3b1f0b;}
div.stButton>button{background:#228B22;color:white;font-weight:bold;border-radius:10px;}
</style>
""", unsafe_allow_html=True)

st.title("Row Economy")
st.markdown("**Drum Food | Calabash Cloth | Hut Event | Garage Car**")

s=st.selectbox("State",["Abuja","Lagos","Kano","Rivers","Kaduna"])
a=st.text_input("Area","Wuse")

t1,t2,t3,t4,t5=st.tabs(["Food","Event","Cloth","Car","Square"])

with t1:
  p=st.number_input("People",1,500,10)
  st.write(f"Total: N {p*1500}")
  txt=f"Food order {p} people {a} {s}"
  q=u.quote(txt)
  st.link_button("Order Food","https://wa.me/"+W+"?text="+q)

with t2:
  ev=st.text_input("Event Name","Concert")
  pr=st.number_input("Ticket Price",500,50000,2000)
  qty=st.number_input("Qty",1,20,1)
  st.write(f"Total: N {pr*qty}")
  txt2=f"Event {ev} {a} {s}"
  st.link_button("Buy Ticket","https://wa.me/"+W+"?text="+u.quote(txt2))

with t3:
  cl=st.selectbox("Cloth",["Ankara","Native","Shirt","Hijab"])
  sz=st.selectbox("Size",["M","L","XL","XXL"])
  st.link_button("Buy Cloth","https://wa.me/"+W+"?text="+u.quote(f"Cloth {cl} {sz} {a} {s}"))

with t4:
  st.warning("Verified Garage - CAC + NIN Required")
  car=st.selectbox("Car",["Corolla","Sienna","Hiace","Camry"])
  vin=st.text_input("Chassis VIN")
  cert=st.file_uploader("Upload CAC/NIN/Cert")
  ag1=st.checkbox("Car papers genuine, not stolen")
  ag2=st.checkbox("Row is marketplace only")
  ag3=st.checkbox("Agree report to Police CMR if fake")
  st.link_button("Verify at Police CMR","https://cmris.npf.gov.ng")
  if cert and ag1 and ag2 and ag3 and vin!="":
    st.success("GREEN VERIFIED DEALER - Ready for Approval")
    st.link_button("Submit","https://wa.me/"+W+"?text="+u.quote(f"Car {car} {vin} Verified {a}"))
  else:
    st.error("Complete VIN + Upload + 3 Ticks")

with t5:
  st.subheader("Village Square - Drum Beat")
  vid=st.file_uploader("Post your market video")
  if vid:
    st.video(vid)
    st.success("Village Square Posted!")

st.divider()
st.caption("Row Economy - Verified Marketplace - Abuja - 08116911722")
st.caption("Always verify chassis at cmris.npf.gov.ng - Law Protected")
