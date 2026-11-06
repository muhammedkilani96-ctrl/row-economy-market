import streamlit as st
import hashlib

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="centered")

# ============ BEAUTIFUL CSS - LIKE YOUR SCREENSHOT ============
st.markdown("""
<style>
.main {background-color: #FFFBF5;}
.big-title {font-size:32px; font-weight:800; color:#111; line-height:1.1;}
.sub {color:#666; font-size:15px;}
.cat-box {border-radius:20px; padding:18px 5px; text-align:center; font-weight:700; font-size:15px; margin-bottom:5px;}
.pink {background:#FBD6E3;} .blue {background:#CDE6FF;} .orange {background:#FFE2B8;}
.green {background:#CFF5D6;} .yellow {background:#FFF0B8;}
.card {background:white; border-radius:18px; padding:14px; box-shadow:0 2px 10px rgba(0,0,0,0.07); margin-bottom:14px;}
.price {color:#0A9D4D; font-weight:800; font-size:18px;}
.btn-green {background:#25D366; color:white; padding:10px 18px; border-radius:12px; text-align:center; font-weight:700;}
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

# ============ TOP HEADER ============
st.markdown('<div class="big-title">🛒 Row Economy<br>Market</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Powered by Mama Oloja 🧕 - She Knows All Prices<br>🎉 FREE for 1 Month - Nov 6 to Dec 6 - 0% Commission</div>', unsafe_allow_html=True)

# Invite button
if st.button("🎁 I Invited a Friend +1"):
    st.session_state.invite += 1
    st.success(f"Thank you! You have invited {st.session_state.invite} friend(s). Keep inviting!")
st.markdown(f"**Your Invites: {st.session_state.invite}**")

# Login - small at top
with st.expander("🔐 Seller Login - Click Here"):
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
        st.success(f"Logged in as {SELLERS[st.session_state.seller]['name']} ✅")
        total = sum(st.session_state.unread.values())
        if total > 0:
            st.error(f"🔔 You have {total} new message(s)!")
        if st.button("Logout"):
            st.session_state.seller = None
            st.rerun()

# ============ MAMA OLOJA ============
st.markdown("### 🧕 Ask Mama Oloja")
ask = st.text_input("Wetin you dey find?", placeholder="E.g. I need sunscreen under 10000...")
if ask:
    q = ask.lower()
    if "ac" in q or "car" in q or "horlance" in q:
        st.success("🧕 Mama Oloja: For Car AC, na Horlance be number 1! Osun & Oyo. WhatsApp 09046044472, Call 09067551606. Tell dem Mama Oloja send you!")
    elif "sunscreen" in q or "sun" in q:
        st.success("🧕 Mama Oloja: Sunscreen: Biore ₦5,000, Nivea ₦9,000, Skin Aqua ₦10,000, La Roche-Posay ₦17,000. Chat Blessing - 07052528772")
    elif "serum" in q or "glow" in q:
        st.success("🧕 Mama Oloja: Serum: Face ₦4,000, Ceramide ₦5,000, Illuminating ₦5,500. Chat Blessing - 07052528772")
    elif "toner" in q:
        st.success("🧕 Mama Oloja: Toner: TONYMOLY ₦6,000, Estelin ₦8,000, Simple ₦10,000, Acwell ₦10,500. Chat Blessing - 07052528772")
    else:
        st.success(f"🧕 Mama Oloja: My pikin, for '{ask}' - Check Blessing for cosmetics, Horlance for Car AC. Blessing: 07052528772 | Horlance: 09046044472")

# ============ CATEGORIES - LIKE YOUR SCREENSHOT ============
st.markdown("### Categories")
st.markdown("Tap a category - you will see ONLY that category:")

# Row 1
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="cat-box pink">💄<br>Cosmetics</div>', unsafe_allow_html=True)
    if st.button("Cosmetics", key="cat_cos"): st.session_state.category = "Cosmetics"; st.rerun()
with c2:
    st.markdown('<div class="cat-box blue">👕<br>Clothes</div>', unsafe_allow_html=True)
    if st.button("Clothes", key="cat_clo"): st.session_state.category = "Clothes"; st.rerun()
with c3:
    st.markdown('<div class="cat-box blue">📱<br>Phones</div>', unsafe_allow_html=True)
    if st.button("Phones", key="cat_pho"): st.session_state.category = "Phones"; st.rerun()
with c4:
    st.markdown('<div class="cat-box orange">🍲<br>Food</div>', unsafe_allow_html=True)
    if st.button("Food", key="cat_food"): st.session_state.category = "Food"; st.rerun()

# Row 2
c5, c6, c7, c8 = st.columns(4)
with c5:
    st.markdown('<div class="cat-box orange">🚗<br>Car Mart</div>', unsafe_allow_html=True)
    if st.button("Car Mart", key="cat_car"): st.session_state.category = "Car Mart"; st.rerun()
with c6:
    st.markdown('<div class="cat-box green">🧰<br>Services</div>', unsafe_allow_html=True)
    if st.button("Services", key="cat_ser"): st.session_state.category = "Services"; st.rerun()
with c7:
    st.markdown('<div class="cat-box pink">🎟️<br>Tickets</div>', unsafe_allow_html=True)
    if st.button("Tickets", key="cat_tick"): st.session_state.category = "Tickets"; st.rerun()
with c8:
    st.markdown('<div class="cat-box green">💬<br>Chat Rooms</div>', unsafe_allow_html=True)
    if st.button("Chat Rooms", key="cat_chat"): st.session_state.category = "Chat Rooms"; st.rerun()

st.markdown(f"**You are viewing: {st.session_state.category}** | [🏠 Show All / Home]")
if st.button("🏠 Home - Show All"):
    st.session_state.category = "Home"; st.rerun()

# ============ LOCATION - FIXED ============
with st.expander("📍 Turn On Your Real Location"):
    st.markdown("We show only your AREA, not your house.")
    st.components.v1.html("""
<div style="word-wrap:break-word;">
<button onclick="getLocation()" style="background:#25D366;color:white;padding:14px 20px;border:none;border-radius:12px;width:100%;font-weight:700;">📍 Turn On My Location</button>
<div id="loc" style="margin-top:10px;padding:10px;background:#E8F5E9;border-radius:10px;line-height:1.6;"></div>
</div>
<script>
function getLocation(){ if(navigator.geolocation){ document.getElementById("loc").innerHTML="Finding you... allow location..."; navigator.geolocation.getCurrentPosition(showPosition,showError);} else {document.getElementById("loc").innerHTML="Phone does not support location.";} }
function showPosition(p){ var lat=p.coords.latitude; var lon=p.coords.longitude; var area="Ikorodu, Lagos"; if(lat>6.5&&lat<6.65) area="Ikorodu, Lagos"; document.getElementById("loc").innerHTML="✅ Location ON!<br>Lat: "+lat.toFixed(4)+"<br>Lon: "+lon.toFixed(4)+"<br>Area: "+area+"<br><a href='https://www.google.com/maps?q="+lat+","+lon+"' target='_blank'>📍 View On Google Map</a>"; }
function showError(e){ document.getElementById("loc").innerHTML="❌ Location blocked. Go to Settings > Location > Allow."; }
</script>
""", height=180)
    area = st.selectbox("Or pick Area:", ["Select Area","Ikorodu","Ikeja","Lekki","Surulere","Yaba","Gwagwalada","Kubwa","Lugbe","Wuse","Garki","Osun","Oyo","Other"])
    if area != "Select Area":
        st.success(f"📍 Location set to: {area}")

# ============ UPLOAD ============
with st.expander("📸 Upload Product - Picture / Video (Sellers Only)"):
    if st.session_state.seller is None:
        st.info("Login as seller to upload. Demo: blessing / row123")
    else:
        st.success(f"Uploading as: {SELLERS[st.session_state.seller]['name']}")
        up_name = st.text_input("Product Name")
        up_price = st.number_input("Price ₦", min_value=0, step=100)
        up_cat = st.selectbox("Category", ["Cosmetics","Services","Car Mart","Food","Clothes","Phones","Tickets"])
        up_file = st.file_uploader("Upload Picture or Video", type=["jpg","jpeg","png","mp4","mov","webm"])
        up_desc = st.text_area("Description")
        if st.button("📤 Post Product"):
            if up_name and up_file:
                st.session_state.uploads.append({"seller": SELLERS[st.session_state.seller]['name'], "name": up_name, "price": up_price, "desc": up_desc, "file": up_file, "type": up_file.type, "cat": up_cat})
                st.success(f"✅ Posted! {up_name} - ₦{up_price:,} is LIVE!")
                st.rerun()
            else:
                st.error("Add Name + Picture/Video")

# ============ SHOW CONTENT BY CATEGORY ============
def show_card(title, price, seller, desc, phone):
    st.markdown(f"""
    <div class="card">
    <b>{title}</b><br>
    <span class="price">₦{price:,}</span><br>
    <span class="small">by {seller} | ✅ Verified</span><br>
    <span class="small">{desc}</span>
    </div>
    """, unsafe_allow_html=True)
    st.link_button(f"Chat {seller} - {phone}", f"https://wa.me/234{phone[1:]}?text=Hi%20I%20want%20{title}%20from%20Row%20Economy%20Market")

# Show uploads filtered by category
if st.session_state.uploads:
    st.markdown("### 🆕 New Uploads")
    for item in reversed(st.session_state.uploads):
        if st.session_state.category == "Home" or item['cat'] == st.session_state.category:
            st.markdown(f"**{item['name']} - ₦{item['price']:,}** by {item['seller']} | {item['cat']}")
            st.markdown(item['desc'])
            if item['type'].startswith("image"): st.image(item['file'], width=320)
            elif item['type'].startswith("video"): st.video(item['file'])

# COSMETICS - Blessing
if st.session_state.category in ["Home", "Cosmetics"]:
    st.markdown("### 💄 Cosmetics - Blessing Cosmetics")
    st.markdown("✅ Verified | 📍 Ikorodu, Lagos | 📱 07052528772")
    show_card("Face Serum - 30ml", 4000, "Blessing", "Active Caviar, Niacinamide, Hyaluronic", "07052528772")
    show_card("Ceramide Serum", 5000, "Blessing", "Nourish + Restore, for dry/stressed skin", "07052528772")
    show_card("Illuminating Serum 10% Niacinamide", 5500, "Blessing", "For glow, uneven tone, dark marks", "07052528772")
    show_card("Biore UV Sunscreen SPF50+", 5000, "Blessing", "Light, everyday face sunscreen", "07052528772")
    show_card("Nivea Sun Sensitive SPF50", 9000, "Blessing", "Sensitive skin, immediate protect", "07052528772")
    show_card("Skin Aqua Super Moisture UV SPF50+", 10000, "Blessing", "Super moisture, no white cast", "07052528772")
    show_card("La Roche-Posay Anthelios UVMune 400", 17000, "Blessing", "Pharmacy grade, sensitive skin", "07052528772")
    show_card("TONYMOLY Ceramide Mochi Toner", 6000, "Blessing", "Bouncy, soft, moisturized", "07052528772")
    show_card("Estelin Whitening Toner", 8000, "Blessing", "Brightening, uneven tone", "07052528772")
    show_card("Simple Soothing Toner", 10000, "Blessing", "Alcohol-free, sensitive skin", "07052528772")
    show_card("Acwell Licorice Toner 5.5", 10500, "Blessing", "Cleansing + Hydrating + Brightening", "07052528772")
    show_card("Nivea Men Body Lotion 400ml", 5000, "Blessing", "Vitalising, Hydra IQ + Vitamin E", "07052528772")

# SERVICES - Horlance
if st.session_state.category in ["Home", "Services", "Car Mart"]:
    st.markdown("### 🧰 Services - Horlance Auto Cooling Ltd")
    st.markdown("✅ Verified | 📍 Osun & Oyo | 📱 WhatsApp 09046044472 | 📞 09067551606")
    st.markdown("**Car AC Repair Specialist - We Keep You Cool, Always!**")
    show_card("AC Diagnosis & Fault Finding", 0, "Horlance", "We find the fault fast", "09046044472")
    show_card("Gas Recharge", 0, "Horlance", "Refrigerant Gas Recharge", "09046044472")
    show_card("Compressor Repair & Replacement", 0, "Horlance", "Compressor expert", "09046044472")
    show_card("Leak Detection & Fixing", 0, "Horlance", "Full system leak fix", "09046044472")
    show_card("Full AC System Servicing", 0, "Horlance", "Complete servicing", "09046044472")
    st.link_button("📞 Call Horlance", "tel:09067551606")

# EMPTY CATEGORIES
if st.session_state.category in ["Clothes", "Phones", "Food", "Tickets"]:
    st.info(f"📢 No seller yet in {st.session_state.category}. Be the FIRST! WhatsApp Admin to join FREE for 1 month. 8 slots left.")
    st.link_button("Join as Seller - WhatsApp Admin", "https://wa.me/2347052528772?text=Hi%20I%20want%20to%20sell%20in%20Row%20Economy%20Market")

# CHAT ROOMS
if st.session_state.category in ["Home", "Chat Rooms"]:
    st.markdown("### 💬 Chat Rooms - Like Messenger")
    chat_choice = st.selectbox("Who to chat?", ["Market Square - Everybody", "Chat Blessing", "Chat Horlance"])
    room = "market_square" if "Market" in chat_choice else "blessing" if "Blessing" in chat_choice else "horlance"
    if st.session_state.unread[room] > 0:
        st.warning(f"🔔 {st.session_state.unread[room]} new message(s)!")
        if st.button("Mark as Read"):
            st.session_state.unread[room] = 0; st.rerun()
    for m in st.session_state.chats[room]:
        st.markdown(f"**{m['sender']}:** {m['text']}")
    yn = st.text_input("Your Name", key=f"n_{room}")
    mt = st.text_input("Type message...", key=f"m_{room}")
    if st.button("Send Message ➡️", key=f"s_{room}"):
        if yn and mt:
            st.session_state.chats[room].append({"sender": yn, "text": mt})
            st.session_state.unread[room] += 1
            st.success("✅ Sent! Seller will see 🔔 notification.")
            st.rerun()
    if st.session_state.seller:
        rep = st.text_input("Reply as Seller...", key=f"r_{room}")
        if st.button("Reply as Seller", key=f"rb_{room}"):
            if rep:
                st.session_state.chats[room].append({"sender": f"{SELLERS[st.session_state.seller]['name']} (Seller) ✅", "text": rep})
                st.rerun()

st.markdown("---")
st.markdown("**How to Pay:** Chat seller inside app or WhatsApp -> Confirm price -> Transfer / Pay on delivery -> Delivered.")
st.markdown("© 2026 Row Economy Market - Powered by Mama Oloja")
