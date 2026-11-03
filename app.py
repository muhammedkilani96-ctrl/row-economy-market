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

# LOGIN - ACCEPTS BOTH CASES
if "user" not in st.session_state:
 st.title("ROW ECONOMY SUPER - LIVE MARKET")
 st.info("Login: 08116911722 / Kilani247")
 phone=st.text_input("Phone")
 pw=st.text_input("Password", type="password")
 if st.button("Login"):
  if phone.strip()=="08116911722" and pw.strip().lower()=="kilani247":
   st.session_state.user=phone.strip()
   st.rerun()
  else:
   st.error("Wrong - use 08116911722 / Kilani247")
 st.stop()

# DATA
wallets=load("wallets.json",{})
if wallets.get("08116911722",0)<1000:
 wallets["08116911722"]=500000
 save("wallets.json",wallets)

products=load("products.json",[])
lives=load("lives.json",[])

bal=wallets.get(st.session_state.user,500000)
st.title("ROW ECONOMY SUPER")
st.success(f"Welcome {st.session_state.user} | Bal N{bal}")

t1,t2,t3,t4,t5,t6,t7=st.tabs(["LIVE MARKET","POST PRODUCT","GO LIVE","MAP","SECURITY","SOS","Wallet"])

# 1 - LIVE MARKET - SEE ALL PRODUCTS + LIVE PEOPLE
with t1:
 st.title("🔴 LIVE MARKETPLACE")
 st.caption("People posting + going live now")
 
 # Show LIVE users first
 if lives:
  st.subheader("🔴 LIVE NOW")
  for live in lives[-5:][::-1]:
   st.error(f"🔴 {live['user']} IS LIVE - {live['title']}")
   st.write(f"{live['desc']} - {live['time']}")
   if st.button(f"Join {live['user']} Live", key=f"join_{live['time']}"):
    st.balloons()
    st.success(f"Joined {live['user']} live!")
  st.divider()
 
 # Show Products
 if not products:
  st.write("No products yet - Be first to post!")
 else:
  st.subheader(f"{len(products)} Products For Sale")
  for p in products[::-1]:
   st.write(f"**{p['name']} - N{p['price']}**")
   st.write(f"By {p['user']} | {p['phone']}")
   st.write(p['desc'])
   if p.get('img'):
    st.image(p['img'], width=250)
   st.link_button(f"Chat Seller {p['phone']}", f"https://wa.me/{p['phone']}")
   st.divider()

# 2 - POST PRODUCT
with t2:
 st.title("Post Your Product")
 st.write("Sell anything - food, clothes, gadgets")
 name=st.text_input("Product Name e.g. Bag of Rice")
 price=st.number_input("Price N", 100, 10000000, 1000)
 desc=st.text_area("Description")
 seller_phone=st.text_input("Your WhatsApp No", value=st.session_state.user)
 img=st.text_input("Image Link (optional) - paste from google")
 if st.button("POST PRODUCT NOW"):
  if name and price:
   new_p
