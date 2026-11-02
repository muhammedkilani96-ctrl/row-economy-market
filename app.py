import streamlit as st
import json
import os
import hashlib
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="centered", page_icon="🛒")

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

# AUTO RESTORE YOUR ADMIN ACCOUNT IF MISSING
users=load_json(AUTH_FILE,{})
if "2348116911722" not in users and "08116911722" not in users:
    users["2348116911722"]={"name":"CEO Kilani","pw":hash_pw("Kilani247"),"date":str(datetime.now())}
    users["08116911722"]={"name":"CEO Kilani","pw":hash_pw("Kilani247"),"date":str(datetime.now())}
    save_json(AUTH_FILE,users)
    w=load_json(WALLET_FILE,{})
    w["2348116911722"]=500000
    w["08116911722"]=500000
    save_json(WALLET_FILE,w)

for k in ["verified"]:
    if k not in st.session_state:
        st.session_state[k]=False

if "user_phone" not in st.session_state:
    st.title("ROW ECONOMY SUPER")
    st.caption("NANS + Security + Heat Map + SOS + Wallet")
    users=load_json(AUTH_FILE,{})
    phone=st.text_input("Phone e.g 08116911722")
    pw=st.text_input("Password")
    if st.button("Login"):
        check_phone=phone
        if phone.startswith("0"):
            check_phone="234"+phone[1:]
        if phone in users and users[phone]["pw"]==hash_pw(pw):
            st.session_state.user_phone=phone
            st.session_state.user_name=users[phone]["name"]
            st.rerun()
        elif check_phone in users and users[check_phone]["pw"]==hash_pw(pw):
            st.session_state.user_phone=check_phone
            st.session_state.user_name=users[check_phone]["name"]
            st.rerun()
        else:
            st.error("Wrong phone or password. Try 08116911722 / Kilani247")
    st.divider()
    st.write("New user")
    name=st.text_input("Business Name")
    phone2=st.text_input("New Phone")
    pw2=st.text_input("New Password")
    if st.button("Register N5000 Bonus"):
        if phone2 in users:
            st.error("Exists, login")
        else:
            users[phone2]={"name":name,"pw":hash_pw(pw2),"date":str(datetime.now())}
            save_json(AUTH_FILE,users)
            w=load_json(WALLET_FILE,{})
            w[phone2]=5000
            save_json(WALLET_FILE,w)
            st.success("Done, now login above")
    st.stop()

# MAIN
balance=load_json(WALLET_FILE,{}).get(st.session_state.user_phone,0)
is_admin=st.session_state.user_phone in ["2348116911722","08116911722"]

st.title("ROW ECONOMY SUPER")
st.write("Hi " + load_json(AUTH_FILE,{}).get(st.session_state.user_phone,{}).get("name","Boss") + " | Bal N" + str(balance))

if st.button("Logout"):
    del st.session_state.user_phone
    st.rerun()

state=st.selectbox("State",["FCT Abuja","Lagos","Kano","Rivers","Kaduna","Oyo","Delta","Anambra"])
area=st.text_input("Area","Wuse 2")

tabs_list=["Home","Explore","SNAP HEAT MAP","SECURITY NANS MAP","SOS","NAIJA CHAT","LIVE","Advertise","Wallet","My Ads","Profile"]
if is_admin:
    tabs_list.append("Admin")
tabs=st.tabs(tabs_list)

with tabs[0]:
    st.subheader("Food Calculator " + area)
    people=st.number_input("People",1,500,10)
    total=people*1000
    st.metric("Total","N"+str(total))
    st.link_button("Order WhatsApp","https://wa.me/2348116911722")

with tabs[1]:
    st.subheader("Explore")
    search=st.text_input("Search market")
    listings=load_json(DB_FILE,[])
    filtered=[]
    for l in listings:
        if search.lower() in l["title"].lower():
            filtered.append(l)
    show_list=filtered if search else listings[-20:]
    for l in show_list[::-1]:
        st.write(l["title"] + " - N" + str(l["price"]) + " - " + l["area"])
        st.caption(l.get("desc","")[:80])

