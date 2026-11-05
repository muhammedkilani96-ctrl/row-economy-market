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

st.markdown("""
<style>
header {visibility:hidden !important}
.block-container {padding-top:0px !important; padding-left:0px !important; padding-right:0px !important; padding-bottom:100px !important; max-width:100% !important}
div.stButton > button { width:100% !important; background:#22C55E !important; color:white !important; border-radius:12px !important; padding:12px !important; border:none !important; font-weight:700 !important; }
div.stLinkButton > a { width:100% !important; background:#22C55E !important; color:white !important; border-radius:12px !important; text-align:center !important; font-weight:700 !important; }
.kk-header { background:#22C55E; border-radius:0 0 24px 24px; padding:14px 16px 20px 16px; display:flex; justify-content:space-between; align-items:center; }
.kk-header h1 { color:white; margin:0; font-size:24px; font-weight:800; }
.cat-grid { display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:12px; padding:0 16px; }
.cat-item { text-align:center; }
.cat-box { border-radius:18px; padding:16px 6px; font-size:32px; }
.cat-item p { font-size:12px; margin:6px 0 0 0; color:#111; font-weight:500; }
.section-head { display:flex; justify-content:space-between; align-items:center; padding:0 16px; margin:18px 0 10px 0; }
.section-head h2 { margin:0; font-size:20px; font-weight:800; }
.featured { background:white; border-radius:20px; box-shadow:0 4px 20px #eee; margin:0 16px 16px 16px; padding:16px; border:1px solid #f0f0f0; }
.featured-img { width:130px; height:110px; object-fit:cover; border-radius:12px; float:right; }
.mama-bubble { background:#DCFCE7; border-radius:18px; border-bottom-left-radius:4px; padding:12px 14px; margin:0 16px 0 60px; font-size:14px; }
.swipe-row { display:flex; overflow-x:auto; scroll-snap-type:x mandatory; gap:12px; padding:8px 16px; -webkit-overflow-scrolling:touch; scrollbar-width:none; }
.swipe-row::-webkit-scrollbar { display:none; }
.swipe-card { min-width:76vw; max-width:76vw; scroll-snap-align:center; background:white; border-radius:20px; overflow:hidden; box-shadow:0 4px 20px #ddd; flex-shrink:0; }
.swipe-card img { width:100%; height:220px; object-fit:cover; }
.swipe-body { padding:14px; }
.feed-card { background:white; border-radius:20px; overflow:hidden; box-shadow:0 4px 20px #eee; margin:0 16px 16px 16px; border:1px solid #f0f0f0; }
.feed-card img { width:100%; height:300px; object-fit:cover; }
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
.cat-active { background:#22C55E; color:white; padding:10px; border-radius:16px; margin:0 16px; text-align:center; font-weight:700; }
div[data-testid="stSegmentedControl"] button { border-radius:20px !important; padding:8px 12px !important; font-size:12px !important; }
div[data-testid="stSegmentedControl"] button[data-testid="stSegmentedControlButton-selected"] { background:#22C55E !important; color:white !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""<div class="kk-header"><div style="font-size:28px;color:white">☰</div><h1>Row Economy Market</h1><div style="background:#FB923C;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px">👤</div></div>""", unsafe_allow_html=True)
st.markdown("""<div class="deal-box"><b>DEAL OF THE DAY - 12% OFF - Ends 4h 23m</b><br>Use code ROW12</div>""", unsafe_allow_html=True)

search_q = st.text_input("Search - Ask Mama Oloja", key="search_v15")
q = search_q

with st.expander("Your Details - Tap to set Name and WhatsApp", expanded=False):
    my_name_input = st.text_input("Your Name", value=st.session_state.my_name, key="my_name_v15")
    if my_name_input and my_name_input != st.session_state.my_name:
        st.session_state.my_name = my_name_input
        if my_name_input not in st.session_state.online_users:
            st.session_state.online_users.append(my_name_input)
    buyer_phone = st.text_input("Your WhatsApp Number", value=st.session_state.buyer_phone_temp, key="buyer_phone_v15")
    st.session_state.buyer_phone_temp = buyer_phone
    st.write("Referral invites:")
    st.write(st.session_state.referral_count)
    if st.button("I Invited a Friend +1", key="invite_v15"):
        st.session_state.referral_count += 1
        st.rerun()

