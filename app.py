import streamlit as st
import json, os, hashlib, random, pandas as pd
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

# INIT
for k in ["ads_today","live_gifts","live_comments","verified"]:
    if k not in st.session_state:
        if k in ["ads_today","live_gifts"]:
            st.session_state[k]=0
        elif k=="live_comments":
            st.session_state[k]=[]
        else:
            st.session_state[k]=False

# LOGIN
if "user_phone" not in st.session_state:
    st.title("ROW ECONOMY SUPER")
    st.caption("NANS + Security + SNAP MAP + SOS + Wallet")
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
            else:
                st.error("Wrong")
    with t2:
        name=st.text_input("Business Name")
        phone2=st.text_input("Number")
        pw2=st.text_input("Create Password",type="password")
        if st.button("Register + N5000",use_container_width=True):
            if phone2 in users:
                st.error("Exists")
            else:
                users[phone2]={"name":name,"pw":hash_pw(pw2),"date":str(datetime.now()),"verified":False}
                save_json(AUTH_FILE,users)
                w=load_json(WALLET_FILE,{})
                w[phone2]=5000
                save_json(WALLET_FILE,w)
                st.success("Done! Now Login")
                st.balloons()
    st.stop()

# MAIN
STATES=["FCT Abuja","Lagos","Kano","Rivers","Kaduna","Oyo","Delta","Anambra","Enugu","Benue","Abia","Adamawa","Akwa Ibom","Bauchi","Bayelsa","Borno","Cross River","Ebonyi","Edo","Ekiti","Gombe","Imo","Jigawa","Katsina","Kebbi","Kogi","Kwara","Nasarawa","Niger","Ogun","Ondo","Osun","Plateau","Sokoto","Taraba","Yobe","Zamfara"]
is_admin=st.session_state.user_phone=="2348116911722"
balance=load_json(WALLET_FILE,{}).get(st.session_state.user_phone,0)

st.title("ROW ECONOMY SUPER")
st.caption(f"Hi {st.session_state.user_name} | Bal N{balance} | Gifts {st.session_state.live_gifts}")
if st.button("Logout"):
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.rerun()

state=st.selectbox("State",STATES,index=0)
area=st.text_input("Area / Town","Wuse 2")
st.markdown(f"<div style='background:#00FF7F;padding:8px;border-radius:8px;color:black;text-align:center;font-weight:bold'> {area}, {state} LIVE | QR + SOS Active</div>",unsafe_allow_html=True)
st.link_button(f"View {area} Maps",f"https://www.google.com/maps/search/{area}+{state}+Nigeria/",use_container_width=True)

tabs_list=["Home","Explore","SNAP MAP","SECURITY","SOS","NAIJA CHAT","LIVE","Advertise","Wallet","My Ads","Profile"] + (["Admin"] if is_admin else [])
tabs=st.tabs(tabs_list)

with tabs[0]:
    people=st.number_input("People",1,500,10)
    meal=st.selectbox("Meal",["Spaghetti","Rice","Indomie","Full"])
    prices={"Spaghetti":1000,"Rice":1500,"Indomie":350}
    spag=(people+3)//4
    rice=(people+4)//5
    if meal=="Spaghetti":
        needs={"Spaghetti":spag}
    elif meal=="Rice":
        needs={"Rice":rice}
    elif meal=="Indomie":
        needs={"Indomie":people}
    else:
        needs={"Rice":rice,"Spaghetti":spag}
    total=sum(prices[k]*v for k,v in needs.items())
    st.write(f"Total N{total}")
    c1,c2=st.columns(2)
    c1.link_button("WhatsApp",f"https://wa.me/2348116911722?text=Order {meal} N{total}",use_container_width=True)
    if c2.button(f"Pay Wallet N{total}",use_container_width=True):
        w=load_json(WALLET_FILE,{})
        if w.get(st.session_state.user_phone,0)>=total:
            w[st.session_state.user_phone]-=total
            save_json(WALLET_FILE,w)
            st.success("Paid!")
        else:
            st.error("Low wallet")

with tabs[1]:
    st.subheader(f"Explore {area}")
    search=st.text_input("Search")
    listings=load_json(DB_FILE,[])
    filt=[l for l in listings if search.lower() in l["title"].lower()] if search else listings[-20:]
    for l in filt[::-1]:
        st.write(f"{l['title']} - N{l['price']} - {l['area']}")
        st.caption(f"{l['desc'][:80]} | {l['owner']}")
        st.link_button("Chat",f"https://wa.me/{l['owner']}",key=f"chat{l['title']}{l['time']}")

with tabs[2]:
    st.title(f
