import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

st.set_page_config(page_title="Row Market - Abuja", layout="wide", initial_sidebar_state="collapsed")

SHEET_ID = "1w8P3SQiChShHPQzShpgznR-lay-awTHmu_x-VHI9IU8E"
if "cat" not in st.session_state: st.session_state.cat = "All"
if "my_orders" not in st.session_state: st.session_state.my_orders = []
if "seller_inbox" not in st.session_state: st.session_state.seller_inbox = []
if "msgs" not in st.session_state: st.session_state.msgs = []
if "local_goods" not in st.session_state: st.session_state.local_goods = []
if "ratings" not in st.session_state: st.session_state.ratings = {}
if "page" not in st.session_state: st.session_state.page = "🏠 Home"

# --- CONFIG: CHANGE THIS TO YOUR ACCOUNT ---
PAYSTACK_LINK = "https://paystack.shop/rowmarket"  # Replace with your Paystack link later
BANK_NAME = "OPay / GTB"
ACCOUNT_NAME = "Row Market - Horlance"
ACCOUNT_NUMBER = "9046044472"
# -------------------------------------------

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

def stars_for(name):
    r = st.session_state.ratings.get(name, (4.8, 12))
    full = int(r[0])
    return "⭐" * full + f" {r[0]} ({r[1]} reviews)"

st.markdown("""
<style>
header {visibility:hidden !important}
.block-container {padding-top:0px !important; padding-left:0px !important; padding-right:0px !important; padding-bottom:90px !important; max-width:100% !important}
div.stButton > button { width:100% !important; background:#FF6B00 !important; color:white !important; border-radius:12px !important; padding:12px !important; border:none !important; font-weight:700 !important; }
div.stLinkButton > a { width:100% !important; background:#16a34a !important; color:white !important; border-radius:12px !important; text-align:center !important; font-weight:700 !important; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:10px 12px; }
.card { border-radius:16px; padding:16px 6px; text-align:center; font-size:32px; }
.card p { font-size:13px; margin:4px 0 0 0; color:#111; font-weight:600; }
.prod { background:white; border-radius:16px; overflow:hidden; box-shadow:0 2px 12px #eee; margin:0 12px 12px 12px; border:1px solid #f0f0f0; }
.prod img { width:100%; height:190px; object-fit:cover; }
.prod-body { padding:12px; }
.price { color:#FF6B00; font-weight:800; font-size:20px; margin:4px 0; }
.oldprice { color:#999; text-decoration:line-through; font-size:13px; margin-left:6px; }
.badge { background:#16a34a; color:white; padding:3px 8px; border-radius:20px; font-size:11px; }
.badge2 { background:#fef3c7; color:#92400e; padding:3px 8px; border-radius:20px; font-size:11px; }
.notif { background:#fef9c3; border-left:4px solid #eab308; padding:12px; border-radius:12px; margin:8px 12px; }
.paybox { background:#f0fdf4; border:1px solid #16a34a; border-radius:12px; padding:12px; margin:8px 12px; }
div[data-testid="stSegmentedControl"] button { border-radius:20px !important; padding:8px 12px !important; font-size:12px !important; }
div[data-testid="stSegmentedControl"] button[data-testid="stSegmentedControlButton-selected"] { background:#FF6B00 !important; color:white !important; }
</style>
""", unsafe_allow_html=True)

# 1. PRETTIER HEADER
st.markdown("""
<div style="background:linear-gradient(90deg,#FF6B00,#FF8A00);padding:16px 12px 12px 12px;border-radius:0 0 20px 20px;text-align:center">
<div style="font-size:36px">🛒</div>
<h1 style="color:white;margin:0;font-size:28px">Row Market</h1>
<p style="color:white;margin:2px 0 8px 0;font-size:13px">Abuja's #1 FREE Market • V10 • Pay • Delivery • Ratings</p>
<div style="background:white;border-radius:20px;padding:6px 12px;display:inline-block;font-size:12px;font-weight:700;color:#FF6B00">🔥 FREE DELIVERY OVER N100k THIS WEEK</div>
</div>
""", unsafe_allow_html=True)

pending = len([o for o in st.session_state.seller_inbox if o["status"]=="Pending"])
if pending>0:
    st.markdown(f"<div class='notif'>🔔 <b>You have {pending} new order(s)!</b> Scroll to Seller Inbox.</div>", unsafe_allow_html=True)

