import streamlit as st
import random
st.set_page_config(page_title="ROW COMPLETE - LIVE MARKET - @kelly", page_icon="🔴", layout="wide")
if 'script' not in st.session_state:
    st.session_state['script'] = ""
if 'twin_name' not in st.session_state:
    st.session_state['twin_name'] = ""
if 'twin_on' not in st.session_state:
    st.session_state['twin_on'] = False
if 'my_product' not in st.session_state:
    st.session_state['my_product'] = ""
if 'live_on' not in st.session_state:
    st.session_state['live_on'] = False
if 'live_seller' not in st.session_state:
    st.session_state['live_seller'] = ""
if 'live_product' not in st.session_state:
    st.session_state['live_product'] = ""
if 'live_price' not in st.session_state:
    st.session_state['live_price'] = ""
st.markdown('<div style="background:linear-gradient(to right, #ff0000, #ff2d55, #ff9a00); padding:20px; border-radius:20px; text-align:center; color:white;"><h1 style="color:white;">ROW LIVE MARKET - 7PM LIVE SHOW!</h1><h3 style="color:white;">Live Market - Mama Oloja Dey Shout Live! Buy Now Before E Finish!</h3><p>TONIGHT 7PM - By @kelly</p><p>🔴 LIVE 🔴 LIVE 🔴 LIVE</p></div>', unsafe_allow_html=True)
st.write("TONIGHT WE COMPLETE ROW! TWIN + MAGIC + LIVE!")
tab1, tab2, tab3 = st.tabs(["LIVE MARKET 7PM", "AI TWIN", "MAGIC PIC"])
with tab1:
    st.markdown('<div style="background:black; padding:20px; border-radius:20px; color:white; text-align:center;"><h1 style="color:red;">LIVE NOW</h1><h2 style="color:white;">ROW LIVE MARKET - IKORODU MARKET FOR YOUR PHONE!</h2><p style="color:#FFD700;">Mama Oloja Dey Host Live - 7PM Every Evening!</p><p>234 People Dey Watch Live Now!</p></div>', unsafe_allow_html=True)
    st.write("JOIN LIVE SHOW - PUT YOUR PRODUCT FOR LIVE TONIGHT!")
    live_seller = st.text_input("Your Name For Live:", placeholder="e.g. Mary", key="ls1")
    live_shop = st.text_input("Shop Name For Live:", placeholder="e.g. Blessing Cosmetics", key="ls2")
    live_prod = st.text_input("Product For Live Tonight:", placeholder="e.g. Black Rapture", key="ls3")
    live_price = st.text_input("Live Flash Price - Make Am Cheap For Live!", placeholder="e.g. 3500 - Normal 4000, Live 3500!", key="ls4")
    live_stock = st.selectbox("How Many You Get For Live?", ["5 Only - Rush Am!", "10 Only", "20 Only", "50 Only"])
    if st.button("GO LIVE NOW! - JOIN 7PM SHOW!"):
        if not live_seller or not live_prod:
            st.warning("Abeg put name and product for live!")
        else:
            st.session_state['live_on'] = True
            st.session_state['live_seller'] = live_seller
            st.session_state['live_product'] = live_prod
            st.session_state['live_price'] = live_price
            a1 = "COME COME COME! LIVE MARKET DON START! Na "
            a2 = live_seller
            a3 = " be this! I bring "
            a4 = live_prod
            a5 = " for live! Flash price "
            a6 = live_price
            a7 = " only for live! If you no buy now, e go finish! Chat me now! Follow @kelly!"
            st.session_state['script'] = a1 + a2 + a3 + a4 + a5 + a6 + a7
    if st.session_state['live_on']:
        st.balloons()
        st.markdown('<div style="background:red; padding:15px; border-radius:15px; color:white; text-align:center;"><h2 style="color:white;">YOU DEY LIVE NOW! MAMA OLOJA DEY SHOUT YOUR NAME!</h2><p>234 People Dey Watch You!</p></div>', unsafe_allow_html=True)
        st.write("LIVE STAGE - YOUR PRODUCT DEY SHOW LIVE!")
        up_live = st.file_uploader("Upload Product Pic For Live Stage:", type=["jpg", "jpeg", "png"], key="livepic")
        if up_live:
            st.image(up_live, caption="LIVE NOW - Your Product Dey Show For 234 People! - @kelly", use_column_width=True)
        else:
            st.info("Upload your product pic for live stage - 234 people dey wait!")
        st.markdown('<div style="background:linear-gradient(to right, #ff0000, #FFD700); padding:15px; border-radius:15px;"><h2 style="color:white;">MAMA OLOJA LIVE:</h2><p style="color:white;">' + st.session_state['script'] + '</p><p style="color:white;">Stock: ' + live_stock + '</p></div>', unsafe_allow_html=True)
        st.write("LIVE CHAT - CUSTOMERS DEY SHOUT!")
        st.write("Blessing: I want am! How much?")
        st.write("Tunde: E still dey? I want 2!")
        st.write("Ada: This one fine die! I don buy!")
        st.write("Mama Oloja: Yes o! E still dey! Chat seller now!")
        chat_msg = st.text_input("Type For Live Chat:", placeholder="e.g. I want am! Keep 1 for me!", key="chat1")
        if st.button("Send To Live Chat"):
            if chat_msg:
                st.success("Your chat don show for live! Everybody see am!")
        st.write("FLASH SALE - BUY NOW BEFORE E FINISH!")
        st.write("Product: " + st.session_state['live_product'])
        st.write("Live Price: " + st.session_state['live_price'])
        st.write("Stock: " + live_stock)
        buy1 = "Hello "
        buy2 = st.session_state['live_seller']
        buy3 = " I see you for ROW LIVE! I want "
        buy4 = st.session_state['live_product']
        buy5 = " Live Price "
        buy6 = st.session_state['live_price']
        buy7 = " Keep am for me! - @kelly"
        buy_text = buy1 + buy2 + buy3 + buy4 + buy5 + buy6 + buy7
        st.markdown("[BUY NOW - LIVE FLASH SALE - WhatsApp](https://wa.me/?text=" + buy_text.replace(" ", "%20") + ")")
        st.markdown("[SHARE LIVE - Invite Friends To Watch](https://wa.me/?text=" + buy_text.replace(" ", "%20") + ")")
        st.write("LIVE END CARD:")
        st.markdown('<div style="background:#111; color:white; padding:20px; border-radius:15px; text-align:center;"><h1 style="color:white;">THANKS FOR WATCHING LIVE!</h1><h1 style="color:#FFD700;">@kelly</h1><p>Follow @kelly - See You Tomorrow 7PM Live!</p></div>', unsafe_allow_html=True)
        if st.button("End Live - Save Live Video"):
            st.session_state['live_on'] = False
            st.rerun()
    else:
        st.write("TONIGHT LIVE LINE-UP - 7PM:")
        st.write("7:00 PM - Mama Oloja Opening - Welcome + Giveaway!")
        st.write("7:10 PM - Mary - Black Rapture - Flash Sale!")
        st.write("7:20 PM - Blessing - Face Serum - Glow Demo!")
        st.write("7:30 PM - Arinfe - Rolex Watch - Unboxing Live!")
        st.write("7:40 PM - YOU - Your Product - Your Turn!")
        st.write("Join live, put your product, sell before e finish!")
