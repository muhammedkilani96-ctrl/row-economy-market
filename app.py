import streamlit as st
import hashlib
import re

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="centered")

st.markdown("""
<style>
.main {background-color: #FFFBF5;}
.big-title {font-size:32px; font-weight:800; color:#111; line-height:1.1;}
.sub {color:#666; font-size:15px;}
.cat-box {border-radius:20px; padding:18px 5px; text-align:center; font-weight:700; font-size:15px;}
.pink {background:#FBD6E3;} .blue {background:#CDE6FF;} .orange {background:#FFE2B8;} .green {background:#CFF5D6;}
.card {background:white; border-radius:18px; padding:14px; box-shadow:0 2px 10px rgba(0,0,0,0.07); margin-bottom:14px;}
.price {color:#0A9D4D; font-weight:800; font-size:18px;}
.small {font-size:13px; color:#666;}
</style>
""", unsafe_allow_html=True)

def make_hash(p):
    return hashlib.sha256(p.encode()).hexdigest()
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

# ===== HEADER =====
st.markdown('<div class="big-title">🛒 Row Economy<br>Market</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Powered by Mama Oloja - She Knows All Prices<br>FREE for 1 Month - Nov 6 to Dec 6 - 0% Commission</div>', unsafe_allow_html=True)

if st.button("I Invited a Friend +1"):
    st.session_state.invite += 1
    st.success(f"Thank you! You have invited {st.session_state.invite} friend(s).")
st.markdown(f"**Your Invites: {st.session_state.invite}**")

# ===== LOGIN =====
with st.expander("Seller Login - Click Here"):
    if st.session_state.seller is None:
        u = st.text_input("Username").lower().strip()
        p = st.text_input("Password", type="password")
        st.caption("Demo: blessing / row123 | horlance / row123 | admin / row123")
        if st.button("Login"):
            if u in SELLERS and make_hash(p) == SELLERS[u]["password_hash"]:
                st.session_state.seller = u
                st.rerun()
            else:
                st.error("Wrong username or password")
    else:
        st.success(f"Logged in as {SELLERS[st.session_state.seller]['name']}")
        total = sum(st.session_state.unread.values())
        if total > 0:
            st.error(f"You have {total} new message(s)!")
        if st.button("Logout"):
            st.session_state.seller = None
            st.rerun()

# ===== MAMA OLOJA V4 - SMART - ONLY ONE COPY HERE =====
PRODUCTS_DB = [
    {"name": "Face Serum", "price": 4000, "seller": "Blessing", "phone": "07052528772", "for": "glow dull dark spot pimple uneven tone serum", "desc": "For glow, dark marks"},
    {"name": "Ceramide Serum", "price": 5000, "seller": "Blessing", "phone": "07052528772", "for": "dry sensitive stressed dehydrated serum", "desc": "For dry, sensitive skin"},
    {"name": "Illuminating Serum 10% Niacinamide", "price": 5500, "seller": "Blessing", "phone": "07052528772", "for": "glow bright uneven dark spot pimple serum", "desc": "For glow, dark marks"},
    {"name": "Biore UV Sunscreen", "price": 5000, "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen protect oily", "desc": "Light, everyday"},
    {"name": "Nivea Sun Sensitive SPF50", "price": 9000, "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen sensitive", "desc": "For sensitive skin"},
    {"name": "Skin Aqua SPF50+", "price": 10000, "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen", "desc": "Super moisture"},
    {"name": "La Roche-Posay Anthelios", "price": 17000, "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen sensitive pharmacy", "desc": "Pharmacy grade"},
    {"name": "TONYMOLY Ceramide Toner", "price": 6000, "seller": "Blessing", "phone": "07052528772", "for": "dry toner sensitive", "desc": "Bouncy, soft"},
    {"name": "Estelin Whitening Toner", "price": 8000, "seller": "Blessing", "phone": "07052528772", "for": "toner bright whitening uneven", "desc": "Brightening"},
    {"name": "Simple Soothing Toner", "price": 10000, "seller": "Blessing", "phone": "07052528772", "for": "toner sensitive", "desc": "Alcohol-free"},
    {"name": "Acwell Licorice Toner", "price": 10500, "seller": "Blessing", "phone": "07052528772", "for": "toner glow bright pimple", "desc": "Cleansing + Brightening"},
    {"name": "Nivea Men Lotion 400ml", "price": 5000, "seller": "Blessing", "phone": "07052528772", "for": "men man lotion dry body", "desc": "For men, fast absorb"},
    {"name": "AC Gas Recharge", "price": 0, "seller": "Horlance", "phone": "09046044472", "for": "ac car cool gas hot air", "desc": "Car AC gas recharge"},
    {"name": "Compressor Repair", "price": 0, "seller": "Horlance", "phone": "09046044472", "for": "ac car compressor noise cool", "desc": "Compressor repair"},
    {"name": "AC Leak Fixing", "price": 0, "seller": "Horlance", "phone": "09046044472", "for": "ac car leak gas", "desc": "Leak detection"},
    {"name": "Full AC Servicing", "price": 0, "seller": "Horlance", "phone": "09046044472", "for": "ac car servicing full", "desc": "Full servicing"},
]

