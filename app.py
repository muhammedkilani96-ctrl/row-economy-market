import streamlit as st
import hashlib

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="centered")
st.title("🛒 Row Economy Market")
st.markdown("**Powered by Mama Oloja 🧕 - She Knows All Prices**")
st.markdown("🎉 FREE for 1 Month - Nov 6 to Dec 6 - 0% Commission | 8 Slots Left")

def make_hash(p):
    return hashlib.sha256(p.encode()).hexdigest()
TEMP_HASH = make_hash("row123")

SELLERS = {
    "blessing": {"name": "Blessing Cosmetics", "phone": "07052528772", "password_hash": TEMP_HASH, "verified": True, "location": "Abuja / Lagos - Location ON ✅", "type": "Cosmetics"},
    "horlance": {"name": "Horlance Auto Cooling Ltd", "phone": "09046044472", "calling": "09067551606", "password_hash": TEMP_HASH, "verified": True, "location": "Osun & Oyo State - Location ON ✅", "type": "Car AC"},
    "admin": {"name": "Admin - Muhammed", "phone": "Admin Only", "password_hash": TEMP_HASH, "verified": True, "location": "Lagos", "type": "Admin"}
}

# --- Keep uploads + chats in memory ---
if "uploads" not in st.session_state:
    st.session_state.uploads = []  # list of {seller, name, price, type}
if "chats" not in st.session_state:
    st.session_state.chats = {"blessing": [], "horlance": [], "market_square": []}
if "seller" not in st.session_state:
    st.session_state.seller = None
if "unread" not in st.session_state:
    st.session_state.unread = {"blessing": 0, "horlance": 0, "market_square": 0}

# ============ LOGIN ============
st.sidebar.markdown("### 🔐 Seller Login")
if st.session_state.seller is None:
    username = st.sidebar.text_input("Username").lower().strip()
    password = st.sidebar.text_input("Password", type="password")
    st.sidebar.caption("Password for now: row123")
    if st.sidebar.button("Login"):
        if username in SELLERS and make_hash(password) == SELLERS[username]["password_hash"]:
            st.session_state.seller = username
            st.rerun()
        else:
            st.sidebar.error("Wrong username or password.")
else:
    s = SELLERS[st.session_state.seller]
    st.sidebar.success(f"Logged in as {s['name']} ✅")
    # NOTIFICATION BADGE
    total_unread = sum(st.session_state.unread.values())
    if total_unread > 0:
        st.sidebar.error(f"🔔 You have {total_unread} new message(s)! Check Chat Room below.")
    else:
        st.sidebar.markdown("🔔 No new messages")
    if st.sidebar.button("Logout"):
        st.session_state.seller = None
        st.rerun()

# ============ MAMA OLOJA ============
st.markdown("---")
st.markdown("### 🧕 Ask Mama Oloja - Wetin You Dey Find?")
ask = st.text_input("Type here:", placeholder="E.g. I need sunscreen under 10000...")
if ask:
    q = ask.lower()
    if "ac" in q or "car" in q or "horlance" in q:
        st.success("🧕 Mama Oloja: For Car AC, na Horlance be number 1! Osun & Oyo. Gas, Compressor, Leak Fixing. WhatsApp 09046044472, Call 09067551606. Tell dem Mama Oloja send you!")
    elif "sunscreen" in q or "sun" in q:
        st.success("🧕 Mama Oloja: Sunscreen from Blessing: Biore ₦5,000, Nivea ₦9,000, Skin Aqua ₦10,000, La Roche-Posay ₦17,000. Chat Blessing - 07052528772")
    elif "serum" in q or "glow" in q:
        st.success("🧕 Mama Oloja: Serum from Blessing: Face ₦4,000, Ceramide ₦5,000, Illuminating ₦5,500. Chat Blessing - 07052528772")
    elif "toner" in q:
        st.success("🧕 Mama Oloja: Toner: TONYMOLY ₦6,000, Estelin ₦8,000, Simple ₦10,000, Acwell ₦10,500. Chat Blessing - 07052528772")
    else:
        st.success(f"🧕 Mama Oloja: My pikin, for '{ask}' - Check Blessing for cosmetics, Horlance for Car AC. Blessing: 07052528772 | Horlance: 09046044472")

