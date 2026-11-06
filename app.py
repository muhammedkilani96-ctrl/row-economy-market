import streamlit as st
import hashlib

# ============ SETUP ============
st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="centered")
st.title("🛒 Row Economy Market")
st.markdown("**Powered by Mama Oloja 🧕 - She Knows All Prices**")
st.markdown("🎉 FREE for 1 Month - Nov 6 to Dec 6 - 0% Commission for Sellers | 8 Slots Left")

def make_hash(p):
    return hashlib.sha256(p.encode()).hexdigest()

TEMP_HASH = make_hash("row123") # TEMP password for all sellers for now

SELLERS = {
    "blessing": {
        "name": "Blessing Cosmetics",
        "phone": "07052528772",
        "password_hash": TEMP_HASH,
        "verified": True,
        "location": "Abuja - Location ON ✅",
        "type": "Cosmetics"
    },
    "horlance": {
        "name": "Horlance Auto Cooling Ltd",
        "phone": "09046044472",
        "calling": "09067551606",
        "password_hash": TEMP_HASH,
        "verified": True,
        "location": "Osun & Oyo State - Location ON ✅",
        "type": "Car AC Repair"
    },
    "admin": {
        "name": "Admin - Muhammed",
        "phone": "Admin Only",
        "password_hash": TEMP_HASH,
        "verified": True,
        "location": "Abuja",
        "type": "Admin"
    }
}

# ============ SELLER LOGIN - SIDEBAR ============
st.sidebar.markdown("### 🔐 Seller Login")
if "seller" not in st.session_state:
    st.session_state.seller = None

if st.session_state.seller is None:
    username = st.sidebar.text_input("Username").lower().strip()
    password = st.sidebar.text_input("Password", type="password")
    st.sidebar.caption("For now, all sellers password is: row123")
    st.sidebar.caption("Demo: blessing / row123 | horlance / row123 | admin / row123")
    if st.sidebar.button("Login"):
        if username in SELLERS and make_hash(password) == SELLERS[username]["password_hash"]:
            st.session_state.seller = username
            st.sidebar.success(f"Welcome {SELLERS[username]['name']} ✅")
            st.rerun()
        else:
            st.sidebar.error("Wrong username or password.")
    st.sidebar.markdown("---")
    st.sidebar.markdown("**New Seller?** WhatsApp Admin to create account. We verify you first.")
else:
    s = SELLERS[st.session_state.seller]
    st.sidebar.success(f"Logged in as {s['name']} ✅ Verified")
    st.sidebar.markdown(f"📍 {s['location']}")
    if st.sidebar.button("Logout"):
        st.session_state.seller = None
        st.rerun()

# ============ SELLER / ADMIN DASHBOARD ============
if st.session_state.seller:
    st.markdown("---")
    st.markdown(f"### 🛍️ My Dashboard - {SELLERS[st.session_state.seller]['name']}")
    if st.session_state.seller == "admin":
        st.warning("👑 ADMIN DASHBOARD - You can see all sellers")
        st.markdown("**Sellers:** Blessing (11 products) | Horlance (7 services) | 8 FREE slots left")
        st.markdown("**Rules:** No scam, No fake product. Block scammer immediately.")
    else:
        st.markdown("Only you can see this. Add new product here - Admin will approve.")
        np = st.text_input("New Product / Service Name")
        nprice = st.number_input("Price ₦", min_value=0, step=100)
        if st.button("Add Product - Send to Admin"):
            if np:
                st.success(f"✅ Added: {np} - ₦{nprice:,} - Waiting for Admin approval. Admin will add it to your shop.")
            else:
                st.error("Type product name first.")

# ============ MAMA OLOJA / IYA OLAJA ============
st.markdown("---")
st.markdown("### 🧕 Ask Mama Oloja - Wetin You Dey Find?")
st.markdown("Ask in English or Pidgin. E.g. *I need serum under 5000* or *my car ac hot*")
ask = st.text_input("Type here:", placeholder="E.g. I need sunscreen under 10000...")

