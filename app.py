import streamlit as st
import json
import os
import hashlib

def load(fn):
    if os.path.exists(fn):
        try:
            f=open(fn)
            d=json.load(f)
            f.close()
            return d
        except:
            return []
    return []

def save(fn, data):
    f=open(fn, "w")
    json.dump(data, f)
    f.close()

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def to_wa(num):
    n=""
    for c in num:
        if c.isdigit():
            n=n+c
    if len(n)==11:
        if n[0]=="0":
            n="234"+n[1:]
    if len(n)==10:
        n="234"+n
    return n

def wa_link(wa):
    return "https://wa.me/"+wa

if "user" not in st.session_state:
    st.session_state.user=None
if "page" not in st.session_state:
    st.session_state.page="Home"

users=load("users.json")
goods=load("goods.json")
notes=load("notes.json")

st.markdown("""
<style>
.main{background:#f5f5f5}
.top{background:#008000;padding:15px;
border-radius:10px;text-align:center}
.top h1{color:white;margin:0px}
.top p{color:#d6ffd6;margin:0px}
.card{background:white;padding:12px;
border-radius:10px;margin:8px 0px;
box-shadow:0px 2px 5px #ddd}
.price{color:#008000;font-weight:bold}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="top">
<h1>🛒 ROW ECONOMY</h1>
<p>Nigeria Sweetest Market - Buy & Sell FREE</p>
</div>
""", unsafe_allow_html=True)

if st.session_state.user is None:
    st.markdown("### Welcome - Login to Sell")
    t1, t2 = st.tabs(["Login", "Create Account"])
    with t1:
        lu=st.text_input("Username Login")
        lp=st.text_input("Password Login",
        type="password")
        if st.button("LOGIN"):
            found=None
            for u in users:
                if u["u"]==lu:
                    if u["p"]==hash_pw(lp):
                        found=u
            if found:
                st.session_state.user=found
                st.success("Welcome "+lu)
                st.rerun()
            else:
                st.error("Wrong username or password")
    with t2:
        nu=st.text_input("New Username")
        npw=st.text_input("New Password",
        type="password")
        nwa=st.text_input("Your WhatsApp Number")
        if st.button("CREATE ACCOUNT FREE"):
            exists=False
            for u in users:
                if u["u"]==nu:
                    exists=True
            if nu=="" or npw=="" or nwa=="":
                st.warning("Fill all")
            elif exists:
                st.error("Username taken, pick another")
            else:
                u2={"u":nu,
                "p":hash_pw(npw),
                "wa":to_wa(nwa)}
                users.append(u2)
                save("users.json", users)
                st.success("Account created! Now Login")
    st.markdown("---")
    st.markdown("### Market - You can still buy without login")
else:
    st.success("Logged in as: "+st.session_state.user["u"])
    if st.button("Logout"):
        st.session_state.user=None
        st.rerun()
    my_notes=[]
    for nt in notes:
        if nt["to"]==st.session_state.user["u"]:
            my_notes.append(nt)
    if len(my_notes)>0:
        st.warning("You have new buyer request!")
        for nt in my_notes:
            st.warning(nt["msg"])
        if st.button("Clear My Notifications"):
            new_notes=[]
            for nt in notes:
                if nt["to"]!=st.session_state.user["u"]:
                    new_notes.append(nt)
            save("notes.json", new_notes)
            st.rerun()

q=st.text_input("🔍 Search - Ask Mama Oloja")
if q:
    qq=q.lower()
    if "car" in qq:
        st.success("Found: Horlance Car AC")
    elif "rice" in qq:
        st.success("Found: Mama T Rice N45000")
    else:
        st.info("Mama dey find: "+q)

st.markdown("### Categories")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("🍚 Food"):
        st.session_state.page="Shop"
        st.rerun()
with c2:
    if st.button("👗 Clothes"):
        st.session_state.page="Shop"
        st.rerun()
