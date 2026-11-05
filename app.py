import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import time

st.set_page_config(page_title="Row Market - Abuja", layout="wide", initial_sidebar_state="collapsed")

SHEET_ID = "1w8P3SQiChShHPQzShpgznR-lay-awTHmu_x-VHI9IU8E"
if "my_orders" not in st.session_state: st.session_state.my_orders = []
if "seller_inbox" not in st.session_state: st.session_state.seller_inbox = []
if "local_goods" not in st.session_state: st.session_state.local_goods = []
if "ratings" not in st.session_state: st.session_state.ratings = {}
if "page" not in st.session_state: st.session_state.page = "Home"
if "cat" not in st.session_state: st.session_state.cat = "All"
if "my_name" not in st.session_state: st.session_state.my_name = ""
if "chat_msgs" not in st.session_state:
    st.session_state.chat_msgs = [
        {"room":"General","user":"Mama Ada","msg":"Welcome! Rice still available 🍚","time":"09:12"},
        {"room":"General","user":"Horlance Auto","msg":"Car AC repair 25k today 🚗❄️","time":"09:20"},
    ]
if "online_users" not in st.session_state: st.session_state.online_users = ["Mama Ada","Horlance Auto","Tunde","Chidi","Aisha"]

PAYSTACK_LINK = "https://paystack.shop/rowmarket"
BANK_NAME = "OPay / GTB"
ACCOUNT_NAME = "Row Market - Horlance"
ACCOUNT_NUMBER = "9046044472"

@st.cache_data(ttl=30)
def load_sheet(sid):
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sid}/export?format=csv"
        df = pd.read_csv(url)
        return df.dropna(subset=["Item"])
    except: return pd.DataFrame()

def get_goods():
    goods = []
    df = load_sheet(SHEET_ID)
    for _, r in df.iterrows():
        try: goods.append({"name":str(r.get("Name","")),"item":str(r.get("Item","")),"price":int(float(r.get("Price",0))),"cat":str(r.get("Category","")),"loc":str(r.get("Location","Abuja")),"phone":str(r.get("Phone","2349046044472")),"img":str(r.get("Image","https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600")),"verified":str(r.get("Verified","")).upper()=="TRUE"})
        except: pass
    goods = st.session_state.local_goods + goods
    if len(goods)==0:
        goods = [
            {"name":"Horlance Auto Cooling Ltd","item":"Car AC Repair","price":25000,"cat":"Car","loc":"Osun & Oyo State","img":"https://images.unsplash.com/photo-1625047509168-a7026f36de04?w=600","phone":"2349046044472","verified":True},
            {"name":"Mama Ada","item":"Bag of Rice 50kg","price":85000,"cat":"Food","loc":"Wuse 2, Abuja","img":"https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600","phone":"2349046044472","verified":True},
        ]
    return goods

def delivery_fee(loc):
    if "Wuse" in loc: return 1500
    if "Garki" in loc: return 1500
    if "Gwarinpa" in loc: return 2000
    if "Osun" in loc or "Oyo" in loc: return 3000
    return 2500