with tab2:
    st.write("AI TWIN - SHOP NEVER SLEEP!")
    twin_name_in = st.text_input("Your Name:", placeholder="e.g. Mary", key="tw1")
    twin_shop = st.text_input("Shop Name:", placeholder="e.g. Blessing Cosmetics", key="tw2")
    twin_product = st.text_input("Main Product:", placeholder="e.g. Black Rapture", key="tw3")
    twin_price = st.text_input("Price:", placeholder="e.g. 4000", key="tw4")
    twin_lang = st.selectbox("Twin Language:", ["Pidgin", "English", "Yoruba", "Igbo", "Hausa"], key="tw5")
    twin_person = st.selectbox("Twin Personality:", ["Funny Twin", "Sweet Twin", "Shout Twin", "Boss Twin"], key="tw6")
    if st.button("CREATE MY AI TWIN NOW!"):
        if not twin_name_in or not twin_product:
            st.warning("Abeg put name and product!")
        else:
            st.session_state['twin_name'] = twin_name_in
            st.session_state['my_product'] = twin_product
            st.session_state['twin_on'] = True
            b1 = "Na Twin of "
            b2 = twin_name_in
            b3 = " be this! I no dey sleep! Come see "
            b4 = twin_product
            b5 = " Price "
            b6 = twin_price
            b7 = " Chat me now! Follow @kelly!"
            st.session_state['script'] = b1 + b2 + b3 + b4 + b5 + b6 + b7
    if st.session_state['twin_on']:
        st.success("TWIN LIVE! Twin of " + st.session_state['twin_name'] + " dey online 24/7!")
        st.balloons()
        st.markdown('<div style="background:black; padding:20px; border-radius:20px; color:white;"><p style="color:#00ff00;">LIVE - Twin Dey Online 24/7</p><h1 style="color:#FFD700;">Twin of ' + st.session_state['twin_name'] + '</h1><p>Product: ' + st.session_state['my_product'] + '</p><p>Language: ' + twin_lang + '</p></div>', unsafe_allow_html=True)
        st.write("Twin Dey Talk:")
        st.write(st.session_state['script'])
        st.write("Twin Auto-Reply - Copy Am:")
        r1 = "Hello! Na Twin of "
        r2 = st.session_state['twin_name']
        r3 = " be this! I dey online! You want "
        r4 = st.session_state['my_product']
        r5 = " Chat me now! Follow @kelly!"
        st.code(r1 + r2 + r3 + r4 + r5)
        st.write("Twin Morning Magic - Copy Am:")
        mm1 = "Good Morning! Twin of "
        mm2 = st.session_state['twin_name']
        mm3 = " don wake up! Today: "
        mm4 = st.session_state['my_product']
        mm5 = " Order now! Follow @kelly!"
        st.code(mm1 + mm2 + mm3 + mm4 + mm5)