with c3:
    if st.button("📱 Phones"):
        st.session_state.page="Shop"
        st.rerun()
with c4:
    if st.button("🚗 Car Mart"):
        st.session_state.page="Shop"
        st.rerun()

choice=st.selectbox("Tap Category",
["All","Perfume","Clothes","Phones",
"Food","Car Mart","Services",
"Tickets","Chat Rooms"])
if choice!="All":
    st.success("Showing: "+choice)

if st.session_state.page=="Profile":
    st.markdown("### My Profile")
    if st.session_state.user:
        st.write("Username: "+st.session_state.user["u"])
        st.write("WhatsApp: "+st.session_state.user["wa"])
        st.write("My goods:")
        for g in goods:
            if g["seller"]==st.session_state.user["u"]:
                st.markdown('<div class="card">'+g["txt"]+'</div>',
                unsafe_allow_html=True)
    else:
        st.info("Login to see profile")

elif st.session_state.page=="Orders":
    st.markdown("### Orders / Requests")
    if st.session_state.user:
        found=False
        for nt in notes:
            if nt["to"]==st.session_state.user["u"]:
                st.success(nt["msg"])
                found=True
        if not found:
            st.info("No orders yet")
    else:
        st.info("Login to see orders")

else:
    st.markdown("### 🔥 Featured - Fine Goods")
    st.markdown('<div class="card"><b>Horlance Auto Cooling</b><br>Car AC<br><span class="price">N25,000</span></div>',
    unsafe_allow_html=True)
    st.link_button("Chat Horlance",
    wa_link("2349046044472"))
    st.markdown('<div class="card"><b>Mama T Rice</b><br>Bag of Rice<br><span class="price">N45,000</span></div>',
    unsafe_allow_html=True)
    st.link_button("Chat Mama T",
    wa_link("2349046044472"))
    st.markdown("### New Goods From Sellers")
    for idx, g in enumerate(goods):
        st.markdown('<div class="card"><b>'+g["txt"]+'</b><br>Seller: '+g["seller"]+'</div>',
        unsafe_allow_html=True)
        st.link_button("I Want This - Chat Seller",
        wa_link(g["wa"]), key="h"+str(idx))
        if st.button("Send Request",
        key="hr"+str(idx)):
            if st.session_state.user is None:
                st.warning("Login first to send request")
            else:
                notes.append({"to":g["seller"],
                "msg":"Buyer "+st.session_state.user["u"]+" wants: "+g["txt"]})
                save("notes.json", notes)
                st.success("Request sent to seller!")
                st.rerun()

st.markdown("### 📦 Sell - FREE")
if st.session_state.user is None:
    st.info("Login or Create Account to Sell FREE")
else:
    pd=st.text_input("Product Name")
    pr=st.text_input("Price")
    pay=st.selectbox("Payment",
    ["Pay on Delivery", "Transfer Before"])
    dlv=st.selectbox("Delivery",
    ["Pickup Only", "Delivery Available"])
    if st.button("POST MY GOODS FOR FREE"):
        if pd=="":
            st.warning("Fill Product Name")
        else:
            txt=pd+" - N"+pr+" - "+pay+" - "+dlv
            g2={"txt":txt,
            "seller":st.session_state.user["u"],
            "wa":st.session_state.user["wa"]}
            goods.append(g2)
            save("goods.json", goods)
            st.success("Posted! "+txt)
            st.balloons()

st.markdown("### Menu")
n1, n2, n3, n4 = st.columns(4)
with n1:
    if st.button("🏠 Home"):
        st.session_state.page="Home"
        st.rerun()
with n2:
    if st.button("🛍️ Shop"):
        st.session_state.page="Shop"
        st.rerun()
with n3:
    if st.button("📦 Orders"):
        st.session_state.page="Orders"
        st.rerun()
with n4:
    if st.button("👤 Profile"):
        st.session_state.page="Profile"
        st.rerun()
