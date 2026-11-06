import streamlit as st
import random
st.set_page_config(page_title="ROW - @kelly MAGIC MARKET - PIC DEY TALK", page_icon="✨", layout="wide")
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
st.markdown('<style>@keyframes floaty {0%{transform:translateY(0px) scale(1);}50%{transform:translateY(-15px) scale(1.05);}100%{transform:translateY(0px) scale(1);}} @keyframes shine {0%{box-shadow:0 0 10px #FFD700;}50%{box-shadow:0 0 40px #ff2d55, 0 0 60px #FFD700;}100%{box-shadow:0 0 10px #FFD700;}} @keyframes dance {0%{transform:rotate(-10deg);}50%{transform:rotate(10deg);}100%{transform:rotate(-10deg);}} .magic-pic{animation:floaty 2s infinite, shine 1.5s infinite; border-radius:20px; border:4px solid #FFD700;} .mama-dance{animation:dance 0.8s infinite; font-size:60px;} .confetti{font-size:30px;}</style>', unsafe_allow_html=True)
st.markdown('<div style="background:linear-gradient(to right, #ff2d55, #ff9a00, #FFD700); padding:20px; border-radius:20px; text-align:center; color:white;"><h1 style="color:white;">MAGIC MARKET - PIC DEY TALK!</h1><h3 style="color:white;">Upload Pic - Pic Go Wake Up, Float, Shine, Talk!</h3><p>100% FREE FOR NOW - By @kelly</p><p class="confetti">🎉 ✨ 🎊 ✨ 🎉</p></div>', unsafe_allow_html=True)
st.write("### STEP 1 - UPLOAD YOUR PRODUCT PIC - YOUR PIC NA THE STAR!")
uploaded = st.file_uploader("Tap To Upload Your Product Pic - Shoe, Hair, Perfume, Cake, Anything:", type=["jpg", "jpeg", "png"])
if uploaded:
    st.success("Magic Pic Uploaded! E don ready to wake up!")
else:
    st.info("You never upload pic yet - Upload your product pic above, make magic start!")
st.write("### STEP 2 - TYPE YOUR PRODUCT + PICK MAMA OLOJA VOICE")
dream = st.text_input("Type Your Product:", placeholder="e.g. Red Shoe, Black Rapture, Hair Wig, Cake...")
price2 = st.text_input("Price:", placeholder="e.g. 8000")
seller2 = st.text_input("Your Name:", placeholder="e.g. Mary")
voice = st.selectbox("Pick Mama Oloja Voice Style:", ["Funny - Mama Oloja Dey Joke, Dey Make People Laugh!", "Sweet - Mama Oloja Soft Voice, Dey Pet Customer!", "Shout - Mama Oloja Loud Market Woman, Dey Shout For Market!"])
style = st.selectbox("Anime Girl Style:", ["C - Cute Anime Girl Pink Hair - Best for TikTok!", "A - Fine Anime Babe - Brown Skin", "B - Cool Anime Boy - For Boys Products"])
magic_word = st.text_input("Magic Word For Your Video (Optional):", placeholder="e.g. Buy Now, Rush Am, Sweet Like Money...")
if st.button("MAKE MY PIC TALK! - MAGIC!"):
    if not uploaded:
        st.warning("Abeg upload your product pic first for STEP 1!")
    elif not dream:
        st.warning("Abeg type your product name!")
    else:
        st.session_state['my_product'] = dream
        st.session_state['voice_style'] = voice
        pinfo = dream
        if price2:
            pinfo = pinfo + " - Price " + price2
        if seller2:
            pinfo = pinfo + " - from " + seller2
        if magic_word:
            pinfo = pinfo + " - " + magic_word
        if "Funny" in voice:
            vtext = "Ha ha ha! My pikin, come see o! " + pinfo + "! E too sweet, if you no buy am, your village people go vex! E fine die! Chat me now, make we laugh and buy! Follow @kelly!"
        elif "Sweet" in voice:
            vtext = "My lovely pikin, come my dear, see " + pinfo + "! E soft, e fine, e perfect for you my love! I keep am specially for you! Chat me now my dear! Follow @kelly!"
        else:
            vtext = "COME COME COME! EVERYBODY COME SEE O! " + pinfo + "! E HOT! E DEY RUSH! IF YOU NO BUY NOW, E GO FINISH! CHAT ME NOW! FOLLOW @kelly!"
        st.session_state['script'] = vtext
        if "Cute" in style or "C -" in style:
            char = "Cute anime girl, pink hair, big eyes, smiling, dancing"
        elif "Fine" in style or "A -" in style:
            char = "Beautiful anime babe, brown skin, long black hair, smiling, dancing"
        else:
            char = "Cool anime boy, short hair, smiling, dancing"
        st.session_state['pic_prompt'] = char + ", with product pic floating and shining like magic, in scene: " + dream + ", sparkles, confetti, full body, smiling at camera, bright, high quality, TikTok style, Nigerian market, magic glow"
        st.session_state['video_prompt'] = char + ", with product pic floating, shining, talking, waving hand, lips moving and talking, blinking, dancing, lively, TikTok anime style, bright colors, 4k, 15 seconds, sparkles and confetti, END SCREEN: big text @kelly on black background with confetti for last 2 seconds"
        st.session_state['master'] = "Create a 15-30 seconds MAGIC TikTok anime advert video. Use the uploaded product pic as STAR - make it float, shine like gold, with sparkles. Scene: " + dream + ". Character: " + char + " dancing in corner. Voiceover in Nigerian Pidgin, " + voice + " style, energetic: " + vtext + " Add bold TikTok subtitle text on screen: " + pinfo + ". Add sparkles, confetti, magic glow. At the END, show big text @kelly on black background with confetti for 2 seconds, with follow @kelly voice. Bright, fast, fun, viral TikTok style."
