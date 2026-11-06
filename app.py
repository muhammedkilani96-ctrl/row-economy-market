import streamlit as st
import random
st.set_page_config(page_title="ROW Economy Market - Type Anything Anime", page_icon="🎬", layout="wide")
if 'coins' not in st.session_state:
    st.session_state['coins'] = 100
if 'script' not in st.session_state:
    st.session_state['script'] = ""
if 'video_prompt' not in st.session_state:
    st.session_state['video_prompt'] = ""
if 'pic_prompt' not in st.session_state:
    st.session_state['pic_prompt'] = ""
if 'my_product' not in st.session_state:
    st.session_state['my_product'] = ""
st.markdown('<div style="background:#ff2d55; padding:20px; border-radius:15px; text-align:center; color:white;"><h1 style="color:white;">MAMA OLOJA VIDEO ANIME - FREE!</h1><h3 style="color:white;">Type ANYTHING - We Go Make Anime Advert For Am!</h3><p>100% FREE FOR NOW - No Payment!</p></div>', unsafe_allow_html=True)
st.write("Type anything you dey sell - shoe, hair, perfume, cake, car AC, groundnut, anything!")
st.write("Example: Try type - Red Shoe 8000 - or - Hair Wig 15000 - or - Jollof Rice")
custom = st.text_input("SEARCH BAR - Type Your Product Here:", placeholder="e.g. Red Shoe 8000, Hair Wig 15000, Cake, Car AC Repair, Groundnut...")
price = st.text_input("Your Price (Optional):", placeholder="e.g. 8000")
seller_name = st.text_input("Your Name / Shop Name (Optional):", placeholder="e.g. Mary, Blessing Shop")
style = st.selectbox("Anime Girl Style:", ["C - Cute Anime Girl Pink Hair - Best for TikTok!", "A - Fine Anime Babe - Brown Skin", "B - Cool Anime Boy - For Boys Products"])
st.write("Quick Pick - Tap one if you no wan type:")
col1, col2, col3, col4 = st.columns(4)
if col1.button("Black Rapture"):
    custom = "Black Rapture Perfume 4000"
if col2.button("Face Serum"):
    custom = "Face Serum 4000"
if col3.button("Rolex Watch"):
    custom = "Rolex Watch 10000"
if col4.button("Lip Combo"):
    custom = "Lip Combo 6000"
st.write("You type: " + custom if custom else "You never type anything yet - type for search bar above!")
if st.button("Generate My Video Advert - FREE!"):
    if not custom:
        st.warning("Abeg type your product for search bar first! Example: Red Shoe 8000")
    else:
        st.session_state['my_product'] = custom
        pname = custom
        pinfo = pname
        if price:
            pinfo = pname + " - Price " + price
        if seller_name:
            pinfo = pinfo + " - from " + seller_name
        low = pname.lower()
        if "shoe" in low or "sneaker" in low or "heel" in low:
            st.session_state['script'] = "My pikin, come see o! " + pinfo + "! E fine well well, e go make your leg fine! If you wear am, everybody go dey look you! Chat me now to order, e dey hot! Mama Oloja talk am!"
        elif "hair" in low or "wig" in low:
            st.session_state['script'] = "My pikin, come see o! " + pinfo + "! E soft, e fine, e go make you look like queen! No wahala, just wear am and shine! Chat me now to order! Mama Oloja recommend am!"
        elif "cake" in low or "food" in low or "rice" in low or "snack" in low or "groundnut" in low:
            st.session_state['script'] = "My pikin, come taste o! " + pinfo + "! E sweet, e fresh, e go make your belle happy! Order now, e go finish quick! Chat me now! Mama Oloja talk am, e no be lie!"
        elif "car" in low or "ac" in low:
            st.session_state['script'] = "My pikin, your car AC don spoil? No worry! " + pinfo + "! We go fix am sharp sharp, e go cold like ice! Chat me now! Mama Oloja guarantee am!"
        elif "perfume" in low or "rapture" in low:
            st.session_state['script'] = "My pikin, come see o! " + pinfo + "! E dey smell like money, e dey last all day! Chat me now to order. Mama Oloja talk am, e no be lie!"
        elif "watch" in low or "rolex" in low:
            st.session_state['script'] = "My pikin, see " + pinfo + "! E go make you look like big boy, big girl! Chat me now, no dull!"
        elif "serum" in low or "cream" in low or "face" in low or "skin" in low:
            st.session_state['script'] = "My pikin, your face go glow! " + pinfo + "! E go clear your face, make you shine! Chat me now!"
        else:
            st.session_state['script'] = "My pikin, come see o! " + pinfo + "! E good well well, price sweet, quality top! Chat me now to order. Mama Oloja recommend am, e no be lie!"
        if "Cute" in style or "C -" in style:
            char = "Cute anime girl, pink hair, big eyes, smiling, Nigerian market background"
        elif "Fine" in style or "A -" in style:
            char = "Beautiful anime babe, brown skin, long black hair, smiling, Nigerian market background"
        else:
            char = "Cool anime boy, short hair, smiling, holding product, Nigerian market background"
        st.session_state['video_prompt'] = char + ", holding " + pinfo + ", waving hand, lips moving and talking, blinking, lively, TikTok anime style, bright colors, 4k"
        st.session_state['pic_prompt'] = char + ", holding " + pinfo + ", full body, smiling at camera, bright, high quality, TikTok style"
