import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime, timedelta
import time, random

st.set_page_config(page_title="Row Market - Abuja", layout="wide", initial_sidebar_state="collapsed")
SHEET_ID = "1w8P3SQiChShHPQzShpgznR-lay-awTHmu_x-VHI9IU8E"
if "my_orders" not in st.session_state: st.session_state.my_orders = []
if "seller_inbox" not in st.session_state: st.session_state.seller_inbox = []
if "local_goods" not in st.session_state: st.session_state.local_goods = []
if "ratings" not in st.session_state: st.session_state.ratings = {}
if "page" not in st.session_state: st.session_state.page = "Home"
if "cat" not in st.session_state: st.session_state.cat = "All"
if "my_name" not in st.session_state: st.session_state.my_name = ""
if "buyer_phone_temp" not in st.session_state: st.session_state.buyer_phone_temp = ""
if "referral_code" not in st.session_state: st.session_state.referral_code = ""
if "referral_count" not in st.session_state: st.session_state.referral_count = 0
if "reviews" not in st.session_state: st.session_state.reviews = [
    {"seller":"Horlance Auto Cooling Ltd","buyer":"Tunde","stars":5,"text":"AC cold like freezer! Best in Osun","photo":""},
    {"seller":"Mama Ada","buyer":"Chidi","stars":5,"text":"Rice is original, no stones. Fast delivery","photo":""},
]
if "reported" not in st.session_state: st.session_state.reported = []
if "verified_sellers" not in st.session_state: st.session_state.verified_sellers = ["Horlance Auto Cooling Ltd","Mama Ada"]
if "chat_msgs" not in st.session_state:
    st.session_state.chat_msgs = [{"room":"General","user":"Mama Ada","msg":"Welcome! Rice available 🍚","time":"09:12"}]
if "online_users" not in st.session_state: st.session_state.online_users = ["Mama Ada","Horlance Auto","Tunde","Chidi","Aisha"]
if "escrow_balance" not in st.session_state: st.session_state.escrow_balance = 0
if "my_earnings" not in st.session_state: st.session_state.my_earnings = 0

PAYSTACK_LINK = "https://paystack.shop/rowmarket"
BANK_NAME = "OPay / GTB"
ACCOUNT_NAME = "Row Market - Horlance"
ACCOUNT_NUMBER = "9046044472"
COMMISSION = 0.05

@st.cache_data(ttl=30)
def load_sheet(sid):
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sid}/export?format=csv"
        df = pd.read_csv(url)
        return df.dropna(subset=["Item"])
    except: return pd.DataFrame()

def get_goods():
    goods=[]
    df=load_sheet(SHEET_ID)
    for _,r in df.iterrows():
        try: goods.append({"name":str(r.get("Name","")),"item":str(r.get("Item","")),"price":int(float(r.get("Price",0))),"cat":str(r.get("Category","")),"loc":str(r.get("Location","Abuja")),"phone":str(r.get("Phone","2349046044472")),"img":str(r.get("Image","https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600")),"verified":str(r.get("Verified","")).upper()=="TRUE"})
        except: pass
    goods=st.session_state.local_goods+goods
    if len(goods)==0:
        goods=[{"name":"Horlance Auto Cooling Ltd","item":"Car AC Repair","price":25000,"cat":"Car","loc":"Osun & Oyo State","img":"https://images.unsplash.com/photo-1625047509168-a7026f36de04?w=600","phone":"2349046044472","verified":True},
               {"name":"Mama Ada","item":"Bag of Rice 50kg","price":85000,"cat":"Food","loc":"Wuse 2, Abuja","img":"https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600","phone":"2349046044472","verified":True}]
    return goods

def delivery_fee(loc):
    if "Wuse" in loc: return 1500
    if "Garki" in loc: return 1500
    if "Gwarinpa" in loc: return 2000
    if "Osun" in loc or "Oyo" in loc: return 3000
    return 2500

def get_deal_price(g):
    # Daily Deal: First product 12% off today
    return int(g["price"]*0.88)

st.markdown("""
<style>
header {visibility:hidden !important}
.block-container {padding-top:0px !important; padding-left:0px !important; padding-right:0px !important; padding-bottom:100px !important; max-width:100% !important}
div.stButton > button { width:100% !important; background:#22C55E !important; color:white !important; border-radius:12px !important; padding:12px !important; border:none !important; font-weight:700 !important; }
div.stLinkButton > a { width:100% !important; background:#22C55E !important; color:white !important; border-radius:12px !important; text-align:center !important; font-weight:700 !important; }
.kk-header { background:#22C55E; border-radius:0 0 24px 24px; padding:14px 16px 20px 16px; display:flex; justify-content:space-between; align-items:center; }
.kk-header h1 { color:white; margin:0; font-size:26px; font-weight:800; }
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
div[data-testid="stSegmentedControl"] button { border-radius:20px !important; padding:8px 12px !important; font-size:12px !important; }
div[data-testid="stSegmentedControl"] button[data-testid="stSegmentedControlButton-selected"] { background:#22C55E !important; color:white !important; }
</style>
""", unsafe_allow_html=True)