buyer_name = st.session_state.my_name
buyer_phone = st.session_state.buyer_phone_temp
page = st.session_state.page

if page == "Home":
    st.markdown("""<div class="section-head"><h2>Categories</h2></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="cat-grid"><div class="cat-item"><div class="cat-box" style="background:#FBCFE8">🧴</div><p>Perfume</p></div><div class="cat-item"><div class="cat-box" style="background:#BFDBFE">👕</div><p>Clothes</p></div><div class="cat-item"><div class="cat-box" style="background:#BFDBFE">📱</div><p>Phones</p></div><div class="cat-item"><div class="cat-box" style="background:#FED7AA">🍲</div><p>Food</p></div><div class="cat-item"><div class="cat-box" style="background:#FED7AA">🚗</div><p>Car Mart</p></div><div class="cat-item"><div class="cat-box" style="background:#BBF7D0">💼</div><p>Services</p></div><div class="cat-item"><div class="cat-box" style="background:#FBCFE8">🎟️</div><p>Tickets</p></div><div class="cat-item"><div class="cat-box" style="background:#A7F3D0">💬</div><p>Chat Rooms</p></div></div>""", unsafe_allow_html=True)
    st.write("Tap a category below - you will see ONLY that category:")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("Perfume", key="cat_perfume_v15"):
            st.session_state.cat = "Perfume"
            st.rerun()
        if st.button("Car", key="cat_car_v15"):
            st.session_state.cat = "Car"
            st.rerun()
    with c2:
        if st.button("Clothes", key="cat_clothes_v15"):
            st.session_state.cat = "Clothes"
            st.rerun()
        if st.button("Services", key="cat_services_v15"):
            st.session_state.cat = "Services"
            st.rerun()
    with c3:
        if st.button("Phones", key="cat_phones_v15"):
            st.session_state.cat = "Phones"
            st.rerun()
        if st.button("Tickets", key="cat_tickets_v15"):
            st.session_state.cat = "Tickets"
            st.rerun()
    with c4:
        if st.button("Food", key="cat_food_v15"):
            st.session_state.cat = "Food"
            st.rerun()
        if st.button("Chat", key="cat_chat_v15"):
            st.session_state.cat = "Chat"
            st.rerun()
    if st.button("Show All Categories", key="cat_all_v15"):
        st.session_state.cat = "All"
        st.rerun()
    current_cat = st.session_state.cat
    st.markdown('<div class="cat-active">Showing ONLY: ' + current_cat + '</div>', unsafe_allow_html=True)
    if current_cat != "All":
        st.write("You are inside " + current_cat + " - only " + current_cat + " products below. Tap Show All to go back.")

    st.markdown("""<div class="post-box"><h3>POST YOUR PRODUCT - FREE</h3><p>Choose category correctly - buyers in that category will see ONLY your product there.</p></div>""", unsafe_allow_html=True)
    with st.expander("TAP TO POST YOUR PRODUCT", expanded=False):
        p_name = st.text_input("Your Name", value=buyer_name, key="post_name_v15")
        p_item = st.text_input("What are you selling?", key="post_item_v15")
        p_price = st.number_input("Price (Naira)", min_value=0, key="post_price_v15")
        p_cat = st.selectbox("Category - Choose correctly", ["Food","Phones","Perfume","Clothes","Car","Services","Tickets","Chat"], key="post_cat_v15")
        p_loc = st.text_input("Location", key="post_loc_v15")
        p_phone = st.text_input("Your WhatsApp", value=buyer_phone, key="post_phone_v15")
        uploaded = st.file_uploader("Upload Product Photo", type=["jpg","png","jpeg"], key="post_photo_v15")
        p_img_link = st.text_input("OR Paste Photo Link", key="post_img_v15")
        img_to_use = "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600"
        if uploaded is not None:
            st.image(uploaded, caption="Preview", width=200)
        if p_img_link:
            img_to_use = p_img_link
        if st.button("POST NOW", key="post_now_v15"):
            if p_name and p_item and p_price > 0:
                is_ver = p_name in st.session_state.verified_sellers
                st.session_state.local_goods.insert(0, {"name":p_name,"item":p_item,"price":int(p_price),"cat":p_cat,"loc":p_loc or "Abuja","phone":p_phone or "2349046044472","img":img_to_use,"verified":is_ver})
                st.success("Posted in " + p_cat + " category!")
                st.balloons()
            else:
                st.error("Fill Name, Product, Price")

    all_goods = get_goods()
    filtered = []
    for g in all_goods:
        if current_cat != "All":
            if g["cat"].lower().strip() != current_cat.lower().strip():
                continue
        if q and q.lower() not in (g["item"] + g["cat"] + g["loc"] + g["name"]).lower():
            continue
        filtered.append(g)

    st.markdown("""<div class="section-head"><h2>Featured Listing</h2></div>""", unsafe_allow_html=True)
    if len(filtered) > 0:
        feat = filtered[0]
        is_ver = feat["name"] in st.session_state.verified_sellers or feat["verified"]
        badge_txt = "VERIFIED" if is_ver else "New Seller"
        deal_p = deal_price(feat["price"])
        st.markdown('<div class="featured"><b>' + feat["name"] + '</b><br>' + feat["item"] + '<br>Location: ' + feat["loc"] + '<br>WhatsApp: ' + feat["phone"] + '<br><span class="price">N' + str(deal_p) + '</span> <span style="text-decoration:line-through;color:#999">N' + str(feat["price"]) + '</span><br>' + badge_txt + '</div>', unsafe_allow_html=True)
        st.image(feat["img"], width=300)
        wa_link = "https://wa.me/" + feat["phone"] + "?text=" + urllib.parse.quote("Hello " + feat["name"] + ", I saw your " + feat["item"] + " on Row Economy Market. Is it available?")
        st.link_button("Chat on WhatsApp", wa_link)
        st.markdown('<div class="mama-bubble">Welcome my dear, I can help you find the best price in the market.</div>', unsafe_allow_html=True)
    else:
        st.write("No products in " + current_cat + " yet. Be the first to post in " + current_cat + "!")

    st.markdown("""<div class="section-head"><h2>Swipe</h2></div>""", unsafe_allow_html=True)
    st.write("Swipe left / right - ONLY " + current_cat + " products here:")
    if len(filtered) > 0:
        cards = ""
        for g in filtered:
            cards += '<div class="swipe-card"><img src="' + g["img"] + '"><div class="swipe-body"><b>' + g["name"] + '</b><p>' + g["item"] + '</p><p class="price">N' + str(deal_price(g["price"])) + '</p></div></div>'
        st.markdown('<div class="swipe-row">' + cards + '</div>', unsafe_allow_html=True)

    st.markdown("""<div class="section-head"><h2>All Products - Scroll Down</h2></div>""", unsafe_allow_html=True)
    st.markdown('<div class="escrow-box"><b>ESCROW PROTECTION:</b> Pay to Row Economy Market, we hold money, seller delivers, you confirm.</div>', unsafe_allow_html=True)
    delivery_loc = st.selectbox("Your Delivery Area", ["Wuse 2, Abuja","Garki, Abuja","Gwarinpa, Abuja","Osun & Oyo","Abuja","Pickup Only"], key="delivery_loc_v15")
    payment = st.selectbox("Pay with", ["Escrow - Paystack (Safest)","Pay on Delivery (Cash)","Bank Transfer to Row Economy Market"], key="payment_v15")
    if payment == "Bank Transfer to Row Economy Market":
        st.markdown('<div class="paybox">Transfer: ' + BANK_NAME + ' - ' + ACCOUNT_NAME + ' - ' + ACCOUNT_NUMBER + '</div>', unsafe_allow_html=True)
    if "Escrow" in payment:
        st.link_button("Pay Safely via Escrow", PAYSTACK_LINK)
    st.write("Showing " + str(len(filtered)) + " products in " + current_cat)
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
        st.markdown('<div class="feed-card"><img src="' + g["img"] + '"><div class="feed-body"><b>' + g["name"] + '</b> - ' + badge_txt + '<p>' + g["item"] + ' - Category: ' + g["cat"] + '</p><p>Location: ' + g["loc"] + '</p><p class="price">N' + str(base) + ' Total N' + str(total) + '</p><p>Escrow: N' + str(comm) + ' to Market, Seller gets N' + str(seller_gets) + '</p></div></div>', unsafe_allow_html=True)
        if st.button("Chat Seller", key="chat_v15_" + str(idx)):
            st.session_state.page = "Profile"
            st.rerun()
        if st.button("Report Seller", key="rep_v15_" + str(idx)):
            st.error("Reported. Admin will check.")
        if st.button("ORDER - Escrow N" + str(total), key="order_v15_" + str(idx) + "_" + g["item"][:6]):
            if not buyer_name or not buyer_phone:
                st.error("Set Name + WhatsApp in Your Details first.")
            else:
                order = {"buyer":buyer_name,"buyer_phone":buyer_phone,"seller":g["name"],"seller_phone":g["phone"],"item":g["item"],"price":base,"total":total,"delivery":delivery_loc,"payment":payment,"status":"Pending","tracking":"Pending - Waiting Seller","time":datetime.now().strftime("%H:%M %d %b"),"commission":comm,"seller_gets":seller_gets}
                st.session_state.my_orders.append(order)
                st.session_state.seller_inbox.append(order)
                st.session_state.escrow_balance += total
                st.success("Order placed! Escrow held.")
                st.balloons()
        notify_msg = "Hello " + g["name"] + ", Row Economy Market NEW ORDER: " + g["item"] + " Total N" + str(total) + " Buyer " + buyer_name + " - " + buyer_phone + ". Reply YES / NO."
        notify_link = "https://wa.me/" + g["phone"] + "?text=" + urllib.parse.quote(notify_msg)
        st.link_button("Notify Seller on WhatsApp", notify_link)

