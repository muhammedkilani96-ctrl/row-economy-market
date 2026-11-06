import streamlit as st
import hashlib
import re
import random
from datetime import datetime

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="centered")

# ===== PREMIUM CSS - BEST DESIGN EVER =====
st.markdown("""
<style>
.stApp {background: #F6F7FB;}
.topbar {background: #0A0A0A; color: white; padding: 10px 14px; border-radius: 0 0 20px 20px; display: flex; justify-content: space-between; font-size: 12px; font-weight: 700;}
.hero-premium {background: linear-gradient(135deg, #0B3D2E 0%, #0A9D4D 45%, #FFB800 100%); border-radius: 26px; padding: 24px 18px 20px 18px; color: white; position: relative; overflow: hidden; box-shadow: 0 12px 30px rgba(10,157,77,0.35);}
.hero-premium h1 {font-size: 36px; line-height: 0.95; margin: 0; color: white; font-weight: 900; letter-spacing: -1px;}
.hero-premium h1 span {color: #FFD700;}
.hero-premium p {font-size: 14px; opacity: 0.92; margin: 8px 0 0 0;}
.hero-btn {background: white; color: #0B3D2E; padding: 9px 16px; border-radius: 999px; font-weight: 800; font-size: 13px; display: inline-block; margin-top: 12px; margin-right: 8px;}
.hero-badge {background: rgba(255,255,255,0.22); border: 1px solid rgba(255,255,255,0.4); padding: 5px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; display: inline-block; margin-top: 10px;}
.flash {background: #FF2D55; color: white; border-radius: 16px; padding: 12px 14px; display: flex; justify-content: space-between; align-items: center;}
.flash b {font-size: 16px;}
.flash span {background: white; color: #FF2D55; padding: 4px 8px; border-radius: 8px; font-weight: 900; font-size: 13px;}
.story-wrap {display: flex; gap: 12px; overflow-x: auto; padding: 6px 2px;}
.story {text-align: center; min-width: 68px;}
.story-circle {width: 62px; height: 62px; border-radius: 50%; border: 3px solid #FF2D55; display: flex; align-items: center; justify-content: center; font-size: 30px; background: white; margin: 0 auto;}
.story-live {background: #FF2D55; color: white; font-size: 9px; font-weight: 900; padding: 2px 6px; border-radius: 999px; margin-top: -10px; display: inline-block;}
.story-name {font-size: 11px; font-weight: 700; margin-top: 4px;}
.mama-premium {background: white; border-radius: 22px; padding: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.08); border: 1px solid #EDE7FF;}
.mama-header {display: flex; align-items: center; gap: 10px;}
.mama-avatar {width: 48px; height: 48px; border-radius: 50%; background: linear-gradient(135deg,#7B2FFF,#FF2D55); display: flex; align-items: center; justify-content: center; font-size: 26px;}
.chat-bubble-user {background: #0A9D4D; color: white; padding: 10px 12px; border-radius: 16px 16px 4px 16px; margin: 8px 0; max-width: 90%; margin-left: auto; font-size: 14px;}
.chat-bubble-mama {background: #F1EFFF; color: #222; padding: 10px 12px; border-radius: 16px 16px 16px 4px; margin: 8px 0; max-width: 92%; font-size: 14px;}
.cat-premium {background: white; border-radius: 18px; padding: 14px 6px; text-align: center; box-shadow: 0 3px 12px rgba(0,0,0,0.05);}
.cat-premium div {font-size: 28px;}
.cat-premium span {font-size: 12px; font-weight: 800;}
.seller-week {background: linear-gradient(135deg,#FFF8D6,#FFE9A8); border: 2px solid #FFD700; border-radius: 20px; padding: 14px;}
.product-premium {background: white; border-radius: 22px; overflow: hidden; box-shadow: 0 6px 20px rgba(0,0,0,0.07); margin-bottom: 16px; border: 1px solid #F0F0F0;}
.product-top {height: 150px; display: flex; align-items: center; justify-content: center; font-size: 72px; position: relative;}
.discount {position: absolute; top: 10px; left: 10px; background: #FF2D55; color: white; font-size: 11px; font-weight: 900; padding: 4px 8px; border-radius: 999px;}
.heart {position: absolute; top: 10px; right: 10px; background: white; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);}
.product-body {padding: 12px 14px 14px 14px;}
.price-big {color: #0A9D4D; font-weight: 900; font-size: 20px;}
.old {color: #999; text-decoration: line-through; font-size: 13px;}
.stars {color: #FFB800; font-size: 13px; font-weight: 800;}
.testimonial {background: white; border-radius: 18px; padding: 14px; border-left: 4px solid #0A9D4D; margin-bottom: 10px;}
.bottom-nav {position: fixed; bottom: 0; left: 0; right: 0; background: white; display: flex; justify-content: space-around; padding: 10px 0; border-top: 1px solid #EEE; z-index: 999;}
.stButton > button {border-radius: 12px !important; font-weight: 700 !important;}
</style>
""", unsafe_allow_html=True)

