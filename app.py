import streamlit as st
import json, hashlib, random, pandas as pd
from datetime import datetime
st.set_page_config(page_title="ROW ECONOMY SUPER", layout="centered", page_icon="🛒")
def load(f,d):
    try: return json.loads(open(f).read())
    except: return d
def save(f,data):
    open(f,"w").write(json.dumps(data))
def hp(p):
    return hashlib.sha256(p.encode()).hexdigest()
users=load("users.json",{})
users["08116911722"]={"name":"CEO Kilani","pw":hp("Kilani247")}
save("users.json",users)
wallets=load("wallets.json",{})
if wallets.get("08116911722",0)<1000:
    wallets["08116911722"]=500000
    save("wallets.json",wallets)
if "user" not in st.session_state:
    st.title("ROW ECONOMY SUPER")
    st.success("Login: 08116911722 / Kilani247")
    phone=st.text_input("Phone","08116911722")
    pw=st.text_input("Password","Kilani247",type="password")
    if st.button("Login",use_container_width=True):
        users=load("users.json",{})
        if phone in users and users[phone]["pw"]==hp(pw):
            st.session_state.user=phone
            st.rerun()
        else:
            st.error("Wrong")
    st.stop()
bal=load("wallets.json",{}).get(st.session_state.user,0)
is_admin=st.session_state.user=="08116911722"
st.title("ROW ECONOMY SUPER")
st.caption(f"Hi {st.session_state.user} | Bal N{bal}")
tabs=st.tabs(["Home","SNAP MAP","SECURITY","SOS","NAIJA CHAT","Advertise","Wallet","Profile","Admin"])
with tabs[0]:
    st.subheader("Food Calculator")
    people=st.number_input("People",1,500,10)
    st.metric("Total",f"N{people*1000}")
    st.link_button("Order WhatsApp",f"https://wa.me/2348116911722?text=Order {people} people")
with tabs[1]:
    st.title("🔥 SNAP HEAT MAP")
    data=[{"lat":9.0667+random.uniform(-0.03,0.03),"lon":7.4833+random.uniform(-0.03,0.03)} for _ in range(40)]
    st.map(pd.DataFrame(data))
with tabs[2]:
    st.title("NANS + SECURITY MAP")
    locs=[{"lat":9.0765,"lon":7.4851,"name":"NANS HQ"},{"