if page == "Shop":
    st.markdown("""<div class="section-head"><h2>Shop</h2></div>""", unsafe_allow_html=True)
    st.info("Shop is same as Home. Tap Home to shop by category.")
    if st.button("Go Home", key="shop_home_v15"):
        st.session_state.page = "Home"
        st.rerun()

if page == "Orders":
    st.markdown("""<div class="section-head"><h2>My Orders + Tracking</h2></div>""", unsafe_allow_html=True)
    if len(st.session_state.my_orders) == 0:
        st.write("No orders yet.")
    for oi, o in enumerate(st.session_state.my_orders):
        st.markdown('<div class="track-box"><b>' + o["item"] + '</b> - N' + str(o.get("total", o["price"])) + '<br>Seller: ' + o["seller"] + '<br>Tracking: ' + o.get("tracking","") + '<br>Status: ' + o["status"] + '</div>', unsafe_allow_html=True)
        if o["status"] == "Available":
            if st.button("Confirm Delivery - Release Escrow", key="confirm_v15_" + str(oi)):
                st.session_state.escrow_balance -= o.get("total",0)
                st.session_state.my_earnings += o.get("commission",0)
                o["status"] = "Delivered"
                o["tracking"] = "Delivered - Escrow Released"
                st.success("Delivered! Escrow released.")
                st.rerun()
    st.markdown("""<div class="section-head"><h2>Seller Inbox</h2></div>""", unsafe_allow_html=True)
    seller_check = st.text_input("Your Seller WhatsApp", key="seller_check_v15")
    if seller_check:
        inbox = [o for o in st.session_state.seller_inbox if seller_check in o["seller_phone"]]
        if len(inbox) == 0:
            st.write("No orders yet.")
        for j, o in enumerate(inbox):
            st.markdown('<div class="notif">NEW ORDER Buyer: ' + o["buyer"] + ' Wants: ' + o["item"] + ' N' + str(o.get("total", o["price"])) + ' Tracking: ' + o.get("tracking","") + '</div>', unsafe_allow_html=True)
            colA, colB = st.columns(2)
            with colA:
                if st.button("YES I Have It", key="yes_v15_" + str(j)):
                    o["status"] = "Available"
                    o["tracking"] = "Packed - Waiting Rider"
                    for mo in st.session_state.my_orders:
                        if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                            mo["status"] = "Available"
                            mo["tracking"] = "Packed - Waiting Rider"
                    st.rerun()
            with colB:
                if st.button("NO Sold Out", key="no_v15_" + str(j)):
                    o["status"] = "Sold Out"
                    o["tracking"] = "Sold Out"
                    for mo in st.session_state.my_orders:
                        if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                            mo["status"] = "Sold Out"
                            mo["tracking"] = "Sold Out"
                    st.rerun()
            if o["status"] == "Available":
                if st.button("Rider Picked Up", key="rider_v15_" + str(j)):
                    o["tracking"] = "On The Way - Rider Picked Up"
                    for mo in st.session_state.my_orders:
                        if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                            mo["tracking"] = "On The Way - Rider Picked Up"
                    st.rerun()
                if st.button("Mark Delivered", key="deliv_v15_" + str(j)):
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
    if st.checkbox("Auto-refresh chat", value=True, key="autorefresh_v15"):
        time.sleep(8)
        st.rerun()
    tab1, tab2 = st.tabs(["General", "DM"])
    with tab1:
        for m in st.session_state.chat_msgs:
            if m["room"] == "General":
                cls = "chat-me" if m["user"] == buyer_name else "chatbox"
                st.markdown('<div class="' + cls + '"><b>' + m["user"] + '</b><br>' + m["msg"] + '</div>', unsafe_allow_html=True)
        msg = st.text_input("Type message", key="chat_general_v15")
        if st.button("Send", key="send_general_v15"):
            if not buyer_name:
                st.error("Set Name first.")
            elif msg:
                st.session_state.chat_msgs.append({"room":"General","user":buyer_name,"msg":msg,"time":datetime.now().strftime("%H:%M")})
                st.rerun()
    with tab2:
        dm_with = st.selectbox("Chat with", st.session_state.online_users, key="dm_select_v15")
        dm_room = "DM_" + dm_with
        for m in st.session_state.chat_msgs:
            if m["room"] == dm_room:
                cls = "chat-me" if m["user"] == buyer_name else "chatbox"
                st.markdown('<div class="' + cls + '"><b>' + m["user"] + '</b><br>' + m["msg"] + '</div>', unsafe_allow_html=True)
        dm_msg = st.text_input("DM message", key="dm_msg_v15")
        if st.button("Send DM", key="send_dm_v15"):
            if not buyer_name:
                st.error("Set Name first.")
            elif dm_msg:
                st.session_state.chat_msgs.append({"room":dm_room,"user":buyer_name,"msg":dm_msg,"time":datetime.now().strftime("%H:%M")})
                st.rerun()

nav = st.segmented_control("Nav", ["Home","Shop","Orders","Profile"], selection_mode="single", default=st.session_state.page, label_visibility="collapsed", key="nav_v15")
if nav and nav != st.session_state.page:
    st.session_state.page = nav
    st.rerun()
st.link_button("Share Row Economy Market", "https://wa.me/?text=Check%20Row%20Economy%20Market%20-%20Post%20FREE")