def make_hash(p): return hashlib.sha256(p.encode()).hexdigest()
TEMP_HASH = make_hash("row123")
SELLERS = {
    "blessing": {"name": "Blessing Cosmetics", "phone": "07052528772", "password_hash": TEMP_HASH, "verified": True, "location": "Ikorodu, Lagos", "type": "Cosmetics"},
    "horlance": {"name": "Horlance Auto Cooling Ltd", "phone": "09046044472", "calling": "09067551606", "password_hash": TEMP_HASH, "verified": True, "location": "Osun & Oyo", "type": "Services"},
    "admin": {"name": "Admin - Muhammed", "phone": "Admin", "password_hash": TEMP_HASH, "verified": True, "location": "Lagos", "type": "Admin"}
}
if "uploads" not in st.session_state: st.session_state.uploads = []
if "chats" not in st.session_state: st.session_state.chats = {"blessing": [], "horlance": [], "market_square": []}
if "seller" not in st.session_state: st.session_state.seller = None
if "unread" not in st.session_state: st.session_state.unread = {"blessing": 0, "horlance": 0, "market_square": 0}
if "category" not in st.session_state: st.session_state.category = "Home"
if "invite" not in st.session_state: st.session_state.invite = 0
if "cart" not in st.session_state: st.session_state.cart = []
if "liked" not in st.session_state: st.session_state.liked = set()
if "mama_history" not in st.session_state: st.session_state.mama_history = []

# ===== TOP BAR =====
st.markdown(f'<div class="topbar"><span>📍 Ikorodu, Lagos • {datetime.now().strftime("%I:%M %p")}</span><span>🔔 {sum(st.session_state.unread.values())} • 🛒 {len(st.session_state.cart)}</span></div>', unsafe_allow_html=True)

# ===== HERO PREMIUM =====
st.markdown("""
<div class="hero-premium">
<div style="font-size:12px; font-weight:800; letter-spacing:1px;">✦ ROW ECONOMY MARKET ✦</div>
<h1>Everything You<br>Need, <span>Near You.</span></h1>
<p>🧕 Mama Oloja dey here. No scam. No fake. Just real sellers, real prices.</p>
<div><span class="hero-btn">🛍️ Shop Now ↓</span><span class="hero-btn" style="background:#FFD700;">💬 Ask Mama Oloja</span></div>
<div><span class="hero-badge">⭐ 4.9 Rating • 2,347 Happy Buyers</span> <span class="hero-badge">🎉 FREE for Sellers till Dec 6</span></div>
</div>
""", unsafe_allow_html=True)

# ===== FLASH SALE =====
st.markdown("""
<div class="flash"><div><b>⚡ FLASH SALE</b><br><span style="font-size:12px; font-weight:600;">Up to 30% OFF - Today Only</span></div><span>02 : 14 : 33</span></div>
""", unsafe_allow_html=True)