# ============ LOCATION - FIXED - NO CUT OFF ============
st.markdown("---")
st.markdown("### 📍 Turn On Your Real Location")
st.markdown("We show only your AREA, not your house.")

# FIXED: Bigger height + word wrap, no cut-off
st.components.v1.html("""
<div style="word-wrap:break-word; white-space:normal; font-family:sans-serif;">
<button onclick="getLocation()" style="background:#25D366;color:white;padding:14px 22px;border:none;border-radius:12px;font-size:16px;cursor:pointer;width:100%;">📍 Turn On My Location</button>
<div id="loc" style="margin-top:12px;padding:12px;background:#E8F5E9;border-radius:10px;font-weight:bold;line-height:1.6;"></div>
</div>
<script>
function getLocation() {
  if (navigator.geolocation) {
    document.getElementById("loc").innerHTML = "Finding you... please allow location...";
    navigator.geolocation.getCurrentPosition(showPosition, showError);
  } else {
    document.getElementById("loc").innerHTML = "Your phone does not support location.";
  }
}
function showPosition(position) {
  var lat = position.coords.latitude;
  var lon = position.coords.longitude;
  var area = "Lagos Area";
  if (lat > 6.5 && lat < 6.65) area = "Ikorodu, Lagos";
  if (lat > 6.4 && lat < 6.5) area = "Lagos - Ikeja / Ikorodu Axis";
  document.getElementById("loc").innerHTML = "✅ Location ON!<br>Lat: " + lat.toFixed(4) + "<br>Lon: " + lon.toFixed(4) + "<br>Area: " + area + "<br><a href='https://www.google.com/maps?q=" + lat + "," + lon + "' target='_blank'>📍 View Me On Google Map</a><br>We will show only your Area, not your house.";
}
function showError(error) {
  document.getElementById("loc").innerHTML = "❌ Location blocked. Go to Settings > Location > Allow, then try again.";
}
</script>
""", height=220)

# FIXED: Added Ikorodu + Lagos areas, no more "Ikoe" cut-off
area = st.selectbox("Or pick your Area manually:", ["Select Area", "Ikorodu", "Ikeja", "Lekki", "Surulere", "Yaba", "Gwagwalada", "Kubwa", "Lugbe", "Wuse", "Garki", "Maitama", "Asokoro", "Nyanya", "Karu", "Jabi", "Utako", "Osun", "Oyo", "Other"])
if area != "Select Area":
    st.success(f"📍 Location set to: {area} - Buyers near {area} will see you first!")

# ============ UPLOAD PICTURE / VIDEO - ANY SELLER ============
st.markdown("---")
st.markdown("### 📸 Upload Product - Picture or Video")
st.markdown("Any seller who is logged in can upload. Buyer will see it instantly.")

if st.session_state.seller is None:
    st.info("🔐 Login as seller to upload. Demo: blessing / row123")
else:
    seller_name = SELLERS[st.session_state.seller]['name']
    st.success(f"Uploading as: {seller_name}")
    up_name = st.text_input("Product Name", placeholder="E.g. Face Serum")
    up_price = st.number_input("Price ₦", min_value=0, step=100)
    up_file = st.file_uploader("Upload Picture or Video", type=["jpg", "jpeg", "png", "mp4", "mov", "webm"])
    up_desc = st.text_area("Description", placeholder="E.g. For dry skin, 30ml original...")
    if st.button("📤 Post Product"):
        if up_name and up_file:
            st.session_state.uploads.append({"seller": seller_name, "name": up_name, "price": up_price, "desc": up_desc, "file": up_file, "type": up_file.type})
            st.success(f"✅ Posted! {up_name} - ₦{up_price:,} is now LIVE for buyers to see.")
            st.rerun()
        else:
            st.error("Add Product Name + Picture/Video first.")

# Show all uploaded products
if st.session_state.uploads:
    st.markdown("#### 🛍️ New Uploads From Sellers")
    for item in reversed(st.session_state.uploads):
        st.markdown(f"**{item['name']} - ₦{item['price']:,}** by {item['seller']}")
        st.markdown(f"{item['desc']}")
        if item['type'].startswith("image"):
            st.image(item['file'], width=300)
        elif item['type'].startswith("video"):
            st.video(item['file'])
        st.markdown("---")

