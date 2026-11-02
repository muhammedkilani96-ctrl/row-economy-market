import streamlit as st
import json
import os
import hashlib
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="ROW ECONOMY", layout="centered")

AUTH_FILE="users.json"
DB_FILE="listings.json"
WALLET_FILE="wallets.json"
CHAT_FILE="global_chat.json"
SOS_FILE="sos_alerts.json"

def load_json(f, default):
    if not os.path.exists(f):
        return default
    try:
        return json.loads(open(f).read())
    except:
        return default

def save_json(f, data):
    open(f,"w").write(json.dumps(data))

def hash_pw(p):
    return hashlib.sha256(p.encode()).hexdigest()

if "user_phone" not in st.session_state:
    st.title("ROW ECONOMY SUPER")
    users=load_json(AUTH_FILE,{})
    tab1=st.tabs(["Login"])
    with tab1[0]:
        phone=st.text_input("Phone")
        pw=st.text_input("Password")
        if st.button("Login"):
            if phone in users:
                if users[phone]["pw"]==hash_pw(pw):
                    st.session_state.user_phone=phone
                    st.session_state.user_name=users[phone]["name"]
                    st.rerun()
        name=st.text_input("Business Name")
        phone2=st.text_input("New Phone")
        pw2=st.text_input("New Password")
        if st.button("Register N5000"):
            users[phone2]={"name":name,"pw":hash_pw(pw2),"date":str(datetime.now())}
            save_json(AUTH_FILE,users)
            w=load_json(WALLET_FILE,{})
            w[phone2]=5000
            save_json(WALLET_FILE,w)
            st.success("Registered now login")
    st.stop()

st.title("ROW ECONOMY SUPER")
balance=load_json(WALLET_FILE,{}).get(st.session_state.user_phone,0)
st.write("Hi")
st.write(balance)

if st.button("Logout"):
    del st.session_state.user_phone
    st.rerun()

state=st.selectbox("State",["FCT Abuja","Lagos","Kano","Rivers"])
area=st.text_input("Area","Wuse 2")

tabs=st.tabs(["Home","MAP","SECURITY","SOS","CHAT","Wallet"])

with tabs[0]:
    st.write("Home " + area)
    st.link_button("Maps", "https://www.google.com/maps")

with tabs[1]:
    st.title("SNAP MAP")
    data=[]
    for i in range(20):
        data.append({"lat":9.0667+random.uniform(-0.02,0.02),"lon":7.4833+random.uniform(-0.02,0.02)})
    df=pd.DataFrame(data)
    st.map(df)

with tabs[2]:
    st.title("NANS SECURITY MAP")
    locs=[{"lat":9.0765,"lon":7.4851,"name":"NANS"},{"lat":9.0579,"lon":7.4951,"name":"Police"},{"lat":9.0667,"lon":7.4833,"name":"Market"}]
    df=pd.DataFrame(locs)
    st.map(df)

with tabs[3]:
    st.title("SOS")
    if st.button("SEND SOS"):
        st.error("SOS SENT")

with tabs[4]:
    st.title("NAIJA CHAT")
    chats=load_json(CHAT_FILE,[])
    for c in chats[-10:]:
        st.write(c["name"] + " " + c["msg"])
    msg=st.text_input("Message")
    if st.button("Send"):
        chats.append({"name":st.session_state.user_phone,"msg":msg})
        save_json(CHAT_FILE,chats)
        st.rerun()

with tabs[5]:
    st.title("WALLET")
    st.write(balance)
    qr="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data="+st.session_state.user_phone
    st.image(qr)
    if st.button("Topup 5000"):
        w=load_json(WALLET_FILE,{})
        w[st.session_state.user_phone]=w.get(st.session_state.user_phone,0)+5000
        save_json(WALLET_FILE,w)
        st.rerun()
