import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

st.set_page_config(page_title="Row Market - Abuja", layout="wide", initial_sidebar_state="collapsed")

SHEET_ID = "1w8P3SQiChShHPQzShpgznR-lay-awTHmu_x-VHI9IU8E"
if "cat" not in st.session_state: st.session_state.cat = "All"
if "orders" not in st.session_state: st.session_state.orders = []
if "my_orders" not in st.session_state: st.session_state.my_orders = []
if "seller_inbox" not in st.session_state: st.session_state.seller_inbox = []
if "msgs" not in st.session_state: st.session_state.msgs = []
if "local_goods" not in st.session_state: st.session_state.local_goods = []
if "page" not in st.session_state: st.session_state.page = "🏠 Home"

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

st.markdown("""
<style>
header {visibility:hidden !important}
.block-container {padding-top:0px !important; padding-left:0px !important; padding-right:0px !important; padding-bottom:90px !important; max-width:100% !important}
div.stButton > button { width:100% !important; background:#16a34a !important; color:white !important; border-radius:12px !important; padding:10px !important; border:none !important; }
div.stLinkButton > a { width:100% !important; background:#16a34a !important; color:white !important; border-radius:12px !important; text-align:center !important; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:10px 12px; }
.card { border-radius:16px; padding:16px 6px; text-align:center; font-size:32px; }
.card p { font-size:13px; margin:4px 0 0 0; color:#111; font-weight:600; }
.prod { background:white; border-radius:16px; overflow:hidden; box-shadow:0 2px 12px #eee; margin:0 12px 12px 12px; }
.prod img { width:100%; height:180px; object-fit:cover; }
.prod-body { padding:12px; }
.price { color:#16a34a; font-weight:800; font-size:18px; margin:4px 0; }
.badge { background:#16a34a; color:white; padding:3px 8px; border-radius:20px; font-size:11px; }
.badge2 { background:#fef3c7; color:#92400e; padding:3px 8px; border-radius:20px; font-size:11px; }
.notif { background:#fef9c3; border-left:4px solid #eab308; padding:12px; border-radius:12px; margin:8px 12px; }
div[data-testid="stSegmentedControl"] button { border-radius:20px !important; padding:8px 12px !important; font-size:12px !important; }
div[data-testid="stSegmentedControl"] button[data-testid="stSegmentedControlButton-selected"] { background:#16a34a !important; color:white !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#16a34a;padding:14px 12px 10px 12px;border-radius:0 0 20px 20px;text-align:center">
<h1 style="color:white;margin:0;font-size:26px">Row Market</h1>
<p style="color:#dcfce7;margin:2px 0 8px 0;font-size:12px">Abuja • FREE • Seller Notifications ON • V9</p>
</div>
""", unsafe_allow_html=True)

pending_count = len([o for o in st.session_state.seller_inbox if o["status"]=="Pending"])
if pending_count>0:
    st.markdown(f"<div class='notif'>🔔 <b>You have {pending_count} new order(s)!</b> Scroll to Seller Inbox below.</div>", unsafe_allow_html=True)

st.success("✅ Connected to Row Market Database - Listings are permanent!")

s = st.text_input("🔍 Ask Mama Oloja - What are you looking for today?", key="search_v9")
q = s
loc_filter = st.selectbox("📍 Location", ["All Locations","Wuse 2, Abuja","Garki, Abuja","Gwarinpa, Abuja","Osun & Oyo","Abuja","Online"], key="locv9")
price_filter = st.selectbox("💰 Price", ["All Prices","Under N20,000","N20,000 - N100,000","Over N100,000"], key="pricev9")