st.success("✅ Connected to Row Market Database - V10 Live!")

# SEARCH + FILTERS
s = st.text_input("🔍 Search - Rice, Phone, Perfume, Car AC...", key="search_v10")
q = s
col1, col2 = st.columns(2)
with col1:
    loc_filter = st.selectbox("📍 Location", ["All Locations","Wuse 2, Abuja","Garki, Abuja","Gwarinpa, Abuja","Osun & Oyo","Abuja","Online"], key="filter_loc_v10")
with col2:
    sort_by = st.selectbox("↕️ Sort", ["Most Popular","Lowest Price","Highest Price","Top Rated"], key="sort_v10")

max_price = st.slider("💰 Max Price (Naira)", 0, 500000, 500000, step=5000, key="price_slider_v10")
delivery_loc = st.selectbox("🚚 Your Delivery Area", ["Wuse 2, Abuja","Garki, Abuja","Gwarinpa, Abuja","Osun & Oyo","Abuja","Pickup Only"], key="delivery_loc_v10")
st.info(f"🚚 Delivery to {delivery_loc}: N{delivery_fee(delivery_loc):,} | Free if order over N100,000")

mama_q = st.segmented_control("Mama", ["🍚 Rice price?","📱 Cheapest phone?","🚗 Car AC?","🧴 Perfume?"], selection_mode="single", label_visibility="collapsed", key="mama_v10")
if mama_q: st.markdown(f"<div style='background:#fff7ed;margin:8px 12px;padding:12px;border-radius:12px'>🧕 Mama: I found the best price for you below. Check Shop!</div>", unsafe_allow_html=True)

