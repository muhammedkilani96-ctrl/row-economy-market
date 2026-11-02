import streamlit as st
import urllib.parse as u

W="2348116911722"

st.markdown("<style>.stApp{background:#fdf6e3;}h1{color:#3b1f0b !important;}</style>",unsafe_allow_html=True)

st.title("Row Economy")

# --- STATES SHORT ---
S=["Abuja","Lagos","Kano"]
s=st.selectbox("State",S)
a=st.text_input("Area","Wuse")

# --- ADINKRA CATS ---
c1,c2,c3,c4=st.columns(4)
with c1:
  st.write("🪘 Food")
  st.caption("Gye Nyame ♻️")
with c2:
  st.write("🛖 Event")
  st.caption("Sankofa 🔄")
with c3:
  st.write("🏺 Cloth")
  st.caption("Duafe 🌸")
with c4:
  st.write("🚗 Car")
  st.caption("Ese Ne 🤝")

t1,t2,t3,t4,t5=st.tabs(["Food","Event","Cloth","Car","Square"])

with t1:
  p=st.number_input("People",1,100,10)
  st.write(f"N {p*1500}")
  txt=f"Food {p} {a} {s}"
  st.link_button("Order Food","https://wa.me/"+W+"?text="+u.quote(txt))

with t2:
  ev=st.text_input("Event","Concert")
  pr=st.number_input("Price",500,50000,2000)
  q=st.number_input("Qty",1,20,1)
  st.write(f"N {pr*q}")
  st.link_button("Buy Ticket","https://wa.me/"+W+"?text="+u.quote(ev))

with t3:
  CL=["Ankara","Native","Shirt"]
  cl=st.selectbox("Cloth",CL)
  SZ=["M","L","XL"]
  sz=st.selectbox("Size",SZ)
  st.link_button("Buy Cloth","https://wa.me/"+W+"?text="+u.quote(cl))

with t4:
  st.warning("Verified Garage")
  CAR=["Corolla","Sienna","Hiace"]
  car=st.selectbox("Car",CAR)
  vin=st.text_input("VIN")
  cert=st.file_uploader("Upload cert")
  ag1=st.checkbox("Car genuine")
  ag2=st.checkbox("Marketplace only")
  ag3=st.checkbox("Report if fake")
  if cert and ag1 and ag2 and ag3 and vin!="":
    st.success("VERIFIED")
    st.link_button("Submit","https://wa.me/"+W+"?text="+u.quote(vin))
  else:
    st.error("Need cert + ticks + VIN")

with t5:
  st.write("Village Square")
  vid=st.file_uploader("Video")
  if vid:
    st.video(vid)
    st.success("Posted!")

st.caption("Row - Gye Nyame ♻️ Sankofa 🔄 Duafe 🌸")
