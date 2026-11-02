import streamlit as st
import json, hashlib
st.set_page_config(page_title="ROW ECONOMY SUPER", layout="centered")
def load(f,d):
 try: return json.loads(open(f).read())
 except: return d
def save(f,data):
 open(f,"w").write(json.dumps(data))
def hp(p):
 import hashlib
 return hashlib.sha256(p.encode()).hexdigest()
users=load("users.json",{})
if "08116911722" not in users:
 users["08116911722"]={"name":"CEO","pw":hp("Kilani247")}
 save("users.json",users)
if "user" not in st.session_state:
 st.title("ROW ECONOMY SUPER")
 st.info("Login 08116911722 / Kilani247")
 phone=st.text_input("Phone")
 pw=st.text_input("Password")
 if st.button("Login"):
  if phone in users and users[phone]["pw"]==hp(pw):
   st.session_state.user=phone
   st.rerun()
  else:
   st.error("Wrong")
 st.stop()
st.title("ROW ECONOMY SUPER")
st.write("Welcome "+st.session_state.user)
if st.button("Logout"):
 del st.session_state.user
 st.rerun()
st.success("APP WORKING! Now I will add maps back")
