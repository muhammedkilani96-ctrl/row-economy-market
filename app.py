import streamlit as st
import random

st.set_page_config(page_title="ROW Economy Market", page_icon="🛍️", layout="wide")

if 'coins' not in st.session_state:
    st.session_state['coins'] = 100
if 'script' not in st.session_state:
    st.session_state['script'] = ""
if 'paid' not in st.session_state:
    st.session_state['paid'] = False

# ===== 🎬 ANIME ADVERT - TOP - ALWAYS VISIBLE =====
st.markdown("""
<div style="background:#ff2d55; padding:20px; border-radius:15px; text-align:center; color:white;">
<h1 style="color:white;">🎬 MAMA OLOJA ANIME ADVERT</h1>
<h3 style="color:white;">Make Anime Video For Your Product - ₦200 ONLY!</h3>
<p>Pay to Opay 8116911722 - Kilani Muhammed Opeyemi</p>
</div>
""", unsafe_allow_html=True)

st.write("Generate FREE, Download na **₦200** only!")
prod = st.selectbox("Pick your product:", [
    "Black Rapture - ₦4000 - Mary - 09031889875",
    "Black Rapture - ₦4000 - Arinfe - 090915907990",
    "Face Serum - ₦4000 - Blessing - 07052528772",
    "Rolex Watch - ₦10000 - Arinfe - 090915907990",
    "Lip Combo - ₦6000 - Arinfe - 090915907990",
    "Jersey Scarf - ₦3500 - Arinfe - 090915907990",
    "Yum Yum Combo - ₦12000 - Arinfe - 090915907990",
    "Vintage Radio - ₦10000 - Mary - 09031889875",
])
style = st.selectbox("Anime Style:", ["C - Cute Anime Girl (Pink) - Best!", "A - Fine Anime Babe", "B - Cool Anime Boy"])

if st.button("✨ Generate My Advert (FREE Preview)"):
    if "Black Rapture" in prod:
        st.session_state['script'] = "My pikin, come see o! Black Rapture don land! E dey smell like money, e dey last all day! Chat me now to order. Mama Oloja talk am, e no be lie!"
    elif "Rolex" in prod:
        st.session_state['script'] = "My pikin, see Rolex Watch! E go make you look like big boy! Price na 10,000 only, with box! Chat me now, no dull!"
    elif "Face Serum" in prod:
        st.session_state['script'] = "My pikin, your face go glow! Face Serum na 4,000 only! E go clear your face, make you shine! Chat Blessing now!"
    else:
        st.session_state['script'] = f"My pikin, come see o! {prod}! E good well well, price sweet! Chat me now to order. Mama Oloja recommend am!"

if st.session_state['script']:
    st.success("Preview Ready!")
    st.code(st.session_state['script'])
    st.write(f"Style: {style}")
    st.markdown("---")
    st.subheader("💰 Pay ₦200 To Unlock Download")
    st.write("**Opay Number: 8116911722**")
    st.write("**Name: Kilani Muhammed Opeyemi**")
    st.write("**Amount: ₦200**")
    st.write("**Narration: Anime Advert - Your Name**")
    ref = st.text_input("Enter Your Opay Name + Reference:", placeholder="e.g. MARY - 200")
    if st.button("✅ I Don Pay ₦200 - Unlock"):
        if ref:
            st.session_state['paid'] = True
            st.success("Payment received! Download don unlock! Mama Oloja don bless your business!")
        else:
            st.warning("Abeg enter Opay name + reference first.")
    if st.session_state['paid']:
        st.markdown("### 🎉 YOUR VIDEO PACKAGE - DOWNLOAD NOW")
        st.download_button("📜 Download Mama Oloja Script", st.session_state['script'], file_name="mama-oloja-script.txt")
        st.write("🎙️ **Voice:** Go ttsmaker.com, paste script, Voice: Female Warm, Speed 0.9x, Download MP3")
        st.write("🖼️ **Anime Picture:** Use Cute Anime Girl picture")
        st.write("🎬 **Video:** Join Picture + Voice for OpenCut, Post for TikTok!")
        st.write("💬 **Need Help?** Chat us: https://wa.me/2348116911722")
        st.balloons()
    else:
        st.warning("🔒 Download Locked - Pay ₦200 to Opay 8116911722 to unlock.")

st.markdown("---")

