import streamlit as st
import json, hashlib, random, pandas as pd

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="centered")

def load(f,d):
    try: return json.loads(open(f).read())
    except: return d
def save(f,data):
    open(f,"w").write(json.dumps(data))
def hp(p):
    return hashlib.sha256(p.encode()).hexdigest()

users=load("users.json",{})
users["08116911722"]={"name":"CEO","pw":hp("Kilani247")}
save("users.json",users)

wallets=load("wallets.json",{})
if wallets.get("08116911722",0)<1000:
    wallets["08116911722"]=500000
    save("wallets.json",wallets)

if "user" not in st.session_state:
    st.title("ROW ECONOMY SUPER")
    st.info("Login: 08116911722 / Kilani247")
    phone=st.text_input("Phone")
    pw=st.text_input("Password", type="password")
    if st.button("Login"):
        u=load("users.json",{})
        if phone in u and u[phone]["pw"]==hp(pw):
            st.session_state.user=phone
            st.rerun()
        else:
            st.error("Wrong")
    st.stop()

bal=load("wallets.json",{}).get(st.session_state.user,0)
st.title("ROW ECONOMY SUPER")
st.caption("Hi "+st.session_state.user+" | Bal N"+str(bal))

c1,c2,c3,c4,c5,c6=st.tabs(["Home","SNAP MAP","SECURITY","SOS","CHAT","Wallet"])

with c1:
    st.subheader("Food Calculator")
    people=st.number_input("People",1,500,10)
    st.metric("Total","N"+str(people*1000))
    st.link_button("Order WA","https://wa.me/2348116911722")

with c2:
    st.title("SNAP MAP")
    lat=[9.06+random.uniform(-0.03,0.03) for _ in range(30)]
    lon=[7.48+random.uniform(-0.03,0.03) for _ in range(30)]
    st.map(pd.DataFrame({"lat":lat,"lon":lon}))

with c3:
    st.title("NANS SECURITY MAP")
    st.map(pd.DataFrame({"lat":[9.0765,9.0579,6.5244],"lon":[7.4851,7.4951,3.3792]}))
    st.write("NANS HQ Abuja | Police HQ | Zone 2 Lagos")

with c4:
    st.title("SOS")
    if st.button("SEND SOS"):
        st.error("SOS SENT to Police!")
        st.balloons()
    st.link_button("Call 112","tel:112")

with c5:
    st.title("NAIJA CHAT")
    chats=load("global_chat.json",[])
    for c in chats[-20:]:
        st.write(c["name"]+": "+c["msg"])
    m=st.text_input("Message")
    if st.button("Send"):
        chats.append({"name":st.session_state.user,"msg":m})
        save("global_chat.json",chats)
        st.rerun()

with c6:
    st.title("Wallet N"+str(bal))
    st.image("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data="+st.session_state.user)
    if st.button("Logout"):
        del st.session_state.user
        st.rerun()