if st.session_state['script']:
    st.success("Your Video Package Ready - 100% FREE! For: " + st.session_state['my_product'])
    st.balloons()
    st.markdown("### YOUR VIDEO ANIME PACKAGE - DO AM IN 3 MINS - FREE!")
    st.markdown("#### STEP A - MAKE ANIME PICTURE - FREE")
    st.write("Copy this prompt, go Bing Create, paste am, download picture:")
    st.code(st.session_state.get('pic_prompt', ''))
    st.markdown("[Click Here - Make Picture FREE (Bing Create)](https://www.bing.com/images/create)")
    st.markdown("---")
    st.markdown("#### STEP B - MAKE VIDEO FROM PICTURE - FREE")
    st.write("Go Hailuo AI, upload picture wey you just make, paste this Video Prompt:")
    st.code(st.session_state.get('video_prompt', ''))
    st.markdown("[Click Here - Make Video FREE (Hailuo AI)](https://hailuoai.video)")
    st.markdown("[Alternative - Make Video FREE (Kling AI)](https://klingai.com)")
    st.write("Wait 1 min, Download Video! Girl go dey move, mouth go dey talk!")
    st.markdown("---")
    st.markdown("#### STEP C - ADD MAMA OLOJA VOICE - FREE")
    st.write("Your Mama Oloja Script:")
    st.write(st.session_state['script'])
    st.write("Copy script, go TTSMaker, paste am, Voice: Female Warm, Speed 0.9x, Download MP3:")
    st.code(st.session_state['script'])
    st.download_button("Download Script FREE", st.session_state['script'], file_name="mama-oloja-script.txt")
    st.markdown("[Click Here - Make Voice FREE (TTSMaker)](https://ttsmaker.com)")
    st.markdown("---")
    st.markdown("#### STEP D - JOIN VIDEO + VOICE - FREE")
    st.write("Go CapCut App (for phone), Import Video + Voice, Export, Post for TikTok / WhatsApp Status!")
    st.markdown("[Download CapCut FREE](https://www.capcut.com)")
    st.write("Enjoy FREE for now! Share am with your friends! Tag @row.economy.market for TikTok!")
    st.write("Need Help? Chat us FREE: https://wa.me/2348116911722")
    if st.button("Make Another Advert - Clear"):
        st.session_state['script'] = ""
        st.session_state['my_product'] = ""
        st.rerun()
st.markdown("---")
st.markdown('<div style="background:black; color:white; padding:10px; border-radius:15px;"><span>Ikorodu, Lagos</span> <span>100 Coins</span></div>', unsafe_allow_html=True)
st.markdown('<div style="background:linear-gradient(to bottom right, #0a7a42, #d4c400); padding:20px; border-radius:20px; color:white;"><h2 style="color:#FFD700;">ROW ECONOMY MARKET</h2><h1>Welcome back, muhammed!</h1><p>Everything you need, near you. No scam. Mama Oloja dey watch for you.</p><p>4.9 Rating - 2,347 Happy Buyers - FREE Delivery Today In Ikorodu</p></div>', unsafe_allow_html=True)
st.info("Mama Oloja Guarantee: If seller scam you, we refund you. 100% Safe. Verified Sellers Only")
st.markdown('<div style="background:linear-gradient(to right, #ff6b35, #ff3b6b); padding:20px; border-radius:20px; color:white; text-align:center;"><h1>YOU WON 500 OFF!</h1><p>Your first order - Use code: ROW500</p></div>', unsafe_allow_html=True)
if st.button("Claim My 500 OFF Now"):
    st.success("Code ROW500 Activated!")
st.markdown('<div style="border:2px dashed #FFD700; padding:15px; border-radius:15px; text-align:center;"><h3>SPIN & WIN - Daily Luck!</h3></div>', unsafe_allow_html=True)
if st.button("SPIN NOW - It is FREE!"):
    prize = random.choice(["50 Coins", "FREE Delivery", "200 OFF", "100 Coins", "Try Again"])
    st.success("You won: " + prize + "!")
    if "Coins" in prize:
        st.session_state['coins'] += 50
search = st.text_input("Search Shop:", placeholder="Search serum, sunscreen, Black Rapture...")
st.write("Blessing Cosmetics")
with st.expander("Seller Login", expanded=True):
    st.success("Logged in as Blessing Cosmetics")