# ===== STORIES - LIKE INSTAGRAM =====
st.markdown("### 📸 Stories - Tap Seller")
st.markdown("""
<div class="story-wrap">
<div class="story"><div class="story-circle">💄</div><span class="story-live">LIVE</span><div class="story-name">Blessing<br>⭐ 4.9</div></div>
<div class="story"><div class="story-circle" style="border-color:#0A9D4D;">❄️</div><span class="story-live" style="background:#0A9D4D;">LIVE</span><div class="story-name">Horlance<br>⭐ 5.0</div></div>
<div class="story"><div class="story-circle" style="border-color:#FFB800;">✨</div><div class="story-name">New<br>Seller?</div></div>
<div class="story"><div class="story-circle" style="border-color:#7B2FFF;">🧕</div><div class="story-name">Mama<br>Oloja</div></div>
</div>
""", unsafe_allow_html=True)

# ===== SEARCH + LOGIN + CART =====
search = st.text_input("", placeholder="🔍 Search serum, sunscreen, Jollof rice, Car AC...", key="search_premium")
if search: st.session_state.category = "Search"

c_top1, c_top2, c_top3 = st.columns(3)
with c_top1:
    if st.button("🎁 Invite +1"):
        st.session_state.invite += 1; st.success(f"You invited {st.session_state.invite} friend(s)!")
with c_top2:
    st.markdown(f"**🛒 Cart: {len(st.session_state.cart)}**")
    if st.session_state.cart:
        tot = sum([x['price'] for x in st.session_state.cart])
        st.markdown(f"Total: **N{tot:,}**")
        st.link_button("Checkout on WhatsApp", "https://wa.me/2347052528772?text=Hi%20I%20want%20to%20checkout%20my%20cart")
        if st.button("Clear Cart"):
            st.session_state.cart=[]; st.rerun()
with c_top3:
    if st.session_state.seller: st.markdown(f"✅ {SELLERS[st.session_state.seller]['name']}")
    else: st.markdown("👤 Guest")

with st.expander("🔐 Seller Login"):
    if st.session_state.seller is None:
        u = st.text_input("Username").lower().strip()
        p = st.text_input("Password", type="password")
        st.caption("Demo: blessing / row123 | horlance / row123 | admin / row123")
        if st.button("Login"):
            if u in SELLERS and make_hash(p)==SELLERS[u]["password_hash"]:
                st.session_state.seller=u; st.rerun()
            else: st.error("Wrong username or password")
    else:
        st.success(f"Logged in as {SELLERS[st.session_state.seller]['name']}")
        if st.button("Logout"): st.session_state.seller=None; st.rerun()

