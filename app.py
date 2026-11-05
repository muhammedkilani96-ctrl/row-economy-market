import streamlit as st
st.set_page_config(page_title="Row Market - Abuja", layout="wide", initial_sidebar_state="collapsed")

# --- STATE ---
if "cat" not in st.session_state: st.session_state.cat = "All"
if "orders" not in st.session_state: st.session_state.orders = []
if "msgs" not in st.session_state: st.session_state.msgs = []
if "page" not in st.session_state: st.session_state.page = "🏠 Home"
if "my_goods" not in st.session_state:
    st.session_state.my_goods = [
        {"name":"Mama Ada","item":"Bag of Rice 50kg","price":85000,"cat":"Food","loc":"Wuse 2, Abuja","img":"https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600","phone":"2349046044472","verified":True},
        {"name":"Chidi Stores","item":"iPhone 12 - Neatly Used","price":285000,"cat":"Phones","loc":"Wuse 2, Abuja","img":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600","phone":"2349046044472","verified":True},
        {"name":"Zara Beauty","item":"Arabian Oud Perfume 100ml","price":15500,"cat":"Perfume","loc":"Garki, Abuja","img":"https://images.unsplash.com/photo-1541643600914-78b084683601?w=600","phone":"2349046044472","verified":True},
        {"name":"Horlance Auto","item":"Car AC Repair + Gas Refill","price":25000,"cat":"Car","loc":"Osun & Oyo","img":"https://images.unsplash.com/photo-1625047509168-a7026f36de04?w=600","phone":"2349046044472","verified":True},
        {"name":"Aso Oke House","item":"Ankara Gown - New Design","price":22000,"cat":"Clothes","loc":"Gwarinpa, Abuja","img":"https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=600","phone":"2349046044472","verified":False},
        {"name":"Lagos Tickets","item":"Abuja to Lagos Flight Ticket","price":95000,"cat":"Tickets","loc":"Online","img":"https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600","phone":"2349046044472","verified":True},
    ]
if "photos" not in st.session_state: st.session_state.photos = []

st.markdown("""
<style>
header {visibility:hidden !important}
.block-container {padding-top:0px !important; padding-left:0px !important; padding-right:0px !important; padding-bottom:90px !important; max-width:100% !important}
.sticky-top { position:sticky; top:0; z-index:99; background:#16a34a; padding:14px 12px 10px 12px; border-radius:0 0 20px 20px; }
div.stButton > button { width:100% !important; background:#16a34a !important; color:white !important; border-radius:12px !important; padding:10px !important; border:none !important; }
div.stLinkButton > a { width:100% !important; background:#16a34a !important; color:white !important; border-radius:12px !important; text-align:center !important; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:10px 12px; }
.card { border-radius:16px; padding:16px 6px; text-align:center; font-size:32px; background:#fff; }
.card p { font-size:13px; margin:4px 0 0 0; color:#111; font-weight:600; }
.prod { background:white; border-radius:16px; overflow:hidden; box-shadow:0 2px 12px #eee; margin:0 12px 12px 12px; }
.prod img { width:100%; height:180px; object-fit:cover; }
.prod-body { padding:12px; }
.price { color:#16a34a; font-weight:800; font-size:18px; margin:4px 0; }
.badge { background:#16a34a; color:white; padding:3px 8px; border-radius:20px; font-size:11px; }
.badge2 { background:#fef3c7; color:#92400e; padding:3px 8px; border-radius:20px; font-size:11px; }
div[data-testid="stSegmentedControl"] button { border-radius:20px !important; padding:8px 12px !important; font-size:12px !important; }
div[data-testid="stSegmentedControl"] button[data-testid="stSegmentedControlButton-selected"] { background:#16a34a !important; color:white !important; }
.sticky-nav { position:fixed; bottom:0; left:0; right:0; background:white; border-top:1px solid #eee; padding:8px 8px 12px 8px; z-index:99; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div class="sticky-top">
<h1 style="color:white;margin:0;font-size:26px;text-align:center">Row Market</h1>
<p style="color:#dcfce7;text-align:center;margin:2px 0 8px 0;font-size:12px">Abuja • FREE to Post • Mama Oloja Helps You</p>
</div>
""", unsafe_allow_html=True)

s = st.text_input("🔍 Ask Mama Oloja - What are you looking for today?", key="search_top")
q = s

# --- MAMA QUICK TAPS ---
st.markdown("<p style='padding:0 12px;margin:8px 0 0 0;font-size:13px'><b>🧕 Mama Oloja - Tap to ask:</b></p>", unsafe_allow_html=True)
mq1, mq2, mq3 = st.columns(3)
# Use segmented for quick asks
mama_q = st.segmented_control("Mama", ["🍚 Rice price?","📱 Cheapest phone?","🚗 Car AC?","🧴 Perfume?"], selection_mode="single", label_visibility="collapsed", key="mamaq")
if mama_q == "🍚 Rice price?":
    st.markdown("<div style='background:#dcfce7;margin:8px 12px;padding:12px;border-radius:12px'>🧕 <b>Mama:</b> Rice 50kg - N85,000 in Wuse 2. Mama Ada has best price. Tap Order below.</div>", unsafe_allow_html=True)
elif mama_q == "📱 Cheapest phone?":
    st.markdown("<div style='background:#dcfce7;margin:8px 12px;padding:12px;border-radius:12px'>🧕 <b>Mama:</b> iPhone 12 - N285,000, tested, no fault. Don't pay before you test!</div>", unsafe_allow_html=True)
elif mama_q == "🚗 Car AC?":
    st.markdown("<div style='background:#dcfce7;margin:8px 12px;padding:12px;border-radius:12px'>🧕 <b>Mama:</b> Go Horlance! Car AC Repair N25,000. WhatsApp 09046044472 - tell them Mama sent you.</div>", unsafe_allow_html=True)
elif mama_q == "🧴 Perfume?":
    st.markdown("<div style='background:#dcfce7;margin:8px 12px;padding:12px;border-radius:12px'>🧕 <b>Mama:</b> Arabian Oud N15,500 in Garki. Original, long lasting.</div>", unsafe_allow_html=True)

# --- CATEGORIES ---
st.markdown("<h3 style='padding:0 12px;margin:12px 0 0 0'>Categories <span style='float:right;color:#16a34a;font-size:14px'>See all ></span></h3>", unsafe_allow_html=True)
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
picked = st.segmented_control("Cat", ["All","Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], selection_mode="single", default=st.session_state.cat, label_visibility="collapsed", key="catv7")
if picked: st.session_state.cat = picked

# --- FEATURED ---
st.markdown("<h3 style='padding:0 12px'>Featured Listing <span style='float:right;color:#16a34a;font-size:14px'>See all ></span></h3>", unsafe_allow_html=True)
st.markdown("""
<div class="prod">
<img src="https://images.unsplash.com/photo-1625047509168-a7026f36de04?w=800">
<div class="prod-body">
<div style="text-align:right"><span class="badge">✅ VERIFIED</span> <span class="badge2">⭐ 4.9 • 120 jobs</span></div>
<h3 style="margin:6px 0">Horlance Auto Cooling Ltd</h3>
<p>🔧 Car AC Repair • Gas Refill • Compressor</p>
<p>📍 Osun & Oyo State • 🟢 Online Now</p>
<p class="price">From N25,000</p>
</div>
</div>
""", unsafe_allow_html=True)
st.link_button("💬 Chat on WhatsApp - Horlance", "https://wa.me/2349046044472?text=Hello%20Horlance,%20I%20came%20from%20Row%20Market.%20I%20need%20Car%20AC%20Repair")

st.markdown("""
<div style="background:#dcfce7;padding:12px;border-radius:16px;margin:0 12px">
🧕 <b>Mama Oloja AI:</b> Welcome my dear, I can help you find the best price in the market. <span style="float:right;font-size:12px">🕐 now</span>
</div>
""", unsafe_allow_html=True)

# --- SHOP ---
st.subheader("🛍️ Shop - Abuja Market")
# Filter
shown = []
for g in st.session_state.my_goods:
    if st.session_state.cat != "All" and st.session_state.cat.lower() not in g["cat"].lower():
        continue
    if q and q.lower() not in (g["item"]+g["cat"]+g["loc"]).lower():
        continue
    shown.append(g)

st.write(f"Showing {len(shown)} goods • Category: {st.session_state.cat}")
for idx, g in enumerate(shown):
    badge = '<span class="badge">✅ VERIFIED</span>' if g["verified"] else '<span class="badge2">New Seller</span>'
    st.markdown(f"""
    <div class="prod">
    <img src="{g['img']}">
    <div class="prod-body">
    <div style="display:flex;justify-content:space-between"><b>{g['name']}</b> {badge}</div>
    <p style="margin:6px 0">{g['item']}</p>
    <p>📍 {g['loc']}</p>
    <p class="price">N{g['price']:,}</p>
    </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"🛒 Order - {g['item']}", key=f"buy{idx}_{g['item']}"):
        st.session_state.orders.append(g)
        st.success(f"Added {g['item']} to cart!")

# --- CART / ORDERS ---
st.subheader("🧾 My Orders / Cart")
st.write(f"Total in cart: {len(st.session_state.orders)}")
total = sum([o["price"] for o in st.session_state.orders])
for o in st.session_state.orders:
    st.write(f"• {o['item']} - N{o['price']:,}")
if total>0:
    st.write(f"**Total: N{total:,}**")
    wa_text = "Hello Row Market, I want to order: " + ", ".join([o["item"] for o in st.session_state.orders]) + f" Total N{total}"
    wa_url = "https://wa.me/2349046044472?text=" + wa_text.replace(" ","%20")
    st.link_button(f"💬 Checkout on WhatsApp - N{total:,}", wa_url)
    if st.button("Clear Cart"):
        st.session_state.orders = []
        st.rerun()

# --- SELL ---
st.subheader("📸 Sell FREE - Post in 30 seconds")
nm = st.text_input("Your Name", key="nmv7")
pd = st.text_input("Product Name", key="pdv7")
pr = st.number_input("Price (Naira)", min_value=0, key="prv7")
ct = st.selectbox("Category", ["Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], key="ctv7")
loc = st.text_input("Location (e.g. Wuse 2)", key="locv7")
pic = st.file_uploader("Add Photo", type=["jpg","png","jpeg"], key="picv7")
if pic is not None:
    st.image(pic)
if st.button("✅ Post Good FREE", key="postv7"):
    if nm and pd and pr>0:
        new = {"name":nm,"item":pd,"price":pr,"cat":ct,"loc":loc or "Abuja","img":"https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600","phone":"2349046044472","verified":False}
        st.session_state.my_goods.insert(0, new)
        st.success("Posted! Your good is now live in Shop!")
    else:
        st.error("Fill Name, Product and Price")

# --- CHAT ROOMS ---
st.subheader("💬 Chat Rooms")
rm = st.selectbox("Chat Room", ["Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], key="rmv7")
cm = st.text_input("Chat Message", key="cmv7")
if st.button("Send Chat", key="sendv7"):
    if cm:
        st.session_state.msgs.append(f"{rm} : {cm}")
        st.success("Sent!")
for m in st.session_state.msgs:
    if rm.lower() in m.lower():
        st.write(m)

# --- PROFILE + SHARE ---
st.subheader("👤 My Profile")
pn = st.text_input("Profile Name", key="pnv7")
if st.button("Save Profile", key="savev7"):
    st.write(f"Profile Saved: {pn} ✅")

st.subheader("📤 Share Row Market")
st.link_button("Share on WhatsApp", "https://wa.me/?text=Check%20Row%20Market%20Abuja%20-%20Post%20goods%20FREE%20https://row-economy-market.streamlit.app")
st.write("Row Market Abuja FREE - Post goods FREE - Chat FREE - Mama Oloja helps you find best price")

# --- BOTTOM NAV PILLS (tappable) ---
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
nav = st.segmented_control("Nav", ["🏠 Home","🛍️ Shop","🧾 Orders","👤 Profile"], selection_mode="single", default=st.session_state.page, label_visibility="collapsed", key="navv7")
if nav: st.session_state.page = nav
st.write(f"Page: {st.session_state.page} - Scroll to use all sections")
