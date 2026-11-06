import streamlit as st
import random
st.set_page_config(page_title="ROW - AI TWIN - @kelly - Shop Never Sleep", page_icon="👯", layout="wide")
if 'coins' not in st.session_state:
    st.session_state['coins'] = 100
if 'script' not in st.session_state:
    st.session_state['script'] = ""
if 'video_prompt' not in st.session_state:
    st.session_state['video_prompt'] = ""
if 'pic_prompt' not in st.session_state:
    st.session_state['pic_prompt'] = ""
if 'master' not in st.session_state:
    st.session_state['master'] = ""
if 'my_product' not in st.session_state:
    st.session_state['my_product'] = ""
if 'voice_style' not in st.session_state:
    st.session_state['voice_style'] = "Funny"
if 'twin_name' not in st.session_state:
    st.session_state['twin_name'] = ""
if 'twin_on' not in st.session_state:
    st.session_state['twin_on'] = False
if 'twin_lang' not in st.session_state:
    st.session_state['twin_lang'] = "Pidgin"
st.markdown('<style>@keyframes floaty {0%{transform:translateY(0px) scale(1);}50%{transform:translateY(-15px) scale(1.05);}100%{transform:translateY(0px) scale(1);}} @keyframes shine {0%{box-shadow:0 0 10px #FFD700;}50%{box-shadow:0 0 40px #ff2d55, 0 0 60px #FFD700;}100%{box-shadow:0 0 10px #FFD700;}} @keyframes dance {0%{transform:rotate(-10deg);}50%{transform:rotate(10deg);}100%{transform:rotate(-10deg);}} @keyframes blink {0%{opacity:1;}50%{opacity:0.3;}100%{opacity:1;}} .twin-live{animation:blink 1s infinite; color:#00ff00;} .mama-dance{animation:dance 0.8s infinite; font-size:60px;}</style>', unsafe_allow_html=True)
st.markdown('<div style="background:linear-gradient(to right, #7b2ff7, #ff2d55, #ff9a00); padding:20px; border-radius:20px; text-align:center; color:white;"><h1 style="color:white;">AI TWIN - YOUR SHOP NEVER SLEEP!</h1><h3 style="color:white;">Create Your Twin - Twin Go Sell For You Even When You Dey Sleep!</h3><p>100% FREE FOR NOW - By @kelly</p><p>👯 ✨ 👯</p></div>', unsafe_allow_html=True)
st.write("### STEP 1 - CREATE YOUR AI TWIN - YOUR TWIN NA YOUR SECOND YOU!")
twin_name_in = st.text_input("Your Name:", placeholder="e.g. Mary")
twin_shop = st.text_input("Your Shop Name:", placeholder="e.g. Blessing Cosmetics")
twin_product = st.text_input("Your Main Product:", placeholder="e.g. Black Rapture, Face Serum, Red Shoe...")
twin_price = st.text_input("Price:", placeholder="e.g. 4000")
twin_phone = st.text_input("WhatsApp Number:", placeholder="e.g. 09031889875")
twin_lang = st.selectbox("Twin Language - Twin Go Speak Customer Language:", ["Pidgin - For Lagos Market!", "English - For London Customer!", "Yoruba - E ku ise!", "Igbo - Ndewo!", "Hausa - Sannu!"])
twin_person = st.selectbox("Twin Personality:", ["Funny Twin - Dey Joke, Dey Make People Laugh!", "Sweet Twin - Soft, Dey Pet Customer Like Baby!", "Shout Twin - Loud Market Woman, Dey Shout For Market!", "Boss Twin - Calm, Rich, Premium Seller!"])
twin_time = st.selectbox("When Twin Go Post Magic Video?", ["Every Morning 7am - Best! Customer Wake Up See Am!", "Every Evening 7pm - After Work, People Dey Buy!", "Every Morning + Evening - Double Sales!"])
if st.button("CREATE MY AI TWIN NOW!"):
    if not twin_name_in or not twin_product:
        st.warning("Abeg put your name and product first!")
    else:
        st.session_state['twin_name'] = twin_name_in
        st.session_state['twin_on'] = True
        st.session_state['twin_lang'] = twin_lang
        st.session_state['my_product'] = twin_product
        st.session_state['voice_style'] = twin_person
        pinfo = twin_product
        if twin_price:
            pinfo = pinfo + " - Price " + twin_price
        if twin_shop:
            pinfo = pinfo + " - from " + twin_shop
        if twin_lang and "Pidgin" in twin_lang:
            vtext = "My pikin, na me be Twin of " + twin_name_in + "! " + twin_name_in + " dey sleep, but me I no dey sleep! Come see o! " + pinfo + "! E good well well! Chat me now, I go reply you sharp sharp! Follow @kelly!"
        elif twin_lang and "Yoruba" in twin_lang:
            vtext = "E ku ise! Na me be Twin of " + twin_name_in + "! " + pinfo + "! E dara pupo! Chat me now, mo wa online! Follow @kelly!"
        elif twin_lang and "Igbo" in twin_lang:
            vtext = "Ndewo! Na me be Twin of " + twin_name_in + "! " + pinfo + "! O di mma! Chat me now, I dey online! Follow @kelly!"
        elif twin_lang and "Hausa" in twin_lang:
            vtext = "Sannu! Na me be Twin of " + twin_name_in + "! " + pinfo + "! Yana da kyau! Chat me now, ina online! Follow @kelly!"
        else:
            vtext = "Hello my lovely customer! I am the AI Twin of " + twin_name_in + "! " + twin_name_in + " is sleeping, but I am awake for you! Check this: " + pinfo + "! It is beautiful, perfect for you! Chat me now, I reply instantly! Follow @kelly!"
        st.session_state['script'] = vtext
        st.session_state['pic_prompt'] = "AI Twin of " + twin_name_in + ", " + twin_person + ", with product " + twin_product + " floating and shining like magic, sparkles, confetti, smiling, dancing, bright, TikTok style, Nigerian market"
        st.session_state['video_prompt'] = "AI Twin of " + twin_name_in + ", " + twin_person + ", product " + twin_product + " floating, shining, talking, waving, lips moving, dancing, TikTok style, 4k, 15 seconds, sparkles, END SCREEN: big text @kelly with confetti for last 2 seconds"
        st.session_state['master'] = "Create 15-30 sec AI Twin advert. Twin of " + twin_name_in + " for shop " + twin_shop + ". Product: " + pinfo + ". Language: " + twin_lang + ". Personality: " + twin_person + ". Voiceover: " + vtext + " Add bold text: " + pinfo + ". End with big @kelly + confetti + Follow @kelly."