if ask:
    q = ask.lower()
    if "ac" in q or "car ac" in q or "car" in q or "cool" in q or "horlance" in q:
        st.success("🧕 Mama Oloja: Ah! For Car AC, na Horlance be number 1! Dem dey Osun & Oyo State. Gas Recharge, Compressor Repair, Leak Fixing, Full Servicing - dem sabi am well well. Chat dem now - WhatsApp 09046044472, Call 09067551606. Tell dem Mama Oloja send you!")
    elif "sunscreen" in q or "sun" in q:
        st.success("🧕 Mama Oloja: My pikin, come! For sunscreen I get 4 from Blessing: Biore UV ₦5,000, Nivea Sun ₦9,000, Skin Aqua ₦10,000, La Roche-Posay ₦17,000. If money small, take Biore ₦5,000. If skin sensitive, take Nivea ₦9,000. Chat Blessing - 07052528772")
    elif "serum" in q or "dark spot" in q or "pimple" in q or "glow" in q:
        st.success("🧕 Mama Oloja: Ah! For serum, Blessing get 3: Face Serum ₦4,000, Ceramide Serum ₦5,000 for dry/stressed skin, Illuminating Serum ₦5,500 for glow and clear skin. Chat Blessing - 07052528772")
    elif "toner" in q:
        st.success("🧕 Mama Oloja: Toner dey! TONYMOLY ₦6,000, Estelin Whitening ₦8,000, Simple Soothing ₦10,000, Acwell Licorice ₦10,500. If you want glow, take Acwell. If skin sensitive, take Simple. Chat Blessing - 07052528772")
    elif "men" in q or "lotion" in q or "man" in q:
        st.success("🧕 Mama Oloja: For men, we get Nivea Men Body Lotion 400ml ₦5,000. Absorbs fast, no stickiness. Vitalising / Energising. Chat Blessing - 07052528772")
    elif "dry" in q:
        st.success("🧕 Mama Oloja: If skin dry, take Ceramide Serum ₦5,000 + TONYMOLY Ceramide Toner ₦6,000. Dem go nourish and restore your skin. Chat Blessing - 07052528772")
    elif "5000" in q or "under" in q or "cheap" in q:
        st.success("🧕 Mama Oloja: Under ₦5,000? I get Face Serum ₦4,000, Ceramide Serum ₦5,000, Biore Sunscreen ₦5,000, Nivea Men Lotion ₦5,000. All from Blessing. Chat 07052528772")
    else:
        st.success(f"🧕 Mama Oloja: My pikin, for '{ask}' - Go to Blessing shop. She get serum from ₦4,000, sunscreen from ₦5,000, toner from ₦6,000. For Car AC, go to Horlance. Tell them your problem, dem go help you. Blessing: 07052528772 | Horlance: 09046044472")

# ============ LOCATION ============
st.markdown("---")
st.markdown("### 📍 Turn On Your Real Location")
st.markdown("Allow location so buyers near you can find you fast. We show only your AREA, not your house.")
st.components.v1.html("""
<button onclick="getLocation()" style="background:#25D366;color:white;padding:12px 20px;border:none;border-radius:10px;font-size:16px;cursor:pointer;">📍 Turn On My Location</button>
<p id="loc" style="margin-top:10px;font-weight:bold;"></p>
<script>
function getLocation() {
  if (navigator.geolocation) {
    document.getElementById("loc").innerHTML = "Finding you... allow location...";
    navigator.geolocation.getCurrentPosition(showPosition, showError);
  } else {
    document.getElementById("loc").innerHTML = "Your phone does not support location.";
  }
}
function showPosition(position) {
  var lat = position.coords.latitude;
  var lon = position.coords.longitude;
  document.getElementById("loc").innerHTML = "✅ Location ON! Lat: " + lat.toFixed(4) + ", Lon: " + lon.toFixed(4) + "<br><a href='https://www.google.com/maps?q=" + lat + "," + lon + "' target='_blank'>View Me On Google Map</a><br>Copy this and send to Admin, we will show your Area only.";
}
function showError(error) {
  document.getElementById("loc").innerHTML = "❌ Location blocked. Go to phone Settings > Location > Allow for this site, then try again.";
}
</script>
""", height=150)
area = st.selectbox("Or pick your Area manually:", ["Select Area", "Gwagwalada", "Kubwa", "Lugbe", "Wuse", "Garki", "Maitama", "Asokoro", "Nyanya", "Karu", "Jabi", "Utako", "Osun", "Oyo", "Other"])
if area != "Select Area":
    st.success(f"📍 Location set to: {area} - Buyers near {area} will see you first!")