def mama_answer(q):
    q = q.lower().strip()
    budget = None
    nums = re.findall(r'(\d+)\s*k', q)
    if nums:
        budget = int(nums[0]) * 1000
    else:
        nums2 = re.findall(r'(\d{3,})', q.replace(",", ""))
        if nums2:
            budget = int(nums2[0])
    if any(w in q for w in ["hello", "hi ", "good morning", "good afternoon", "how are you"]):
        return "Mama Oloja: Hello my pikin! Welcome. Wetin you dey find? Tell me: 1) Product 2) Budget 3) Area. E.g. 'I need serum under 5000 in Ikorodu'"
    food_words = ["jollof", "rice", "food", "stew", "soup", "amala", "eba", "suya", "shawarma", "pizza", "burger", "chicken", "hungry"]
    if any(w in q for w in food_words):
        return f"Mama Oloja: For '{q}' - Honest talk, we NO get food seller YET. Na only Blessing (cosmetics) and Horlance (Car AC) we get now. If you be food seller, join FREE - 8 slots left! If you be buyer, tell me your area and budget, I go find food seller for you."
    if any(w in q for w in ["cloth", "dress", "shirt", "shoe", "sneaker", "bag", "wig", "hair"]):
        return f"Mama Oloja: For '{q}' - We no get clothes seller yet. Tell me your area + budget, or if YOU sell clothes, join FREE! Tap Clothes to be first!"
    if any(w in q for w in ["phone", "iphone", "samsung", "laptop"]):
        return f"Mama Oloja: For '{q}' - We no get phone seller yet. Tell me which phone + budget + area, I go find am for you."
    if any(w in q for w in ["ac", "car", "cool", "horlance", "compressor", "gas"]):
        return "Mama Oloja: For Car AC, na Horlance be number 1! Osun & Oyo. Gas Recharge, Compressor Repair, Leak Fixing, Full Servicing. WhatsApp 09046044472, Call 09067551606. Tell dem Mama Oloja send you."
    if any(w in q for w in ["pimple", "acne", "dark spot", "dark mark"]):
        return "Mama Oloja: For pimple / dark spot: 1) Illuminating Serum 5500 2) Acwell Toner 10500 3) Biore Sunscreen 5000. If money small, start with Illuminating Serum 5500 only. Chat Blessing - 07052528772"
    if "dry" in q:
        return "Mama Oloja: Dry skin? Take Ceramide Serum 5000 + TONYMOLY Toner 6000 = 11000. Chat Blessing - 07052528772"
    if "oily" in q:
        return "Mama Oloja: Oily skin? Take Face Serum 4000 + Biore Sunscreen 5000 = 9000. Chat Blessing - 07052528772"
    if "sensitive" in q:
        return "Mama Oloja: Sensitive? Take Simple Toner 10000 + Nivea Sun Sensitive 9000 + Ceramide Serum 5000. Chat Blessing - 07052528772"
    matches = []
    for p in PRODUCTS_DB:
        if any(word in p["name"].lower() or word in p["for"] for word in q.split() if len(word) > 2):
            if budget is None or p["price"] == 0 or p["price"] <= budget:
                matches.append(p)
    if matches:
        seen = set(); uniq = []
        for m in matches:
            if m["name"] not in seen:
                seen.add(m["name"]); uniq.append(m)
        uniq = sorted(uniq, key=lambda x: x["price"])[:5]
        text = "Mama Oloja: I find for you:"
        for m in uniq:
            price_txt = f"N{m['price']:,}" if m["price"] > 0 else "Chat for price"
            text += f"\n- {m['name']} - {price_txt} - {m['desc']} - {m['seller']} {m['phone']}"
        text += "\nWhich one you want?"
        return text
    if budget:
        cheap = [p for p in PRODUCTS_DB if p["price"] > 0 and p["price"] <= budget]
        cheap = sorted(cheap, key=lambda x: x["price"])[:6]
        if cheap:
            text = f"Mama Oloja: With N{budget:,} you fit buy:"
            for m in cheap:
                text += f"\n- {m['name']} - N{m['price']:,} - {m['seller']} {m['phone']}"
            return text
    if any(w in q for w in ["cheap", "cheapest", "affordable"]):
        return "Mama Oloja: Cheapest: Face Serum 4000, Biore Sunscreen 5000, Ceramide Serum 5000, Nivea Men Lotion 5000. All from Blessing - 07052528772"
    if any(w in q for w in ["best", "recommend", "suggest"]):
        return "Mama Oloja: Best: Face Serum 4000, Biore Sunscreen 5000, TONYMOLY Toner 6000. Tell me your skin - dry? oily? pimple? - I go pick exact one for YOU."
    if any(w in q for w in ["where", "location", "area", "ikorodu", "abuja", "lagos", "osun", "oyo"]):
        return "Mama Oloja: Blessing dey Ikorodu, Lagos / Abuja - 07052528772. Horlance dey Osun & Oyo - 09046044472. Where you dey?"
    if any(w in q for w in ["sell", "seller", "join", "vendor"]):
        return "Mama Oloja: You want sell? Join FREE for 1 month - 0% commission. 8 slots left. WhatsApp Admin, tell us wetin you sell + area + picture."
    return f"Mama Oloja: I hear you - '{q}'. Help me help you: 1) Wetin exactly? (serum, sunscreen, food, car AC) 2) Budget? (e.g. 5000) 3) Area? (Ikorodu, Osun, Abuja?) Tell me those 3, I go give exact answer."

