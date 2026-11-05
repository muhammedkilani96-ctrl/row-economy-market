import streamlit as st
st.set_page_config(page_title="Row Market", layout="wide", initial_sidebar_state="collapsed")

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

st.markdown("""
<style>
header {visibility:hidden !important}
.block-container {padding-top:0px !important; padding-left:8px !important; padding-right:8px !important; max-width:100% !important}
div.stButton > button { width:100% !important; background:#16a34a !important; color:white !important; border-radius:14px !important; padding:12px !important; }
div.stLinkButton > a { width:100% !important; background:#16a34a !important; color:white !important; border-radius:14px !important; text-align:center !important; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:10px 0; }
.card { border-radius:16px; padding:16px 6px; text-align:center; font-size:32px; }
.card p { font-size:13px; margin:4px 0 0 0; color:#111; }
.navgrid { display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:8px; text-align:center; margin-top:16px; padding:10px 0; border-top:1px solid #eee; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#16a34a;padding:18px 10px 14px 10px;border-radius:0 0 20px 20px;text-align:center;margin-top:0">
<h1 style="color:white;margin:0;font-size:28px">Row Market</h1>
</div>
""", unsafe_allow_html=True)

s = st.text_input("🔍 Ask Mama Oloja - What are you looking for today?")
q = s

st.markdown("<h3 style='margin:10px 0 0 0'>Categories <span style='float:right;color:#16a34a;font-size:14px'>See all ></span></h3>", unsafe_allow_html=True)

# HTML GRID - STAYS 2 PER ROW ON PHONE
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

ct_list = ["All", "Perfume", "Clothes", "Phones", "Food", "Car", "Services", "Tickets", "Chat"]
st.session_state.cat = st.selectbox("Tap to choose category", ct_list, key="catpick")
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
ct = st.selectbox("Category", ct_list[1:], key="ct1")
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
rm = st.selectbox("Chat Room", ct_list[1:], key="rm1")
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

st.markdown("""
<div class="navgrid">
<div>🏠<br><b>Home</b></div>
<div>🛍️<br>Shop</div>
<div>🧾<br>Orders</div>
<div>👤<br>Profile</div>
</div>
""", unsafe_allow_html=True)
st.write("Page: Home - Scroll to use all sections")
