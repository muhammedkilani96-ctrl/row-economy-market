import streamlit as st
import urllib.parse as u
import requests, json
st.set_page_config(page_title="Row Economy", layout="wide")
BUCKET="SzHmbyQQ1X1ns5LY4Qi8u9"
KV="https://kvdb.io/"+BUCKET+"/goods"
D1="Horlance Auto Cooling Ltd|Car AC Repair|25000|Osun & Oyo State|09046044472|Car Mart|YES|Pay on Delivery|Delivery Available"
D2="Mama T|Bag of Rice|45000|Abuja|09046044472|Food|YES|Transfer Before Delivery|Pickup Only"
DEFAULT=[D1,D2]
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
    msg=u.quote("Hello "+seller+", I want "+name)
    link="https://wa.me/234"+wa[1:]+"?text="+msg
    img="https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=400"
    if "AC" not in name:
        img="https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400"
    c1="<div style='background:white;margin:0 14px 16px;"
    c1+="padding:16px;border-radius:20px;"
    c1+="box-shadow:0 4px 16px #EDEDED'>
