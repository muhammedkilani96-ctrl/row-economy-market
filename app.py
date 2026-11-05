import streamlit as st

if "cat" not in st.session_state:
    st.session_state.cat = "All"
if "goods" not in st.session_state:
    st.session_state.goods = []
if "photos" not in st.session_state:
    st.session_state.photos = []
if "orders" not in st.session_state:
    st.session_state.orders = []
if "msgs" not in st.session_state:
    st.session_state.msgs = []
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.markdown("""
<style>
/* FIX: Allow wrap, no sideways scroll */
[data-testid="stHorizontalBlock"] { flex-wrap: wrap !important; gap: 8px !important; }
[data-testid="column"] { min-width: calc(50% - 8px) !important; flex: 1 1 calc(50% - 8px) !important; }
div.stButton > button { width: 100% !important; border-radius: 14px !important; padding: 10px 2px !important; font-size: 14px !important; }
div.stLinkButton > a { width: 100% !important; background: #16a34a !important; color: white !important; border-radius: 14px !important; }
.cat-box { text-align:center; padding:14px 2px; border-radius:16px; margin-bottom:2px; font-size:32px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#16a34a;padding:16px 12px;border-radius:0 0 20px 20px;text-align:center">
<h1 style="color:white;margin:0;font-size:30px">Row Market</h1>
</div>
""", unsafe_allow_html=True)

s = st.text_input("🔍 Ask Mama Oloja - What are you looking for today?")
q = s

st.markdown("<h3 style='margin:10px 0 5px 0'>Categories <span style='float:right;color:#16a34a;font-size:14px'>See all ></span></h3>", unsafe_allow_html=True)

# 2 PER ROW - FITS PHONE, NO SCROLL
a1, a2 = st.columns(2)
with a1:
    st.markdown("<div class='cat-box' style='background:#fbcfe8'>🧴</div><p style='text-align:center;font-size:13px;margin:0'>Perfume</p>", unsafe_allow_html=True)
    if st.button("Perfume", key="c1"):
        st.session_state.cat = "Perfume"
with a2:
    st.markdown("<div class='cat-box' style='background:#bfdbfe'>👕</div><p style='text-align:center;font-size:13px;margin:0'>Clothes</p>", unsafe_allow_html=True)
    if st.button("Clothes", key="c2"):
        st.session_state.cat = "Clothes"

b1, b2 = st.columns(2)
with b1:
    st.markdown("<div class='cat-box' style='background:#bfdbfe'>📱</div><p style='text-align:center;font-size:13px;margin:0'>Phones</p>", unsafe_allow_html=True)
    if st.button("Phones", key="c3"):
        st.session_state.cat = "Phones"
with b2:
    st.markdown("<div class='cat-box' style='background:#fed7aa'>🍲</div><p style='text-align:center;font-size:13px;margin:0'>Food</p>", unsafe_allow_html=True)
    if st.button("Food", key="c4"):
        st.session_state.cat = "Food"

d1, d2 = st.columns(2)
with d1:
    st.markdown("<div class='cat-box' style='background:#fed7aa'>🚗</div><p style='text-align:center;font-size:13px;margin:0'>Car Mart</p>", unsafe_allow_html=True)
    if st.button("Car Mart", key="c5"):
        st.session_state.cat = "Car"
with d2:
    st.markdown("<div class='cat-box' style='background:#bbf7d0'>💼</div><p style='text-align:center;font-size:13px;margin:0'>Services</p>", unsafe_allow_html=True)
    if st.button("Services", key="c6"):
        st.session_state.cat = "Services"

e1, e2 = st.columns(2)
with e1:
    st.markdown("<div class='cat-box' style='background:#fbcfe8'>🎟️</div><p style='text-align:center;font-size:13px;margin:0'>Tickets</p>", unsafe_allow_html=True)
    if st.button("Tickets", key="c7"):
        st.session_state.cat = "Tickets"
with e2:
    st.markdown("<div class='cat-box' style='background:#a7f3d0'>💬</div><p style='text-align:center;font-size:13px;margin:0'>Chat Rooms</p>", unsafe_allow_html=True)
    if st.button("Chat Rooms", key="c8"):
        st.session_state.cat = "Chat"

st.write("Category:", st.session_state.cat)

