import streamlit as st
if "goods" not in st.session_state:
    st.session_state.goods=[]

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

st.markdown("""
<style>
.stApp{background:#f7f7f7}
.block-container{padding-top:0px;padding-left:0px;padding-right:0px;padding-bottom:90px}
.header{background:#00A651;padding:18px 12px 30px 12px;
border-radius:0px 0px 25px 25px;
display:flex;justify-content:space-between;align-items:center}
.header h1{color:white;margin:0px;font-size:28px}
.menu{color:white;font-size:28px}
.avatar{background:#FF7A00;width:45px;height:45px;border-radius:50%;
display:flex;align-items:center;justify-content:center;font-size:28px}
.search{background:white;border-radius:25px;padding:12px 14px;
margin:-18px 12px 0px 12px;box-shadow:0px 2px 8px #ddd;font-size:14px}
.pad{padding:0px 12px}
.title{font-size:22px;font-weight:800}
.green{color:#00A651;font-size:14px;font-weight:bold}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px}
.catbox{border-radius:15px;padding:14px 2px;text-align:center;font-size:28px}
.catlabel{text-align:center;font-size:12px;margin:4px 0px 12px 0px}
.card{background:white;border-radius:15px;padding:14px;
box-shadow:0px 2px 8px #ddd;margin:0px 12px}
.verified{background:#00A651;color:white;padding:4px 8px;border-radius:20px;font-size:11px}
.wabtn{background:#00A651;color:white;text-align:center;padding:13px;
border-radius:12px;font-weight:bold;display:block;text-decoration:none;margin:10px 12px}
.mama{background:#D6FFD6;border-radius:15px;padding:10px;font-size:13px}
.bottom{position:fixed;bottom:0px;left:0px;right:0px;background:white;
display:flex;justify-content:space-around;padding:10px 0px;
border-top:1px solid #ddd;z-index:999}
.bottom div{text-align:center;font-size:12px}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
<div class="menu">☰</div>
<h1>K&K Market</h1>
<div class="avatar">👤</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="search">🔍 Ask Mama Oloja - What are you looking for today? 🎤</div>', unsafe_allow_html=True)

st.markdown('<div class="pad">', unsafe_allow_html=True)
q=st.text_input("Search", label_visibility="collapsed", placeholder="Type here to search...")
if q:
    qq=q.lower()
    if "car" in qq:
        st.success("Found: Horlance Car AC")
    elif "rice" in qq:
        st.success("Found: Mama T Rice N45000")
    else:
        st.info("Mama dey find: "+q)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="pad" style="display:flex;justify-content:space-between;margin-top:10px">
<span class="title">Categories</span><span class="green">See all ></span>
</div>
<div class="pad"><div class="grid">
<div><div class="catbox" style="background:#FFD6E8">🧴</div><div class="catlabel">Perfume</div></div>
<div><div class="catbox" style="background:#CDE7FF">👕</div><div class="catlabel">Clothes</div></div>
<div><div class="catbox" style="background:#CDE7FF">📱</div><div class="catlabel">Phones</div></div>
<div><div class="catbox" style="background:#FFE0B8">🍲</div><div class="catlabel">Food</div></div>
<div><div class="catbox" style="background:#FFE0B8">🚗</div><div class="catlabel">Car Mart</div></div>
<div><div class="catbox" style="background:#C8FFC8">💼</div><div class="catlabel">Services</div></div>
<div><div class="catbox" style="background:#FFC8C8">🎟️</div><div class="catlabel">Tickets</div></div>
<div><div class="catbox" style="background:#B8F0E8">💬</div><div class="catlabel">Chat Rooms</div></div>
</div></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="pad" style="display:flex;justify-content:space-between">
<span class="title">Featured Listing</span><span class="green">See all ></span>
</div>
<div class="card">
<div style="display:flex;justify-content:space-between">
<b>Horlance Auto Cooling Ltd</b>
<span class="verified">✅ VERIFIED</span>
</div>
<p>🔧 Car AC Repair</p>
<p>📍 Osun & Oyo State</p>
<p>🟢 WhatsApp 09046044472</p>
</div>
<a class="wabtn" href="https://wa.me/2349046044472">💬 Chat on WhatsApp</a>
""", unsafe_allow_html=True)

st.markdown('<div class="pad"><b>New Goods</b></div>', unsafe_allow_html=True)
for g in st.session_state.goods:
    st.markdown('<div class="card"><b>'+g[0]+'</b></div>', unsafe_allow_html=True)
    st.markdown('<a class="wabtn" href="https://wa.me/'+g[1]+'">💬 Chat on WhatsApp</a>', unsafe_allow_html=True)

st.markdown("""
<div class="pad" style="display:flex;gap:8px;align-items:center;margin-top:15px">
<div style="font-size:35px">🧕</div>
<div class="mama">Welcome my dear, I can help you find the best price in the market. 🕒 now</div>
</div>
<div class="pad"><h3>📦 Sell - FREE</h3></div>
""", unsafe_allow_html=True)

st.markdown('<div class="pad">', unsafe_allow_html=True)
nm=st.text_input("Your Name")
pd=st.text_input("Product Name")
pr=st.text_input("Price")
wa=st.text_input("Your WhatsApp Number")
if st.button("POST MY GOODS FOR FREE"):
    if nm=="" or pd=="" or wa=="":
        st.warning("Fill Name, Product, WhatsApp")
    else:
        txt=nm+" - "+pd+" - N"+pr
        st.session_state.goods.append((txt, to_wa(wa)))
        st.success("Posted! "+txt)
        st.balloons()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="bottom">
<div>🏠<br>Home</div>
<div>🛍️<br>Shop</div>
<div>📋<br>Orders</div>
<div>👤<br>Profile</div>
</div>
""", unsafe_allow_html=True)
