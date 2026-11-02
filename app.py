import streamlit as st
import json, hashlib, random, pandas as pd
from datetime import datetime

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="centered")

AUTH_FILE="users.json"
DB_FILE="listings.json"
WALLET_FILE="wallets.json"
CHAT_FILE="global_chat.json"

def load_json(f, d):
    try: return json.loads(open(f).read())
    except: return d

def save_json(f, data):
    open(f,"w").write(json.dumps(data))

def hash_pw(p):
    return hashlib.sha256(p.encode()).hexdigest()

users=load_json(AUTH_FILE,{})
if "08116911722" not in users:
    users["08116911722"]={"name":"CEO Kilani","pw":hash_pw("Kilani247")}
    users["2348116911722"]={"name":"CEO Kilani","pw":hash_pw("Kilani247")}
    save_json(AUTH_FILE,users)
    w=load_json(WALLET_FILE,{})
    w["08116911722"]=500000
    w["2348116911722"]=500000
    save_json(WALLET_FILE,w)

if "user_phone" not in st.session_state:
    st.title("ROW ECONOMY SUPER")
    st.caption("Use 08116911722 / Kilani247 - Data Restored")
    phone=st.text_input("Phone")
    pw=st.text_input("Password")
    if st.button("Login"):
        users=load_json(AUTH_FILE,{})
        ok=False
        for k in [phone, "234"+phone[1:]]:
            if phone.startswith("0") and k in users:
                if users[k]["pw"]==hash_pw(pw):
                    st.session_state.user_phone=k
                    ok=True
            if k in users:
                if users[k]["pw"]==hash_pw(pw):
                    st.session_state.user_phone=k
                    ok=True
        if ok:
            st.rerun()
        else:
            st.error("Wrong - Use 08116911722 / Kilani247")
    st.stop()

balance=load_json(WALLET