# ===== TOP BAR =====
st.markdown("""
<div style="background:black; color:white; padding:10px; border-radius:15px; display:flex; justify-content:space-between;">
<span>📍 Ikorodu, Lagos</span><span>🪙 100 Coins • 🛒 0</span>
</div>
""", unsafe_allow_html=True)

# ===== WELCOME =====
st.markdown("""
<div style="background:linear-gradient(to bottom right, #0a7a42, #d4c400); padding:20px; border-radius:20px; color:white;">
<h2 style="color:#FFD700;">✦ ROW ECONOMY MARKET ✦</h2>
<h1>Welcome back,<br>muhammed! 👋</h1>
<p>Everything you need, near you. No scam.<br>Mama Oloja dey watch for you.</p>
<p>⭐ 4.9 Rating • 2,347 Happy Buyers • 🚚 FREE Delivery Today In Ikorodu</p>
</div>
""", unsafe_allow_html=True)
st.info("🛡️ **Mama Oloja Guarantee:** If seller scam you, we refund you. 100% Safe. ✅ Verified Sellers Only")

# ===== YOU WON =====
st.markdown("""
<div style="background:linear-gradient(to right, #ff6b35, #ff3b6b); padding:20px; border-radius:20px; color:white; text-align:center;">
<h1>🎁 YOU WON ₦500 OFF!</h1><p>Your first order - Use code: <b>ROW500</b></p>
</div>
""", unsafe_allow_html=True)
if st.button("🎁 Claim My ₦500 OFF Now"):
    st.success("Code ROW500 Activated!")

# ===== SPIN & REFER =====
st.markdown("""<div style="border:2px dashed #FFD700; padding:15px; border-radius:15px; text-align:center;"><h3>🎡 SPIN & WIN - Daily Luck!</h3></div>""", unsafe_allow_html=True)
if st.button("🎡 SPIN NOW - It's FREE!"):
    prize = random.choice(["50 Coins", "FREE Delivery", "₦200 OFF", "100 Coins", "Try Again"])
    st.success(f"You won: {prize}!")
    if "Coins" in prize:
        st.session_state['coins'] += 50
st.markdown("""<div style="background:#7b2ff7; padding:15px; border-radius:15px; color:white;"><h3>👥 REFER & EARN ₦200</h3><p>Invite friend, you get ₦200, friend gets ₦200.</p></div>""", unsafe_allow_html=True)
st.markdown("""<div style="background:#ff2d55; padding:15px; border-radius:15px; color:white;"><h3>⚡ FLASH SALE - Up to 30% OFF - Today Only</h3></div>""", unsafe_allow_html=True)

# ===== SEARCH =====
search = st.text_input("🔍 Search:", placeholder="Search serum, sunscreen, Black Rapture...")

# ===== SELLER LOGIN =====
st.write("✅ **Blessing Cosmetics**")
with st.expander("🔐 Seller Login", expanded=True):
    st.success("Logged in as Blessing Cosmetics")

# ===== MAMA OLOJA CHAT =====
st.markdown("""
<div style="background:white; padding:15px; border-radius:15px;">
<h3>Mama Oloja • <span style="color:green;">Online • Replies in 2 secs</span></h3>
<p>Your Market Aunty - She sabi price, skin & Car AC</p>
</div>
""", unsafe_allow_html=True)
with st.expander("🤖 Ask Mama Oloja - Wetin You Dey Find?"):
    q = st.text_input("Ask Mama Oloja:", placeholder="e.g. I get 5000, wetin I fit buy?").lower()
    if st.button("💬 Ask Mama Oloja"):
        if "5000" in q:
            st.success("Mama Oloja: Buy Black Rapture ₦4,000 from Mary - e sweet pass!")
        elif "girlfriend" in q:
            st.success("Mama Oloja: For girlfriend? Buy Lip Combo ₦6,000 - girls dey love am!")
        elif "ibadan" in q:
            st.success("Mama Oloja: You dey Ibadan? Arinfe dey Academy! Rolex ₦10k, Lip Combo ₦6k, Scarf ₦3.5k!")
        elif "perfume" in q:
            st.success("Mama Oloja: Best perfume for ₦4,000 na Black Rapture - 20 reviews, ⭐5.0!")
        elif q:
            st.success(f"Mama Oloja: Tell me your budget, who you dey buy for, where you dey - I go help you!")

