import streamlit as st
import urllib.parse as u
import requests, json
st.set_page_config(page_title="Row Economy", layout="wide")
BUCKET="SzHmbyQQ1X1ns5LY4Qi8u9"
KV="https://kvdb.io/"+BUCKET+"/goods"
DEFAULT=[]
DEFAULT.append("Horlance Auto Cooling Ltd|Car AC Repair|25000|Osun & Oyo State|09046044472|Car Mart|YES")
DEFAULT.append("Mama T|Bag of Rice|45000|Abuja|09046044472|Food|YES")
def load_goods():
    try:
        r=requests.get(KV, timeout=5)
        if r.status_code==200 and len(r.text)>2:
            d=json.loads(r.text)
            if isinstance(d, list) and len(d)>0:
                return d
    except:
        pass
    return DEFAULT.copy()
def save_goods(data):
    try:
        requests.post(KV, data=json.dumps(data), timeout=5)
    except:
        pass
if "g" not in st.session_state:
    st.session_state.g=load_goods()
if "orders" not in st.session_state:
    st.session_state.orders=[]
page=st.query_params.get("page","Home")
cat_now=st.query_params.get("cat","All")
# HEADER - built in small pieces
h1="<div style='background:#00A651;"
h1+="padding:16px 14px 28px;"
h1+="border-radius:0 0 28px 28px;color:white;"
h1+="display:flex;justify-content:space-between;"
h1+="align-items:center'>"
h1+="<span>☰</span>"
h1+="<b style='font-size:25px'>ROW ECONOMY</b>"
h1+="<span style='background:#FF8A00;width:40px;"
h1+="height:40px;border-radius:50%;"
h1+="display:flex;align-items:center;"
h1+="justify-content:center'>👤</span></div>"
st.markdown(h1, unsafe_allow_html=True)
t1="<p style='text-align:center;color:#00A651;"
t1+="font-weight:bold'>Nigeria Sweetest Market - "
t1+=page+" - SAVED FOREVER</p>"
st.markdown(t1, unsafe_allow_html=True)
def show_card(line):
    p=line.split("|")
    seller=p[0]
    name=p[1]
    price=p[2]
    loc=p[3]
    wa=p[4]
    msg=u.quote("Hello "+seller+", I want "+name+" for N"+price)
    link="https://wa.me/234"+wa[1:]+"?text="+msg
    img="https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=400"
    if "AC" not in name:
        img="https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400"
    c1="<div style='background:white;margin:0 14px 16px;"
    c1+="padding:16px;border-radius:20px;"
    c1+="box-shadow:0 4px 16px #EDEDED'>"
    c1+="<div style='text-align:right'>"
    c1+="<span style='background:#00A651;color:white;"
    c1+="padding:5px 12px;border-radius:20px;"
    c1+="font-size:12px'>VERIFIED</span></div>"
    c1+="<div style='display:flex;gap:12px'>"
    c1+="<div style='flex:1'><b>"+seller+"</b>"
    c1+="<p>Product: "+name+" - <b style='color:#00A651'>N"+price+"</b></p>"
    c1+="<p>Location: "+loc+"</p>"
    c1+="<p>WhatsApp: "+wa+"</p></div>"
    c1+="<img src='"+img+"' style='width:140px;"
    c1+="height:130px;object-fit:cover;"
    c1+="border-radius:14px'></div>"
    c1+="<a href='"+link+"' style='display:block;"
    c1+="background:#00A651;color:white;text-align:center;"
    c1+="padding:12px;border-radius:14px;"
    c1+="text-decoration:none;font-weight:bold;"
    c1+="margin-top:12px'>Chat on WhatsApp</a></div>"
    st.markdown(c1, unsafe_allow_html=True)
if page=="Shop":
    st.markdown("<div style='padding:10px 14px'><b>Shop - All Goods</b></div>", unsafe_allow_html=True)
    s2=st.text_input("Search Shop", placeholder="Search shop - Rice, AC...", label_visibility="collapsed")
    for line in st.session_state.g:
        if s2=="" or s2.lower() in line.lower():
            show_card(line)
elif page=="Orders":
    st.markdown("<div style='padding:10px 14px'><b>My Orders</b></div>", unsafe_allow_html=True)
    st.info("Orders are tracked on WhatsApp with seller.")
    if len(st.session_state.orders)==0:
        st.write("No orders yet. Go to Shop and order.")
    for o in st.session_state.orders:
        st.success(o)
    if st.button("I Made An Order"):
        st.session_state.orders.append("Order - Chat on WhatsApp")
        st.rerun()
elif page=="Profile":
    st.markdown("<div style='padding:10px 14px'><b>My Profile</b></div>", unsafe_allow_html=True)
    pname=st.text_input("Your Name", value="Text seller")
    pwa=st.text_input("Your WhatsApp", value="09046044472")
    ploc=st.selectbox("Your Location", ["Abuja","Osun & Oyo State","Ogbomoso","Ilorin","Lagos"])
    if st.button("Save My Profile"):
        st.success("Saved! "+pname+" - "+ploc)
    st.write("My Listings:")
    for line in st.session_state.g:
        if pname.lower() in line.lower():
            show_card(line)