# ============ SELLER 1 - BLESSING ============
st.markdown("---")
st.markdown("## 💄 Blessing Cosmetics - Seller #1")
st.markdown("**✅ Verified | 📍 Abuja / Lagos | 📱 07052528772 | FREE Promo**")
st.markdown("**Serums:** Face ₦4,000 | Ceramide ₦5,000 | Illuminating ₦5,500")
st.markdown("**Sunscreen:** Biore ₦5,000 | Nivea ₦9,000 | Skin Aqua ₦10,000 | La Roche-Posay ₦17,000")
st.markdown("**Toner:** TONYMOLY ₦6,000 | Estelin ₦8,000 | Simple ₦10,000 | Acwell ₦10,500")
st.markdown("**Nivea Men Lotion 400ml - ₦5,000**")
st.link_button("Chat Blessing on WhatsApp", "https://wa.me/2347052528772?text=Hi%20Blessing%20I%20want%20to%20buy%20from%20Row%20Economy%20Market")

# ============ SELLER 2 - HORLANCE ============
st.markdown("---")
st.markdown("## ❄️ Horlance Auto Cooling Ltd - Seller #2")
st.markdown("**✅ Verified | 📍 Osun & Oyo | 📱 WhatsApp 09046044472 | 📞 09067551606**")
st.markdown("Car AC Repair Specialist - Gas Recharge, Compressor, Leak Fixing, Full Servicing")
st.link_button("Chat Horlance on WhatsApp", "https://wa.me/2349046044472?text=Hi%20Horlance%20I%20need%20Car%20AC%20Repair")
st.link_button("Call Horlance", "tel:09067551606")

# ============ CHAT ROOM LIKE FACEBOOK MESSENGER ============
st.markdown("---")
st.markdown("## 💬 Chat Room - Like Messenger")
st.markdown("Chat seller inside app. Seller gets 🔔 notification.")

chat_choice = st.selectbox("Who do you want to chat?", ["Market Square - Everybody", "Chat Blessing - Cosmetics", "Chat Horlance - Car AC"])
room_key = "market_square" if "Market" in chat_choice else "blessing" if "Blessing" in chat_choice else "horlance"

# Show unread badge
if st.session_state.unread[room_key] > 0:
    st.warning(f"🔔 {st.session_state.unread[room_key]} new message(s) in this room!")
    if st.button("Mark as Read"):
        st.session_state.unread[room_key] = 0
        st.rerun()

# Show messages
for msg in st.session_state.chats[room_key]:
    st.markdown(f"**{msg['sender']}:** {msg['text']}")

# Send message
your_name = st.text_input("Your Name", placeholder="E.g. Chinedu - Buyer", key=f"name_{room_key}")
msg_text = st.text_input("Type message...", placeholder="E.g. Hi Blessing, is Face Serum still available?", key=f"msg_{room_key}")
if st.button("Send Message ➡️", key=f"send_{room_key}"):
    if your_name and msg_text:
        st.session_state.chats[room_key].append({"sender": your_name, "text": msg_text})
        # Notify seller - increase unread for seller
        if room_key in ["blessing", "horlance"]:
            st.session_state.unread[room_key] += 1
        else:
            st.session_state.unread["market_square"] += 1
        st.success("✅ Message sent! Seller will see 🔔 notification.")
        st.rerun()
    else:
        st.error("Type your name + message first.")

# Seller reply quickly
if st.session_state.seller:
    st.markdown(f"**Reply as {SELLERS[st.session_state.seller]['name']}:**")
    reply = st.text_input("Reply...", key=f"reply_{room_key}")
    if st.button("Reply as Seller", key=f"replybtn_{room_key}"):
        if reply:
            st.session_state.chats[room_key].append({"sender": f"{SELLERS[st.session_state.seller]['name']} (Seller) ✅", "text": reply})
            st.rerun()

st.markdown("---")
st.markdown("**How to Pay:** Chat seller inside app or WhatsApp -> Seller confirms -> You transfer / Pay on delivery -> Seller delivers.")
st.markdown("**Want to Sell?** WhatsApp Admin to join FREE. 8 slots left.")
st.markdown("© 2026 Row Economy Market - Powered by Mama Oloja")