if st.session_state['twin_on']:
    st.success("TWIN CREATED! " + st.session_state['twin_name'] + " Twin Dey Online Now! Shop Never Sleep Again!")
    st.balloons()
    st.markdown('<div style="background:black; padding:20px; border-radius:20px; color:white;"><h2 style="color:white;">YOUR AI TWIN - LIVE NOW!</h2><p><span class="twin-live">● LIVE</span> - Twin Dey Online 24/7 - Even When You Dey Sleep!</p><h1 style="color:#FFD700;">Twin of ' + st.session_state['twin_name'] + '</h1><p>Shop: ' + twin_shop + ' | Product: ' + st.session_state['my_product'] + ' | Language: ' + st.session_state['twin_lang'] + '</p><p>Personality: ' + st.session_state['voice_style'] + '</p><p>Auto-Post: ' + twin_time + '</p></div>', unsafe_allow_html=True)
    st.write("### TWIN MAGIC PROJECTOR - TWIN PIC DEY TALK!")
    st.write("Upload your product pic, Twin go use am to sell!")
    uploaded = st.file_uploader("Upload Your Product Pic For Twin To Sell:", type=["jpg", "jpeg", "png"])
    if uploaded:
        st.image(uploaded, caption="TWIN MAGIC PIC - Your Product Dey Float, Dey Shine, Dey Talk! - @kelly", use_column_width=True)
        st.markdown('<div style="text-align:center;"><p style="font-size:40px;">✨ 👯 ✨</p><p style="color:#ff2d55;">Twin Dey Hold Your Product, Dey Shine Like Gold!</p></div>', unsafe_allow_html=True)
    else:
        st.info("Upload your product pic above - Twin go show am for projector!")
    st.markdown('<div style="background:linear-gradient(to right, #7b2ff7, #ff2d55); padding:15px; border-radius:15px; display:flex; justify-content:space-between; align-items:center;"><div><h2 style="color:white;">TWIN DEY TALK</h2><p style="color:white;">' + st.session_state['script'][:150] + '...</p></div><div class="mama-dance">👯</div></div>', unsafe_allow_html=True)
    st.write("### TWIN AUTO-REPLY - TWIN GO REPLY CUSTOMER FOR YOU!")
    st.write("Copy this, put for your WhatsApp Auto-Reply / Status - Twin go reply even when you dey sleep!")
    st.code("Hello my dear! Na Twin of " + st.session_state['twin_name'] + " be this! I dey online 24/7! You
