import streamlit as st
st.set_page_config(page_title="ROW AI TWIN - @kelly", page_icon="👯", layout="wide")
if 'script' not in st.session_state:
    st.session_state['script'] = ""
if 'twin_name' not in st.session_state:
    st.session_state['twin_name'] = ""
if 'twin_on' not in st.session_state:
    st.session_state['twin_on'] = False
if 'my_product' not in st.session_state:
    st.session_state['my_product'] = ""
if 'twin_lang' not in st.session_state:
    st.session_state['twin_lang'] = "Pidgin"
if 'twin_person' not in st.session_state:
    st.session_state['twin_person'] = "Funny"
if 'twin_price' not in st.session_state:
    st.session_state['twin_price'] = ""
if 'twin_shop' not in st.session_state:
    st.session_state['twin_shop'] = ""
st.markdown('<div style="background:linear-gradient(to right, #7b2ff7, #ff2d55); padding:20px; border-radius:20px; text-align:center; color:white;"><h1 style="color:white;">AI TWIN - SHOP NEVER SLEEP!</h1><h3 style="color:white;">Create Twin - Twin Go Sell For You When You Dey Sleep!</h3><p>By @kelly</p></div>', unsafe_allow_html=True)
st.write("STEP 1 - CREATE YOUR AI TWIN")
twin_name_in = st.text_input("Your Name:", placeholder="e.g. Mary")
twin_shop = st.text_input("Shop Name:", placeholder="e.g. Blessing Cosmetics")
twin_product = st.text_input("Main Product:", placeholder="e.g. Black Rapture")
twin_price = st.text_input("Price:", placeholder="e.g. 4000")
twin_lang = st.selectbox("Twin Language:", ["Pidgin", "English", "Yoruba", "Igbo", "Hausa"])
twin_person = st.selectbox("Twin Personality:", ["Funny Twin", "Sweet Twin", "Shout Twin", "Boss Twin"])
twin_time = st.selectbox("When Twin Go Post?", ["Every Morning 7am", "Every Evening 7pm", "Morning + Evening"])
if st.button("CREATE MY AI TWIN NOW!"):
    if not twin_name_in or not twin_product:
        st.warning("Abeg put name and product!")
    else:
        st.session_state['twin_name'] = twin_name_in
        st.session_state['twin_shop'] = twin_shop
        st.session_state['my_product'] = twin_product
        st.session_state['twin_price'] = twin_price
        st.session_state['twin_lang'] = twin_lang
        st.session_state['twin_person'] = twin_person
        st.session_state['twin_on'] = True
        base = twin_product + " Price " + twin_price
        if twin_lang == "Pidgin":
            vtext = "My pikin, na Twin of " + twin_name_in + " be this! I no dey sleep! Come see " + base + "! Chat me now! Follow @kelly!"
        elif twin_lang == "Yoruba":
            vtext = "E ku ise! Na Twin of " + twin_name_in + " be this! " + base + "! E dara! Chat me now! Follow @kelly!"
        elif twin_lang == "Igbo":
            vtext = "Ndewo! Na Twin of " + twin_name_in + " be this! " + base + "! O di mma! Chat me now! Follow @kelly!"
        elif twin_lang == "Hausa":
            vtext = "Sannu! Na Twin of " + twin_name_in + " be this! " + base + "! Yana da kyau! Chat me now! Follow @kelly!"
        else:
            vtext = "Hello! I am Twin of " + twin_name_in + "! I am awake for you! Check " + base + "! Chat me now! Follow @kelly!"
        st.session_state['script'] = vtext