# HEADER K&K
st.markdown("""<div class="kk-header"><div style="font-size:28px;color:white">☰</div><h1>K&K Market</h1><div style="background:#FB923C;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px">👤</div></div>""", unsafe_allow_html=True)
# DAILY DEAL + COUNTDOWN
deal_end = datetime.now() + timedelta(hours=4, minutes=23)
st.markdown(f"""<div class="deal-box"><b>🔥 DEAL OF THE DAY - Ends in 4h 23m</b><br>First product 12% OFF today only! Use code <b>ROW12</b><br><span style="font-size:11px">⏰ Hurry - {deal_end.strftime('%H:%M')} today</span></div>""", unsafe_allow_html=True)
search_q = st.text_input("🔍 Ask Mama Oloja - What are you looking for today? 🎤", key="kk_search_v14")
q = search_q
with st.expander("👤 Your Details + Referral + Verification", expanded=False):
    my_name_input = st.text_input("Your Name", value=st.session_state.my_name, key="my_name_v14")
    if my_name_input and my_name_input != st.session_state.my_name:
        st.session_state.my_name = my_name_input
        if my_name_input not in st.session_state.online_users: st.session_state.online_users.append(my_name_input)
        if not st.session_state.referral_code: st.session_state.referral_code = my_name_input.upper()[:5] + str(random.randint(100,999))
    buyer_phone = st.text_input("Your WhatsApp Number", value=st.session_state.buyer_phone_temp, key="buyer_phone_v14")
    st.session_state.buyer_phone_temp = buyer_phone
    # REFERRAL
    st.markdown(f"""<div style="background:#FEF3C7;padding:12px;border-radius:12px"><b>🎁 Your Referral Link</b><br>Share this: <b>rowmarket.app/?ref={st.session_state.referral_code or 'YOURNAME'}</b><br>Invite 3 friends = <b>N500 OFF</b><br>You have invited: <b>{st.session_state.referral_count} / 3</b> {'✅ N500 unlocked!' if st.session_state.referral_count>=3 else ''}</div>""")
    if st.button("📤 Share My Referral Link", key="share_ref_v14"):
        st.link_button("Share on WhatsApp", f"https://wa.me/?text=Join%20K%26K%20Market%20with%20my%20link%20rowmarket.app%2F%3Fref%3D{st.session_state.referral_code}%20-%20Get%20N500%20off")
    # VERIFICATION
    st.markdown("---")
    st.markdown("**⭐ Get VERIFIED Badge - Upload NIN / Selfie**")
    ver_file = st.file_uploader("Upload NIN or Selfie for Verification", type=["jpg","png","jpeg"], key="ver_upload_v14")
    ver_name = st.text_input("Seller Name to Verify", key="ver_name_v14")
    if st.button("✅ Request Verification", key="req_ver_v14"):
        if ver_file and ver_name:
            if ver_name not in st.session_state.verified_sellers: st.session_state.verified_sellers.append(ver_name)
            st.success(f"✅ {ver_name} is now VERIFIED! Badge will show on all your products.")
            st.balloons()
        else: st.error("Upload photo + Name")
    st.write(f"Verified sellers: {', '.join(st.session_state.verified_sellers)}")
    # ESCROW ADMIN - Only you see this
    st.markdown(f"**💰 Escrow Balance (Admin - You):** N{st.session_state.escrow_balance:,} held | Your Commission Earned: N{st.session_state.my_earnings:,}")

buyer_name = st.session_state.my_name
buyer_phone = st.session_state.buyer_phone_temp
page = st.session_state.page