if st.session_state['script']:
    st.success("MAGIC DONE! Your Pic Don Wake Up! For: " + st.session_state['my_product'] + " - Voice: " + st.session_state['voice_style'])
    st.balloons()
    st.markdown("### YOUR MAGIC PROJECTOR - YOUR PIC DEY TALK NOW!")
    st.markdown('<div style="background:black; padding:20px; border-radius:20px; text-align:center; color:white;"><h3 style="color:#FFD700;">NOW SHOWING - MAGIC MARKET</h3><p style="color:white;">' + st.session_state['my_product'] + ' - ' + st.session_state['voice_style'] + '</p></div>', unsafe_allow_html=True)
    if uploaded:
        st.image(uploaded, caption="YOUR MAGIC PIC - E Dey Float, Dey Shine, Dey Talk! - @kelly", use_column_width=True)
        st.markdown('<div style="text-align:center;"><p style="font-size:40px;">✨ ⭐ ✨</p><p style="color:#ff2d55; font-size:20px;">Your Pic Dey Shine Like Gold!</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:linear-gradient(to right, #ff2d55, #FFD700); padding:15px; border-radius:15px; display:flex; justify-content:space-between; align-items:center;"><div><h2 style="color:white;">MAMA OLOJA</h2><p style="color:white;">' + st.session_state['script'][:140] + '...</p></div><div class="mama-dance">🧕💃</div></div>', unsafe_allow_html=True)
    st.write("Mama Oloja dey dance for corner, dey talk your script - word by word like TikTok subtitle!")
    st.markdown('<div style="background:#111; color:white; padding:20px; border-radius:15px; text-align:center;"><p class="confetti">🎉 🎊 ✨ 🎉 🎊</p><h1 style="color:white;">THANKS FOR WATCHING</h1><h1 style="color:#FFD700;">@kelly</h1><p>Follow @kelly for More Magic!</p><p class="confetti">🎉 🎊 ✨ 🎉 🎊</p></div>', unsafe_allow_html=True)
    st.write("END CARD: @kelly + Confetti - Every video go end like this!")
    st.markdown("### POST NOW OR SAVE MAGIC VIDEO")
    share_text = "My Pic Don Wake Up! Magic Advert! " + st.session_state['my_product'] + " - Voice: " + st.session_state['voice_style'] + " - Follow @kelly - " + st.session_state['script'][:100]
    st.markdown("[POST NOW - WhatsApp - Customer Go See Am](https://wa.me/?text=" + share_text.replace(" ", "%20") + ")")
    st.markdown("[POST NOW - TikTok - Open TikTok](https://www.tiktok.com/upload)")
    st.markdown("[POST NOW - Instagram Reels](https://www.instagram.com/reels/)")
    st.markdown("[PLAY AGAIN - Make Another Magic Video - Tap Here](https://www.tiktok.com/upload)")
    st.download_button("SAVE MAGIC VIDEO PACKAGE - Download All (Script + Prompts + @kelly End)", st.session_state['script'] + "\n\nVOICE STYLE: " + st.session_state['voice_style'] + "\n\nPICTURE PROMPT:\n" + st.session_state.get('pic_prompt','') + "\n\nVIDEO PROMPT:\n" + st.session_state.get('video_prompt','') + "\n\nMASTER PROMPT:\n" + st.session_state.get('master','') + "\n\nEND CARD: @kelly + Confetti", file_name="kelly-magic-package.txt")
    st.markdown("---")
    st.write("#### YOUR MAGIC SCRIPT - Voice: " + st.session_state['voice_style'])
    st.code(st.session_state['script'])
    st.write("#### YOUR MAGIC VIDEO PROMPT - Pic Dey Float + Shine + @kelly End!")
    st.code(st.session_state.get('video_prompt', ''))
    st.markdown("[Make Real Moving Magic Video FREE - Upload Same Pic For Hailuo](https://hailuoai.video)")
    st.write("For Hailuo: Upload SAME pic you upload here, paste Video Prompt above, e go make your pic dey float and talk for real!")
    st.write("#### YOUR MASTER MAGIC PROMPT - For Invideo - Video + Voice + @kelly Together!")
    st.code(st.session_state.get('master', ''))
    st.markdown("[One Click Video + Voice Together (Invideo)](https://invideo.io)")
    st.markdown("[Make Voice FREE - Pick Funny / Sweet / Shout (TTSMaker)](https://ttsmaker.com)")
    st.write("### LEADERBOARD - TOP MAGIC VIDEO THIS WEEK")
    st.write("1. Mary - Black Rapture - 12k views - @kelly")
    st.write("2. Blessing - Face Serum - 8k views - @kelly")
    st.write("3. Arinfe - Rolex Watch - 5k views - @kelly")
    st.write("Your video fit enter leaderboard if you post am now!")
    if st.button("Make Another Magic Video - Clear"):
        st.session_state['script'] = ""
        st.session_state['my_product'] = ""
        st.rerun()