st.markdown("""
<style>
header {visibility:hidden !important}
.block-container {padding-top:0px !important; padding-left:0px !important; padding-right:0px !important; padding-bottom:100px !important; max-width:100% !important}
div.stButton > button { width:100% !important; background:#22C55E !important; color:white !important; border-radius:12px !important; padding:12px !important; border:none !important; font-weight:700 !important; }
div.stLinkButton > a { width:100% !important; background:#22C55E !important; color:white !important; border-radius:12px !important; text-align:center !important; font-weight:700 !important; }
/* K&K STYLE */
.kk-header { background:#22C55E; border-radius:0 0 24px 24px; padding:14px 16px 20px 16px; display:flex; justify-content:space-between; align-items:center; }
.kk-header h1 { color:white; margin:0; font-size:26px; font-weight:800; letter-spacing:-0.5px; }
.kk-search { background:#F1F5F9; border-radius:16px; margin:-10px 16px 0 16px; padding:12px 14px; display:flex; align-items:center; gap:8px; box-shadow:0 2px 10px #ddd; position:relative; z-index:10; }
.kk-search input { border:none; background:transparent; outline:none; width:100%; font-size:14px; }
.cat-grid { display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:12px; padding:0 16px; }
.cat-item { text-align:center; }
.cat-box { border-radius:18px; padding:16px 6px; font-size:32px; }
.cat-item p { font-size:12px; margin:6px 0 0 0; color:#111; font-weight:500; }
.section-head { display:flex; justify-content:space-between; align-items:center; padding:0 16px; margin:18px 0 10px 0; }
.section-head h2 { margin:0; font-size:20px; font-weight:800; }
.section-head span { color:#22C55E; font-size:13px; font-weight:600; }
.featured { background:white; border-radius:20px; box-shadow:0 4px 20px #eee; margin:0 16px 16px 16px; padding:16px; border:1px solid #f0f0f0; }
.featured-img { width:130px; height:110px; object-fit:cover; border-radius:12px; float:right; }
.mama-bubble { background:#DCFCE7; border-radius:18px; border-bottom-left-radius:4px; padding:12px 14px; margin:0 16px 0 60px; font-size:14px; line-height:1.4; }
.mama-avatar { width:44px; height:44px; border-radius:50%; object-fit:cover; position:absolute; left:16px; }
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
.chatbox { background:#F8FAFC; border-radius:12px; padding:10px; margin:6px 16px; border:1px solid #E2E8F0; }
.chat-me { background:#DCFCE7; border-radius:12px; padding:10px; margin:6px 16px; text-align:right; }
.post-box { background:#FFF7ED; border:2px dashed #22C55E; border-radius:20px; padding:16px; margin:12px 16px; }
.bottom-bar { position:fixed; bottom:0; left:0; right:0; background:white; border-top:1px solid #eee; padding:10px 0 14px 0; display:flex; justify-content:space-around; z-index:999; }
.bottom-bar div { text-align:center; font-size:11px; color:#94A3B8; }
.bottom-bar .active { color:#22C55E; font-weight:700; }
div[data-testid="stSegmentedControl"] button { border-radius:20px !important; padding:8px 12px !important; font-size:12px !important; }
div[data-testid="stSegmentedControl"] button[data-testid="stSegmentedControlButton-selected"] { background:#22C55E !important; color:white !important; }
</style>
""", unsafe_allow_html=True)

# ===== K&K HEADER - EXACT LIKE PHOTO =====
st.markdown("""
<div class="kk-header">
<div style="font-size:28px;color:white">☰</div>
<h1>K&K Market</h1>
<div style="background:#FB923C;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px">👤</div>
</div>
""", unsafe_allow_html=True)

# Search bar - Ask Mama Oloja
search_q = st.text_input("🔍 Ask Mama Oloja - What are you looking for today? 🎤", key="kk_search_v13", placeholder="Ask Mama Oloja - What are you looking for today?")
q = search_q

# Your details - hidden but needed
with st.expander("👤 Your Details - Tap to set Name & WhatsApp", expanded=False):
    my_name_input = st.text_input("Your Name", value=st.session_state.my_name, key="my_name_v13")
    if my_name_input and my_name_input != st.session_state.my_name:
        st.session_state.my_name = my_name_input
        if my_name_input not in st.session_state.online_users: st.session_state.online_users.append(my_name_input)
    buyer_phone = st.text_input("Your WhatsApp Number", key="buyer_phone_v13", placeholder="e.g. 2348031234567")
    st.session_state.buyer_phone_temp = buyer_phone
buyer_name = st.session_state.my_name
buyer_phone = st.session_state.get("buyer_phone_temp","")

page = st.session_state.page