with tab3:
    st.write("MAGIC PIC - PIC DEY TALK!")
    magic_prod = st.text_input("Product For Magic Pic:", placeholder="e.g. Red Shoe", key="mg1")
    magic_price = st.text_input("Price For Magic:", placeholder="e.g. 8000", key="mg2")
    magic_voice = st.selectbox("Voice:", ["Funny", "Sweet", "Shout"], key="mg3")
    if st.button("MAKE MY PIC TALK! - MAGIC!"):
        if not magic_prod:
            st.warning("Abeg type product!")
        else:
            c1 = "Ha! Come see o! "
            c2 = magic_prod
            c3 = " Price "
            c4 = magic_price
            c5 = " E too sweet! Chat me now! Follow @kelly!"
            st.session_state['script'] = c1 + c2 + c3 + c4 + c5
            st.session_state['my_product'] = magic_prod
    if st.session_state['script'] and st.session_state['my_product']:
        st.success("MAGIC DONE! For: " + st.session_state['my_product'])
        st.write(st.session_state['script'])
    up_magic = st.file_uploader("Upload Your Product Pic For Magic:", type=["jpg", "jpeg", "png"], key="mgpic")
    if up_magic:
        st.image(up_magic, caption="MAGIC PIC - E Dey Float, Dey Shine! - @kelly", use_column_width=True)
        st.write("Your Pic Dey Shine Like Gold!")
    st.markdown('<div style="background:#111; color:white; padding:20px; border-radius:15px; text-align:center;"><h1 style="color:white;">THANKS FOR WATCHING</h1><h1 style="color:#FFD700;">@kelly</h1></div>', unsafe_allow_html=True)
    st.write("POST MAGIC NOW:")
    st.markdown("[POST NOW - WhatsApp](https://wa.me/?text=My%20Pic%20Don%20Wake%20Up!%20Follow%20@kelly)")
    st.markdown("[POST NOW - TikTok](https://www.tiktok.com/upload)")
    st.markdown("[POST NOW - Instagram](https://www.instagram.com/reels/)")
    st.download_button("SAVE MAGIC PACKAGE", st.session_state['script'], file_name="kelly-magic.txt")
st.markdown("---")
st.markdown('<div style="background:linear-gradient(to bottom right, #0a7a42, #d4c400); padding:20px; border-radius:20px; color:white;"><h2 style="color:#FFD700;">ROW ECONOMY MARKET</h2><h1>Welcome back, muhammed!</h1><p>Everything you need, near you. No scam. Mama Oloja dey watch for you.</p><p>Follow @kelly - Complete Tonight!</p></div>', unsafe_allow_html=True)
st.info("Mama Oloja Guarantee: If seller scam you, we refund you. 100% Safe - Follow @kelly")
search = st.text_input("Search Shop:", placeholder="Search serum, sunscreen, Black Rapture...")
st.header("Shop - All Products")
PRODUCTS = [("Black Rapture", 4000, "Mary", "09031889875", "Lagos", "Bold, long-lasting"), ("Face Serum", 4000, "Blessing", "07052528772", "Abuja", "Clear face, glow"), ("Rolex Watch", 10000, "Arinfe", "090915907990", "Ibadan", "Black strap, with box"), ("Lip Combo", 6000, "Arinfe", "090915907990", "Ibadan", "Brown + Pink + Liner")]
for name, price, seller, phone, loc, desc in PRODUCTS:
    if search and search.lower() not in name.lower():
        continue
    st.write(name + " - " + str(price) + " | " + seller + " - " + loc)
    st.write(desc)
    st.markdown("[Buy via WhatsApp - " + seller + "](https://wa.me/234" + phone[1:] + "?text=Hello " + seller + ", I want " + name + " - " + str(price) + " from ROW Market - @kelly)")
    st.markdown("---")
st.write("2026 Row Economy Market - Powered by Mama Oloja - Follow @kelly - COMPLETE TONIGHT!")
