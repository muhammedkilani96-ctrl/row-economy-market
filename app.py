import streamlit as st
import json, random, pandas as pd
from datetime import datetime

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="centered")

def load(f,d):
 try:
  return json.loads(open(f).read())
 except:
  return d

def save(f,data):
 open(f,"w").write(json.dumps(data))

if "user" not in st.session_state:
 st.title("ROW ECONOMY SUPER")
 st.info("Login: 08116911722 / Kilani247")
 phone=st.text_input("Phone")
 pw=st.text_input("Password", type="password")
 if st.button("Login"):
  if phone.strip()=="08116911722" and pw.strip().lower()=="kilani247":
   st.session_state.user=phone.strip()
   st.rerun()
  else:
   st.error("Wrong login")
 st.stop()

wallets=load("wallets.json",{})
if wallets.get("08116911722",0)<1000:
 wallets["08116911722"]=500000
 save("wallets.json",wallets)

products=load("products.json",[])
lives=load("lives.json",[])

bal=wallets.get(st.session_state.user,500000)
st.title("ROW ECONOMY SUPER")
st.success(f"Welcome {st.session_state.user} | Bal N{bal}")

tab1,tab2,tab3,tab4,tab5,tab6,tab7=st.tabs(["LIVE MARKET","POST PRODUCT","GO LIVE","MAP","SECURITY","SOS","Wallet"])

with tab1:
 st.title("LIVE MARKETPLACE")
 st.caption("People posting + going live now")
 if lives:
  st.subheader("LIVE NOW")
  for live in lives[-5:][::-1]:
   st.error(f"LIVE {live['user']} - {live['title']}")
   st.write(live['desc'])
  st.divider()
 if not products:
  st.write("No products yet - Be first to post!")
 else:
  st.subheader(f"{len(products)} Products")
  for p in products[::-1]:
   st.write(f"{p['name']} - N{p['price']}")
   st.write(f"By {p['user']} | {p['phone']}")
   st.write
