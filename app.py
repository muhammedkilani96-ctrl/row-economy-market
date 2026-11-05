import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import time

st.set_page_config(page_title="Row Economy Market", layout="wide", initial_sidebar_state="collapsed")
SHEET_ID = "1w8P3SQiChShHPQzShpgznR-lay-awTHmu_x-VHI9IU8E"
if "my_orders" not in st.session_state: st.session_state.my_orders = []
if "seller_inbox" not in st.session_state: st.session_state.seller_inbox = []
if "local_goods" not in st.session_state: st.session_state.local_goods = []
if "page" not in st.session_state: st.session_state.page = "Home"
if "cat" not in st.session_state: st.session_state.cat = "All"
if "my_name" not in st.session_state: st.session_state.my_name = ""
if "buyer_phone_temp" not in st.session_state: st.session_state.buyer_phone_temp = ""
if "referral_count" not in st.session_state: st.session_state.referral_count = 0
if "verified_sellers" not in st.session_state: st.session_state.verified_sellers = ["Horlance Auto Cooling Ltd", "Mama Ada"]
if "chat_msgs" not in st.session_state: st.session_state.chat_msgs = [{"room":"General","user":"Mama Ada","msg":"Welcome to Row Economy Market","time":"09:12"}]
if "online_users" not in st.session_state: st.session_state.online_users = ["Mama Ada","Horlance Auto","Tunde"]
if "escrow_balance" not in st.session_state: st.session_state.escrow_balance = 0
if "my_earnings" not in st.session_state: st.session_state.my_earnings = 0

PAYSTACK_LINK = "https://paystack.shop/rowmarket"
BANK_NAME = "OPay / GTB"
ACCOUNT_NAME = "Row Economy Market - Horlance"
ACCOUNT_NUMBER = "9046044472"
COMMISSION = 0.05

@st.cache_data(ttl=30)
def load_sheet(sid):
    try:
        url = "https://docs.google.com/spreadsheets/d/" + sid + "/export?format=csv"
        df = pd.read_csv(url)
        return df.dropna(subset=["Item"])
    except:
        return pd.DataFrame()

def get_goods():
    goods = []
    df = load_sheet(SHEET_ID)
    for _, r in df.iterrows():
        try:
            nm = str(r.get("Name",""))
            it = str(r.get("Item",""))
            pr = int(float(r.get("Price",0)))
            ct = str(r.get("Category",""))
            lc = str(r.get("Location","Abuja"))
            ph = str(r.get("Phone","2349046044472"))
            im = str(r.get("Image","https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600"))
            vf = str(r.get("Verified","")).upper() == "TRUE"
            goods.append({"name":nm,"item":it,"price":pr,"cat":ct,"loc":lc,"phone":ph,"img":im,"verified":vf})
        except:
            pass
    goods = st.session_state.local_goods + goods
    if len(goods) == 0:
        goods = [
            {"name":"Horlance Auto Cooling Ltd","item":"Car AC Repair","price":25000,"cat":"Car","loc":"Osun & Oyo State","img":"https://images.unsplash.com/photo-1625047509168-a7026f36de04?w=600","phone":"2349046044472","verified":True},
            {"name":"Mama Ada","item":"Bag of Rice 50kg","price":85000,"cat":"Food","loc":"Wuse 2, Abuja","img":"https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600","phone":"2349046044472","verified":True},
            {"name":"Tunde Perfumes","item":"Oud Perfume 100ml","price":15000,"cat":"Perfume","loc":"Garki, Abuja","img":"https://images.unsplash.com/photo-1541643600914-78b084683601?w=600","phone":"2349046044472","verified":False},
            {"name":"Chidi Phones","item":"iPhone 12 - Neatly Used","price":280000,"cat":"Phones","loc":"Wuse 2, Abuja","img":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600","phone":"2349046044472","verified":False},
            {"name":"Aisha Fashion","item":"Ankara Gown","price":25000,"cat":"Clothes","loc":"Gwarinpa, Abuja","img":"https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=600","phone":"2349046044472","verified":False},
        ]
    return goods

def delivery_fee(loc):
    if "Wuse" in loc:
        return 1500
    if "Garki" in loc:
        return 1500
    if "Gwarinpa" in loc:
        return 2000
    if "Osun" in loc or "Oyo" in loc:
        return 3000
    return 2500

def deal_price(p):
    return int(p * 0.88)

def seller_avatar(name):
    if "Mama" in name or "Aisha" in name:
        return "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=100"
    if "Horlance" in name:
        return "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100"
    return "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100"

def open_cat(cat_name):
    st.session_state.cat = cat_name
    st.session_state.page = "Category"
    st.rerun()

st.markdown("""
<style>
header {visibility:hidden !important}
.block-container {padding-top:0px !important; padding-left:0px !important; padding-right:0px !important; padding-bottom:120px !important; max-width:100% !important}
div.stButton > button { width:100% !important; background:#22C55E !important; color:white !important; border-radius:16px !important; padding:14px 6px !important; border:none !important; font-weight:700 !important; font-size:15px !important; }
div.stLinkButton > a { width:100% !important; background:#22C55E !important; color:white !important; border-radius:12px !important; text-align:center !important; font-weight:700 !important; }
.kk-header { background:#22C55E; border-radius:0 0 24px 24px; padding:14px 16px 20px 16px; display:flex; justify-content:space-between; align-items:center; }
.kk-header h1
