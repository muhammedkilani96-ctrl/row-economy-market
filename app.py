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
if "page" not in st.session_state: st.session_state.page = "🛍️ Feed"
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
        goods = [{"name":"Mama Ada","item":"Bag of Rice 50kg","price":85000,"cat":"Food","loc":"Wuse 2, Abuja","img":"https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600","phone":"2349046044472","verified":True}]
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
.block-container {padding-top:0px !important; padding-left:0px !important; padding-right:0px !important; padding-bottom:110px !important; max-width:100% !important}
div.stButton > button { width:100% !important; background:#FF6B00 !important; color:white !important; border-radius:14px !important; padding:14px !important; border:none !important; font-weight:700 !important; font-size:15px !important; }
div.stLinkButton > a { width:100% !important; background:#16a34a !important; color:white !important; border-radius:14px !important; text-align:center !important; font-weight:700 !important; }
/* SWIPE CAROUSEL - horizontal scroll */
.swipe-row { display:flex; overflow-x:auto; scroll-snap-type:x mandatory; gap:12px; padding:12px; -webkit-overflow-scrolling:touch; scrollbar-width:none; }
.swipe-row::-webkit-scrollbar { display:none; }
.swipe-card { min-width:78vw; max-width:78vw; scroll-snap-align:center; background:white; border-radius:20px; overflow:hidden; box-shadow:0 4px 20px #ddd; flex-shrink:0; }
.swipe-card img { width:100%; height:260px; object-fit:cover; }
.swipe-card-body { padding:14px; }
/* LONG FEED CARD - full width, tall */
.feed-card { background:white; border-radius:20px; overflow:hidden; box-shadow:0 4px 20px #eee; margin:0 12px 20px 12px; border:1px solid #f0f0f0; }
.feed-card img { width:100%; height:340px; object-fit:cover; }
.feed-body { padding:16px; }
.price { color:#FF6B00; font-weight:800; font-size:22px; margin:4px 0; }
.badge { background:#16a34a; color:white; padding:3px 8px; border-radius:20px; font-size:11px; }
.badge2 { background:#fef3c7; color:#92400e; padding:3px 8px; border-radius:20px; font-size:11px; }
.notif { background:#fef9c3; border-left:4px solid #eab308; padding:12px; border-radius:12px; margin:8px 12px; }
.paybox { background:#f0fdf4; border:1px solid #16a34a; border-radius:12px; padding:12px; margin:8px 12px; }
.chatbox { background:#f8fafc; border-radius:12px; padding:10px; margin:6px 12px; border:1px solid #e2e8f0; }
.chat-me { background:#dcfce7; border-radius:12px; padding:10px; margin:6px 12px; text-align:right; }
.post-box { background:linear-gradient(135deg,#FFF7ED,#FFEDD5); border:2px dashed #FF6B00; border-radius:20px; padding:16px; margin:12px; }
div[data-testid="stSegmentedControl"] button { border-radius:20px !important; padding:8px 12px !important; font-size:12px !important; }
div[data-testid="stSegmentedControl"] button[data-testid="stSegmentedControlButton-selected"] { background:#FF6B00 !important; color:white !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:linear-gradient(90deg,#FF6B00,#FF8A00);padding:16px 12px 12px 12px;border-radius:0 0 20px 20px;text-align:center;position:sticky;top:0;z-index:999">
<div style="font-size:32px">🛒</div>
<h1 style="color:white;margin:0;font-size:26px">Row Market</h1>
<p style="color:white;margin:2px 0 0 0;font-size:12px">Swipe ➡️ • Scroll Down ⬇️ • Post FREE • V12</p>
</div>
""", unsafe_allow_html=True)

pending = len([o for o in st.session_state.seller_inbox if o["status"]=="Pending"])
if pending>0:
    st.markdown(f"<div class='notif'>🔔 <b>You have {pending} new order(s)!</b> Tap Inbox below.</div>", unsafe_allow_html=True)

my_name_input = st.text_input("👤 Your Name (for Chat, Orders & Posting)", value=st.session_state.my_name, key="my_name_v12", placeholder="e.g. Tunde")
if my_name_input and my_name_input != st.session_state.my_name:
    st.session_state.my_name = my_name_input
    if my_name_input not in st.session_state.online_users: st.session_state.online_users.append(my_name_input)
buyer_name = st.session_state.my_name
buyer_phone = st.text_input("📱 Your WhatsApp Number", key="buyer_phone_v12", placeholder="e.g. 2348031234567")

page = st.session_state.page

# ================= FEED PAGE - SWIPE + LONG SCROLL + POST =================
if page == "🛍️ Feed":
    # --- 1. POST YOUR PRODUCT - TOP, BIG, ALWAYS VISIBLE ---
    st.markdown("""
    <div class="post-box">
    <h3 style="margin:0">📸 POST YOUR PRODUCT - FREE</h3>
    <p style="margin:4px 0 0 0;font-size:13px;color:#666">Post in 10 secs. It appears instantly in Swipe + Feed below. 👇 Fill below.</p>
    </div>
    """, unsafe_allow_html=True)
    with st.expander("➕ TAP HERE TO POST YOUR PRODUCT - FREE", expanded=False):
        p_name = st.text_input("Your Name", value=buyer_name, key="post_name_v12")
        p_item = st.text_input("What are you selling? e.g. Bag of Rice 50kg", key="post_item_v12")
        p_price = st.number_input("Price (Naira)", min_value=0, key="post_price_v12")
        p_cat = st.selectbox("Category", ["Food","Phones","Perfume","Clothes","Car","Services","Tickets","Chat"], key="post_cat_v12")
        p_loc = st.text_input("Location e.g. Wuse 2, Abuja", key="post_loc_v12")
        p_phone = st.text_input("Your WhatsApp Number (seller)", value=buyer_phone, key="post_phone_v12")
        p_img = st.text_input("Photo Link (paste Unsplash / any image link, or leave empty)", key="post_img_v12", placeholder="https://...")
        st.caption("No photo? Leave empty - we use a default shop photo.")
        if st.button("🚀 POST NOW - Show in Feed Instantly", key="post_now_v12"):
            if p_name and p_item and p_price>0:
                new = {"name":p_name,"item":p_item,"price":int(p_price),"cat":p_cat,"loc":p_loc or "Abuja","phone":p_phone or "2349046044472","img":p_img or "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600","verified":False}
                st.session_state.local_goods.insert(0, new)
                st.success(f"✅ Posted! '{p_item}' is now LIVE at top of Swipe + Feed! Scroll down to see it.")
                st.balloons()
            else: st.error("Fill Name, Product, Price")
        st.info("💡 To make it PERMANENT, also add same row to your Google Sheet. Temporary posts disappear on reboot, Sheet posts stay forever.")

    # --- 2. SEARCH + FILTERS ---
    s = st.text_input("🔍 Search - Rice, Phone, Perfume...", key="search_v12")
    q = s
    col1, col2 = st.columns(2)
    with col1: loc_filter = st.selectbox("📍 Location", ["All Locations","Wuse 2, Abuja","Garki, Abuja","Gwarinpa, Abuja","Osun & Oyo","Abuja","Online"], key="filter_loc_v12")
    with col2: sort_by = st.selectbox("↕️ Sort", ["Newest First","Lowest Price","Highest Price"], key="sort_v12")
    max_price = st.slider("💰 Max Price", 0, 500000, 500000, step=5000, key="price_slider_v12")
    delivery_loc = st.selectbox("🚚 Your Delivery Area", ["Wuse 2, Abuja","Garki, Abuja","Gwarinpa, Abuja","Osun & Oyo","Abuja","Pickup Only"], key="delivery_loc_v12")
    payment = st.selectbox("💳 Pay with", ["Pay on Delivery (Cash)","Bank Transfer","Paystack (Card)"], key="payment_v12")
    if payment=="Bank Transfer": st.markdown(f"<div class='paybox'><b>Transfer:</b> {BANK_NAME} - {ACCOUNT_NAME} - <b>{ACCOUNT_NUMBER}</b></div>", unsafe_allow_html=True)
    if payment=="Paystack (Card)": st.link_button("💳 Pay with Paystack", PAYSTACK_LINK)
    cat_pick = st.segmented_control("Cat", ["All","Food","Phones","Perfume","Clothes","Car","Services","Tickets"], selection_mode="single", default="All", label_visibility="collapsed", key="cat_v12")

    all_goods = get_goods()
    shown=[]
    for g in all_goods:
        if cat_pick!="All" and cat_pick.lower() not in g["cat"].lower(): continue
        if q and q.lower() not in (g["item"]+g["cat"]+g["loc"]).lower(): continue
        if loc_filter!="All Locations" and loc_filter.lower() not in g["loc"].lower(): continue
        if g["price"]>max_price: continue
        shown.append(g)
    if sort_by=="Lowest Price": shown = sorted(shown, key=lambda x: x["price"])
    if sort_by=="Highest Price": shown = sorted(shown, key=lambda x: x["price"], reverse=True)

    # --- 3. SWIPE CAROUSEL - SWIPE LEFT/RIGHT ---
    st.markdown(f"<h3 style='padding:0 12px'>👉 SWIPE ➡️ - {len(shown)} Products - Swipe to see all</h3>", unsafe_allow_html=True)
    st.markdown("<p style='padding:0 12px;font-size:12px;color:#666;margin-top:-8px'>👆 Put finger on card, drag left / right like Instagram</p>", unsafe_allow_html=True)
    if len(shown)>0:
        cards_html = ""
        for g in shown:
            badge = '<span class="badge">✅ VERIFIED</span>' if g["verified"] else '<span class="badge2">New</span>'
            fee = delivery_fee(delivery_loc)
            total = g["price"] + (0 if g["price"]>=100000 else fee)
            cards_html += f"""<div class="swipe-card"><img src="{g['img']}"><div class="swipe-card-body"><div style="display:flex;justify-content:space-between"><b>{g['name']}</b> {badge}</div><p style="margin:6px 0;font-weight:600">{g['item']}</p><p style="font-size:12px;color:#666">📍 {g['loc']}</p><p class="price">N{g['price']:,} • Total N{total:,}</p><p style="font-size:12px;color:#16a34a">⬇️ Scroll down to Order This</p></div></div>"""
        st.markdown(f"<div class='swipe-row'>{cards_html}</div>", unsafe_allow_html=True)
    else:
        st.write("No products in this filter. Try All.")

    # --- 4. LONG SCROLL FEED - SCROLL DOWN FOREVER ---
    st.markdown("<h3 style='padding:0 12px'>⬇️ LONG SCROLL FEED - Scroll Down, Order Any</h3>", unsafe_allow_html=True)
    st.markdown("<p style='padding:0 12px;font-size:12px;color:#666;margin-top:-8px'>Like TikTok - Keep scrolling, each product is big & full</p>", unsafe_allow_html=True)
    for idx, g in enumerate(shown):
        badge = '<span class="badge">✅ VERIFIED</span>' if g["verified"] else '<span class="badge2">New Seller</span>'
        fee = delivery_fee(delivery_loc)
        total = g["price"] + (0 if g["price"]>=100000 else fee)
        st.markdown(f"""<div class="feed-card"><img src="{g['img']}"><div class="feed-body"><div style="display:flex;justify-content:space-between"><b style="font-size:16px">{g['name']}</b> {badge}</div><p style="margin:8px 0;font-size:16px">{g['item']}</p><p style="font-size:13px;color:#666">📍 {g['loc']} • 📞 {g['phone']} • ⭐ 4.8 (12)</p><p class="price">N{g['price']:,} <span style="font-size:13px;color:#999;text-decoration:line-through">N{int(g['price']*1.15):,}</span></p><p style="font-size:13px;color:#16a34a;font-weight:700">🚚 Delivery N{fee:,} • TOTAL N{total:,} • {payment}</p></div></div>""", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            if st.button(f"💬 Chat {g['name'][:10]}", key=f"feed_chat_v12_{idx}"):
                st.session_state.page="💬 Chat"; st.rerun()
        with c2:
            if st.button(f"⭐ Rate 5", key=f"feed_rate_v12_{idx}"):
                st.session_state.ratings[g["name"]] = (5.0, 13); st.success("Thanks for 5 stars!")
        if st.button(f"🛒 ORDER THIS - N{total:,} total", key=f"feed_order_v12_{idx}_{g['item'][:10]}"):
            if not buyer_name or not buyer_phone: st.error("⚠️ Enter Your Name + WhatsApp at top first.")
            else:
                order = {"buyer":buyer_name,"buyer_phone":buyer_phone,"seller":g["name"],"seller_phone":g["phone"],"item":g["item"],"price":g["price"],"total":total,"delivery":delivery_loc,"payment":payment,"status":"Pending","time":datetime.now().strftime("%H:%M %d %b")}
                st.session_state.my_orders.append(order); st.session_state.seller_inbox.append(order)
                st.success(f"✅ Ordered! Total N{total:,} ({payment})"); st.balloons()
        notify_text = f"Hello {g['name']}, Row Market V12 👋\n\nNEW ORDER:\n• {g['item']} - N{g['price']:,}\n• Delivery: {delivery_loc} (N{fee:,}) TOTAL N{total:,}\n• Payment: {payment}\n• Buyer: {buyer_name or '[Name]'} - {buyer_phone or '[Number]'}\n\nReply YES / NO.\nRow Market"
        st.link_button(f"🔔 Notify Seller on WhatsApp - {g['name']}", f"https://wa.me/{g['phone']}?text=" + urllib.parse.quote(notify_text))
        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;padding:20px;color:#999'>🎉 You've seen all products<br>Post yours above to appear here!</div>", unsafe_allow_html=True)

if page == "🧾 Orders":
    st.subheader("🧾 My Orders")
    if len(st.session_state.my_orders)==0: st.write("No orders yet. Go to Feed and order.")
    for o in st.session_state.my_orders:
        color = "🟡 Pending" if o["status"]=="Pending" else "🟢 Available" if o["status"]=="Available" else "🔴 Sold Out"
        st.markdown(f"<div class='notif'><b>{o['item']}</b> - N{o.get('total',o['price']):,}<br>Seller: {o['seller']}<br>Payment: {o.get('payment','')} | Delivery: {o.get('delivery','')}<br>Status: {color}<br>Time: {o['time']}</div>", unsafe_allow_html=True)

if page == "🔔 Inbox":
    st.subheader("🔔 Seller Inbox")
    seller_check_phone = st.text_input("Your Seller WhatsApp Number", key="seller_check_v12", placeholder="2349046044472")
    if seller_check_phone:
        my_inbox = [o for o in st.session_state.seller_inbox if seller_check_phone in o["seller_phone"]]
        if len(my_inbox)==0: st.write("No new orders for this number yet.")
        for j, o in enumerate(my_inbox):
            st.markdown(f"<div class='notif'><b>🔔 NEW ORDER!</b><br>Buyer: {o['buyer']} - {o['buyer_phone']}<br>Wants: <b>{o['item']} - N{o.get('total',o['price']):,}</b><br>Payment: {o.get('payment','')} | Delivery: {o.get('delivery','')}<br>Time: {o['time']} | Status: {o['status']}</div>", unsafe_allow_html=True)
            colA, colB = st.columns(2)
            with colA:
                if st.button(f"✅ YES, I Have It", key=f"yes_v12_{j}_{o['item'][:8]}"):
                    o["status"]="Available"
                    for mo in st.session_state.my_orders:
                        if mo["item"]==o["item"] and mo["buyer"]==o["buyer"]: mo["status"]="Available"
                    st.success("You said YES!"); st.rerun()
            with colB:
                if st.button(f"❌ NO, Sold Out", key=f"no_v12_{j}_{o['item'][:8]}"):
                    o["status"]="Sold Out"
                    for mo in st.session_state.my_orders:
                        if mo["item"]==o["item"] and mo["buyer"]==o["buyer"]: mo["status"]="Sold Out"
                    st.error("You said NO."); st.rerun()

if page == "💬 Chat":
    st.subheader("💬 Live Chat - Talk to Anyone Online")
    st.markdown(f"<div style='background:#dcfce7;padding:10px;border-radius:12px;margin:0 12px'>🟢 <b>{len(st.session_state.online_users)} Online:</b> {', '.join(st.session_state.online_users)}<br>You are: <b>{buyer_name or 'Guest'}</b></div>", unsafe_allow_html=True)
    if st.checkbox("🔄 Auto-refresh chat", value=True, key="autorefresh_v12"):
        time.sleep(8); st.rerun()
    tab1, tab2 = st.tabs(["🌍 General Chat", "👤 DM Private"])
    with tab1:
        for m in st.session_state.chat_msgs:
            if m["room"]=="General":
                cls = "chat-me" if m["user"]==buyer_name else "chatbox"
                st.markdown(f"<div class='{cls}'><b>{m['user']}</b> <span style='font-size:11px'>{m['time']}</span><br>{m['msg']}</div>", unsafe_allow_html=True)
        msg = st.text_input("Type message...", key="chat_general_v12")
        if st.button("📤 Send to General", key="send_general_v12"):
            if not buyer_name: st.error("Enter Your Name at top first.")
            elif msg:
                st.session_state.chat_msgs.append({"room":"General","user":buyer_name,"msg":msg,"time":datetime.now().strftime("%H:%M")}); st.rerun()
    with tab2:
        dm_with = st.selectbox("Chat with:", st.session_state.online_users, key="dm_select_v12")
        dm_room = f"DM_{dm_with}"
        for m in st.session_state.chat_msgs:
            if m["room"]==dm_room:
                cls = "chat-me" if m["user"]==buyer_name else "chatbox"
                st.markdown(f"<div class='{cls}'><b>{m['user']}</b> <span style='font-size:11px'>{m['time']}</span><br>{m['msg']}</div>", unsafe_allow_html=True)
        dm_msg = st.text_input(f"DM to {dm_with}...", key="dm_msg_v12")
        if st.button(f"📤 Send DM to {dm_with}", key="send_dm_v12"):
            if not buyer_name: st.error("Enter Your Name at top first.")
            elif dm_msg:
                st.session_state.chat_msgs.append({"room":dm_room,"user":buyer_name,"msg":dm_msg,"time":datetime.now().strftime("%H:%M")}); st.rerun()

# ===== BOTTOM NAV - WORKS =====
st.markdown("---")
nav = st.segmented_control("Nav", ["🛍️ Feed","🧾 Orders","🔔 Inbox","💬 Chat"], selection_mode="single", default=st.session_state.page, label_visibility="collapsed", key="nav_v12")
if nav and nav != st.session_state.page:
    st.session_state.page = nav; st.rerun()
st.link_button("📤 Share Row Market on WhatsApp", "https://wa.me/?text=Check%20Row%20Market%20Abuja%20-%20Swipe%2C%20Post%20FREE%2C%20Chat%20Live")
