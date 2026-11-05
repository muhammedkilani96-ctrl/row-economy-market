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
.block-container {padding-top:0px !important; padding-left:0px !important; padding-right:0px !important; padding-bottom:100px !important; max-width:100% !important}
div.stButton > button { width:100% !important; background:#22C55E !important; color:white !important; border-radius:16px !important; padding:14px 6px !important; border:none !important; font-weight:700 !important; font-size:14px !important; }
div.stLinkButton > a { width:100% !important; background:#22C55E !important; color:white !important; border-radius:12px !important; text-align:center !important; font-weight:700 !important; }
.kk-header { background:#22C55E; border-radius:0 0 24px 24px; padding:14px 16px 20px 16px; display:flex; justify-content:space-between; align-items:center; }
.kk-header h1 { color:white; margin:0; font-size:24px; font-weight:800; }
.section-head { display:flex; justify-content:space-between; align-items:center; padding:0 16px; margin:18px 0 10px 0; }
.section-head h2 { margin:0; font-size:20px; font-weight:800; }
.cat-page-header { border-radius:0 0 24px 24px; padding:18px 16px; margin-bottom:12px; text-align:center; color:white; }
.cat-page-header h1 { margin:0; font-size:28px; }
.cat-page-header p { margin:4px 0 0 0; font-size:13px; }
.feed-card { background:white; border-radius:20px; overflow:hidden; box-shadow:0 4px 20px #eee; margin:0 16px 16px 16px; border:1px solid #f0f0f0; }
.feed-card img { width:100%; height:280px; object-fit:cover; }
.feed-body { padding:14px; }
.price { color:#16A34A; font-weight:800; font-size:20px; margin:4px 0; }
.badge { background:#22C55E; color:white; padding:4px 10px; border-radius:20px; font-size:11px; font-weight:700; }
.badge2 { background:#FEF3C7; color:#92400E; padding:4px 10px; border-radius:20px; font-size:11px; }
.notif { background:#FEF9C3; border-left:4px solid #EAB308; padding:12px; border-radius:12px; margin:8px 16px; }
.paybox { background:#F0FDF4; border:1px solid #16A34A; border-radius:12px; padding:12px; margin:8px 16px; }
.escrow-box { background:#EFF6FF; border:1px solid #3B82F6; border-radius:12px; padding:12px; margin:8px 16px; }
.deal-box { background:linear-gradient(90deg,#EF4444,#F97316); color:white; border-radius:16px; padding:14px; margin:0 16px; text-align:center; }
.track-box { background:#F8FAFC; border-radius:12px; padding:12px; margin:8px 16px; border:1px solid #E2E8F0; }
.chatbox { background:#F8FAFC; border-radius:12px; padding:10px; margin:6px 16px; border:1px solid #E2E8F0; }
.chat-me { background:#DCFCE7; border-radius:12px; padding:10px; margin:6px 16px; text-align:right; }
.post-box { background:#FFF7ED; border:2px dashed #22C55E; border-radius:20px; padding:16px; margin:12px 16px; }
.swipe-row { display:flex; overflow-x:auto; scroll-snap-type:x mandatory; gap:12px; padding:8px 16px; -webkit-overflow-scrolling:touch; scrollbar-width:none; }
.swipe-row::-webkit-scrollbar { display:none; }
.swipe-card { min-width:76vw; max-width:76vw; scroll-snap-align:center; background:white; border-radius:20px; overflow:hidden; box-shadow:0 4px 20px #ddd; flex-shrink:0; }
.swipe-card img { width:100%; height:220px; object-fit:cover; }
.swipe-body { padding:14px; }
div[data-testid="stSegmentedControl"] button { border-radius:20px !important; padding:8px 12px !important; font-size:12px !important; }
div[data-testid="stSegmentedControl"] button[data-testid="stSegmentedControlButton-selected"] { background:#22C55E !important; color:white !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""<div class="kk-header"><div style="font-size:28px;color:white">☰</div><h1>Row Economy Market</h1><div style="background:#FB923C;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px">👤</div></div>""", unsafe_allow_html=True)

with st.expander("Your Details - Tap to set Name and WhatsApp", expanded=False):
    my_name_input = st.text_input("Your Name", value=st.session_state.my_name, key="my_name_v17")
    if my_name_input and my_name_input != st.session_state.my_name:
        st.session_state.my_name = my_name_input
        if my_name_input not in st.session_state.online_users:
            st.session_state.online_users.append(my_name_input)
    buyer_phone = st.text_input("Your WhatsApp Number", value=st.session_state.buyer_phone_temp, key="buyer_phone_v17")
    st.session_state.buyer_phone_temp = buyer_phone
    st.write("Referral invites:")
    st.write(st.session_state.referral_count)
    if st.button("I Invited a Friend +1", key="invite_v17"):
        st.session_state.referral_count += 1
        st.rerun()

buyer_name = st.session_state.my_name
buyer_phone = st.session_state.buyer_phone_temp
page = st.session_state.page
current_cat = st.session_state.cat

CAT_INFO = {
    "Food": {"emoji":"🍲","color":"#F97316","title":"Food Market","desc":"Rice, Garri, Oil, Fresh Food"},
    "Phones": {"emoji":"📱","color":"#3B82F6","title":"Phones Market","desc":"iPhone, Samsung, Accessories"},
    "Perfume": {"emoji":"🧴","color":"#EC4899","title":"Perfume Market","desc":"Oud, Designer Perfumes"},
    "Clothes": {"emoji":"👕","color":"#3B82F6","title":"Clothes Market","desc":"Ankara, Gowns, Shirts"},
    "Car": {"emoji":"🚗","color":"#F97316","title":"Car Mart","desc":"Car AC, Repairs, Car Sales"},
    "Services": {"emoji":"💼","color":"#22C55E","title":"Services Market","desc":"Plumber, Electrician, Hair"},
    "Tickets": {"emoji":"🎟️","color":"#EC4899","title":"Tickets Market","desc":"Event, Flight, Bus Tickets"},
    "Chat": {"emoji":"💬","color":"#10B981","title":"Chat Rooms","desc":"Talk to Sellers"},
}

def show_category_page(cat_name):
    info = CAT_INFO.get(cat_name, {"emoji":"🛒","color":"#22C55E","title":cat_name,"desc":""})
    st.markdown('<div class="cat-page-header" style="background:' + info["color"] + '"><h1>' + info["emoji"] + ' ' + info["title"] + '</h1><p>' + info["desc"] + '</p><p>Row Economy Market - ' + cat_name + ' ONLY</p></div>', unsafe_allow_html=True)
    if st.button("Back to Home - All Categories", key="back_home_" + cat_name):
        st.session_state.page = "Home"
        st.session_state.cat = "All"
        st.rerun()
    search_in_cat = st.text_input("Search in " + cat_name + " only", key="search_in_" + cat_name)
    st.markdown('<div class="post-box"><h3>POST YOUR ' + cat_name.upper() + ' PRODUCT - FREE</h3><p>Your product will show ONLY in ' + cat_name + ' page. People who press ' + cat_name + ' will see you.</p></div>', unsafe_allow_html=True)
    with st.expander("TAP TO POST IN " + cat_name.upper(), expanded=False):
        p_name = st.text_input("Your Name", value=buyer_name, key="post_name_" + cat_name)
        p_item = st.text_input("What are you selling in " + cat_name + "?", key="post_item_" + cat_name)
        p_price = st.number_input("Price (Naira)", min_value=0, key="post_price_" + cat_name)
        p_loc = st.text_input("Location", key="post_loc_" + cat_name)
        p_phone = st.text_input("Your WhatsApp", value=buyer_phone, key="post_phone_" + cat_name)
        uploaded = st.file_uploader("Upload Photo of your " + cat_name + " product", type=["jpg","png","jpeg"], key="post_photo_" + cat_name)
        p_img_link = st.text_input("OR Paste Photo Link", key="post_img_" + cat_name)
        img_to_use = "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600"
        if uploaded is not None:
            st.image(uploaded, caption="Your photo preview", width=200)
        if p_img_link:
            img_to_use = p_img_link
        if st.button("POST IN " + cat_name.upper() + " NOW", key="post_now_" + cat_name):
            if p_name and p_item and p_price > 0:
                is_ver = p_name in st.session_state.verified_sellers
                st.session_state.local_goods.insert(0, {"name":p_name,"item":p_item,"price":int(p_price),"cat":cat_name,"loc":p_loc or "Abuja","phone":p_phone or "2349046044472","img":img_to_use,"verified":is_ver})
                st.success("Posted in " + cat_name + "! People who press " + cat_name + " will see you now!")
                st.balloons()
                st.rerun()
            else:
                st.error("Fill Name, Product, Price")
    all_goods = get_goods()
    filtered = []
    for g in all_goods:
        if g["cat"].lower().strip() != cat_name.lower().strip():
            continue
        if search_in_cat and search_in_cat.lower() not in (g["item"] + g["name"] + g["loc"]).lower():
            continue
        filtered.append(g)
    st.write("Showing " + str(len(filtered)) + " products in " + cat_name + " - ONLY " + cat_name)
    if len(filtered) == 0:
        st.write("No products in " + cat_name + " yet. Be the first to post in " + cat_name + " above!")
        st.image("https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600", width=300)
    st.markdown("""<div class="section-head"><h2>Swipe - """ + cat_name + """</h2></div>""", unsafe_allow_html=True)
    if len(filtered) > 0:
        cards = ""
        for g in filtered:
            cards += '<div class="swipe-card"><img src="' + g["img"] + '"><div class="swipe-body"><b>' + g["name"] + '</b><p>' + g["item"] + '</p><p class="price">N' + str(deal_price(g["price"])) + '</p></div></div>'
        st.markdown('<div class="swipe-row">' + cards + '</div>', unsafe_allow_html=True)
    st.markdown("""<div class="section-head"><h2>All """ + cat_name + """ Products - With Seller Pics</h2></div>""", unsafe_allow_html=True)
    delivery_loc = st.selectbox("Your Delivery Area", ["Wuse 2, Abuja","Garki, Abuja","Gwarinpa, Abuja","Osun & Oyo","Abuja","Pickup Only"], key="delivery_" + cat_name)
    payment = st.selectbox("Pay with", ["Escrow - Paystack (Safest)","Pay on Delivery (Cash)","Bank Transfer to Row Economy Market"], key="payment_" + cat_name)
    if payment == "Bank Transfer to Row Economy Market":
        st.markdown('<div class="paybox">Transfer: ' + BANK_NAME + ' - ' + ACCOUNT_NAME + ' - ' + ACCOUNT_NUMBER + '</div>', unsafe_allow_html=True)
    if "Escrow" in payment:
        st.link_button("Pay Safely via Escrow", PAYSTACK_LINK)
    for idx, g in enumerate(filtered):
        is_ver = g["name"] in st.session_state.verified_sellers or g["verified"]
        badge_txt = "VERIFIED" if is_ver else "New Seller"
        fee = delivery_fee(delivery_loc)
        base = deal_price(g["price"])
        discount = 500 if st.session_state.referral_count >= 3 else 0
        total = base + (0 if base >= 100000 else fee) - discount
        if total < 0:
            total = 0
        comm = int(total * COMMISSION)
        seller_gets = int(total * (1 - COMMISSION))
        avatar = seller_avatar(g["name"])
        st.markdown('<div class="feed-card"><img src="' + g["img"] + '"><div class="feed-body"><div style="display:flex;gap:10px;align-items:center"><img src="' + avatar + '" style="width:48px;height:48px;border-radius:50%;object-fit:cover"><div><b>' + g["name"] + '</b> - ' + badge_txt + '<br><span style="font-size:12px;color:#666">Seller in ' + g["cat"] + ' - ' + g["loc"] + '</span></div></div><p style="margin:10px 0 4px 0;font-size:16px">' + g["item"] + '</p><p style="font-size:12px;color:#666">Category: ' + g["cat"] + ' | Location: ' + g["loc"] + '</p><p class="price">N' + str(base) + ' <span style="font-size:12px;color:#999;text-decoration:line-through">N' + str(g["price"]) + '</span> Total N' + str(total) + '</p><p style="font-size:11px;color:#3B82F6">Escrow: N' + str(comm) + ' to Market, Seller gets N' + str(seller_gets) + '</p></div></div>', unsafe_allow_html=True)
        if st.button("Chat Seller", key="chat_" + cat_name + "_" + str(idx)):
            st.session_state.page = "Profile"
            st.rerun()
        if st.button("ORDER - Escrow N" + str(total), key="order_" + cat_name + "_" + str(idx) + "_" + g["item"][:5]):
            if not buyer_name or not buyer_phone:
                st.error("Set Name + WhatsApp in Your Details first.")
            else:
                order = {"buyer":buyer_name,"buyer_phone":buyer_phone,"seller":g["name"],"seller_phone":g["phone"],"item":g["item"],"price":base,"total":total,"delivery":delivery_loc,"payment":payment,"status":"Pending","tracking":"Pending - Waiting Seller","time":datetime.now().strftime("%H:%M %d %b"),"commission":comm,"seller_gets":seller_gets}
                st.session_state.my_orders.append(order)
                st.session_state.seller_inbox.append(order)
                st.session_state.escrow_balance += total
                st.success("Order placed in " + cat_name + "! Escrow held.")
                st.balloons()
        notify_msg = "Hello " + g["name"] + ", Row Economy Market NEW ORDER in " + cat_name + ": " + g["item"] + " Total N" + str(total) + " Buyer " + buyer_name + " - " + buyer_phone + ". Reply YES / NO."
        notify_link = "https://wa.me/" + g["phone"] + "?text=" + urllib.parse.quote(notify_msg)
        st.link_button("Notify Seller on WhatsApp", notify_link)

if page == "Home":
    st.markdown("""<div class="deal-box"><b>DEAL OF THE DAY - 12% OFF - Ends 4h 23m</b><br>Use code ROW12</div>""", unsafe_allow_html=True)
    search_q = st.text_input("Search - Ask Mama Oloja", key="search_home_v17")
    st.markdown("""<div class="section-head"><h2>Categories - Tap the Box to Open Its Page</h2></div>""", unsafe_allow_html=True)
    st.write("Tap any box below - it opens its OWN page with ONLY that category + seller pics:")
    # ROW 1 - 4 CATEGORIES - EACH BUTTON IS THE BOX
    r1c1, r1c2, r1c3, r1c4 = st.columns(4)
    with r1c1:
        st.markdown("<div style='text-align:center;font-size:40px'>🧴</div>", unsafe_allow_html=True)
        if st.button("Perfume", key="home_perfume_v17"):
            open_cat("Perfume")
    with r1c2:
        st.markdown("<div style='text-align:center;font-size:40px'>👕</div>", unsafe_allow_html=True)
        if st.button("Clothes", key="home_clothes_v17"):
            open_cat("Clothes")
    with r1c3:
        st.markdown("<div style='text-align:center;font-size:40px'>📱</div>", unsafe_allow_html=True)
        if st.button("Phones", key="home_phones_v17"):
            open_cat("Phones")
    with r1c4:
        st.markdown("<div style='text-align:center;font-size:40px'>🍲</div>", unsafe_allow_html=True)
        if st.button("Food", key="home_food_v17"):
            open_cat("Food")
    # ROW 2
    r2c1, r2c2, r2c3, r2c4 = st.columns(4)
    with r2c1:
        st.markdown("<div style='text-align:center;font-size:40px'>🚗</div>", unsafe_allow_html=True)
        if st.button("Car Mart", key="home_car_v17"):
            open_cat("Car")
    with r2c2:
        st.markdown("<div style='text-align:center;font-size:40px'>💼</div>", unsafe_allow_html=True)
        if st.button("Services", key="home_services_v17"):
            open_cat("Services")
    with r2c3:
        st.markdown("<div style='text-align:center;font-size:40px'>🎟️</div>", unsafe_allow_html=True)
        if st.button("Tickets", key="home_tickets_v17"):
            open_cat("Tickets")
    with r2c4:
        st.markdown("<div style='text-align:center;font-size:40px'>💬</div>", unsafe_allow_html=True)
        if st.button("Chat Rooms", key="home_chat_v17"):
            open_cat("Chat")
    st.markdown("""<div class="section-head"><h2>Preview - Tap to Open Category Page</h2></div>""", unsafe_allow_html=True)
    all_goods = get_goods()
    for g in all_goods[:3]:
        st.markdown('<div class="feed-card"><img src="' + g["img"] + '"><div class="feed-body"><b>' + g["name"] + '</b><p>' + g["item"] + ' - ' + g["cat"] + '</p><p class="price">N' + str(deal_price(g["price"])) + '</p></div></div>', unsafe_allow_html=True)
        if st.button("Open " + g["cat"] + " Page", key="open_cat_" + g["cat"] + "_" + g["item"][:4]):
            open_cat(g["cat"])

if page == "Category":
    show_category_page(current_cat)

if page == "Shop":
    st.markdown("""<div class="section-head"><h2>Shop</h2></div>""", unsafe_allow_html=True)
    st.info("Tap Home, then tap a category box to open its page.")
    if st.button("Go Home", key="shop_home_v17"):
        st.session_state.page = "Home"
        st.rerun()

if page == "Orders":
    st.markdown("""<div class="section-head"><h2>My Orders + Tracking</h2></div>""", unsafe_allow_html=True)
    if len(st.session_state.my_orders) == 0:
        st.write("No orders yet.")
    for oi, o in enumerate(st.session_state.my_orders):
        st.markdown('<div class="track-box"><b>' + o["item"] + '</b> - N' + str(o.get("total", o["price"])) + '<br>Seller: ' + o["seller"] + '<br>Tracking: ' + o.get("tracking","") + '<br>Status: ' + o["status"] + '</div>', unsafe_allow_html=True)
        if o["status"] == "Available":
            if st.button("Confirm Delivery - Release Escrow", key="confirm_v17_" + str(oi)):
                st.session_state.escrow_balance -= o.get("total",0)
                st.session_state.my_earnings += o.get("commission",0)
                o["status"] = "Delivered"
                o["tracking"] = "Delivered - Escrow Released"
                st.success("Delivered! Escrow released.")
                st.rerun()
    st.markdown("""<div class="section-head"><h2>Seller Inbox</h2></div>""", unsafe_allow_html=True)
    seller_check = st.text_input("Your Seller WhatsApp", key="seller_check_v17")
    if seller_check:
        inbox = [o for o in st.session_state.seller_inbox if seller_check in o["seller_phone"]]
        if len(inbox) == 0:
            st.write("No orders yet.")
        for j, o in enumerate(inbox):
            st.markdown('<div class="notif">NEW ORDER Buyer: ' + o["buyer"] + ' Wants: ' + o["item"] + ' N' + str(o.get("total", o["price"])) + ' Tracking: ' + o.get("tracking","") + '</div>', unsafe_allow_html=True)
            colA, colB = st.columns(2)
            with colA:
                if st.button("YES I Have It", key="yes_v17_" + str(j)):
                    o["status"] = "Available"
                    o["tracking"] = "Packed - Waiting Rider"
                    for mo in st.session_state.my_orders:
                        if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                            mo["status"] = "Available"
                            mo["tracking"] = "Packed - Waiting Rider"
                    st.rerun()
            with colB:
                if st.button("NO Sold Out", key="no_v17_" + str(j)):
                    o["status"] = "Sold Out"
                    o["tracking"] = "Sold Out"
                    for mo in st.session_state.my_orders:
                        if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                            mo["status"] = "Sold Out"
                            mo["tracking"] = "Sold Out"
                    st.rerun()
            if o["status"] == "Available":
                if st.button("Rider Picked Up", key="rider_v17_" + str(j)):
                    o["tracking"] = "On The Way - Rider Picked Up"
                    for mo in st.session_state.my_orders:
                        if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                            mo["tracking"] = "On The Way - Rider Picked Up"
                    st.rerun()
                if st.button("Mark Delivered", key="deliv_v17_" + str(j)):
                    o["tracking"] = "Delivered - Waiting Buyer Confirmation"
                    for mo in st.session_state.my_orders:
                        if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                            mo["tracking"] = "Delivered - Waiting Buyer Confirmation"
                    st.rerun()

if page == "Profile":
    st.markdown("""<div class="section-head"><h2>Profile + Chat</h2></div>""", unsafe_allow_html=True)
    st.write("Name: " + (buyer_name or "Guest"))
    st.write("Phone: " + (buyer_phone or "No number"))
    st.write("Escrow Held: N" + str(st.session_state.escrow_balance))
    st.write("Your Earnings: N" + str(st.session_state.my_earnings))
    st.write("Online users: " + ", ".join(st.session_state.online_users))
    if st.checkbox("Auto-refresh chat", value=True, key="autorefresh_v17"):
        time.sleep(8)
        st.rerun()
    tab1, tab2 = st.tabs(["General", "DM"])
    with tab1:
        for m in st.session_state.chat_msgs:
            if m["room"] == "General":
                cls = "chat-me" if m["user"] == buyer_name else "chatbox"
                st.markdown('<div class="' + cls + '"><b>' + m["user"] + '</b><br>' + m["msg"] + '</div>', unsafe_allow_html=True)
        msg = st.text_input("Type message", key="chat_general_v17")
        if st.button("Send", key="send_general_v17"):
            if not buyer_name:
                st.error("Set Name first.")
            elif msg:
                st.session_state.chat_msgs.append({"room":"General","user":buyer_name,"msg":msg,"time":datetime.now().strftime("%H:%M")})
                st.rerun()
    with tab2:
        dm_with = st.selectbox("Chat with", st.session_state.online_users, key="dm_select_v17")
        dm_room = "DM_" + dm_with
        for m in st.session_state.chat_msgs:
            if m["room"] == dm_room:
                cls = "chat-me" if m["user"] == buyer_name else "chatbox"
                st.markdown('<div class="' + cls + '"><b>' + m["user"] + '</b><br>' + m["msg"] + '</div>', unsafe_allow_html=True)
        dm_msg = st.text_input("DM message", key="dm_msg_v17")
        if st.button("Send DM", key="send_dm_v17"):
            if not buyer_name:
                st.error("Set Name first.")
            elif dm_msg:
                st.session_state.chat_msgs.append({"room":dm_room,"user":buyer_name,"msg":dm_msg,"time":datetime.now().strftime("%H:%M")})
                st.rerun()

nav = st.segmented_control("Nav", ["Home","Shop","Orders","Profile"], selection_mode="single", default="Home" if page=="Category" else page, label_visibility="collapsed", key="nav_v17")
if nav and nav != st.session_state.page:
    st.session_state.page = nav
    st.rerun()
st.link_button("Share Row Economy Market", "https://wa.me/?text=Check%20Row%20Economy%20Market%20-%20Post%20FREE")
