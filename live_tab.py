import streamlit as st
import random
import time

st.set_page_config(page_title="ROW Economy Market", page_icon="🛍️", layout="wide")

# ===== SESSION STATE =====
if 'cart' not in st.session_state:
    st.session_state['cart'] = 0
if 'coins' not in st.session_state:
    st.session_state['coins'] = 100
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = "Muhammd"
if 'seller_name' not in st.session_state:
    st.session_state['seller_name'] = "Blessing Cosmetics"
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = True

# ===== TOP BAR =====
st.markdown("""
<div style="background:black; color:white; padding:10px; border-radius:15px; display:flex; justify-content:space-between;">
<span>📍 Ikorodu, Lagos • 06:49 PM</span><span>🪙 100 Coins • 🛒 0</span>
</div>
""", unsafe_allow_html=True)

# ===== WELCOME =====
st.markdown(f"""
<div style="background:linear-gradient(to bottom right, #0a7a42, #d4c400); padding:20px; border-radius:20px; color:white;">
<h2 style="color:#FFD700;">✦ ROW ECONOMY MARKET ✦</h2>
<h1>Welcome back,<br>{st.session_state['user_name']}! 👋</h1>
<p>Everything you need, near you. No scam.<br>Mama Oloja dey watch for you.</p>
<button style="background:white; padding:10px; border-radius:20px; border:none; font-weight:bold;">🛍️ Shop Now ↓</button>
<button style="background:#FFD700; padding:10px; border-radius:20px; border:none; font-weight:bold; margin-left:10px;">🪙 100 Coins</button>
<p style="background:rgba(255,255,255,0.3); padding:8px; border-radius:10px; margin-top:15px;">⭐ 4.9 Rating • 2,347 Happy Buyers • 🚚 FREE Delivery Today In Ikorodu</p>
</div>
""", unsafe_allow_html=True)

st.info("🛡️ **Mama Oloja Guarantee:** If seller scam you, we refund you. 100% Safe. ✅ Verified Sellers Only")

# ===== YOU WON ₦500 =====
st.markdown("""
<div style="background:linear-gradient(to right, #ff6b35, #ff3b6b); padding:20px; border-radius:20px; color:white; text-align:center;">
<h1>🎁 YOU WON ₦500 OFF!</h1>
<p>Your first order - Use code: <b>ROW500</b></p>
</div>
""", unsafe_allow_html=True)
if st.button("🎁 Claim My ₦500 OFF Now"):
    st.success("Code ROW500 Activated! Use am for your first order!")