else:
    search=st.text_input("S", placeholder="Ask Mama Oloja - What are you looking for?", label_visibility="collapsed")
    st.markdown("<div style='display:flex;justify-content:space-between;padding:10px 14px'><b>Categories</b><a href='?page=Shop' style='color:#00A651;text-decoration:none'>See all ></a></div>", unsafe_allow_html=True)
    # CATEGORIES GRID - small pieces
    g="<div style='display:grid;"
    g+="grid-template-columns:1fr 1fr 1fr 1fr;"
    g+="gap:10px;padding:0 14px'>"
    cats=[("Perfume","🧴","#FFE4F1"),("Clothes","👕","#D6EAF8"),("Phones","📱","#D6EAF8"),("Food","🍲","#FFE8CC")]
    for nm, em, bg in cats:
        g+="<a href='?cat="+nm+"&page=Home' style='text-decoration:none'>"
        g+="<div style='background:"+bg+";border-radius:16px;"
        g+="padding:14px;text-align:center;font-size:28px'>"+em+"</div>"
        g+="<p style='text-align:center;color:#111;font-size:13px'>"+nm+"</p></a>"
    g+="</div>"
    st.markdown(g, unsafe_allow_html=True)
    g2="<div style='display:grid;"
    g2+="grid-template-columns:1fr 1fr 1fr 1fr;"
    g2+="gap:10px;padding:10px 14px'>"
    cats2=[("Car Mart","🚗","#FFE8CC"),("Services","💼","#D5F5E3"),("Tickets","🎟️","#FADBD8"),("Chat Rooms","💬","#D5F5E3")]
    for nm, em, bg in cats2:
        g2+="<a href='?cat="+nm+"&page=Home' style='text-decoration:none'>"
        g2+="<div style='background:"+bg+";border-radius:16px;"
        g2+="padding:14px;text-align:center;font-size:28px'>"+em+"</div>"
        g2+="<p style='text-align:center;color:#111;font-size:13px'>"+nm+"</p></a>"
    g2+="</div>"
    st.markdown(g2, unsafe_allow_html=True)
    st.markdown("<div style='display:flex;justify-content:space-between;padding:8px 14px'><b>Featured Listing - Showing: "+cat_now+"</b></div>", unsafe_allow_html=True)
    shown=[]
    for line in st.session_state.g:
        p=line.split("|")
        ok_cat=(cat_now=="All" or p[5]==cat_now)
        ok_s=(search=="" or search.lower() in line.lower())
        if ok_cat and ok_s:
            shown.append(line)
    if len(shown)==0:
        st.info("No goods in "+cat_now+" yet. Be first to post!")
    for line in shown:
        show_card(line)
    m1="<div style='display:flex;gap:8px;padding:0 14px'>"
    m1+="<div style='text-align:center'><div style='font-size:36px'>👩🏾</div>"
    m1+="<span style='background:#00A651;color:white;font-size:10px;"
    m1+="padding:3px 7px;border-radius:10px'>Mama Oloja AI</span></div>"
    m1+="<div style='background:#D5F5E3;border-radius:18px;"
    m1+="padding:12px;flex:1'>Welcome my dear, I can help you find the best price.</div></div>"
    st.markdown(m1, unsafe_allow_html=True)
    q=st.text_input("Ask Mama", placeholder="Ask Mama Oloja... e.g. Rice, AC", label_visibility="collapsed")
    if q:
        found=[l for l in st.session_state.g if q.lower() in l.lower()]
        if len(found)>0:
            f=found[0].split("|")
            st.success("Mama: Yes! "+f[1]+" is N"+f[2]+" from "+f[0]+" in "+f[3])
        else:
            st.warning("Mama: Sorry, no "+q+" yet. Post it!")
    st.markdown("<div style='padding:16px'><b>Sell - FREE for First 10</b></div>", unsafe_allow_html=True)
    with st.form("f"):
        n1=st.text_input("1. Your Name")
        n2=st.text_input("2. WhatsApp")
        n3=st.selectbox("3. Location", ["Abuja","Osun & Oyo State","Ogbomoso","Ilorin","Lagos"])
        n4=st.selectbox("Category", ["Food","Phones","Clothes","Perfume","Car Mart","Services","Tickets","Chat Rooms"])
        n5=st.text_input("5. Product Name")
        n6=st.text_input("5. Price - e.g. 25000")
        pic=st.file_uploader("4. Upload Picture", type=["jpg","png"])
        if pic:
            st.image(pic)
        go=st.form_submit_button("POST MY GOODS FOR FREE")
        if go:
            if n1=="" or n2=="":
                st.error("Fill Name and WhatsApp")
            elif n5=="":
                st.error("Fill Product Name")
            else:
                new=n1+"|"+n5+"|"+n6+"|"+n3+"|"+n2+"|"+n4+"|NO"
                st.session_state.g.append(new)
                save_goods(st.session_state.g)
                st.success("Done! LIVE and SAVED FOREVER!")
                st.balloons()
                st.rerun()
# BOTTOM NAV - small pieces
b1="<div style='background:white;display:flex;"
b1+="justify-content:space-around;padding:12px;"
b1+="border-top:1px solid #eee;position:sticky;bottom:0'>"
b1+="<a href='?page=Home' style='text-decoration:none;color:#00A651;font-weight:bold'>🏠 Home</a>"
b1+="<a href='?page=Shop' style='text-decoration:none;color:#111'>🛍️ Shop</a>"
b1+="<a href='?page=Orders' style='text-decoration:none;color:#111'>📦 Orders</a>"
b1+="<a href='?page=Profile' style='text-decoration:none;color:#111'>👤 Profile</a></div>"
st.markdown(b1, unsafe_allow_html=True)
