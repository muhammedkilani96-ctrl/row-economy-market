import streamlit as st
import database, explore_tab, advertise_tab, live_tab, chats_tab, profile_tab
from datetime import date
import json, os, hashlib
from datetime import datetime

st.set_page_config(page_title="Row Economy Market Wuse 2 LIVE", layout="centered", page_icon="🛒")

# --- SECURITY: USERS DB ---
AUTH_FILE="users.json"
def hash_pw(p): return hashlib.sha256(p.encode()).hexdigest()
def get_users():
    if not os.path.exists(AUTH_FILE): return {}
    try: return json.loads(open(AUTH_FILE).read())
    except: return {}
def save_users(u): open(AUTH_FILE,"w").write(json.dumps(u))

if "ads_today" not in st.session_state: st.session_state.ads_today = 0
if "ads_date" not in st.session_state: st.session_state.ads_date = str(date.today())
if "paid_unlock" not in st.session_state: st.session_state.paid_unlock = 0
if "live_gifts" not in st.session_state: st.session_state.live_gifts = 0
if "live_comments" not in st.session_state: st.session_state.live_comments = []

# --- LOGIN GATE ---
if "user_phone" not in st.session_state:
    st.title("🔐 ROW ECONOMY LOGIN")
    st.caption("Secure login with your WhatsApp number")
    users=get_users()
    t1,t2=st.tabs(["Login","Register"])
    with t1:
        phone=st.text_input("WhatsApp e.g 2348116911722", key="lp")
        pw=st.text_input("Password", type="password", key="lpw")
        if st.button("Login", use_container_width=True):
            if phone in users and users[phone]["pw"]==hash_pw(pw):
                st.session_state.user_phone=phone
                st.session_state.user_name=users[phone]["name"]
                st.success("Welcome!"); st.rerun()
            else: st.error("Wrong number/password")
    with t2:
        name=st.text_input("Business Name", key="rn")
        phone=st.text_input("WhatsApp Number", key="rp")
        pw=st.text_input("Create Password min 6", type="password", key="rpw")
        if st.button("Register", use_container_width=True):
            if len(pw)<6: st.error("Password too short")
            elif phone in users: st.error("Number exists, login")
            elif not phone or not name: st.error("Fill all")
            else:
                users[phone]={"name":name,"pw":hash_pw(pw),"date":str(datetime.now())}
                save_users(users)
                st.success("Registered! Login now"); st.balloons()
    st.stop()

STATES = ["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","FCT Abuja","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nasarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara"]

# --- HEADER ---
st.title("ROW ECONOMY MARKET Wuse 2 🔴 LIVE")
st.caption(f"Welcome {st.session_state.user_name} | {st.session_state.user_phone}")
st.write("WhatsApp: 08116911722 | Official: https://row-economy-market.streamlit.app")
if st.button("Logout"): 
    del st.session_state.user_phone; del st.session_state.user_name; st.rerun()

state = st.selectbox("State", STATES, index=14)
area = st.text_input("Area / Town", "Wuse 2")
st.markdown(f"""<div style="background:#00FF7F; padding:10px; border-radius:10px; color:black; font-weight:bold">📍 You dey for {area}, {state} - LIVE NOW</div>""", unsafe_allow_html=True)

# GOOGLE MAPS
maps_link = f"https://www.google.com/maps/search/{area}+{state}+Nigeria/"
st.link_button(f"🗺️ View {area} on Google Maps", maps_link, use_container_width=True)

tabs = st.tabs(["🏠 Home","🔍 Explore","🔴 LIVE","📢 Advertise","💬 Chats","👤 Profile"])

with tabs[0]:
    people = st.number_input("Number of people",1,500,10)
    meal = st.selectbox("Meal",["Spaghetti","Rice","Indomie","Full Package"])
    spag=(people+3)//4; rice=(people+4)//5
    prices={"Spaghetti":1000,"Rice":1500,"Indomie":350}
    if meal=="Spaghetti": needs={"Spaghetti":spag}
    elif meal=="Rice": needs={"Rice":rice}
    elif meal=="Indomie": needs={"Indomie":people}
    else: needs={"Rice":rice,"Spaghetti":spag}
    total=sum(prices[k]*v for k,v in needs.items())
    for k,v in needs.items(): st.metric(f"{k} x {v}", f"N{prices[k]*v}")
    st.write(f"### Total: N{total}")
    st.link_button(f"Order {area}", f"https://wa.me/2348116911722?text=Food {people} {meal} N{total} {area}", use_container_width=True)

with tabs[1]: explore_tab.show(area,state)
with tabs[2]: live_tab.show(area,state)
with tabs[3]: advertise_tab.show(area,state)
with tabs[4]: chats_tab.show(area,state)
with tabs[5]: profile_tab.show(area,state)

st.caption("Secured with hashed passwords | Each user has private account")