# ===== HOME PAGE - LIKE PHOTO =====
if page == "Home":
    # Categories - EXACT LIKE PHOTO 4x2
    st.markdown("""
    <div class="section-head"><h2>Categories</h2><span>See all ›</span></div>
    <div class="cat-grid">
    <div class="cat-item"><div class="cat-box" style="background:#FBCFE8">🧴</div><p>Perfume</p></div>
    <div class="cat-item"><div class="cat-box" style="background:#BFDBFE">👕</div><p>Clothes</p></div>
    <div class="cat-item"><div class="cat-box" style="background:#BFDBFE">📱</div><p>Phones</p></div>
    <div class="cat-item"><div class="cat-box" style="background:#FED7AA">🍲</div><p>Food</p></div>
    <div class="cat-item"><div class="cat-box" style="background:#FED7AA">🚗</div><p>Car Mart</p></div>
    <div class="cat-item"><div class="cat-box" style="background:#BBF7D0">💼</div><p>Services</p></div>
    <div class="cat-item"><div class="cat-box" style="background:#FBCFE8">🎟️</div><p>Tickets</p></div>
    <div class="cat-item"><div class="cat-box" style="background:#A7F3D0">💬</div><p>Chat Rooms</p></div>
    </div>
    """, unsafe_allow_html=True)
    cat_pick = st.segmented_control("Cat", ["All","Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], selection_mode="single", default=st.session_state.cat, label_visibility="collapsed", key="cat_v13")
    if cat_pick: st.session_state.cat = cat_pick

    # POST - Big button like in photo style
    st.markdown("""<div class="post-box"><h3 style="margin:0">📸 POST YOUR PRODUCT - FREE</h3><p style="margin:4px 0 0 0;font-size:13px;color:#666">Tap below, post in 10 secs, appear in Featured + Swipe + Feed</p></div>""", unsafe_allow_html=True)
    with st.expander("➕ TAP TO POST YOUR PRODUCT", expanded=False):
        p_name = st.text_input("Your Name", value=buyer_name, key="post_name_v13")
        p_item = st.text_input("What are you selling?", key="post_item_v13", placeholder="e.g. Bag of Rice 50kg")
        p_price = st.number_input("Price (Naira)", min_value=0, key="post_price_v13")
        p_cat = st.selectbox("Category", ["Food","Phones","Perfume","Clothes","Car","Services","Tickets","Chat"], key="post_cat_v13")
        p_loc = st.text_input("Location", key="post_loc_v13", placeholder="Wuse 2, Abuja")
        p_phone = st.text_input("Your WhatsApp", value=buyer_phone, key="post_phone_v13")
        p_img = st.text_input("Photo Link (optional)", key="post_img_v13")
        if st.button("🚀 POST NOW", key="post_now_v13"):
            if p_name and p_item and p_price>0:
                st.session_state.local_goods.insert(0, {"name":p_name,"item":p_item,"price":int(p_price),"cat":p_cat,"loc":p_loc or "Abuja","phone":p_phone or "2349046044472","img":p_img or "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600","verified":False})
                st.success(f"✅ Posted! '{p_item}' is LIVE!"); st.balloons()
            else: st.error("Fill Name, Product, Price")

    # Featured Listing - EXACT LIKE PHOTO
    st.markdown("""<div class="section-head"><h2>Featured Listing</h2><span>See all ›</span></div>""", unsafe_allow_html=True)
    all_goods = get_goods()
    # Filter by cat + search
    filtered=[]
    for g in all_goods:
        if st.session_state.cat!="All" and st.session_state.cat.lower() not in g["cat"].lower(): continue
        if q and q.lower() not in (g["item"]+g["cat"]+g["loc"]+g["name"]).lower(): continue
        filtered.append(g)
    # Show first as Featured like photo - Horlance style
    if len(filtered)>0:
        feat = filtered[0]
        badge = '<span class="badge">✅ VERIFIED</span>' if feat["verified"] else '<span class="badge2">New Seller</span>'
        st.markdown(f"""
        <div class="featured">
        <div style="display:flex;justify-content:space-between;align-items:start"><div><b style="font-size:16px">{feat['name']}</b><br><span style="font-size:14px;color:#333">🔧 {feat['item']}</span><br><br><span style="font-size:13px;color:#555">📍 {feat['loc']}</span><br><span style="font-size:13px;color:#555">🟢 WhatsApp {feat['phone']}</span><br><span class="price">N{feat['price']:,}</span></div><img src="{feat['img']}" class="featured-img"></div>
        <div style="text-align:right">{badge}</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"💬 Chat on WhatsApp - {feat['name']}", f"https://wa.me/{feat['phone']}?text=" + urllib.parse.quote(f"Hello {feat['name']}, I saw your {feat['item']} on K&K Market. Is it available?"))
        # Mama Oloja AI Bubble - EXACT LIKE PHOTO
        st.markdown("""
        <div style="position:relative;margin:16px 0">
        <img src="https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=100" style="width:44px;height:44px;border-radius:50%;object-fit:cover;position:absolute;left:16px;top:0">
        <div class="mama-bubble">Welcome my dear, I can help you find the best price in the market. <span style="float:right;font-size:11px;color:#666">🕐 now</span></div>
        <p style="font-size:10px;color:#22C55E;margin:2px 0 0 60px;font-weight:600">Mama Oloja AI</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🧕 Ask Mama Oloja - Find Best Price", key="ask_mama_v13"):
            if q: st.success(f"🧕 Mama: Best price for '{q}' is N{filtered[0]['price']:,} from {filtered[0]['name']} in {filtered[0]['loc']}. Check Featured above!")
            else: st.info("🧕 Mama: Type what you want in search above, e.g. Rice, Phone, Car AC - I will find best price!")

    # SWIPE + LONG SCROLL - Keep our V12 feature but in K&K style
    st.markdown("""<div class="section-head"><h2>👉 Swipe ➡️</h2><span>Swipe to see all</span></div>""", unsafe_allow_html=True)
    if len(filtered)>0:
        cards=""
        for g in filtered:
            cards+=f"""<div class="swipe-card"><img src="{g['img']}"><div class="swipe-body"><b>{g['name']}</b><p style="margin:4px 0">{g['item']}</p><p style="font-size:12px;color:#666">📍 {g['loc']}</p><p class="price">N{g['price']:,}</p></div></div>"""
        st.markdown(f"<div class='swipe-row'>{cards}</div>", unsafe_allow_html=True)

    st.markdown("""<div class="section-head"><h2>⬇️ All Products - Scroll Down</h2><span>Long Scroll</span></div>""", unsafe_allow_html=True)
    delivery_loc = st.selectbox("🚚 Your Delivery Area", ["Wuse 2, Abuja","Garki, Abuja","Gwarinpa, Abuja","Osun & Oyo","Abuja","Pickup Only"], key="delivery_loc_v13")
    payment = st.selectbox("💳 Pay with", ["Pay on Delivery (Cash)","Bank Transfer","Paystack (Card)"], key="payment_v13")
    if payment=="Bank Transfer": st.markdown(f"<div class='paybox'><b>Transfer:</b> {BANK_NAME} - {ACCOUNT_NAME} - <b>{ACCOUNT_NUMBER}</b></div>", unsafe_allow_html=True)
    if payment=="Paystack (Card)": st.link_button("💳 Pay with Paystack", PAYSTACK_LINK)
    for idx, g in enumerate(filtered):
        badge = '<span class="badge">✅ VERIFIED</span>' if g["verified"] else '<span class="badge2">New</span>'
        fee = delivery_fee(delivery_loc)
        total = g["price"] + (0 if g["price"]>=100000 else fee)
        st.markdown(f"""<div class="feed-card"><img src="{g['img']}"><div class="feed-body"><div style="display:flex;justify-content:space-between"><b>{g['name']}</b> {badge}</div><p style="margin:6px 0">{g['item']}</p><p style="font-size:12px;color:#666">📍 {g['loc']} • ⭐ 4.8</p><p class="price">N{g['price']:,} • Total N{total:,}</p></div></div>""", unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            if st.button(f"💬 Chat {g['name'][:10]}", key=f"home_chat_v13_{idx}"):
                st.session_state.page="Shop"; st.rerun()
        with c2:
            if st.button(f"⭐ Rate 5", key=f"home_rate_v13_{idx}"):
                st.session_state.ratings[g["name"]] = (5.0, 13); st.success("Thanks!")
        if st.button(f"🛒 ORDER - N{total:,}", key=f"home_order_v13_{idx}_{g['item'][:8]}"):
            if not buyer_name or not buyer_phone: st.error("⚠️ Set Your Name + WhatsApp in 'Your Details' at top first.")
            else:
                order = {"buyer":buyer_name,"buyer_phone":buyer_phone,"seller":g["name"],"seller_phone":g["phone"],"item":g["item"],"price":g["price"],"total":total,"delivery":delivery_loc,"payment":payment,"status":"Pending","time":datetime.now().strftime("%H:%M %d %b")}
                st.session_state.my_orders.append(order); st.session_state.seller_inbox.append(order)
                st.success(f"✅ Ordered! Total N{total:,}"); st.balloons()
        st.link_button(f"🔔 Notify Seller - {g['name']}", f"https://wa.me/{g['phone']}?text=" + urllib.parse.quote(f"Hello {g['name']}, Row Market 👋 NEW ORDER: {g['item']} N{g['price']:,} Total N{total:,} Delivery {delivery_loc} Payment {payment} Buyer {buyer_name} - {buyer_phone}. Reply YES/NO."))

if page == "Shop":
    st.markdown("""<div class="section-head"><h2>🛍️ Shop - All Products</h2><span>See all ›</span></div>""", unsafe_allow_html=True)
    # Reuse same feed but simpler - jump to Home feed
    st.info("Shop = Same as Home feed. Use Search + Categories on Home to filter. Tap Home below to shop.")
    if st.button("🏠 Go to Home Shop", key="shop_to_home_v13"):
        st.session_state.page="Home"; st.rerun()
    # Show orders count
    st.write(f"You have {len(st.session_state.my_orders)} orders. Check Orders tab.")

if page == "Orders":
    st.markdown("""<div class="section-head"><h2>🧾 My Orders</h2><span>Track</span></div>""", unsafe_allow_html=True)
    if len(st.session_state.my_orders)==0: st.write("No orders yet.")
    for o in st.session_state.my_orders:
        color = "🟡 Pending" if o["status"]=="Pending" else "🟢 Available" if o["status"]=="Available" else "🔴 Sold Out"
        st.markdown(f"<div class='notif'><b>{o['item']}</b> - N{o.get('total',o['price']):,}<br>Seller: {o['seller']}<br>Payment: {o.get('payment','')} | Delivery: {o.get('delivery','')}<br>Status: {color}<br>Time: {o['time']}</div>", unsafe_allow_html=True)
    st.markdown("""<div class="section-head"><h2>🔔 Seller Inbox</h2><span>For Sellers</span></div>""", unsafe_allow_html=True)
    seller_check = st.text_input("Your Seller WhatsApp", key="seller_check_v13", placeholder="2349046044472")
    if seller_check:
        inbox = [o for o in st.session_state.seller_inbox if seller_check in o["seller_phone"]]
        if len(inbox)==0: st.write("No orders yet.")
        for j,o in enumerate(inbox):
            st.markdown(f"<div class='notif'><b>🔔 NEW ORDER!</b><br>Buyer: {o['buyer']} - {o['buyer_phone']}<br>Wants: {o['item']} - N{o.get('total',o['price']):,}<br>Status: {o['status']}</div>", unsafe_allow_html=True)
            colA,colB = st.columns(2)
            with colA:
                if st.button("✅ YES", key=f"yes_v13_{j}"):
                    o["status"]="Available"
                    for mo in st.session_state.my_orders:
                        if mo["item"]==o["item"] and mo["buyer"]==o["buyer"]: mo["status"]="Available"
                    st.rerun()
            with colB:
                if st.button("❌ NO", key=f"no_v13_{j}"):
                    o["status"]="Sold Out"
                    for mo in st.session_state.my_orders:
                        if mo["item"]==o["item"] and mo["buyer"]==o["buyer"]: mo["status"]="Sold Out"
                    st.rerun()

if page == "Profile":
    st.markdown("""<div class="section-head"><h2>👤 Profile</h2><span>Edit</span></div>""", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center;padding:20px'><div style='font-size:64px'>👤</div><h3>{buyer_name or 'Guest'}</h3><p style='color:#666'>{buyer_phone or 'No number yet'}</p><p>🟢 Online • {len(st.session_state.my_orders)} Orders • {len(st.session_state.local_goods)} Products Posted</p></div>", unsafe_allow_html=True)
    st.markdown("""<div class="section-head"><h2>💬 Chat Rooms - Talk to Anyone</h2><span>Live</span></div>""", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#DCFCE7;padding:10px;border-radius:12px;margin:0 16px'>🟢 <b>{len(st.session_state.online_users)} Online:</b> {', '.join(st.session_state.online_users)}</div>", unsafe_allow_html=True)
    if st.checkbox("🔄 Auto-refresh chat", value=True, key="autorefresh_v13"):
        time.sleep(8); st.rerun()
    tab1, tab2 = st.tabs(["🌍 General", "👤 DM"])
    with tab1:
        for m in st.session_state.chat_msgs:
            if m["room"]=="General":
                cls = "chat-me" if m["user"]==buyer_name else "chatbox"
                st.markdown(f"<div class='{cls}'><b>{m['user']}</b> {m['time']}<br>{m['msg']}</div>", unsafe_allow_html=True)
        msg = st.text_input("Type message...", key="chat_general_v13")
        if st.button("📤 Send", key="send_general_v13"):
            if not buyer_name: st.error("Set Your Name in Your Details first.")
            elif msg:
                st.session_state.chat_msgs.append({"room":"General","user":buyer_name,"msg":msg,"time":datetime.now().strftime("%H:%M")}); st.rerun()
    with tab2:
        dm_with = st.selectbox("Chat with:", st.session_state.online_users, key="dm_select_v13")
        dm_room = f"DM_{dm_with}"
        for m in st.session_state.chat_msgs:
            if m["room"]==dm_room:
                cls = "chat-me" if m["user"]==buyer_name else "chatbox"
                st.markdown(f"<div class='{cls}'><b>{m['user']}</b><br>{m['msg']}</div>", unsafe_allow_html=True)
        dm_msg = st.text_input(f"DM to {dm_with}...", key="dm_msg_v13")
        if st.button(f"📤 Send DM to {dm_with}", key="send_dm_v13"):
            if not buyer_name: st.error("Set Your Name first.")
            elif dm_msg:
                st.session_state.chat_msgs.append({"room":dm_room,"user":buyer_name,"msg":dm_msg,"time":datetime.now().strftime("%H:%M")}); st.rerun()
    st.link_button("💚 Join WhatsApp Group", "https://wa.me/?text=I%20want%20to%20join%20K%26K%20Market%20Chat")

# ===== BOTTOM NAV - EXACT LIKE PHOTO =====
st.markdown("---")
nav = st.segmented_control("Nav", ["Home","Shop","Orders","Profile"], selection_mode="single", default=st.session_state.page, label_visibility="collapsed", key="nav_v13")
if nav and nav != st.session_state.page:
    st.session_state.page = nav; st.rerun()
st.markdown("""
<div style="text-align:center;font-size:11px;color:#94A3B8;margin-top:6px">🏠 Home &nbsp;•&nbsp; 🛍️ Shop &nbsp;•&nbsp; 🧾 Orders &nbsp;•&nbsp; 👤 Profile</div>
""", unsafe_allow_html=True)
st.link_button("📤 Share K&K Market on WhatsApp", "https://wa.me/?text=Check%20K%26K%20Market%20-%20Post%20FREE%2C%20Chat%20Live%2C%20Swipe%20%26%20Shop")