# ===== MAMA OLOJA - CHATGPT STYLE =====
PRODUCTS_DB = [
    {"name": "Face Serum", "price": 4000, "old": 5500, "seller": "Blessing", "phone": "07052528772", "for": "glow dull dark spot pimple uneven tone serum", "desc": "For glow, dark marks, dull skin", "emoji": "💧", "bg": "#E0F7FF", "sold": "1.2k sold", "rating": "4.9"},
    {"name": "Ceramide Serum", "price": 5000, "old": 6500, "seller": "Blessing", "phone": "07052528772", "for": "dry sensitive stressed dehydrated serum", "desc": "For dry, sensitive, stressed skin", "emoji": "💧", "bg": "#FFE0F0", "sold": "890 sold", "rating": "4.8"},
    {"name": "Illuminating Serum", "price": 5500, "old": 7000, "seller": "Blessing", "phone": "07052528772", "for": "glow bright uneven dark spot pimple serum", "desc": "For glow, dark marks", "emoji": "✨", "bg": "#FFF3D6", "sold": "2.1k sold", "rating": "5.0"},
    {"name": "Biore UV Sunscreen", "price": 5000, "old": 6500, "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen protect oily", "desc": "Light, everyday, no white cast", "emoji": "☀️", "bg": "#FFF3D6", "sold": "3.4k sold", "rating": "4.9"},
    {"name": "Nivea Sun Sensitive SPF50", "price": 9000, "old": 11000, "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen sensitive", "desc": "Sensitive skin, immediate protect", "emoji": "☀️", "bg": "#E0F7FF", "sold": "760 sold", "rating": "4.8"},
    {"name": "Skin Aqua SPF50+", "price": 10000, "old": 12000, "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen", "desc": "Super moisture", "emoji": "☀️", "bg": "#E0FFE0", "sold": "540 sold", "rating": "4.7"},
    {"name": "La Roche-Posay Anthelios", "price": 17000, "old": 20000, "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen sensitive pharmacy", "desc": "Pharmacy grade, best for sensitive", "emoji": "☀️", "bg": "#F1EFFF", "sold": "320 sold", "rating": "5.0"},
    {"name": "TONYMOLY Ceramide Toner", "price": 6000, "old": 7500, "seller": "Blessing", "phone": "07052528772", "for": "dry toner sensitive", "desc": "Bouncy, soft, moisturized", "emoji": "💧", "bg": "#FFE0F0", "sold": "980 sold", "rating": "4.8"},
    {"name": "Estelin Whitening Toner", "price": 8000, "old": 9500, "seller": "Blessing", "phone": "07052528772", "for": "toner bright whitening uneven", "desc": "Brightening, uneven tone", "emoji": "💧", "bg": "#FFF3D6", "sold": "670 sold", "rating": "4.7"},
    {"name": "Simple Soothing Toner", "price": 10000, "old": 11500, "seller": "Blessing", "phone": "07052528772", "for": "toner sensitive", "desc": "Alcohol-free, sensitive", "emoji": "💧", "bg": "#E0FFE0", "sold": "430 sold", "rating": "4.8"},
    {"name": "Acwell Licorice Toner", "price": 10500, "old": 12500, "seller": "Blessing", "phone": "07052528772", "for": "toner glow bright pimple", "desc": "Cleansing + Hydrating + Brightening", "emoji": "💧", "bg": "#E0F7FF", "sold": "1.1k sold", "rating": "4.9"},
    {"name": "Nivea Men Lotion 400ml", "price": 5000, "old": 6500, "seller": "Blessing", "phone": "07052528772", "for": "men man lotion dry body", "desc": "For men, fast absorb", "emoji": "💙", "bg": "#E0F7FF", "sold": "1.5k sold", "rating": "4.9"},
    {"name": "AC Gas Recharge", "price": 0, "old": 0, "seller": "Horlance", "phone": "09046044472", "for": "ac car cool gas hot air", "desc": "Car AC gas recharge - ask price", "emoji": "❄️", "bg": "#E0F7FF", "sold": "340 jobs", "rating": "5.0"},
    {"name": "Compressor Repair", "price": 0, "old": 0, "seller": "Horlance", "phone": "09046044472", "for": "ac car compressor noise cool", "desc": "Compressor repair & replacement", "emoji": "🔧", "bg": "#FFF3D6", "sold": "210 jobs", "rating": "5.0"},
    {"name": "AC Leak Fixing", "price": 0, "old": 0, "seller": "Horlance", "phone": "09046044472", "for": "ac car leak gas", "desc": "Leak detection & fixing", "emoji": "🔧", "bg": "#E0FFE0", "sold": "180 jobs", "rating": "4.9"},
    {"name": "Full AC Servicing", "price": 0, "old": 0, "seller": "Horlance", "phone": "09046044472", "for": "ac car servicing full", "desc": "Full AC system servicing", "emoji": "❄️", "bg": "#F1EFFF", "sold": "290 jobs", "rating": "5.0"},
]

