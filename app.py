import streamlit as st
import json, random, pandas as pd

st.set_page_config(page_title="ROW ECONOMY", layout="centered")

def load(f,d):
 try:
  return json.loads(open(f).read())
 except:
  return d

def save(f,data):
 open(f,"w").write(json.dumps(data))

if "user" not in st.session_state:
 st.title("ROW ECONOMY SUPER")
 st.info("08116911722 / Kilani247")
 phone=st.text_input("Phone")
 pw=st.text_input("Password", type="password")
 if st.button("Login"):
  if phone=="08116911722" and pw=="Kilani247":
   st.session_state.user=phone
   st.rerun()
  else:
   st.error("Wrong login")
 st.stop()

wallets=load("wallets.json",{})
if wallets.get("08116911722",0)<1000:
 wallets["08116911722"]=500000
 save("wallets.json",wallets)

bal=wallets.get(st.session_state.user,500000)
st.title("ROW ECONOMY SUPER")
st.success("Welcome")

t1,t2,t3,t4,t5,t6=st.tabs(["Home","MAP","SECURITY","SOS","CHAT","Wallet"])

with t1:
 st.write("Food Calculator")
 people=st.number_input("People",1,500,10)
 st.write(people*1000)
 st.link_button("Order WA","https://wa.me/2348116911722")

with t2:
 st.title("SNAP MAP")
 lat=[]
 lon=[]
 for i in range(30):
  lat.append(9.06+random.uniform(-0.03,0.03))
  lon.append(7.48+random.uniform(-0.03,0.03))
 df=pd.DataFrame({"lat":lat,"lon":lon})
 st.map(df)

with t3:
 st.title("SECURITY MAP")
 st.map(pd.DataFrame({"lat":[9.07,9.05,6.52],"lon":[7.48,7.49,3.37]}))
 st.write("NANS HQ Abuja")
 st.write("Police HQ")

with t4:
 st.title("SOS")
 if st.button("SEND SOS"):
  st.error("SOS SENT")
  st.balloons()
 st.link_button("Call 112","tel:112")

with t5:
 st.title("CHAT")
 chats=load("global_chat.json",[])
 for chat in chats:
  st.write(chat)
 msg=st.text_input("Message")
 if st.button("Send"):
  new_msg=st.session_state.user+": "+msg
  chats.append(new_msg)
  save("global_chat.json",chats)
  st.rerun()

with t6:
 st.title("Wallet")
 st.write(bal)
 st.image("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data="+st.session_state.user)
 if st.button("Logout"):
  del st.session_state.user
  st.rerun()