st.markdown("<h3>Featured Listing <span style='float:right;color:#16a34a;font-size:14px'>See all ></span></h3>", unsafe_allow_html=True)
st.markdown("""
<div style="background:white;padding:16px;border-radius:16px;box-shadow:0 2px 12px #eee">
<div style="text-align:right"><span style="background:#16a34a;color:white;padding:4px 10px;border-radius:20px;font-size:12px">✅ VERIFIED</span></div>
<h3 style="margin:5px 0">Horlance Auto Cooling Ltd</h3>
<p>🔧 Car AC Repair</p>
<p>📍 Osun & Oyo State</p>
<p>🟢 WhatsApp 09046044472</p>
</div>
""", unsafe_allow_html=True)
u = "https://wa.me/2349046044472"
st.link_button("💬 Chat on WhatsApp", u)

st.markdown("""
<div style="background:#dcfce7;padding:12px;border-radius:16px;margin-top:12px">
🧕 <b>Mama Oloja AI:</b> Welcome my dear, I can help you find the best price in the market. <span style="float:right;font-size:12px">🕐 now</span>
</div>
""", unsafe_allow_html=True)

st.subheader("Sell FREE")
nm = st.text_input("Your Name", key="nm1")
pd = st.text_input("Product Name", key="pd1")
pr = st.text_input("Price", key="pr1")
ct_list = ["Perfume", "Clothes", "Phones", "Food", "Car", "Services", "Tickets", "Chat"]
ct = st.selectbox("Category", ct_list, key="ct1")
pic = st.file_uploader("Add Photo", type=["jpg", "png", "jpeg"], key="pic1")
if pic is not None:
    st.image(pic)
if st.button("Post Good", key="post1"):
    item = nm + " - " + pd + " - N" + pr + " - " + ct
    st.session_state.goods.append(item)
    st.session_state.photos.append(pic)
    st.write("Posted! Thank you")

st.subheader("Shop")
st.write("Total Goods:", len(st.session_state.goods))
for idx, g in enumerate(st.session_state.goods):
    gl = g.lower()
    sl = s.lower()
    ok = True
    if sl not in gl:
        ok = False
    if st.session_state.cat != "All":
        cl = st.session_state.cat.lower()
        if cl not in gl:
            ok = False
    if ok:
        st.write(g)
        ph = st.session_state.photos[idx]
        if ph is not None:
            st.image(ph)
        if st.button("Order This", key=f"ord{idx}"):
            st.session_state.orders.append(g)
            st.write("Order Added!")
        st.write("---")

st.subheader("My Orders")
st.write("Total Orders:", len(st.session_state.orders))
for o in st.session_state.orders:
    st.write(o)
if len(st.session_state.orders) > 0:
    st.link_button("Order on WhatsApp", u)

st.subheader("Chat Rooms")
rm = st.selectbox("Chat Room", ct_list, key="rm1")
cm = st.text_input("Chat Message", key="cm1")
if st.button("Send Chat", key="send1"):
    st.session_state.msgs.append(rm + " : " + cm)
    st.write("Sent!")
for m in st.session_state.msgs:
    if rm.lower() in m.lower():
        st.write(m)

st.subheader("Mama Answers")
ql = q.lower()
if "rice" in ql:
    st.write("Rice N80000 Abuja best price")
if "perfume" in ql:
    st.write("Perfume N15000")
if "car" in ql:
    st.write("Car go Horlance - 09046044472")
if "phone" in ql:
    st.write("Phone test first")
if "food" in ql:
    st.write("Food fresh daily")
if "clothes" in ql:
    st.write("Clothes new stock")
if "hello" in ql or "hi" in ql:
    st.write("Mama Welcome dear")

st.subheader("My Profile")
pn = st.text_input("Profile Name", key="pn1")
if st.button("Save Profile", key="save1"):
    st.write("Profile Saved:", pn)

st.subheader("Share Row Market")
w = "https://wa.me/?text=RowMarketAbuja"
st.link_button("Share on WhatsApp", w)
st.write("Row Market Abuja FREE - Post goods FREE - Chat FREE")
st.markdown("<hr>", unsafe_allow_html=True)

n1, n2 = st.columns(2)
if n1.button("🏠 Home", key="n1"):
    st.session_state.page = "Home"
if n2.button("🛍️ Shop", key="n2"):
    st.session_state.page = "Shop"
n3, n4 = st.columns(2)
if n3.button("🧾 Orders", key="n3"):
    st.session_state.page = "Orders"
if n4.button("👤 Profile", key="n4"):
    st.session_state.page = "Profile"
st.write("Page:", st.session_state.page)
