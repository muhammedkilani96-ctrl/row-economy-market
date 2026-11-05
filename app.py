import streamlit as st
import urllib.parse as u
import requests, json
st.set_page_config(page_title="Row Economy", layout="wide")
BUCKET="SzHmbyQQ1X1ns5LY4Qi8u9"
KV="https://kvdb.io/"+BUCKET+"/goods"
DEFAULT=[]
DEFAULT.append("Horlance Auto Cooling Ltd|Car AC Repair|25000|Osun & Oyo State|09046044472|Car Mart|YES|Pay on Delivery|Delivery Available")
DEFAULT.append("Mama T|Bag of Rice|45000|Abuja|09046044472|Food|YES|Transfer Before Delivery|Pickup Only")
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
    pay="Pay on Delivery"
    deli="Delivery Available"
    if len(p)>7:
        pay=p[7]
    if len(p)>8:
        deli=p[8]
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
    c1+="<p>WhatsApp: "+wa+"</p>"
    c1+="<p>💳 Payment: <b>"+pay+"</b></p>"
    c1+="<p>🚚 Delivery: <b>"+deli+"</b></p></div>"
    c1+="<img src='"+img+"' style='width:140px;"
    c1+="height:130px;object-fit:cover;"
    c1+="border-radius:14px'></div>"
    c1+="<a href='"+link+"' style='display:block;"
    c1+="background:#00A651;color:white;text-align:center;"
    c1+="padding:12px;border-radius:14px;"
    c1+="text-decoration:none;font-weight:bold;"
    c1+="margin-top:12px'>Chat on WhatsApp</a>"
    c1+="<a href='?page=Orders' style='display:block;"
    c1+="background:#FF8A00;color:white;text-align:center;"
    c1+="padding:10px;border-radius:14px;"
    c1+="text-decoration:none;font-weight:bold;"
    c1+="margin-top:8px'>Order + Pay / Delivery</a></div>"
    st.markdown(c1, unsafe_allow_html=True)
if page=="Shop":
    st.markdown("<div style='padding:10
