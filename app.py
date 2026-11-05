import streamlit as st
if "goods" not in st.session_state:
    st.session_state.goods=[]
if "page" not in st.session_state:
    st.session_state.page="Home"
if "cat" not in st.session_state:
    st.session_state.cat="All"

qp=st.query_params
if "page" in qp:
    st.session_state.page=qp["page"]
if "cat" in qp:
    st.session_state.cat=qp["cat"]
    st.session_state.page="Shop"

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
.pad{padding:0px 12px}
.title{font-size:22px;font-weight:800}
.green{color:#00A651;font-size:14px;font-weight:bold}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px}
.catbox{border-radius:15px;padding:14px 2px;text-align:center;font-size:28px}
.catlabel{text-align:center;font-size:12px;margin:4px 0px 12px 0px}
.card{background:white;border-radius:15px;padding:14px;
box-shadow:0px 2px 8px #ddd;margin:10px 12px}
.verified{background:#00A651;color:white;padding:4px 8px;border-radius:20px;font-size:11px}
.wabtn{background:#00A651;color:white !important;text-align:center;padding:13px;
border-radius:12px;font-weight:bold;display:block;text-decoration:none;margin:10px 12px}
.mama{background:#D6FFD6;border-radius:15px;padding:10px;font-size:13px}
.bottom{position:fixed;bottom:0px;left:0px;right:0px;background:white;
display:flex;justify-content:space-around;padding:10px 0px;
border-top:1px solid #ddd;z-index:999}
.bottom a{text-align:center;font-size:12px;text-decoration:none;color:#333}
.active{color:#00A651 !important;font-weight:bold}
.catlink{text-decoration:none;color:#333}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
<div class="menu">☰</div>
<h1>K&K Market</h1>
<div class="avatar">👤</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="pad">', unsafe_allow_html=True)
q=st.text_input("🔍 Ask