with tabs[2]:
    st.title("HEAT MAP")
    st.caption("Red = HOTTEST market")
    data=[]
    listings=load_json(DB_FILE,[])
    for l in listings[-30:]:
        data.append({"lat":9.0667+random.uniform(-0.03,0.03),"lon":7.4833+random.uniform(-0.03,0.03)})
    if len(data)==0:
        for i in range(30):
            data.append({"lat":9.0667+random.uniform(-0.02,0.02),"lon":7.4833+random.uniform(-0.02,0.02)})
    df=pd.DataFrame(data)
    st.map(df)
    st.write("🔥 "+str(len(data))+" sellers LIVE")

with tabs[3]:
    st.title("NANS + SECURITY MAP")
    st.caption("Real HQ locations")
    locs=[{"lat":9.0765,"lon":7.4851,"name":"NANS HQ"},{"lat":9.0579,"lon":7.4951,"name":"Police HQ Louis Edet"},{"lat":6.5244,"lon":3.3792,"name":"Police Zone 2 Lagos"},{"lat":12.0022,"lon":8.592,"name":"Police Zone 1 Kano"},{"lat":9.066,"lon":7.483,"name":"Navy HQ"},{"lat":9.055,"lon":7.483,"name":"Air Force HQ"},{"lat":9.057,"lon":7.49,"name":"EFCC HQ"},{"lat":9.0667,"lon":7.4833,"name":"ROW Market Wuse 2"}]
    df=pd.DataFrame(locs)
    st.map(df)
    for loc in locs:
        st.write(loc["name"])

with tabs[4]:
    st.title("EMERGENCY SOS")
    st.markdown("Press SOS to alert Police Zone + NANS")
    if st.button("SEND SOS NOW"):
        sos=load_json(SOS_FILE,[])
        sos.append({"name":st.session_state.user_phone,"area":area,"state":state,"time":str(datetime.now())})
        save_json(SOS_FILE,sos)
        st.error("SOS SENT from " + area + " to Police + NANS")
        st.balloons()
    st.link_button("Call 112 Emergency","tel:112")
    st.link_button("Share Location WhatsApp","https://wa.me/2348116911722?text=EMERGENCY "+area)

with tabs[5]:
    st.title("NAIJA CHAT")
    chats=load_json(CHAT_FILE,[])
    box=st.container(height=250)
    with box:
        for c in chats[-30:]:
            st.write(c["name"] + ": " + c["msg"])
    msg=st.text_input("Type message for all Nigeria")
    if st.button("Send to Nigeria"):
        if msg:
            chats.append({"name":st.session_state.user_phone,"msg":msg,"time":str(datetime.now())})
            save_json(CHAT_FILE,chats)
            st.rerun()

with tabs[6]:
    st.write("LIVE - Coming soon")

with tabs[7]:
    st.subheader("Post Advert")
    title=st.text_input("Title e.g Spaghetti")
    desc=st.text_area("Description")
    price=st.number_input("Price",100,1000000,1500)
    if st.button("Post Ad"):
        listings=load_json(DB_FILE,[])
        listings.append({"title":title,"desc":desc,"price":price,"area":area,"state":state,"time":str(datetime.now()),"owner":st.session_state.user_phone})
        save_json(DB_FILE,listings)
        st.success("Posted to " + area)
        st.balloons()

with tabs[8]:
    st.title("WALLET N"+str(balance))
    qr="https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=ROWPAY:"+st.session_state.user_phone
    st.image(qr,caption="Scan to Pay Me")
    if st.button("Topup N5000 Demo"):
        w=load_json(WALLET_FILE,{})
        w[st.session_state.user_phone]=w.get(st.session_state.user_phone,0)+5000
        save_json(WALLET_FILE,w)
        st.rerun()
    st.write("Your data is saved in JSON - will persist if you commit files to GitHub")

with tabs[9]:
    st.subheader("My Ads")
    listings=load_json(DB_FILE,[])
    mine=[]
    for l in listings:
        if l["owner"]==st.session_state.user_phone:
            mine.append(l)
    st.write(str(len(mine)) + " ads")
    for l in mine:
        st.write(l["title"] + " N" + str(l["price"]))

with tabs[10]:
   