st.markdown("### Ask Mama Oloja - She Sabi Everything Now")
st.markdown("Try: 'Jollof rice' | 'I have pimple' | 'I need serum under 5000' | 'My car AC hot'")
ask = st.text_input("Wetin you dey find?", placeholder="E.g. I need serum under 5000 in Ikorodu...")
if ask:
    st.success(mama_answer(ask))

# ===== CATEGORIES =====
st.markdown("### Categories")
st.markdown("Tap a category - you will see ONLY that category:")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="cat-box pink">Cosmetics</div>', unsafe_allow_html=True)
    if st.button("Cosmetics", key="cat_cos"): st.session_state.category = "Cosmetics"; st.rerun()
with c2:
    st.markdown('<div class="cat-box blue">Clothes</div>', unsafe_allow_html=True)
    if st.button("Clothes", key="cat_clo"): st.session_state.category = "Clothes"; st.rerun()
with c3:
    st.markdown('<div class="cat-box blue">Phones</div>', unsafe_allow_html=True)
    if st.button("Phones", key="cat_pho"): st.session_state.category = "Phones"; st.rerun()
with c4:
    st.markdown('<div class="cat-box orange">Food</div>', unsafe_allow_html=True)
    if st.button("Food", key="cat_food"): st.session_state.category = "Food"; st.rerun()
