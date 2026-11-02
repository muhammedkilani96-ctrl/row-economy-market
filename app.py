import streamlit as st, json, os, hashlib, random, pandas as pd
from datetime import datetime, date

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="centered", page_icon="🛒")

# --- FILES ---
AUTH_FILE="users.json"
DB_FILE="listings.json"
WALLET_FILE="wallets.json"
TX_FILE="transactions.json"
CHAT_FILE="global_chat.json"
SOS_FILE="sos_alerts.json"

def load_json(f, default):
    if not os.path.exists(f): return default
    try: return json.loads(open(f).read())
    except: return default
def save_json(f, data): open(f,"w").write(json.dumps(data))

def hash_pw(p): return hashlib.sha256(p.encode()).hexdigest()

# --- INIT ---
for k in ["ads_today","paid_unlock","live_gifts","live_comments","verified"]:
    if k not in st.session_state:
        if k in ["ads_today","live_gifts"]: st.session_state[k]=0
        elif k=="live_comments": st.session_state[k]=[]
        else: st.session_state[k]=False

# --- LOGIN ---
if "user_phone" not in st.session_state:
    st.title("🔐 ROW ECONOMY SUPER")
    st.caption("NANS + Security + SNAP MAP + SOS + Wallet + N5000 Bonus")
    users=load_json(AUTH_FILE,{})
    t1,t2=st.tabs(["Login","Register"])
    with t1:
        phone=st.text_input("WhatsApp e.g 2348116911722")
        pw=st.text_input("Password",type="password")
        if st.button("Login",use_container_width=True):
            if phone in users and users[phone]["pw"]==hash_pw(pw):
                st.session_state.user_phone=phone
                st.session_state.user_name=users[phone]["name"]
                st.rerun()
            else: st.error("Wrong")
    with t2:
        name=st.text_input("Business Name")
        phone=st.text_input("Number",key="rp")
        pw=st.text_input("Create Password