# ===== SPIN & WIN + REFER =====
with st.container():
    st.markdown("""
    <div style="border:2px dashed #FFD700; padding:15px; border-radius:15px; text-align:center;">
    <h3>🎡 SPIN & WIN - Daily Luck!</h3>
    <p>Spin once a day, win Coins, Free Delivery, Discount</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🎡 SPIN NOW - It's FREE!"):
        prize = random.choice(["50 Coins", "FREE Delivery", "₦200 OFF", "100 Coins", "Try Again"])
        st.success(f"You won: {prize}!")
        if "Coins" in prize:
            st.session_state['coins'] += 50

st.markdown("""
<div style="background:#7b2ff7; padding:15px; border-radius:15px; color:white;">
<h3>👥 REFER & EARN ₦200</h3>
<p>Invite friend, you get ₦200, friend gets ₦200. No limit!</p>
<p><b>Your Referrals: 0 • You earned: ₦0</b></p>
<p>Your Link: roweconomy.streamlit.app/?ref=Muhammd</p>
</div>
""", unsafe_allow_html=True)

# ===== FLASH SALE =====
st.markdown("""
<div style="background:#ff2d55; padding:15px; border-radius:15px; color:white; display:flex; justify-content:space-between;">
<div><h3>⚡ FLASH SALE</h3><p style="background:white; color:#ff2d55; padding:5px; border-radius:10px;">Up to 30% OFF - Today Only</p></div>
<div style="background:white; color:#ff2d55; padding:10px; border-radius:10px; font-weight:bold;">01 : 59 : 12</div>
</div>
""", unsafe_allow_html=True)

search = st.text_input("🔍 Search:", placeholder="Search serum, sunscreen, Jollof rice, Car AC...")
st.write(f"🛒 **Cart: {st.session_state['cart']}**")

# ===== SELLER LOGIN =====
st.write("✅ **Blessing Cosmetics**")
with st.expander("🔐 Seller Login", expanded=True):
    if st.session_state['logged_in']:
        st.success(f"Logged in as {st.session_state['seller_name']}")
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()
    else:
        s = st.text_input("Seller Name:", value="Blessing Cosmetics")
        if st.button("Login as Seller"):
            st.session_state['seller_name'] = s
            st.session_state['logged_in'] = True
            st.rerun()

# ===== MAMA OLOJA CARD =====
st.markdown("""
<div style="background:white; padding:15px; border-radius:15px; box-shadow:0 2px 10px rgba(0,0,0,0.1); display:flex; gap:15px;">
<div style="background:linear-gradient(purple, pink); width:60px; height:60px; border-radius:50%; text-align:center; font-size:35px;">🧕</div>
<div>
<h3>Mama Oloja • <span style="color:green; font-size:14px;">Online • Replies in 2 secs</span></h3>
<p>Your Market Aunty - She sabi price, skin & Car AC</p>
</div>
</div>
""", unsafe_allow_html=True)

# ===== MAMA OLOJA AI CHAT =====
with st.expander("🤖 Ask Mama Oloja - Wetin You Dey Find?", expanded=False):
    st.write("Talk to me like you dey market! I sabi all products!")
    q = st.text_input("Ask Mama Oloja:", placeholder="e.g. I get 5000, wetin I fit buy?").lower()
    c1, c2, c3, c4 = st.columns(4)
    if c1.button("I get ₦5,000"):
        q = "i get 5000"
    if c2.button("Gift for Girlfriend"):
        q = "gift for girlfriend"
    if c3.button("I dey Ibadan"):
        q = "i dey ibadan"
    if c4.button("Best Perfume"):
        q = "best perfume"
    if st.button("💬 Ask Mama Oloja"):
        if "5000" in q:
            st.success("Mama Oloja: Ah! ₦5,000? Buy Black Rapture ₦4,000 from Mary - e sweet pass! Or Hand Chain ₦2,000 + Mini Perfume ₦3,500!")
        elif "girlfriend" in q:
            st.success("Mama Oloja: For girlfriend? Buy Lip Combo ₦6,000 - girls dey love am! Or Hand Chain ₦2,000 + Mini Perfume ₦3,500 = ₦5,500 - she go think say you spend ₦10k!")
        elif "ibadan" in q:
            st.success("Mama Oloja: You dey Ibadan? Arinfe dey Academy! Rolex ₦10k, Lip Combo ₦6k, Scarf ₦3.5k. Delivery ₦1,000 or Pickup FREE!")
        elif "perfume" in q:
            st.success("Mama Oloja: Best perfume for ₦4,000 na Black Rapture - 20 reviews, ⭐5.0! For ₦10,000 na Vintage Radio!")
        elif q:
            st.success(f"Mama Oloja: You ask '{q}' - Tell me your budget, who you dey buy for, where you dey - I go help you!")
        else:
            st.write("Ask me anything: budget, gift, location, perfume, combo!")

# ===== 🎬 ANIME ADVERT - NEW PERMANENT FEATURE - ₦200 =====
st.markdown("---")
st.markdown("### 🎬 Mama Oloja Anime Advert - Permanent For All Sellers")
st.write("Generate FREE, Download na **₦200** only! Mama Oloja voice + Anime Girl = Sell fast!")
with st.expander("🎬 Make Anime Advert For Your Product - ₦200 To Download", expanded=False):
    st.write(f"Uploading as: **{st.session_state['seller_name']}**")
    prod_name = st.text_input("Product Name for Advert:", value="Face Serum")
    prod_price = st.text_input("Price:", value="4000")
    prod_phone = st.text_input("Your WhatsApp Number:", value="07052528772")
    anime_style = st.selectbox("Anime Style:", ["C - Cute Anime Girl (Pink) - Best for Perfume/Beauty", "A - Fine Anime Babe - Best for Luxury", "B - Cool Anime Boy - Best for Watch/Men"])
    voice_style = st.selectbox("Mama Oloja Voice:", ["Mama Oloja Pidgin (Funny) - Best!", "Mama Oloja English (Clear)", "Mama Oloja Yoruba Mix"])

    if st.button("✨ Generate My Advert - FREE Preview"):
        st.session_state['anime_ready'] = True
        if "Black Rapture" in prod_name:
            st.session_state['anime_script'] = "My pikin, come see o! Black Rapture don land! E dey smell like money, e dey last all day! Chat me now to order. Mama Oloja talk am, e no be lie!"
        elif "Rolex" in prod_name:
            st.session_state['anime_script'] = "My pikin, see Rolex Watch! E go make you look like big boy! Price na 10,000 only, with box! Chat me now, no dull!"
        elif "Face Serum" in prod_name:
            st.session_state['anime_script'] = "My pikin, your face go glow! Face Serum na 4,000 only! E go clear your face, make you shine! Chat Blessing now!"
        else:
            st.session_state['anime_script'] = f"My pikin, come see o! {prod_name} don land! Price na {prod_price} only! E good well well! Chat me for {prod_phone} now to order. Mama Oloja talk am!"

    if st.session_state.get('anime_ready'):
        st.success("Preview Ready!")
        st.code(st.session_state['anime_script'])
        st.write(f"Style: {anime_style} | Voice: {voice_style}")
        st.info("Preview FREE. Download na ₦200.")
        st.write("**Pay ₦200 to:**")
        st.write("**Opay: 8116911722**")
        st.write("**Name: Kilani Muhammed Opeyemi**")
        st.write("**Narration: Anime Advert - Your Name**")
        pay_ref = st.text_input("Enter Opay Name + Reference after you pay:", placeholder="e.g. BLESSING - 200")
        if st.button("✅ I Don Pay ₦200 - Unlock Download"):
            if pay_ref:
                st.session_state['anime_paid'] = True
                st.success("Payment received! Download don unlock! Mama Oloja don bless your business!")
            else:
                st.warning("Abeg enter Opay name + reference first.")
        if st.session_state.get('anime_paid'):
            st.download_button("📜 Download Mama Oloja Script (TXT)", st.session_state['anime_script'], file_name="mama-oloja-script.txt")
            st.write("🎙️ **Voice:** Go ttsmaker.com, paste script, Voice: Female Warm, Speed 0.9x, Download MP3")
            st.write("🖼️ **Anime Picture:** Use Cute Anime Girl picture as cover")
            st.write("🎬 **Video:** Join Picture + Voice for OpenCut, Post for TikTok!")
            st.write("💬 **Need Help?** Chat CEO: https://wa.me/2348116911722")
            st.balloons()
        else:
            st.warning("🔒 Download Locked - Pay ₦200 to Opay 8116911722 - Kilani Muhammed Opeyemi")

# ===== CATEGORIES =====
st.markdown("---")
st.subheader("Shop by Category")
for emoji, label, color in [("💄","Cosmetics","#ffd6e0"), ("🚗","Car Mart","#ffe4b5"), ("👕","Clothes","#cceaff"), ("🧰","Services","#c8f7c5")]:
    st.markdown(f"""<div style="background:{color}; padding:20px; border-radius:20px; text-align:center; margin-bottom:5px;"><div style="font-size:35px;">{emoji}</div><h3>{label}</h3></div>""", unsafe_allow_html=True)
    if st.button(label, key=f"cat_{label}"):
        st.info(f"You click {label} - Showing {label} products...")

# ===== SELLER OF THE WEEK =====
st.markdown("""
<div style="background:#fff9c4; padding:15px; border-radius:15px; border:1px solid #FFD700;">
<h3>👑 SELLER OF THE WEEK</h3>
<h3>❄️ Horlance Auto Cooling Ltd • ⭐ 5.0 • 340 Jobs Done</h3>
<p>Car AC Specialist - Osun & Oyo - "We Keep You Cool, Always!"</p>
<p>✅ Verified • 📞 09046044472 • 📞 09067551606</p>
</div>
""", unsafe_allow_html=True)
if st.button("📍 Turn On Location"):
    st.success("Location ON - Showing sellers near Ikorodu!")

# ===== UPLOAD PRODUCT =====
with st.expander("📸 Upload Product - Picture / Video (Sellers)", expanded=False):
    st.success(f"Uploading as: {st.session_state['seller_name']}")
    p_name = st.text_input("Product Name")
    p_price = st.number_input("Price", value=0)
    p_cat = st.selectbox("Category", ["Cosmetics", "Car Mart", "Clothes", "Services", "Perfume", "Beauty"])
    p_desc = st.text_area("Description")
    p_img = st.file_uploader("Upload Picture / Video", type=["jpg","png","mp4"])
    if st.button("Post Product"):
        if p_name:
            st.success(f"Product {p_name} - ₦{p_price} posted! Mama Oloja go push am!")
            # Also offer anime advert immediately
            st.info("Want Anime Advert for this product? Scroll up to Mama Oloja Anime Advert - ₦200 only!")
        else:
            st.warning("Enter Product Name first.")

# ===== HOT DEALS =====
st.header("🔥 Hot Deals - Today Only")
st.markdown("""
<div style="background:#e0f7ff; padding:15px; border-radius:20px;">
<span style="background:#ff2d55; color:white; padding:5px 10px; border-radius:20px;">-27% OFF</span>
<div style="text-align:center; font-size:80px;">💧</div>
<p style="background:#0a9a3a; color:white; padding:5px 10px; border-radius:20px; display:inline-block;">🚚 FREE Delivery Today</p>
</div>
<div style="padding:15px;">
<h3>Face Serum</h3>
<p>by Blessing ✅ Verified • 1.2k sold</p>
<p>⭐ 4.9 (1.2k sold)</p>
<h2 style="color:green;">N4,000 <span style="text-decoration:line-through; color:grey; font-size:16px;">N5,500</span> <span style="color:red; font-size:14px;">Use ROW500 = N3,500 if first order</span></h2>
<p>For glow, dark marks, dull skin</p>
</div>
""", unsafe_allow_html=True)
if st.button("❤️ Add Face Serum to Wishlist"):
    st.success("Added to Wishlist! +10 Coins")
    st.session_state['coins'] += 10
if st.button("💬 Buy Face Serum via WhatsApp - Blessing"):
    st.markdown("[Chat Blessing](https://wa.me/2347052528772?text=Hello Blessing, I want Face Serum - 4000 from ROW Market)")
if st.button("🎬 Make Anime Advert For Face Serum - ₦200"):
    st.info("Scroll up to Anime Advert section, pick Face Serum, pay ₦200 to Opay 8116911722!")

# ===== MESSENGER =====
st.markdown("---")
st.header("Messenger")
st.write("Who to chat?")
chat_to = st.selectbox("", ["Market Square - Everybody", "Mama Oloja", "Blessing Cosmetics", "Horlance Auto Cooling"])
your_name = st.text_input("Your Name", value="Muhammd")
msg = st.text_area("Type message...")
if st.button("Send Message"):
    if msg:
        st.success(f"{your_name} to {chat_to}: {msg} - Sent!")
        st.session_state['coins'] += 5
reply = st.text_area("Reply as Seller...")
if st.button("Reply as Seller"):
    if reply:
        st.success(f"Seller reply: {reply}")

# ===== FOOTER =====
st.markdown("---")
st.write(f"**Your Coins: {st.session_state['coins']}** - Earn coins by liking, adding to cart, inviting friends. Use coins for discount!")
st.write("**How to Pay:** Chat seller → Confirm price → Use code ROW500 for N500 OFF → Transfer / Pay on delivery → Delivered.")
st.write("**Want to Sell?** Join FREE - 8 slots left. WhatsApp Admin: https://wa.me/2348116911722")
st.write("**Anime Advert:** Any seller fit make Mama Oloja Anime Advert - ₦200 to Opay 8116911722 - Kilani Muhammed Opeyemi")
st.write("© 2026 Row Economy Market - Powered by Mama Oloja 🧕")