# ===== CATEGORIES =====
st.subheader("Shop by Category")
for emoji, label, color in [("💄","Cosmetics","#ffd6e0"), ("🚗","Car Mart","#ffe4b5"), ("👕","Clothes","#cceaff"), ("🧰","Services","#c8f7c5")]:
    st.markdown(f"""<div style="background:{color}; padding:20px; border-radius:20px; text-align:center;"><div style="font-size:35px;">{emoji}</div><h3>{label}</h3></div>""", unsafe_allow_html=True)

# ===== SELLER OF WEEK =====
st.markdown("""
<div style="background:#fff9c4; padding:15px; border-radius:15px; border:1px solid #FFD700;">
<h3>👑 SELLER OF THE WEEK</h3>
<h3>❄️ Horlance Auto Cooling Ltd • ⭐ 5.0 • 340 Jobs Done</h3>
<p>Car AC Specialist - Osun & Oyo • 📞 09046044472</p>
</div>
""", unsafe_allow_html=True)

# ===== SHOP PRODUCTS =====
st.header("🛍️ Shop - All Products")
PRODUCTS = [
    ("Black Rapture", 4000, "Mary", "09031889875", "Lagos", "Bold, long-lasting"),
    ("Black Rapture", 4000, "Arinfe", "090915907990", "Ibadan", "Bold, long-lasting"),
    ("Vintage Radio", 10000, "Mary", "09031889875", "Lagos", "Warm, vintage"),
    ("Face Serum", 4000, "Blessing", "07052528772", "Abuja", "Clear face, glow"),
    ("Rolex Watch", 10000, "Arinfe", "090915907990", "Ibadan", "Black strap, with box"),
    ("Lip Combo", 6000, "Arinfe", "090915907990", "Ibadan", "Brown + Pink + Liner"),
    ("Jersey Scarf", 3500, "Arinfe", "090915907990", "Ibadan", "Soft, no slip"),
    ("Yum Yum Combo", 12000, "Arinfe", "090915907990", "Ibadan", "Perfume + Spray"),
    ("Tote Bag", 6500, "Arinfe", "090915907990", "Ibadan", "Big, strong bag"),
    ("Hand Chain", 2000, "Arinfe", "090915907990", "Ibadan", "Gold + Black LV"),
]
for name, price, seller, phone, loc, desc in PRODUCTS:
    if search and search.lower() not in name.lower():
        continue
    st.write(f"**{name}** - ₦{price:,} | {seller} - {loc}")
    st.write(desc)
    st.markdown(f"[💬 Buy via WhatsApp - {seller}](https://wa.me/234{phone[1:]}?text=Hello {seller}, I want {name} - {price} from ROW Market)")
    st.markdown("---")

# ===== UPLOAD =====
with st.expander("📸 Upload Product - Sellers"):
    st.write("Uploading as: Blessing Cosmetics")
    pn = st.text_input("Product Name")
    pp = st.number_input("Price", value=0)
    if st.button("Post Product"):
        if pn:
            st.success(f"{pn} - ₦{pp} posted! Want Anime Advert? Scroll to TOP - RED BANNER - ₦200 only!")
        else:
            st.warning("Enter Product Name first.")

# ===== HOT DEALS =====
st.header("🔥 Hot Deals - Face Serum ₦4,000")
st.write("by Blessing ✅ Verified • ⭐ 4.9 (1.2k sold) • 🚚 FREE Delivery Today")
if st.button("❤️ Add Face Serum to Wishlist"):
    st.success("Added to Wishlist! +10 Coins")
if st.button("💬 Buy Face Serum via WhatsApp - Blessing"):
    st.markdown("[Chat Blessing](https://wa.me/2347052528772?text=Hello Blessing, I want Face Serum - 4000)")

# ===== MESSENGER =====
st.header("Messenger")
st.write("Chat: Market Square - Mama Oloja - Blessing - Horlance")
msg = st.text_area("Type message...")
if st.button("Send Message"):
    if msg:
        st.success(f"Sent: {msg}")

st.markdown("---")
st.write(f"**Your Coins: {st.session_state['coins']}**")
st.write("**Want to Sell?** Join FREE - WhatsApp Admin: https://wa.me/2348116911722")
st.write("**Anime Advert:** ₦200 to Opay 8116911722 - Kilani Muhammed Opeyemi")
st.write("© 2026 Row Economy Market - Powered by Mama Oloja 🧕")