c5, c6, c7, c8 = st.columns(4)
with c5:
    st.markdown('<div class="cat-box orange">Car Mart</div>', unsafe_allow_html=True)
    if st.button("Car Mart", key="cat_car"): st.session_state.category = "Car Mart"; st.rerun()
with c6:
    st.markdown('<div class="cat-box green">Services</div>', unsafe_allow_html=True)
    if st.button("Services", key="cat_ser"): st.session_state.category = "Services"; st.rerun()
with c7:
    st.markdown('<div class="cat-box pink">Tickets</div>', unsafe_allow_html=True)
    if st.button("Tickets", key="cat_tick"): st.session_state.category = "Tickets"; st.rerun()
with c8:
    st.markdown('<div class="cat-box green">Chat Rooms</div>', unsafe_allow_html=True)
    if st.button("Chat Rooms", key="cat_chat"): st.session_state.category = "Chat Rooms"; st.rerun()

st.markdown(f"**You are viewing: {st.session_state.category}**")
if st.button("Home - Show All"):
    st.session_state.category = "Home"; st.rerun()

# ===== LOCATION =====
with st.expander("Turn On Your Real Location"):
    st.components.v1.html("""
<div style="word-wrap:break-word;">
<button onclick="getLocation()" style="background:#25D366;color:white;padding:14px 20px;border:none;border-radius:12px;width:100%;font-weight:700;">Turn On My Location</button>
<div id="loc" style="margin-top:10px;padding:10px;background:#E8F5E9;border-radius:10px;"></div>
</div>
<script>
function getLocation(){ if(navigator.geolocation){ document.getElementById("loc").innerHTML="Finding you..."; navigator.geolocation.getCurrentPosition(showPosition,showError);} }
function showPosition(p){ var lat=p.coords.latitude; var lon=p.coords.longitude; document.getElementById("loc").innerHTML="Location ON! Lat: "+lat.toFixed(4)+"<br>Lon: "+lon.toFixed(4)+"<br><a href='https://www.google.com/maps?q="+lat+","+lon+"' target='_blank'>View On Google Map</a>"; }
function showError(e){ document.getElementById("loc").innerHTML="Location blocked. Go to Settings > Location > Allow."; }
</script>
""", height=180)
    area = st.selectbox("Or pick Area:", ["Select Area","Ikorodu","Ikeja","Lekki","Surulere","Yaba","Gwagwalada","Kubwa","Lugbe","Wuse","Garki","Osun","Oyo","Other"])
    if area != "Select Area":
        st.success(f"Location set to: {area}")

# ===== UPLOAD =====
with st.expander("Upload Product - Picture / Video (Sellers Only)"):
    if st.session_state.seller is None:
        st.info("Login as seller to upload. Demo: blessing / row123")
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
                st.success(f"Posted! {up_name} - N{up_price:,} is LIVE!")
                st.rerun()
            else:
                st.error("Add Name + Picture/Video")

if st.session_state.uploads:
    st.markdown("### New Uploads")
    for item in reversed(st.session_state.uploads):
        if st.session_state.category == "Home" or item['cat'] == st.session_state.category:
            st.markdown(f"**{item['name']} - N{item['price']:,}** by {item['seller']} | {item['cat']}")
            st.markdown(item['desc'])
            if item['type'].startswith("image"): st.image(item['file'], width=320)
            elif item['type'].startswith("video"): st.video(item['file'])

def show_card(title, price, seller, desc, phone):
    st.markdown(f"""<div class="card"><b>{title}</b><br><span class="price">N{price:,}</span><br><span class="small">by {seller} | Verified</span><br><span class="small">{desc}</span></div>""", unsafe_allow_html=True)
    st.link_button(f"Chat {seller} - {phone}", f"https://wa.me/234{phone[1:]}?text=Hi%20I%20want%20{title}%20from%20Row%20Economy%20Market")