def mama_answer(q):
    q=q.lower().strip()
    budget=None
    nums=re.findall(r'(\d+)\s*k', q)
    if nums: budget=int(nums[0])*1000
    else:
        nums2=re.findall(r'(\d{3,})', q.replace(",",""))
        if nums2: budget=int(nums2[0])
    if any(w in q for w in ["hello","hi ","good morning","good afternoon","how are you"]):
        return "Hello my pikin! Welcome to Row Market. Wetin you dey find? Tell me: 1) Product 2) Budget 3) Area. E.g. 'I need serum under 5000 in Ikorodu'"
    food_words=["jollof","rice","food","stew","soup","amala","eba","suya","shawarma","pizza","burger","chicken","hungry"]
    if any(w in q for w in food_words):
        return f"For '{q}' - Honest talk, we NO get food seller YET. Na only Blessing (cosmetics) and Horlance (Car AC) we get. If you be food seller, join FREE - 8 slots left! If you be buyer, tell me your area + budget, I go find food seller for you."
    if any(w in q for w in ["cloth","dress","shirt","shoe","sneaker","bag","wig","hair"]):
        return f"For '{q}' - We no get clothes seller yet. Tell me area + budget, or if YOU sell clothes, join FREE! Tap Clothes to be first!"
    if any(w in q for w in ["phone","iphone","samsung","laptop"]):
        return f"For '{q}' - We no get phone seller yet. Tell me which phone + budget + area."
    if any(w in q for w in ["ac","car","cool","horlance","compressor","gas"]):
        return "For Car AC, na Horlance be number 1! Osun & Oyo. Gas, Compressor, Leak, Full Servicing. WhatsApp 09046044472, Call 09067551606. Tell dem Mama Oloja send you. Wetin be your car problem? Hot air? No gas? Noise?"
    if any(w in q for w in ["pimple","acne","dark spot","dark mark"]):
        return "For pimple / dark spot: 1) Illuminating Serum 5500 (dark marks) 2) Acwell Toner 10500 (cleansing) 3) Biore Sunscreen 5000 (MUST use). If money small, start with Illuminating Serum 5500 only. Chat Blessing - 07052528772"
    if "dry" in q: return "Dry skin? Ceramide Serum 5000 + TONYMOLY Toner 6000 = 11000. Chat Blessing - 07052528772"
    if "oily" in q: return "Oily skin? Face Serum 4000 + Biore Sunscreen 5000 = 9000. Chat Blessing - 07052528772"
    if "sensitive" in q: return "Sensitive? Simple Toner 10000 + Nivea Sun Sensitive 9000 + Ceramide Serum 5000. Chat Blessing - 07052528772"
    matches=[]
    for p in PRODUCTS_DB:
        if any(word in p["name"].lower() or word in p["for"] for word in q.split() if len(word)>2):
            if budget is None or p["price"]==0 or p["price"]<=budget: matches.append(p)
    if matches:
        seen=set(); uniq=[]
        for m in matches:
            if m["name"] not in seen: seen.add(m["name"]); uniq.append(m)
        uniq=sorted(uniq, key=lambda x: x["price"])[:5]
        text="I find for you:"
        for m in uniq:
            pt=f"N{m['price']:,}" if m["price"]>0 else "Chat for price"
            text+=f"\n- {m['name']} - {pt} - {m['desc']} - {m['seller']} {m['phone']}"
        return text
    if budget:
        cheap=[p for p in PRODUCTS_DB if p["price"]>0 and p["price"]<=budget]
        cheap=sorted(cheap, key=lambda x: x["price"])[:6]
        if cheap:
            text=f"With N{budget:,} you fit buy:"
            for m in cheap: text+=f"\n- {m['name']} - N{m['price']:,} - {m['seller']} {m['phone']}"
            return text
    if any(w in q for w in ["cheap","cheapest","affordable"]):
        return "Cheapest: Face Serum 4000, Biore Sunscreen 5000, Ceramide Serum 5000, Nivea Men Lotion 5000. All from Blessing - 07052528772"
    if any(w in q for w in ["best","recommend","suggest"]):
        return "Best: Face Serum 4000, Biore Sunscreen 5000, TONYMOLY Toner 6000. Tell me your skin - dry? oily? pimple?"
    if any(w in q for w in ["sell","seller","join","vendor"]):
        return "You want sell? Join FREE for 1 month - 0% commission. 8 slots left. WhatsApp Admin."
    return f"I hear you - '{q}'. Help me: 1) Wetin exactly? 2) Budget? 3) Area? Tell me those 3, I go give exact answer."