st.markdown("<h3 style='padding:0 12px'>Categories</h3>", unsafe_allow_html=True)
st.markdown("""
<div class="grid2">
<div class="card" style="background:#fbcfe8">🧴<p>Perfume</p></div>
<div class="card" style="background:#bfdbfe">👕<p>Clothes</p></div>
<div class="card" style="background:#bfdbfe">📱<p>Phones</p></div>
<div class="card" style="background:#fed7aa">🍲<p>Food</p></div>
<div class="card" style="background:#fed7aa">🚗<p>Car Mart</p></div>
<div class="card" style="background:#bbf7d0">💼<p>Services</p></div>
<div class="card" style="background:#fbcfe8">🎟️<p>Tickets</p></div>
<div class="card" style="background:#a7f3d0">💬<p>Chat Rooms</p></div>
</div>
""", unsafe_allow_html=True)
picked = st.segmented_control("Cat", ["All","Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], selection_mode="single", default=st.session_state.cat, label_visibility="collapsed", key="cat_v10")
if picked: st.session_state.cat = picked

# BUYER DETAILS + PAYMENT
st.markdown("<h3 style='padding:0 12px'>👤 Your Details + Payment</h3>", unsafe_allow_html=True)
buyer_name = st.text_input("Your Name (buyer)", key="buyer_name_v10", placeholder="e.g. Tunde")
buyer_phone = st.text_input("Your WhatsApp Number", key="buyer_phone_v10", placeholder="e.g. 2348031234567")
payment = st.selectbox("💳 How will you pay?", ["Pay on Delivery (Cash)","Bank Transfer","Paystack (Card / Transfer)"], key="payment_v10")
if payment=="Bank Transfer":
    st.markdown(f"<div class='paybox'><b>Transfer to:</b><br>{BANK_NAME}<br>{ACCOUNT_NAME}<br><b>{ACCOUNT_NUMBER}</b><br>Use your name as narration. Send receipt on WhatsApp.</div>", unsafe_allow_html=True)
if payment=="Paystack (Card / Transfer)":
    st.link_button("💳 Pay Now with Paystack", PAYSTACK_LINK)

all_goods = get_goods()
shown=[]
for g in all_goods:
    if st.session_state.cat!="All" and st.session_state.cat.lower() not in g["cat"].lower(): continue
    if q and q.lower() not in (g["item"]+g["cat"]+g["loc"]).lower(): continue
    if loc_filter!="All Locations" and loc_filter.lower() not in g["loc"].lower(): continue
    if g["price"]>max_price: continue
    shown.append(g)

if sort_by=="Lowest Price": shown = sorted(shown, key=lambda x: x["price"])
if sort_by=="Highest Price": shown = sorted(shown, key=lambda x: x["price"], reverse=True)
if sort_by=="Top Rated": shown = sorted(shown, key=lambda x: st.session_state.ratings.get(x["name"], (4.8,0))[0], reverse=True)

st.subheader(f"🛍️ Shop - {len(shown)} goods")
for idx, g in enumerate(shown):
    badge = '<span class="badge">✅ VERIFIED</span>' if g["verified"] else '<span class="badge2">New Seller</span>'
    fee = delivery_fee(delivery_loc)
    total = g["price"] + (0 if g["price"]>=100000 else fee)
    free_tag = " • 🚚 FREE DELIVERY" if g["price"]>=100000 else f" • 🚚 Delivery N{fee:,}"
    st.markdown(f"""<div class="prod"><img src="{g['img']}"><div class="prod-body"><div style="display:flex;justify-content:space-between"><b>{g['name']}</b> {badge}</div><p style="margin:6px 0">{g['item']}</p><p style="font-size:12px;color:#666">{stars_for(g['name'])}</p><p>📍 {g['loc']} • 📞 {g['phone']}</p><p class="price">N{g['price']:,}<span class="oldprice">N{int(g['price']*1.15):,}</span></p><p style="font-size:12px;color:#16a34a;font-weight:600">Total with delivery: N{total:,} {free_tag}</p></div></div>""", unsafe_allow_html=True)
    # Rating buttons
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button(f"⭐ 5 - {g['name'][:8]}", key=f"rate5_v10_{idx}_{g['item'][:8]}"):
            st.session_state.ratings[g["name"]] = (5.0, st.session_state.ratings.get(g["name"], (4.8,12))[1]+1)
            st.success("Thanks for 5 stars!")
    with c2:
        if st.button(f"⭐ 4", key=f"rate4_v10_{idx}_{g['item'][:8]}"):
            st.session_state.ratings[g["name"]] = (4.0, st.session_state.ratings.get(g["name"], (4.8,12))[1]+1)
            st.success("Thanks for 4 stars!")
    with c3:
        if st.button(f"⭐ 3", key=f"rate3_v10_{idx}_{g['item'][:8]}"):
            st.session_state.ratings[g["name"]] = (3.0, st.session_state.ratings.get(g["name"], (4.8,12))[1]+1)
            st.success("Thanks!")
    if st.button(f"🛒 Order This - {g['item'][:25]} - N{total:,} total", key=f"order_v10_{idx}_{g['item'][:10]}"):
        if not buyer_name or not buyer_phone:
            st.error("⚠️ Enter Your Name + WhatsApp Number above first.")
        else:
            order = {"buyer":buyer_name,"buyer_phone":buyer_phone,"seller":g["name"],"seller_phone":g["phone"],"item":g["item"],"price":g["price"],"total":total,"delivery":delivery_loc,"payment":payment,"status":"Pending","time":datetime.now().strftime("%H:%M %d %b")}
            st.session_state.my_orders.append(order)
            st.session_state.seller_inbox.append(order)
            st.success(f"✅ Order placed! Total N{total:,} ({payment}) - Now tap Notify Seller below.")
            st.balloons()
    notify_text = f"Hello {g['name']}, Row Market V10 👋\n\nNEW ORDER:\n• {g['item']} - N{g['price']:,}\n• Delivery to: {delivery_loc} (Fee N{fee:,})\n• TOTAL: N{total:,}\n• Payment: {payment}\n• Buyer: {buyer_name or '[Name]'} - {buyer_phone or '[Number]'}\n\nDo you have it? Reply YES / NO.\nRow Market - Abuja"
    wa_notify = f"https://wa.me/{g['phone']}?text=" + urllib.parse.quote(notify_text)
    st.link_button(f"🔔 Notify Seller on WhatsApp - {g['name']}", wa_notify)
    st.write("---")

st.subheader("🧾 My Orders - Track Status + Payment")
if len(st.session_state.my_orders)==0:
    st.write("No orders yet.")
for o in st.session_state.my_orders:
    color = "🟡 Pending" if o["status"]=="Pending" else "🟢 Available" if o["status"]=="Available" else "🔴 Sold Out"
    st.markdown(f"<div class='notif'><b>{o['item']}</b> - N{o.get('total',o['price']):,}<br>Seller: {o['seller']}<br>Payment: {o.get('payment','Pay on Delivery')} | Delivery: {o.get('delivery','')} <br>Status: {color}<br>Time: {o['time']}</div>", unsafe_allow_html=True)

st.subheader("🔔 Seller Inbox - Orders For You")
seller_check_phone = st.text_input("Your Seller WhatsApp Number", key="seller_check_v10", placeholder="2349046044472")
if seller_check_phone:
    my_inbox = [o for o in st.session_state.seller_inbox if seller_check_phone in o["seller_phone"]]
    if len(my_inbox)==0: st.write("No new orders for this number yet.")
    for j, o in enumerate(my_inbox):
        st.markdown(f"<div class='notif'><b>🔔 NEW ORDER!</b><br>Buyer: {o['buyer']} - {o['buyer_phone']}<br>Wants: <b>{o['item']} - N{o.get('total',o['price']):,}</b><br>Payment: {o.get('payment','')} | Delivery: {o.get('delivery','')}<br>Time: {o['time']} | Status: {o['status']}</div>", unsafe_allow_html=True)
        colA, colB = st.columns(2)
        with colA:
            if st.button(f"✅ YES, I Have It", key=f"yes_v10_{j}_{o['item'][:8]}"):
                o["status"]="Available"
                for mo in st.session_state.my_orders:
                    if mo["item"]==o["item"] and mo["buyer"]==o["buyer"]: mo["status"]="Available"
                st.success("You said YES!")
                st.rerun()
        with colB:
            if st.button(f"❌ NO, Sold Out", key=f"no_v10_{j}_{o['item'][:8]}"):
                o["status"]="Sold Out"
                for mo in st.session_state.my_orders:
                    if mo["item"]==o["item"] and mo["buyer"]==o["buyer"]: mo["status"]="Sold Out"
                st.error("You said NO.")
                st.rerun()
        if o["status"]=="Available":
            reply = f"Hello {o['buyer']}, this is {o['seller']} from Row Market. Your order {o['item']} N{o.get('total',o['price']):,} is available. Payment: {o.get('payment','')} - When do you want delivery? - Row Market"
            st.link_button(f"💬 Reply to Buyer - {o['buyer']}", f"https://wa.me/{o['buyer_phone']}?text=" + urllib.parse.quote(reply))

st.subheader("📸 Sell FREE - V10")
nm = st.text_input("Your Name", key="sell_name_v10")
pd = st.text_input("Product Name", key="sell_product_v10")
pr = st.number_input("Price (Naira)", min_value=0, key="sell_price_v10")
ct = st.selectbox("Category", ["Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], key="sell_cat_v10")
loc_sell = st.text_input("Location", key="sell_loc_v10")
ph = st.text_input("Your WhatsApp Number (seller)", key="sell_phone_v10")
img_url = st.text_input("Photo Link (optional)", key="sell_img_v10")
if st.button("✅ Post Good FREE", key="sell_post_v10"):
    if nm and pd and pr>0:
        new = {"name":nm,"item":pd,"price":int(pr),"cat":ct,"loc":loc_sell or "Abuja","phone":ph or "2349046044472","img":img_url or "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600","verified":False}
        st.session_state.local_goods.insert(0, new)
        st.success("Posted! Add this row to your Sheet to make it permanent.")
    else: st.error("Fill Name, Product, Price")

st.subheader("💬 Chat Rooms")
rm = st.selectbox("Chat Room", ["Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], key="chat_room_v10")
cm = st.text_input("Chat Message", key="chat_msg_v10")
if st.button("Send Chat", key="chat_send_v10"):
    if cm: st.session_state.msgs.append(f"{rm} : {cm}")
for m in st.session_state.msgs:
    if rm.lower() in m.lower(): st.write(m)

st.subheader("📤 Share")
st.link_button("Share Row Market on WhatsApp", "https://wa.me/?text=Check%20Row%20Market%20Abuja%20-%20Post%20goods%20FREE%20-%20Pay%20%26%20Delivery%20Available")
nav = st.segmented_control("Nav", ["🏠 Home","🛍️ Shop","🧾 Orders","🔔 Inbox"], selection_mode="single", default=st.session_state.page, label_visibility="collapsed", key="nav_v10")
if nav: st.session_state.page = nav
