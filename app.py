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
if "cat" not in st.session_state:
    st.session_state.cat="All"

users=load("users.json")
goods=load("goods.json")
notes=load("notes.json")

st.markdown("""
<style>
.stApp{background:#f7f7f7}
.block-container{padding-top:0px;padding-bottom:80px}
.header{background:#00A651;padding:18px 12px 28px 12px;
border-radius:0px 0px 25px 25px;
display:flex;justify-content:space-between;
align-items:center}
.header h1{color:white;margin:0px;font-size:28px}
.menu{color:white;font-size:28px}
.avatar{background:#FF7A00;width:45px;height:45px;
border-radius:50%;text-align:center;
font-size:28px}
.search{background:white;border-radius:25px;
padding:10px 14px;margin:-18px 10px 0px 10px;
box-shadow:0px 2px 8px #ddd;font-size:14px}
.title{font-size:22px;font-weight:800}
.green{color:#00A651;font-size:14px}
.catbox{border-radius:15px;padding:14px 5px;
text-align:center;font-size:28px}
.catlabel{text-align:center;font-size:13px;margin:4px 0px 12px 0px}
.card{background:white;border-radius:15px;
padding:14px;box-shadow:0px 2px 8px #ddd}
.verified{background:#00A651;color:white;
padding:4px 8px;border-radius:20px;font-size:11px}
.wabtn{background:#00A651;color:white;
text-align:center;padding:12px;border-radius:12px;
font-weight:bold;display:block;text-decoration:none}
.mama{background:#D6FFD6;border-radius:15px;
padding:10px;font-size:13px}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
<div class="menu">☰</div>
<h1>K&K Market</h1>
<div class="avatar">👤</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="search">🔍 &nbsp; Ask Mama Oloja - What are you looking for today? &nbsp; 🎤</div>', unsafe_allow_html=True)
q=st.text_input("Search here", label_visibility="collapsed")
if q:
    qq=q.lower()
    if "car" in qq:
        st.success("Found: Horlance Car AC")
    elif "rice" in qq:
        st.success("Found: Mama T Rice N45000")
    else:
        st.info("Mama dey find: "+q)

if st.session_state.user is None:
    st.markdown("### Login to Sell - FREE")
    t1, t2 = st.tabs(["Login", "Create Account"])
    with t1:
        lu=st.text_input("Username Login")
        lp=st.text_input("Password Login", type="password")
        if st.button("LOGIN"):
            found=None
            for u in users:
                if u["u"]==lu and u["p"]==hash_pw(lp):
                    found=u
            if found:
                st.session_state.user=found
                st.rerun()
            else:
                st.error("Wrong username or password")
    with t2:
        nu=st.text_input("New Username")
        npw=st.text_input("New Password", type="password")
        nwa=st.text_input("Your WhatsApp Number")
        if st.button("CREATE ACCOUNT FREE"):
            exists=False
            for u in users:
                if u["u"]==nu:
                    exists=True
            if nu=="" or npw=="" or nwa=="":
                st.warning("Fill all")
            elif exists:
                st.error("Username taken")
            else:
                users.append({"u":nu,
                "p":hash_pw(npw),
                "wa":to_wa(nwa)})
                save("users.json", users)
                st.success("Created! Now Login")
else:
    st.success("Logged in: "+st.session_state.user["u"])
    if st.button("Logout"):
        st.session_state.user=None
        st.rerun()
    for nt in notes:
        if nt["to"]==st.session_state.user["u"]:
            st.warning(nt["msg"])
    if st.button("Clear My Notifications"):
        new=[]
        for nt in notes:
            if nt["to"]!=st.session_state.user["u"]:
                new.append(nt)
        save("notes.json", new)
        st.rerun()

st.markdown('<div style="display:flex;justify-content:space-between"><span class="title">Categories</span><span class="green">See all ></span></div>', unsafe_allow_html=True)
def cat_btn(emoji, label, color):
    st.markdown('<div class="catbox" style="background:'+color+'">'+emoji+'</div>', unsafe_allow_html=True)
    if st.button(label, key="c"+label):
        st.session_state.cat=label
        st.session_state.page="Shop"
        st.rerun()
    st.markdown('<div class="catlabel">'+label+'</div>', unsafe_allow_html=True)

a1,a2,a3,a4=st.columns(4)
with a1: cat_btn("🧴","Perfume","#FFD6E8")
with a2: cat_btn("👕","Clothes","#CDE7FF")
with a3: cat_btn("📱","Phones","#CDE7FF")
with a4: cat_btn("🍲","Food","#FFE0B8")
b1,b2,b3,b4=st.columns(4)
with b1: cat_btn("🚗","Car Mart","#FFE0B8")
with b2: cat_btn("💼","Services","#C8FFC8")
with b3: cat_btn("🎟️","Tickets","#FFC8C8")
with b4: cat_btn("💬","Chat Rooms","#B8F0E8")
if st.session_state.cat!="All":
    st.success("Showing: "+st.session_state.cat)

st.markdown('<div style="display:flex;justify-content:space-between"><span class="title">Featured Listing</span><span class="green">See all ></span></div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
<div style="display:flex;justify-content:space-between">
<b>Horlance Auto Cooling Ltd</b>
<span class="verified">✅ VERIFIED</span>
</div>
<p>🔧 Car AC Repair</p>
<p>📍 Osun & Oyo State</p>
<p>🟢 WhatsApp 09046044472</p>
</div>
""", unsafe_allow_html=True)
st.link_button("💬 Chat on WhatsApp", wa_link("2349046044472"))
if st.button("Send Request to Horlance"):
    if st.session_state.user is None:
        st.warning("Login first")
    else:
        notes.append({"to":"Horlance",
        "msg":"Buyer wants Horlance Car AC"})
        save("notes.json", notes)
        st.success("Request sent!")