st.markdown("""
<div class="mama-premium">
<div class="mama-header"><div class="mama-avatar">🧕</div><div><b style="font-size:16px;">Mama Oloja</b> <span style="color:#0A9D4D; font-size:12px;">● Online • Replies in 2 secs</span><br><span style="font-size:12px; color:#666;">Your Market Aunty - She sabi price, skin & Car AC</span></div></div>
</div>
""", unsafe_allow_html=True)

# Chat history bubbles
for h in st.session_state.mama_history[-4:]:
    if h["role"]=="user": st.markdown(f'<div class="chat-bubble-user">{h["text"]}</div>', unsafe_allow_html=True)
    else: st.markdown(f'<div class="chat-bubble-mama">🧕 {h["text"]}</div>', unsafe_allow_html=True)

qm1, qm2, qm3 = st.columns(3)
if qm1.button("😩 Pimple"): st.session_state.mama_history.append({"role":"user","text":"I have pimple"}); st.session_state.mama_history.append({"role":"mama","text":mama_answer("I have pimple")}); st.rerun()
if qm2.button("💰 Under 5000"): st.session_state.mama_history.append({"role":"user","text":"Under 5000"}); st.session_state.mama_history.append({"role":"mama","text":mama_answer("under 5000")}); st.rerun()
if qm3.button("❄️ Car AC hot"): st.session_state.mama_history.append({"role":"user","text":"Car AC hot"}); st.session_state.mama_history.append({"role":"mama","text":mama_answer("car ac hot")}); st.rerun()

ask = st.text_input("Ask Mama Oloja...", placeholder="E.g. I need serum under 5000 in Ikorodu...", key="mama_premium")
if ask:
    st.session_state.mama_history.append({"role":"user","text":ask})
    st.session_state.mama_history.append({"role":"mama","text":mama_answer(ask)})
    st.rerun()

# ===== CATEGORIES PREMIUM =====
st.markdown("### 🗂️ Categories")
cat_data = [("💄","Cosmetics","#FBD6E3"),("👕","Clothes","#CDE6FF"),("📱","Phones","#CDE6FF"),("🍲","Food","#FFE2B8"),("🚗","Car Mart","#FFE2B8"),("🧰","Services","#CFF5D6"),("🎟️","Tickets","#FBD6E3"),("💬","Chat","#CFF5D6")]
cols = st.columns(4)
for i,(emo,name,col) in enumerate(cat_data):
    with cols[i%4]:
        st.markdown(f'<div class="cat-premium" style="background:{col};"><div>{emo}</div><span>{name}</span></div>', unsafe_allow_html=True)
        if st.button(name, key=f"cat_p_{name}"): st.session_state.category=name; st.rerun()
if st.button("🏠 Home - Show All"): st.session_state.category="Home"; st.rerun()
st.markdown(f"**Viewing: {st.session_state.category}**")

# ===== SELLER OF THE WEEK =====
st.markdown("""
<div class="seller-week">
<b>👑 SELLER OF THE WEEK</b><br>
<b style="font-size:18px;">❄️ Horlance Auto Cooling Ltd</b> • ⭐ 5.0 • 340 Jobs Done<br>
<span style="font-size:13px; color:#666;">Car AC Specialist - Osun & Oyo - "We Keep You Cool, Always!"</span><br>
<span style="font-size:12px; font-weight:800; color:#0A9D4D;">✅ Verified • 📱 09046044472 • 📞 09067551606</span>
</div>
""", unsafe_allow_html=True)

# ===== LOCATION + UPLOAD =====
with st.expander("📍 Turn On Location"):
    st.components.v1.html("""
<div><button onclick="getLocation()" style="background:#0A9D4D;color:white;padding:12px 20px;border:none;border-radius:12px;width:100%;font-weight:700;">📍 Turn On My Location</button><div id="loc" style="margin-top:10px;padding:10px;background:#E8F5E9;border-radius:10px;"></div></div>
<script>function getLocation(){ if(navigator.geolocation){ document.getElementById("loc").innerHTML="Finding you..."; navigator.geolocation.getCurrentPosition(showPosition,showError);} } function showPosition(p){ var lat=p.coords.latitude; var lon=p.coords.longitude; document.getElementById("loc").innerHTML="Location ON! Lat: "+lat.toFixed(4)+"<br>Lon: "+lon.toFixed(4)+"<br><a href='https://www.google.com/maps?q="+lat+","+lon+"' target='_blank'>View On Map</a>"; } function showError(e){ document.getElementById("loc").innerHTML="Location blocked. Allow in Settings."; }</script>
""", height=160)
    area = st.selectbox("Or pick Area:", ["Select Area","Ikorodu","Ikeja","Lekki","Surulere","Yaba","Gwagwalada","Kubwa","Lugbe","Wuse","Garki","Osun","Oyo","Other"])
    if area!="Select Area": st.success(f"📍 {area}")