if st.session_state['twin_on']:
    st.success("TWIN LIVE! Twin of " + st.session_state['twin_name'] + " dey online!")
    st.balloons()
    st.markdown('<div style="background:black; padding:20px; border-radius:20px; color:white;"><h2 style="color:white;">YOUR AI TWIN - LIVE NOW!</h2><p style="color:#00ff00;">LIVE - Twin Dey Online 24/7</p><h1 style="color:#FFD700;">Twin of ' + st.session_state['twin_name'] + '</h1><p>Shop: ' + st.session_state['twin_shop'] + '</p><p>Product: ' + st.session_state['my_product'] + '</p><p>Language: ' + st.session_state['twin_lang'] + '</p><p>Personality: ' + st.session_state['twin_person'] + '</p><p>Auto-Post: ' + twin_time + '</p></div>', unsafe_allow_html=True)
    st.write("STEP 2 - UPLOAD YOUR PRODUCT PIC - TWIN GO SELL AM!")
    uploaded = st.file_uploader("Upload Product Pic:", type=["jpg", "jpeg", "png"])
    if uploaded:
        st.image(uploaded, caption="TWIN MAGIC PIC - Your Product Dey Shine! - @kelly", use_column_width=True)
        st.write("Your Pic Dey Shine Like Gold! Twin Dey Hold Am!")
    else:
        st.info("Upload your product pic above - Twin go show am!")
    st.write("TWIN DEY TALK:")
    st.write(st.session_state['script'])
    st.write("TWIN AUTO-REPLY - Copy Am For WhatsApp:")
    reply1 = "Hello! Na Twin of "
    reply2 = st.session_state['twin_name']
    reply3 = " be this! I dey online! You want "
    reply4 = st.session_state['my_product']
    reply5 = " Price "
    reply6 = st.session_state['twin_price']
    reply7 = " Chat me now! Follow @kelly!"
    full_reply = reply1 + reply2 + reply3 + reply4 + reply5 + reply6 + reply7
    st.code(full_reply)
    st.write("TWIN MORNING MAGIC - Copy Am Every Morning:")
    m1 = "Good Morning! Twin of "
    m2 = st.session_state['twin_name']
    m3 = " don wake up! Today: "
    m4 = st.session_state['my_product']
    m5 = " Price "
    m6 = st.session_state['twin_price']
    m7 = " Order now! Follow @kelly!"
    full_morning = m1 + m2 + m3 + m4 + m5 + m6 + m7
    st.code(full_morning)
    st.markdown('<div style="background:#111; color:white; padding:20px; border-radius:15px; text-align:center;"><h1 style="color:white;">THANKS FOR WATCHING</h1><h1 style="color:#FFD700;">@kelly</h1><p>Follow @kelly - Twin Dey Online!</p></div>', unsafe_allow_html=True)
    st.write("POST TWIN NOW:")
    share1 = "Meet My AI Twin! Twin of "
    share2 = st.session_state['twin_name']
    share3 = " dey sell "
    share4 = st.session_state['my_product']
    share5 = " 24/7! Follow @kelly!"
    share_text = share1 + share2 + share3 + share4 + share5
    st.markdown("[POST TWIN NOW - WhatsApp](https://wa.me/?text=" + share_text.replace(" ", "%20") + ")")
    st.markdown("[POST TWIN NOW - TikTok](https://www.tiktok.com/upload)")
    st.markdown("[POST TWIN NOW - Instagram](https://www.instagram.com/reels/)")
    st.download_button("SAVE TWIN PACKAGE", st.session_state['script'], file_name="kelly-twin.txt")
    st.write("TWIN VIDEO PROMPT - For Hailuo:")
    vp1 = "AI Twin of "
    vp2 = st.session_state['twin_name']
    vp3 = " product "
    vp4 = st.session_state['my_product']
    vp5 = " floating, shining, talking, dancing, TikTok style, END with @kelly"
    vp_full = vp1 + vp2 + vp3 + vp4 + vp5
    st.code(vp_full)
    st.markdown("[Make Real Twin Video FREE - Hailuo](https://hailuoai.video)")
    st.markdown("[Make Twin Voice FREE - TTSMaker](https://ttsmaker.com)")
    if st.button("Delete Twin"):
        st.session_state['twin_on'] = False
        st.session_state['script'] = ""
        st.rerun()
else:
    st.write("HOW TWIN GO WORK:")
    st.write("1. Create Twin - Put name, product")
    st.write("2. Twin Go Wake Up - Twin dey online 24/7")
    st.write("3. You Sleep, Twin Sell - You wake up see orders!")
st.markdown("---")
st.markdown('<div style="background:linear-gradient(to bottom right, #0a7a42, #d4c400); padding:20px; border-radius:20px; color:white;"><h2 style="color:#FFD700;">ROW ECONOMY MARKET</h2><h1>Welcome back, muhammed!</h1><p>Follow @kelly - AI Twin Live</p></div>', unsafe_allow_html=True)
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
st.write("2026 Row Economy Market - Powered by Mama Oloja - Follow @kelly")