# ============ SELLER 1 - BLESSING ============
st.markdown("---")
st.markdown("## 💄 Blessing Cosmetics - Seller #1")
st.markdown("**✅ Verified Seller | 📍 Abuja - Location ON | 📱 07052528772 | FREE Promo - She keeps 100%**")
st.markdown("**Cream for any skin concern - Tell Blessing your skin concern**")

st.markdown("### 💧 Serums")
st.markdown("**Face Serum - ₦4,000** - Active Caviar, Pei Mei Hyaluronic, Niacinamide. 30ml Original.")
st.link_button("Buy Face Serum ₦4,000", "https://wa.me/2347052528772?text=Hi%20Blessing%20I%20want%20Face%20Serum%20N4000")
st.markdown("**Ceramide Serum - ₦5,000** - Nourish + Restore. Ceramide + Hyaluronic Acid. For stressed & dehydrated skin.")
st.link_button("Buy Ceramide ₦5,000", "https://wa.me/2347052528772?text=Hi%20Blessing%20I%20want%20Ceramide%20Serum%20N5000")
st.markdown("**Illuminating Serum 10% Niacinamide - ₦5,500** - Enhance + Radiate. For uneven tone, dull skin, dark marks.")
st.link_button("Buy Illuminating ₦5,500", "https://wa.me/2347052528772?text=Hi%20Blessing%20I%20want%20Illuminating%20Serum%20N5500")

st.markdown("### ☀️ Sunscreen - From ₦5,000")
st.markdown("1. Biore UV - ₦5,000 | 2. Nivea Sun SPF50 - ₦9,000 | 3. Skin Aqua SPF50+ - ₦10,000 | 4. La Roche-Posay Anthelios - ₦17,000")
st.link_button("Buy Sunscreen", "https://wa.me/2347052528772?text=Hi%20Blessing%20I%20want%20Sunscreen")

st.markdown("### 💧 Toner - From ₦6,000")
st.markdown("1. TONYMOLY Ceramide - ₦6,000 | 2. Estelin Whitening - ₦8,000 | 3. Simple Soothing - ₦10,000 | 4. Acwell Licorice - ₦10,500")
st.link_button("Buy Toner", "https://wa.me/2347052528772?text=Hi%20Blessing%20I%20want%20Toner")

st.markdown("### 💙 Nivea Men Body Lotion 400ml - ₦5,000")
st.markdown("Vitalising / Energising. Hydra IQ + Vitamin E. Absorbs fast, no stickiness.")
st.link_button("Buy Nivea Men ₦5,000", "https://wa.me/2347052528772?text=Hi%20Blessing%20I%20want%20Nivea%20Men%20Lotion%20N5000")

# ============ SELLER 2 - HORLANCE ============
st.markdown("---")
st.markdown("## ❄️ Horlance Auto Cooling Ltd - Seller #2")
st.markdown("**✅ Verified Seller | 📍 Osun & Oyo State - Location ON | Your Vehicle, Our Priority**")
st.markdown("**Car AC Repair Specialist - We Keep You Cool, Always!**")
st.markdown("1. AC Diagnosis & Fault Finding")
st.markdown("2. Refrigerant Gas Recharge")
st.markdown("3. Compressor Repair & Replacement")
st.markdown("4. Condenser, Evaporator & Expansion Valve Service")
st.markdown("5. AC System Leak Detection & Fixing")
st.markdown("6. Full AC System Servicing")
st.markdown("7. AC Electrical & Control System Check")
st.markdown("📱 WhatsApp: 09046044472 | 📞 Call: 09067551606 | FB/IG: Horlance Automobile")
st.link_button("Chat Horlance on WhatsApp", "https://wa.me/2349046044472?text=Hi%20Horlance%20I%20need%20Car%20AC%20Repair%20from%20Row%20Economy%20Market")
st.link_button("Call Horlance", "tel:09067551606")

# ============ FOOTER ============
st.markdown("---")
st.markdown("### 🧕 Mama Oloja's Market Square")
st.markdown("Welcome! No scam here. Mama Oloja dey watch. Ask question, post your product, respect everybody.")
st.markdown("**How to Pay:** Chat seller on WhatsApp -> Seller confirms price -> You transfer / Pay on delivery -> Seller delivers. Simple.")
st.markdown("**Want to Sell?** WhatsApp Admin to join FREE for 1 month. 8 slots left.")
st.markdown("© 2026 Row Economy Market - Powered by Mama Oloja")