with st.expander("📸 Upload Product - Picture / Video (Sellers)"):
    if st.session_state.seller is None: st.info("Login as seller to upload. Demo: blessing / row123")
    else:
        st.success(f"Uploading as: {SELLERS[st.session_state.seller]['name']}")
        up_name = st.text_input("Product Name")
        up_price = st.number_input("Price", min_value=0, step=100)
        up_cat = st.selectbox("Category", ["Cosmetics","Services","Car Mart","Food","Clothes","Phones","Tickets"])
        up_file = st.file_uploader("Upload Picture or Video", type=["jpg","jpeg","png","mp4","mov","webm"])
        up_desc = st.text_area("Description")
        if st.button("Post Product"):
            if up_name and up_file:
                st.session_state.uploads.append({"seller": SELLERS[st.session_state.seller]['name'], "name": up_name, "price": up_price, "desc": up_desc, "file": up_file, "type": up_file.type, "cat": up_cat})
                st.success(f"Posted! {up_name} - N{up_price:,} is LIVE!"); st.rerun()
            else: st.error("Add Name + Picture/Video")

# ===== PRODUCTS PREMIUM =====
def product_card_premium(p, idx):
    discount = ""
    if p['old']>0 and p['price']>0:
        off = int((p['old']-p['price'])/p['old']*100)
        discount = f"<div class='discount'>-{off}% OFF</div>"
    heart = "❤️" if p['name'] in st.session_state.liked else "🤍"
    price_txt = f"N{p['price']:,}" if p['price']>0 else "Chat for Price"
    old_txt = f"<span class='old'>N{p['old']:,}</span>" if p['old']>p['price'] and p['price']>0 else ""
    st.markdown(f"""
    <div class="product-premium">
    <div class="product-top" style="background:{p['bg']};">{discount}<div class="heart">{heart}</div>{p['emoji']}</div>
    <div class="product-body">
    <div style="font-weight:900; font-size:15px;">{p['name']}</div>
    <div style="font-size:12px; color:#888;">by {p['seller']} ✅ Verified • {p['sold']}</div>
    <div><span class="stars">⭐ {p['rating']}</span> <span style="font-size:12px; color:#666;">({p['sold']})</span></div>
    <div style="margin:6px 0;"><span class="price-big">{price_txt}</span> {old_txt}</div>
    <div style="font-size:13px; color:#666;">{p['desc']}</div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    with c1:
        if st.button("❤️", key=f"like_{p['name']}_{idx}"):
            if p['name'] in st.session_state.liked: st.session_state.liked.remove(p['name'])
            else: st.session_state.liked.add(p['name'])
            st.rerun()
    with c2:
        if st.button("🛒 Add", key=f"add_p_{p['name']}_{idx}"):
            st.session_state.cart.append(p); st.success(f"Added {p['name']}!"); st.rerun()
    with c3:
        st.link_button("💬 Chat", f"https://wa.me/234{p['phone'][1:]}?text=Hi%20I%20want%20{p['name']}%20from%20Row%20Economy%20Market")

to_show = PRODUCTS_DB
if st.session_state.category=="Cosmetics": to_show=[p for p in PRODUCTS_DB if p['seller']=="Blessing"]
elif st.session_state.category in ["Services","Car Mart"]: to_show=[p for p in PRODUCTS_DB if p['seller']=="Horlance"]
elif st.session_state.category=="Search" and search:
    to_show=[p for p in PRODUCTS_DB if search.lower() in p['name'].lower() or search.lower() in p['for']]
    if not to_show: st.warning(f"No product for '{search}' yet. Ask Mama Oloja!")
elif st.session_state.category in ["Clothes","Phones","Food","Tickets"]:
    st.info(f"No seller yet in {st.session_state.category}. Be FIRST! Join FREE - 8 slots left.")
    to_show=[]
    st.link_button("Join as Seller", "https://wa.me/2347052528772?text=Hi%20I%20want%20to%20sell%20in%20Row%20Economy%20Market")

if st.session_state.uploads:
    st.markdown("### 🆕 New Uploads From Sellers")
    for item in reversed(st.session_state.uploads):
        if st.session_state.category=="Home" or item['cat']==st.session_state.category:
            st.markdown(f"**{item['name']} - N{item['price']:,}** by {item['seller']} | {item['cat']}")
            st.markdown(item['desc'])
            if item['type'].startswith("image"): st.image(item['file'], width=320)
            elif item['type'].startswith("video"): st.video(item['file'])

if to_show and st.session_state.category!="Chat":
    if st.session_state.category=="Home": st.markdown("### 🔥 Hot Deals - Today Only")
    elif st.session_state.category=="Search": st.markdown("### 🔍 Search Results")
    else: st.markdown(f"### {st.session_state.category}")
    for idx,p in enumerate(to_show):
        product_card_premium(p, idx)

# ===== TESTIMONIALS =====
st.markdown("### 💬 What Buyers Say")
st.markdown("""
<div class="testimonial"><b>⭐⭐⭐⭐⭐ Chiamaka - Ikorodu</b><br>"Mama Oloja helped me pick correct serum. My face don glow! Blessing delivered same day."</div>
<div class="testimonial"><b>⭐⭐⭐⭐⭐ Tunde - Osun</b><br>"Horlance fixed my AC in 1 hour. Cold like fridge now. I recommend!"</div>
<div class="testimonial"><b>⭐⭐⭐⭐⭐ Fatima - Lagos</b><br>"I thought it was scam, but Mama Oloja no dey lie. Real sellers, real prices."</div>
""", unsafe_allow_html=True)

# ===== CHAT =====
if st.session_state.category in ["Home","Chat"]:
    st.markdown("### 💬 Chat Rooms - Like Messenger")
    chat_choice = st.selectbox("Who to chat?", ["Market Square - Everybody", "Chat Blessing", "Chat Horlance"])
    room = "market_square" if "Market" in chat_choice else "blessing" if "Blessing" in chat_choice else "horlance"
    if st.session_state.unread[room]>0:
        st.warning(f"🔔 {st.session_state.unread[room]} new message(s)!")
        if st.button("Mark as Read"): st.session_state.unread[room]=0; st.rerun()
    for m in st.session_state.chats[room]:
        st.markdown(f"**{m['sender']}:** {m['text']}")
    yn = st.text_input("Your Name", key=f"n_{room}")
    mt = st.text_input("Type message...", key=f"m_{room}")
    if st.button("Send Message", key=f"s_{room}"):
        if yn and mt:
            st.session_state.chats[room].append({"sender": yn, "text": mt})
            st.session_state.unread[room]+=1
            st.success("Sent! Seller will see notification."); st.rerun()
    if st.session_state.seller:
        rep = st.text_input("Reply as Seller...", key=f"r_{room}")
        if st.button("Reply as Seller", key=f"rb_{room}"):
            if rep:
                st.session_state.chats[room].append({"sender": f"{SELLERS[st.session_state.seller]['name']} (Seller)", "text": rep}); st.rerun()

st.markdown("---")
st.markdown("**How to Pay:** Chat seller -> Confirm price -> Transfer / Pay on delivery -> Delivered. No scam, Mama Oloja dey watch.")
st.markdown("**Want to Sell?** Join FREE - 8 slots left. WhatsApp Admin.")
st.markdown("© 2026 Row Economy Market - Powered by Mama Oloja 🧕")
st.markdown("<br><br>", unsafe_allow_html=True)