st.markdown("### New Goods From Sellers")
for idx, g in enumerate(goods):
    st.markdown('<div class="card"><b>'+g["txt"]+'</b><br>Seller: '+g["seller"]+'</div>', unsafe_allow_html=True)
    st.link_button("💬 Chat on WhatsApp", wa_link(g["wa"]), key="w"+str(idx))
    if st.button("Send Request", key="r"+str(idx)):
        if st.session_state.user is None:
            st.warning("Login first")
        else:
            notes.append({"to":g["seller"],
            "msg":"Buyer "+st.session_state.user["u"]+" wants: "+g["txt"]})
            save("notes.json", notes)
            st.success("Request sent!")

st.markdown("""
<div style="display:flex;gap:8px;align-items:center">
<div style="font-size:35px">🧕</div>
<div class="mama">Welcome my dear, I can help you find the best price in the market. 🕒 now</div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📦 Sell - FREE")
if st.session_state.user is None:
    st.info("Login to Sell FREE")
else:
    pd=st.text_input("Product Name")
    pr=st.text_input("Price")
    pay=st.selectbox("Payment", ["Pay on Delivery", "Transfer Before"])
    dlv=st.selectbox("Delivery", ["Pickup Only", "Delivery Available"])
    if st.button("POST MY GOODS FOR FREE"):
        if pd=="":
            st.warning("Fill Product Name")
        else:
            txt=pd+" - N"+pr+" - "+pay+" - "+dlv
            goods.append({"txt":txt,
            "seller":st.session_state.user["u"],
            "wa":st.session_state.user["wa"]})
            save("goods.json", goods)
            st.success("Posted! "+txt)
            st.balloons()

st.markdown("---")
n1,n2,n3,n4=st.columns(4)
with n1:
    if st.button("🏠 Home"):
        st.session_state.page="Home"
        st.rerun()
with n2:
    if st.button("🛍️ Shop"):
        st.session_state.page="Shop"
        st.rerun()
with n3:
    if st.button("📋 Orders"):
        st.session_state.page="Orders"
        st.rerun()
with n4:
    if st.button("👤 Profile"):
        st.session_state.page="Profile"
        st.rerun()
if st.session_state.page=="Orders":
    st.markdown("### Orders")
    st.info("Your buyer requests appear here after login")
if st.session_state.page=="Profile":
    st.markdown("### Profile")
    if st.session_state.user:
        st.write("Username: "+st.session_state.user["u"])
        st.write("WhatsApp: "+st.session_state.user["wa"])
    else:
        st.info("Login to see profile")
