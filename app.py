import streamlit as st
import urllib.parse as u

W="2348116911722"
c1="<style>"
c2=".stApp{background:#fdf6e3;}"
c3="h1{color:#8B4513;}"
c4="</style>"
st.markdown(c1+c2+c3+c4,unsafe_allow_html=True)

st.title("Row Economy")
st.write("Drum Calabash Hut Garage")

s=st.selectbox("State",["Abuja","Lagos","Kano"])
a=st.text_input("Area","Wuse")
t1,t2,t3,t4,t5=st.tabs(["Food","Event","Cloth","Car","Square"])

with t1:
  p=st.number_input("People",1,500,10)
  tot=p*1500
  st.write(f"Total N{tot}")
  txt=f"Food {p} {a} {s}"
  q=u.quote(txt)
  lk="https://wa.me/"+W+"?text="+q
  st.link_button("Order Food",lk)

with t2:
  ev=st.text_input("Event","Concert")
  pr=st.number_input("Price",500,50000,2000)
  qty=st.number_input("Qty",1,20,1)
  tot2=pr*qty
  st.write(f"Total N{tot2}")
  txt2=f"Event {ev} {a} {s}"
  q2=u.quote(txt2)
  lk2="https://wa.me/"+W+"?text="+q2
  st.link_button("Buy Ticket",lk2)

with t3:
  cl=st.selectbox("Cloth",["Shirt","Native"])
  sz=st.selectbox("Size",["M","L","XL"])
  txt3=f"Cloth {cl} {sz} {a} {s}"
  q3=u.quote(txt3)
  lk3="https://wa.me/"+W+"?text="+q3
  st.link_button("Buy Cloth",lk3)

with t4:
  st.info("Law Protected - Must Verify")
  car=st.selectbox("Car",["Corolla","Sienna"])
  vin=st.text_input("Chassis VIN")
  cert=st.file_uploader("Upload cert")
  ag1=st.checkbox("Car not stolen")
  ag2=st.checkbox("Row is marketplace only")
  ag3=st.checkbox("Report to Police if fake")
  st.link_button("Police CMR","https://cmris.npf.gov.ng")
  if cert and ag1 and ag2 and ag3 and vin!="":
    st.success("VERIFIED DEALER")
    txt4=f"Car {car} {vin} Verified {a} {s}"
    q4=u.quote(txt4)
    lk4="https://wa.me/"+W+"?text="+q4
    st.link_button("Submit For Approval",lk4)
  else:
    st.error("Upload + 3 ticks + VIN")

with t5:
  st.write("Village Square")
  vid=st.file_uploader("Post video")
  if vid:
    st.video(vid)
    st.success("Posted!")

st.caption("Row Economy - Verified - Abuja 08116911722")