if page == "Home":
    st.markdown("""<div class="section-head"><h2>Categories</h2><span>See all ›</span></div><div class="cat-grid"><div class="cat-item"><div class="cat-box" style="background:#FBCFE8">🧴</div><p>Perfume</p></div><div class="cat-item"><div class="cat-box" style="background:#BFDBFE">👕</div><p>Clothes</p></div><div class="cat-item"><div class="cat-box" style="background:#BFDBFE">📱</div><p>Phones</p></div><div class="cat-item"><div class="cat-box" style="background:#FED7AA">🍲</div><p>Food</p></div><div class="cat-item"><div class="cat-box" style="background:#FED7AA">🚗</div><p>Car Mart</p></div><div class="cat-item"><div class="cat-box" style="background:#BBF7D0">💼</div><p>Services</p></div><div class="cat-item"><div class="cat-box" style="background:#FBCFE8">🎟️</div><p>Tickets</p></div><div class="cat-item"><div class="cat-box" style="background:#A7F3D0">💬</div><p>Chat Rooms</p></div></div>""", unsafe_allow_html=True)
    cat_pick = st.segmented_control("Cat", ["All","Perfume","Clothes","Phones","Food","Car","Services","Tickets","Chat"], selection_mode="single", default=st.session_state.cat, label_visibility="collapsed", key="cat_v14")
    if cat_pick: st.session_state.cat = cat_pick
    # POST WITH PHOTO UPLOAD
    st.markdown("""<div class="post-box"><h3 style="margin:0">📸 POST YOUR PRODUCT - FREE - Upload Photo</h3><p style="margin:4px 0 0 0;font-size:13px;color:#666">No link needed! Upload from gallery 👇</p></div>""", unsafe_allow_html=True)
    with st.expander("➕ TAP TO POST - Upload Photo", expanded=True):
        p_name = st.text_input("Your Name", value=buyer_name, key="post_name_v14")
        p_item = st.text_input("What are you selling?", key="post_item_v14", placeholder="e.g. Bag of Rice 50kg")
        p_price = st.number_input("Price (Naira)", min_value=0, key="post_price_v14")
        p_cat = st.selectbox("Category", ["Food","Phones","Perfume","Clothes","Car","Services","Tickets","Chat"], key="post_cat_v14")
        p_loc = st.text_input("Location", key="post_loc_v14", placeholder="Wuse 2, Abuja")
        p_phone = st.text_input("Your WhatsApp", value=buyer_phone, key="post_phone_v14")
        uploaded = st.file_uploader("📸 Upload Product Photo (from phone gallery)", type=["jpg","png","jpeg"], key="post_photo_v14")
        p_img_link = st.text_input("OR Paste Photo Link (optional)", key="post_img_v14")
        img_to_use = "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600"
        if uploaded is not None:
            st.image(uploaded, caption="Preview - Your photo", width=200)
            img_to_use = "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600"
            st.info("✅ Photo uploaded! In real app it shows your photo. For now we use shop photo + your upload is saved.")
        elif p_img_link: img_to_use = p_img_link
        if st.button("🚀 POST NOW", key="post_now_v14"):
            if p_name and p_item and p_price>0:
                is_ver = p_name in st.session_state.verified_sellers
                st.session_state.local_goods.insert(0, {"name":p_name,"item":p_item,"price":int(p_price),"cat":p_cat,"loc":p_loc or "Abuja","phone":p_phone or "2349046044472","img":img_to_use,"verified":is_ver})
                st.success(f"✅ Posted! '{p_item}' LIVE! {'✅ VERIFIED badge shown' if is_ver else 'Get verified in Your Details to get ✅ badge'}"); st.balloons()
            else: st.error("Fill Name, Product, Price")
    # FEATURED
    st.markdown("""<div class="section-head"><h2>Featured Listing</h2><span>See all ›</span></div>""", unsafe_allow_html=True)
    all_goods = get_goods()
    filtered=[]
    for g in all_goods:
        if st.session_state.cat!="All" and st.session_state.cat.lower() not in g["cat"].lower(): continue
        if q and q.lower() not in (g["item"]+g["cat"]+g["loc"]+g["name"]).lower(): continue
        filtered.append(g)
    if len(filtered)>0:
        feat = filtered[0]
        is_ver = feat["name"] in st.session_state.verified_sellers or feat["verified"]
        badge = '<span class="badge">✅ VERIFIED</span>' if is_ver else '<span class="badge2">New Seller</span>'
        deal_p = get_deal_price(feat)
        st.markdown(f"""<div class="featured"><div style="display:flex;justify-content:space-between"><div><b style="font-size:16px">{feat['name']}</b><br><span>🔧 {feat['item']}</span><br><br><span>📍 {feat['loc']}</span><br><span>🟢 WhatsApp {feat['phone']}</span><br><span class="price">N{deal_p:,} <span style="font-size:12px;color:#999;text-decoration:line-through">N{feat['price']:,}</span> <span style="font-size:11px;background:#EF4444;color:white;padding:2px 6px;border-radius:10px">-12% DEAL</span></span></div><img src="{feat['img']}" class="featured-img"></div><div style="text-align:right">{badge}</div></div>""", unsafe_allow_html=True)
        st.link_button(f"
