import streamlit as st
import random
st.set_page_config(page_title="ROW Economy Market", page_icon="🛍️", layout="wide")

if 'coins' not in st.session_state: st.session_state['coins']=100
if 'show_anime' not in st.session_state: st.session_state['show_anime']=False
if 'anime_paid' not in st.session_state: st.session_state['anime_paid']=False

PRODUCTS=[
{"name":"Black Rapture","price":4000,"seller":"Mary","phone":"09031889875","loc":"Lagos","cat":"Perfume","desc":"Bold, long-lasting, smell like money"},
{"name":"Black Rapture","price":4000,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Perfume","desc":"Bold, long-lasting"},
{"name":"Vintage Radio","price":10000,"seller":"Mary","phone":"09031889875","loc":"Lagos","cat":"Perfume","desc":"Warm, vintage, Lattafa"},
{"name":"Body Mist","price":4000,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Perfume","desc":"Soft, sweet, everyday"},
{"name":"Yum Yum Combo","price":12000,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Perfume","desc":"Perfume + Body Spray"},
{"name":"Musk Vanille","price":6000,"seller":"Mary","phone":"09031889875","loc":"Lagos","cat":"Perfume","desc":"Vanilla sweet"},
{"name":"Face Serum","price":4000,"seller":"Blessing","phone":"07052528772","loc":"Abuja","cat":"Beauty","desc":"Clear face, glow"},
{"name":"Ceramide Serum","price":5000,"seller":"Blessing","phone":"07052528772","loc":"Abuja","cat":"Beauty","desc":"For dry skin"},
{"name":"TONYMOLY Toner","price":6000,"seller":"Blessing","phone":"07052528772","loc":"Abuja","cat":"Beauty","desc":"Tone + glow"},
{"name":"Sunscreen","price":5000,"seller":"Blessing","phone":"07052528772","loc":"Abuja","cat":"Beauty","desc":"Protect your skin"},
{"name":"Lip Combo","price":6000,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Beauty","desc":"Brown + Pink + Liner"},
{"name":"Rolex Watch","price":10000,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Watch","desc":"Black strap, 3 designs, with box"},
{"name":"Hand Chain","price":2000,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Jewelry","desc":"Gold + Black LV"},
{"name":"Gold Necklace","price":8000,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Jewelry","desc":"Shine for owambe"},
{"name":"Earrings","price":3000,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Jewelry","desc":"Fine earrings"},
{"name":"Jersey Scarf Plain","price":3500,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Scarf","desc":"Soft, no slip, for hijab"},
{"name":"Jersey Scarf Pattern","price":4000,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Scarf","desc":"Stylish, for owambe"},
{"name":"Tote Bag","price":6500,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Bag","desc":"Big, strong bag"},
{"name":"Real Man Spray","price":4500,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Perfume","desc":"Fresh, Morning, Active - for men"},
{"name":"Mini Perfume","price":3500,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Perfume","desc":"Small, sweet, carry anywhere"},
{"name":"Suger Pink Spray","price":6000,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Perfume","desc":"Sweet pink, girls love am"},
{"name":"Doneva Lipgloss","price":3500,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Beauty","desc":"Shine lipgloss"},
{"name":"Skin Glow Oil","price":5000,"seller":"Blessing","phone":"07052528772","loc":"Abuja","cat":"Beauty","desc":"Glow oil for body"},
{"name":"Hair Bonnet","price":2500,"seller":"Arinfe","phone":"090915907990","loc":"Ibadan","cat":"Clothes","desc":"Protect your hair"},
{"name":"Car AC Repair","price":15000,"seller":"Horlance","phone":"09046044472","loc":"Osun","cat":"Services","desc":"Car AC Specialist - 340 Jobs Done"},
]

# ===== ANIME ADVERT TOP - ALWAYS VISIBLE =====
st.markdown("""<div style="background:#ff2d55; padding:20px; border-radius:15px; text-align:center; color:white;"><h1 style="color:white;">🎬 MAMA OLOJA ANIME ADVERT</h1><h3 style="color:white;">Make Anime Video For Your Product - ₦200 ONLY!</h3><p>Pay to Opay 8116911722 - Kilani Muhammed Opeyemi</p></div>""", unsafe_allow_html=True)
if st.button("🎬 CLICK HERE - Make My Anime Advert - ₦200"):
    st.session_state['show_anime']=True
if st.session_state['show_anime']:
    st.header("🎬 Mama Oloja Anime Advert")
    names=[f"{p['name']} - ₦{p['price']} - {p['seller']}" for p in PRODUCTS]
    chosen=st.selectbox("Pick your product:", names)
    prod_name=st.text_input("Or type new product:", value="Face Serum")
    prod_price=st.text_input("Price:", value="4000")
    prod_phone=st.text_input("Your WhatsApp:", value="07052528772")
    style=st.selectbox("Anime Style:", ["C - Cute Anime Girl (Pink) - Best!", "A - Fine Anime Babe", "B - Cool Anime Boy"])
    if st.button("✨ Generate FREE Preview"):
        final = prod_name if prod_name else chosen
        if "Black Rapture" in final: st.session_state['script']="My pikin, come see o! Black Rapture don land! E dey smell like money, e dey last all day! Chat me now to order. Mama Oloja talk am, e no be lie!"
        elif "Rolex" in final: st.session_state['script']="My pikin, see Rolex Watch! E go make you look like big boy! Price na 10,000 only, with box! Chat me now, no dull!"
        elif "Face Serum" in final: st.session_state['script']="My pikin, your face go glow! Face Serum na 4,000 only! E go clear your face, make you shine! Chat Blessing now!"
        else: st.session_state['script']=f"My pikin, come see o! {final} don land! Price na {prod_price} only! E good well well! Chat me for {prod_phone} now! Mama Oloja talk am!"
    if st.session_state.get('script'):
        st.code(st.session_state['script'])
        st.write(f"Style: {style}")
        st.write("**Pay ₦200 to: Opay 8116911722 - Kilani Muhammed Opeyemi**")
        ref=st.text_input("Enter Opay Name + Ref after you pay:", placeholder="e.g. BLESSING - 200")
        if st.button("✅ I Don Pay ₦200 - Unlock Download"):
            if ref: st.session_state['anime_paid']=True; st.success("Unlocked! Download don open!")
            else: st.warning("Enter Opay name first.")
        if st.session_state['anime_paid']:
            st.download_button("📜 Download Mama Oloja Script", st.session_state['script'], file_name="mama-oloja-script.txt")
            st.write("🎙️ Voice: Go ttsmaker.com, paste script, Female Warm, Speed 0.9x")
            st.write("🖼️ Picture: Use Cute Anime Girl picture | 🎬 Video: Join for OpenCut, post for TikTok!")
            st.balloons()
        else: st.warning("🔒 Locked - Pay ₦200 to Opay 8116911722 to unlock.")

st.markdown("---")
# ===== WELCOME =====
st.markdown("""<div style="background:linear-gradient(to bottom right, #0a7a42, #d4c400); padding:20px; border-radius:20px; color:white;"><h2 style="color:#FFD700;">✦ ROW ECONOMY MARKET ✦</h2><h1>Welcome back,<br>Muhammd! 👋</h1><p>Everything you need, near you. No scam. Mama Oloja dey watch for you.</p><p>⭐ 4.9 Rating • 2,347 Happy Buyers • 🚚 FREE Delivery Today In Ikorodu</p></div>""", unsafe_allow_html=True)
st.info("🛡️ **Mama Oloja Guarantee:** If seller scam you, we refund you. 100% Safe.")
st.markdown("""<div style="background:linear-gradient(to right, #ff6b35, #ff3b6b); padding:20px; border-radius:20px; color:white; text-align:center;"><h1>🎁 YOU WON ₦500 OFF!</h1><p>Use code: <b>ROW500</b></p></div>""", unsafe_allow_html=True)
if st.button("🎁 Claim My ₦500 OFF Now"): st.success("Code ROW500 Activated!")
st.markdown("""<div style="border:2px dashed #FFD700; padding:15px; border-radius:15px; text-align:center;"><h3>🎡 SPIN & WIN</h3></div>""", unsafe_allow_html=True)
if st.button("🎡 SPIN NOW - It's FREE!"):
    prize=random.choice(["50 Coins","FREE Delivery","₦200 OFF","100 Coins","Try Again"]); st.success(f"You won: {prize}!")
    if "Coins" in prize: st.session_state['coins']+=50
st.markdown("""<div style="background:#7b2ff7; padding:15px; border-radius:15px; color:white;"><h3>👥 REFER & EARN ₦200</h3><p>Invite friend, you get ₦200, friend gets ₦200.</p></div>""", unsafe_allow_html=True)
st.markdown("""<div style="background:#ff2d55; padding:15px; border-radius:15px; color:white;"><h3>⚡ FLASH SALE - Up to 30% OFF - 01 : 59 : 12</h3></div>""", unsafe_allow_html=True)

# ===== SHOP 25 PRODUCTS =====
st.header(f"🛍️ Shop - {len(PRODUCTS)} Products")
search=st.text_input("🔍 Search:", placeholder="Search serum, sunscreen, Black Rapture...")
cat=st.selectbox("Filter Category:", ["All","Perfume","Beauty","Watch","Jewelry","Scarf","Bag","Clothes","Services"])
loc=st.selectbox("Filter Location:", ["All","Ibadan","Lagos","Abuja","Osun"])
for p in PRODUCTS:
    if search and search.lower() not in p["name"].lower(): continue
    if cat!="All" and p["cat"]!=cat: continue
    if loc!="All" and p["loc"]!=loc: continue
    st.write(f"**{p['name']}** - ₦{p['price']:,} | {p['seller']} - {p['loc']} | {p['cat']}")
    st.write(p["desc"])
    st.markdown(f"[💬 Buy via WhatsApp - {p['seller']}](https://wa.me/234{p['phone'][1:]}?text=Hello {p['seller']}, I want {p['name']} - {p['price']} from ROW Market)")
    st.markdown("---")

# ===== MAMA OLOJA CHAT =====
st.header("🤖 Mama Oloja - Ask Me!")
q=st.text_input("Ask Mama Oloja:", placeholder="e.g. I get 5000, wetin I fit buy?").lower()
if st.button("💬 Ask Mama Oloja"):
    if "5000" in q: st.success("Mama Oloja: Buy Black Rapture ₦4,000 from Mary - e sweet pass! Or Hand Chain ₦2,000 + Mini Perfume ₦3,500!")
    elif "girlfriend" in q: st.success("Mama Oloja: For girlfriend? Buy Lip Combo ₦6,000 - girls dey love am!")
    elif "ibadan" in q: st.success("Mama Oloja: You dey Ibadan? Arinfe dey Academy! Rolex ₦10k, Lip Combo ₦6k, Scarf ₦3.5k. Delivery ₦1,000!")
    elif "perfume" in q: st.success("Mama Oloja: Best perfume for ₦4,000 na Black Rapture - 20 reviews, ⭐5.0!")
    elif q: st.success(f"Mama Oloja: Tell me your budget, who you dey buy for, where you dey - I go help you!")
    else: st.write("Ask me: budget, gift, location, perfume!")

# ===== SELLER OF WEEK + UPLOAD =====
st.markdown("""<div style="background:#fff9c4; padding:15px; border-radius:15px;"><h3>👑 SELLER OF THE WEEK - Horlance Auto Cooling Ltd • ⭐ 5.0 • 340 Jobs Done</h3><p>Car AC Specialist - Osun & Oyo • 📞 09046044472</p></div>""", unsafe_allow_html=True)
with st.expander("📸 Upload Product - Sellers", expanded=False):
    st.write("Uploading as: Blessing Cosmetics")
    pn=st.text_input("Product Name"); pp=st.number_input("Price", value=0); pd=st.text_area("Description")
    if st.button("Post Product"):
        if pn: st.success(f"{pn} - ₦{pp} posted! Want Anime Advert? Scroll to TOP - RED BANNER - ₦200 only!")
        else: st.warning("Enter Product Name first.")

st.header("Messenger")
st.write("Chat: Market Square - Mama Oloja - Blessing - Horlance")
st.write(f"**Your Coins: {st.session_state['coins']}** | How to Pay: Chat seller → Confirm price → Use ROW500 → Transfer / Pay on delivery")
st.write("**Want to Sell?** Join FREE - WhatsApp Admin: https://wa.me/2348116911722 | **Anime Advert ₦200 to Opay 8116911722 - Kilani Muhammed Opeyemi**")
st.write("© 2026 Row Economy Market - Powered by Mama Oloja 🧕")
