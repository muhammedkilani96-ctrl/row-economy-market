import streamlit as st
import database, explore_tab, advertise_tab, live_tab, chats_tab, profile_tab, wallet_tab, admin_tab, my_ads_tab
import map_tab, security_map_tab, emergency_tab, global_chat_tab
from datetime import date
import json, os, hashlib
from datetime import datetime

st.set_page_config(page_title="ROW ECONOMY SUPER - NIGERIA NATIONAL MAP", layout="centered", page_icon="🛒")

# AUTH SYSTEM
AUTH_FILE="users.json"
def hash_pw(p): return hashlib.sha256(p.encode()).hexdigest()
def get_users():
    if not os.path.exists(AUTH_FILE): return {}
    try: return json.loads(open(AUTH_FILE).read())
    except: return {}
def save_users(u): open(AUTH_FILE,"w").write(json.dumps(u))

# INIT SESSION
for k in ["ads_today","paid_unlock","live_gifts","live_comments","verified"]:
    if k not in st.session_state:
        if k in ["ads_today","live_gifts"]: st.session_state[k]=0
        elif k=="live_comments": st.session_state[k]=[]
        else: st.session_state[k]=False

if "ads_date" not in st.session_state:
    st.session_state.ads_date=str(date.today())

# LOGIN WITH N5000 BONUS
if "user_phone" not in st.session_state:
    st.title("🔐 ROW ECONOMY SUPER")
    st.caption("NANS + Security Map + SNAP MAP + SOS + Wallet + N5000 Bonus")
    users=get_users()
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
                st.error("Wrong phone/password")
    with t2:
        name=st.text_input("Business Name")
        phone=st.text_input("Number",key="rp")
        pw=st.text_input("Create Password",type="password",key="rpw")
        ref=st.text_input("Referral Code (optional)")
        if st.button("Register + Get N5000 Bonus",use_container_width=True):
            if phone in users:
                st.error("Exists, Login")
            else:
                users[phone]={"name":name,"pw":hash_pw(pw),"date":str(datetime.now()),"verified":False,"ref":ref}
                save_users(users)
                w=json.loads(open("wallets.json").read()) if os.path.exists("wallets.json") else {}
                w[phone]=5000
                open("wallets.json","w").write(json.dumps(w))
                st.success("Registered! N5000 added. Now Login")
                st.balloons()
    st.stop()

# MAIN APP
STATES=["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","FCT Abuja","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nasarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara"]

is_admin=st.session_state.user_phone=="2348116911722"

# BALANCE
try:
    wallets=json.loads(open("wallets.json").read())
    balance=wallets.get(st.session_state.user_phone,0)
except:
    balance=0

st.title("ROW ECONOMY 💰 SUPER")
st.caption(f"Hi {st.session_state.user_name} {'✅' if st.session_state.verified else ''} | Bal N{balance} | Gifts {st.session_state.live_gifts} | {st.session_state.user_phone}")

if st.button("Logout"):
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.rerun()

# LOCATION
state