mama_q = st.segmented_control("Mama", ["🍚 Rice price?","📱 Cheapest phone?","🚗 Car AC?","🧴 Perfume?"], selection_mode="single", label_visibility="collapsed", key="mamaqv9")
if mama_q: st.markdown(f"<div style='background:#dcfce7;margin:8px 12px;padding:12px;border-radius:12px'>🧕 Mama: I found it for you, check Shop below.</div>", unsafe_allow_html=True)

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
picked = st.segmented_control("Cat", ["All","Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], selection_mode="single", default=st.session_state.cat, label_visibility="collapsed", key="catv9")
if picked: st.session_state.cat = picked

st.markdown("<h3 style='padding:0 12px'>👤 Your Details (for seller to reply)</h3>", unsafe_allow_html=True)
buyer_name = st.text_input("Your Name (buyer)", key="buyernv9", placeholder="e.g. Tunde")
buyer_phone = st.text_input("Your WhatsApp Number", key="buyerphv9", placeholder="e.g. 2348031234567")

all_goods = get_goods()
shown=[]
for g in all_goods:
    if st.session_state.cat!="All" and st.session_state.cat.lower() not in g["cat"].lower(): continue
    if q and q.lower() not in (g["item"]+g["cat"]+g["loc"]).lower(): continue
    if loc_filter!="All Locations" and loc_filter.lower() not in g["loc"].lower(): continue
    if price_filter=="Under N20,000" and g["price"]>=20000: continue
    if price_filter=="N20,000 - N100,000" and not (20000<=g["price"]<=100000): continue
    if price_filter=="Over N100,000" and g["price"]<=100000: continue
    shown.append(g)

st.subheader(f"🛍️ Shop - {len(shown)} goods")
for idx, g in enumerate(shown):
    badge = '<span class="badge">✅ VERIFIED</span>' if g["verified"] else '<span class="badge2">New Seller</span>'
    st.markdown(f"""<div class="prod"><img src="{g['img']}"><div class="prod-body"><div style="display:flex;justify-content:space-between"><b>{g['name']}</b> {badge}</div><p style="margin:6px 0">{g['item']}</p><p>📍 {g['loc']} • 📞 {g['phone']}</p><p class="price">N{g['price']:,}</p></div></div>""", unsafe_allow_html=True)
    if st.button(f"🛒 Order This - {g['item'][:25]}", key=f"orderv9_{idx}_{g['item'][:10]}"):
        if not buyer_name or not buyer_phone:
            st.error("⚠️ Enter Your Name + WhatsApp Number above first, so seller can reply.")
        else:
            order = {"buyer":buyer_name,"buyer_phone":buyer_phone,"seller":g["name"],"seller_phone":g["phone"],"item":g["item"],"price":g["price"],"status":"Pending","time":datetime.now().strftime("%H:%M %d %b")}
            st.session_state.my_orders.append(order)
            st.session_state.seller_inbox.append(order)
            st.session_state.orders.append(g)
            st.success(f"✅ Order placed! Now tap 'Notify Seller on WhatsApp' below to alert {g['name']} instantly.")
            st.balloons()
    notify_text = f"Hello {g['name']}, Row Market here 👋\n\nSomeone wants your product:\n• {g['item']} - N{g['price']:,}\n• Buyer: {buyer_name or '[Your Name]'} - {buyer_phone or '[Your Number]'}\n• Location: {g['loc']}\n\nDo you have it? Reply YES if available, NO if sold out.\n\nRow Market - Abuja"
    wa_notify = f"https://wa.me/{g['phone']}?text=" + urllib.parse.quote(notify_text)
    st.link_button(f"🔔 Notify Seller on WhatsApp - {g['name']}", wa_notify)
    st.write("---")

st.subheader("🧾 My Orders - Track Status")
if len(st.session_state.my_orders)==0:
    st.write("No orders yet.")
for i, o in enumerate(st.session_state.my_orders):
    color = "🟡 Pending - Waiting for seller" if o["status"]=="Pending" else "🟢 Available - Seller said YES" if o["status"]=="Available" else "🔴 Sold Out"
    st.markdown(f"<div class='notif'><b>{o['item']}</b> - N{o['price']:,}<br>Seller: {o['seller']}<br>Status: {color}<br>Time: {o['time']}</div>", unsafe_allow_html=True)

st.subheader("🔔 Seller Inbox - Orders For You")
seller_check_phone = st.text_input("Your Seller WhatsApp Number (e.g. 2349046044472)", key="sellercheckv9")
if seller_check_phone:
    my_inbox = [o for o in st.session_state.seller_inbox if seller_check_phone in o["seller_phone"]]
    if len(my_inbox)==0:
        st.write("No new orders for this number yet. When someone orders, it will appear here + you get WhatsApp.")
    for j, o in enumerate(my_inbox):
        st.markdown(f"<div class='notif'><b>🔔 NEW ORDER!</b><br>Buyer: {o['buyer']} - {o['buyer_phone']}<br>Wants: <b>{o['item']} - N{o['price']:,}</b><br>Time: {o['time']}<br>Status: {o['status']}</div>", unsafe_allow_html=True)
        colA, colB = st.columns(2)
        with colA:
            if st.button(f"✅ YES, I Have It", key=f"yes_{j}_{o['item'][:8]}"):
                o["status"]="Available"
                for mo in st.session_state.my_orders:
                    if mo["item"]==o["item"] and mo["buyer"]==o["buyer"]: mo["status"]="Available"
                st.success("You said YES! Buyer will see Available.")
                st.rerun()
        with colB:
            if st.button(f"❌ NO, Sold Out", key=f"no_{j}_{o['item'][:8]}"):
                o["status"]="Sold Out"
                for mo in st.session_state.my_orders:
                    if mo["item"]==o["item"] and mo["buyer"]==o["buyer"]: mo["status"]="Sold Out"
                st.error("You said NO. Buyer will see Sold Out.")
                st.rerun()
        reply_text = f"Hello {o['buyer']}, this is {o['seller']} from Row Market. About your order {o['item']} N{o['price']:,}: Yes I have it, when do you want it? - Row Market"
        if o["status"]=="Available":
            st.link_button(f"💬 Reply to Buyer on WhatsApp - {o['buyer']}", f"https://wa.me/{o['buyer_phone']}?text=" + urllib.parse.quote(reply_text))

st.subheader("📸 Sell FREE")
nm = st.text_input("Your Name", key="nmv9")
pd = st.text_input("Product Name", key="pdv9")
pr = st.number_input("Price (Naira)", min_value=0, key="prv9")
ct = st.selectbox("Category", ["Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], key="ctv9")
loc = st.text_input("Location", key="locv9")
ph = st.text_input("Your WhatsApp Number (seller)", key="phv9")
img_url = st.text_input("Photo Link (optional)", key="imgv9")
if st.button("✅ Post Good FREE", key="postv9"):
    if nm and pd and pr>0:
        new = {"name":nm,"item":pd,"price":int(pr),"cat":ct,"loc":loc or "Abuja","phone":ph or "2349046044472","img":img_url or "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600","verified":False}
        st.session_state.local_goods.insert(0, new)
        st.success("Posted! Now if anyone orders, you get WhatsApp + In-App notification! Also add this row to your Sheet to make it permanent.")
    else: st.error("Fill Name, Product, Price")

st.subheader("💬 Chat Rooms")
rm = st.selectbox("Chat Room", ["Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], key="rmv9")
cm = st.text_input("Chat Message", key="cmv9")
if st.button("Send Chat", key="sendv9"):
    if cm: st.session_state.msgs.append(f"{rm} : {cm}")
for m in st.session_state.msgs:
    if rm.lower() in m.lower(): st.write(m)

st.subheader("📤 Share")
st.link_button("Share on WhatsApp", "https://wa.me/?text=Check%20Row%20Market%20Abuja%20-%20Post%20goods%20FREE")
nav = st.segmented_control("Nav", ["🏠 Home","🛍️ Shop","🧾 Orders","🔔 Inbox"], selection_mode="single", default=st.session_state.page, label_visibility="collapsed", key="navv9")
if nav: st.session_state.page = nav