st.markdown("---")
st.markdown('<div style="background:black; color:white; padding:10px; border-radius:15px;"><span>Ikorodu, Lagos</span> <span>100 Coins - @kelly Magic</span></div>', unsafe_allow_html=True)
st.markdown('<div style="background:linear-gradient(to bottom right, #0a7a42, #d4c400); padding:20px; border-radius:20px; color:white;"><h2 style="color:#FFD700;">ROW ECONOMY MARKET</h2><h1>Welcome back, muhammed!</h1><p>Everything you need, near you. No scam. Mama Oloja dey watch for you.</p><p>Follow @kelly - Magic Market</p></div>', unsafe_allow_html=True)
st.info("Mama Oloja Guarantee: If seller scam you, we refund you. 100% Safe. Verified Sellers Only - Follow @kelly")
search = st.text_input("Search Shop:", placeholder="Search serum, sunscreen, Black Rapture...")
st.write("Blessing Cosmetics - @kelly")
with st.expander("Seller Login", expanded=True):
    st.success("Logged in as Blessing Cosmetics")
st.header("Shop - All Products")
PRODUCTS = [("Black Rapture", 4000, "Mary", "09031889875", "Lagos", "Bold, long-lasting"), ("Face Serum", 4000, "Blessing", "07052528772", "Abuja", "Clear face, glow"), ("Rolex Watch", 10000, "Arinfe", "090915907990", "Ibadan", "Black strap, with box"), ("Lip Combo", 6000, "Arinfe", "090915907990", "Ibadan", "Brown + Pink + Liner")]
for name, price, seller, phone, loc, desc in PRODUCTS:
    if search and search.lower() not in name.lower():
        continue
    st.write(name + " - " + str(price) + " | " + seller + " - " + loc)
    st.write(desc)
    st.markdown("[Buy via WhatsApp - " + seller + "](https://wa.me/234" + phone[1:] + "?text=Hello " + seller + ", I want " + name + " - " + str(price) + " from ROW Market - @kelly)")
    st.markdown("---")
st.write("2026 Row Economy Market - Powered by Mama Oloja - Follow @kelly - Magic Market")