if st.session_state.category in ["Home", "Cosmetics"]:
    st.markdown("### Cosmetics - Blessing Cosmetics")
    st.markdown("Verified | Ikorodu, Lagos | 07052528772")
    show_card("Face Serum - 30ml", 4000, "Blessing", "Active Caviar, Niacinamide", "07052528772")
    show_card("Ceramide Serum", 5000, "Blessing", "For dry/stressed skin", "07052528772")
    show_card("Illuminating Serum 10% Niacinamide", 5500, "Blessing", "For glow, dark marks", "07052528772")
    show_card("Biore UV Sunscreen SPF50+", 5000, "Blessing", "Light, everyday", "07052528772")
    show_card("Nivea Sun Sensitive SPF50", 9000, "Blessing", "Sensitive skin", "07052528772")
    show_card("Skin Aqua SPF50+", 10000, "Blessing", "Super moisture", "07052528772")
    show_card("La Roche-Posay Anthelios", 17000, "Blessing", "Pharmacy grade", "07052528772")
    show_card("TONYMOLY Ceramide Toner", 6000, "Blessing", "Bouncy, soft", "07052528772")
    show_card("Estelin Whitening Toner", 8000, "Blessing", "Brightening", "07052528772")
    show_card("Simple Soothing Toner", 10000, "Blessing", "Alcohol-free", "07052528772")
    show_card("Acwell Licorice Toner", 10500, "Blessing", "Cleansing + Brightening", "07052528772")
    show_card("Nivea Men Lotion 400ml", 5000, "Blessing", "For men", "07052528772")

if st.session_state.category in ["Home", "Services", "Car Mart"]:
    st.markdown("### Services - Horlance Auto Cooling Ltd")
    st.markdown("Verified | Osun & Oyo | WhatsApp 09046044472 | Call 09067551606")
    st.markdown("Car AC Repair Specialist - We Keep You Cool!")
    show_card("AC Diagnosis", 0, "Horlance", "We find fault fast", "09046044472")
    show_card("Gas Recharge", 0, "Horlance", "Refrigerant Gas", "09046044472")
    show_card("Compressor Repair", 0, "Horlance", "Compressor expert", "09046044472")
    show_card("Leak Fixing", 0, "Horlance", "Leak detection", "09046044472")
    show_card("Full AC Servicing", 0, "Horlance", "Complete servicing", "09046044472")
    st.link_button("Call Horlance", "tel:09067551606")

if st.session_state.category in ["Clothes", "Phones", "Food", "Tickets"]:
    st.info(f"No seller yet in {st.session_state.category}. Be FIRST! WhatsApp Admin to join FREE. 8 slots left.")

if st.session_state.category in ["Home", "Chat Rooms"]:
    st.markdown("### Chat Rooms - Like Messenger")
    chat_choice = st.selectbox("Who to chat?", ["Market Square - Everybody", "Chat Blessing", "Chat Horlance"])
    room = "market_square" if "Market" in chat_choice else "blessing" if "Blessing" in chat_choice else "horlance"
    if st.session_state.unread[room] > 0:
        st.warning(f"{st.session_state.unread[room]} new message(s)!")
        if st.button("Mark as Read"):
            st.session_state.unread[room] = 0; st.rerun()
    for m in st.session_state.chats[room]:
        st.markdown(f"**{m['sender']}:** {m['text']}")
    yn = st.text_input("Your Name", key=f"n_{room}")
    mt = st.text_input("Type message...", key=f"m_{room}")
    if st.button("Send Message", key=f"s_{room}"):
        if yn and mt:
            st.session_state.chats[room].append({"sender": yn, "text": mt})
            st.session_state.unread[room] += 1
            st.success("Sent! Seller will see notification.")
            st.rerun()
    if st.session_state.seller:
        rep = st.text_input("Reply as Seller...", key=f"r_{room}")
        if st.button("Reply as Seller", key=f"rb_{room}"):
            if rep:
                st.session_state.chats[room].append({"sender": f"{SELLERS[st.session_state.seller]['name']} (Seller)", "text": rep})
                st.rerun()

st.markdown("---")
st.markdown("How to Pay: Chat seller -> Confirm price -> Transfer / Pay on delivery -> Delivered.")
st.markdown("2026 Row Economy Market - Powered by Mama Oloja")