st.markdown('<div style="background:white; padding:15px; border-radius:15px;"><h3>Mama Oloja - Online - Replies in 2 secs</h3><p>Your Market Aunty - She sabi price, skin & Car AC</p></div>', unsafe_allow_html=True)
with st.expander("Ask Mama Oloja - Wetin You Dey Find?"):
    q = st.text_input("Ask Mama Oloja:", placeholder="e.g. I get 5000, wetin I fit buy?").lower()
    if st.button("Ask Mama Oloja"):
        if "5000" in q:
            st.success("Mama Oloja: Buy Black Rapture 4,000 from Mary - e sweet pass!")
        elif "girlfriend" in q:
            st.success("Mama Oloja: For girlfriend? Buy Lip Combo 6,000 - girls dey love am!")
        elif "ibadan" in q:
            st.success("Mama Oloja: You dey Ibadan? Arinfe dey Academy! Rolex 10k, Lip Combo 6k, Scarf 3.5k!")
        elif "perfume" in q:
            st.success("Mama Oloja: Best perfume for 4,000 na Black Rapture - 20 reviews, 5.0!")
        elif q:
            st.success("Mama Oloja: Tell me your budget, who you dey buy for, where you dey - I go help you!")
st.subheader("Shop by Category")
for emoji, label, color in [("Cosmetics", "Cosmetics", "#ffd6e0"), ("Car", "Car Mart", "#ffe4b5"), ("Clothes", "Clothes", "#cceaff"), ("Services", "Services", "#c8f7c5")]:
    st.markdown('<div style="background:' + color + '; padding:20px; border-radius:20px; text-align:center;"><h3>' + label + '</h3></div>', unsafe_allow_html=True)
st.markdown('<div style="background:#fff9c4; padding:15px; border-radius:15px; border:1px solid #FFD700;"><h3>SELLER OF THE WEEK</h3><h3>Horlance Auto Cooling Ltd - 5.0 - 340 Jobs Done</h3><p>Car AC Specialist - Osun & Oyo - 09046044472</p></div>', unsafe_allow_html=True)
st.header("Shop - All Products")
PRODUCTS = [("Black Rapture", 4000, "Mary", "09031889875", "Lagos", "Bold, long-lasting"), ("Black Rapture", 4000, "Arinfe", "090915907990", "Ibadan", "Bold, long-lasting"), ("Vintage Radio", 10000, "Mary", "09031889875", "Lagos", "Warm, vintage"), ("Face Serum", 4000, "Blessing", "07052528772", "Abuja", "Clear face, glow"), ("Rolex Watch", 10000, "Arinfe", "090915907990", "Ibadan", "Black strap, with box"), ("Lip Combo", 6000, "Arinfe", "090915907990", "Ibadan", "Brown + Pink + Liner"), ("Jersey Scarf", 3500, "Arinfe", "090915907990", "Ibadan", "Soft, no slip"), ("Yum Yum Combo", 12000, "Arinfe", "090915907990", "Ibadan", "Perfume + Spray"), ("Tote Bag", 6500, "Arinfe", "090915907990", "Ibadan", "Big, strong bag"), ("Hand Chain", 2000, "Arinfe", "090915907990", "Ibadan", "Gold + Black LV")]
for name, price, seller, phone, loc, desc in PRODUCTS:
    if search and search.lower() not in name.lower():
        continue
    st.write(name + " - " + str(price) + " | " + seller + " - " + loc)
    st.write(desc)
    st.markdown("[Buy via WhatsApp - " + seller + "](https://wa.me/234" + phone[1:] + "?text=Hello " + seller + ", I want " + name + " - " + str(price) + " from ROW Market)")
    st.markdown("---")
with st.expander("Upload Product - Sellers"):
    st.write("Uploading as: Blessing Cosmetics")
    pn = st.text_input("Product Name")
    pp = st.number_input("Price", value=0)
    if st.button("Post Product"):
        if pn:
            st.success(pn + " - " + str(pp) + " posted! Want Video Anime FREE? Scroll to TOP - Type anything for search bar!")
        else:
            st.warning("Enter Product Name first.")
st.header("Hot Deals - Face Serum 4,000")
st.write("by Blessing Verified - 4.9 (1.2k sold) - FREE Delivery Today")
if st.button("Add Face Serum to Wishlist"):
    st.success("Added to Wishlist! +10 Coins")
if st.button("Buy Face Serum via WhatsApp - Blessing"):
    st.markdown("[Chat Blessing](https://wa.me/2347052528772?text=Hello Blessing, I want Face Serum - 4000)")
st.header("Messenger")
st.write("Chat: Market Square - Mama Oloja - Blessing - Horlance")
msg = st.text_area("Type message...")
if st.button("Send Message"):
    if msg:
        st.success("Sent: " + msg)
st.markdown("---")
st.write("Your Coins: " + str(st.session_state['coins']))
st.write("Want to Sell? Join FREE - WhatsApp Admin: https://wa.me/2348116911722")
st.write("Video Anime: 100% FREE FOR NOW - Type Anything!")
st.write("2026 Row Economy Market - Powered by Mama Oloja")
