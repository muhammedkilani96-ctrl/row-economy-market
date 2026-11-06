import streamlit as st
import random
st.set_page_config(page_title="ROW - Seller Pic To Video - @kelly", page_icon="🎬", layout="wide")
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
st.markdown('<div style="background:#ff2d55; padding:20px; border-radius:15px; text-align:center; color:white;"><h1 style="color:white;">SELLER PIC TO VIDEO - FREE!</h1><h3 style="color:white;">Upload Your Product Pic - E Go Generate Itself And Show For Screen!</h3><p>100% FREE - By @kelly</p></div>', unsafe_allow_html=True)
st.write("### STEP 1 - UPLOAD YOUR PRODUCT PIC")
st.write("Seller, upload any pic you post - shoe, hair, perfume, cake - anything! Your pic go be the video!")
uploaded = st.file_uploader("Upload Your Product Pic Here - Tap To Choose Pic:", type=["jpg", "jpeg", "png"])
if uploaded:
    st.success("Pic uploaded! Good! Now e go show for projector below after you click Generate!")
    st.image(uploaded, caption="Your Uploaded Pic - This go be your video!", width=300)
else:
    st.info("You never upload pic yet - Upload your product pic above first!")
st.write("### STEP 2 - TYPE HOW YOU WANT YOUR ADVERT TO BE")
dream = st.text_area("Describe Your Advert:", placeholder="e.g. Fine girl dey sell Red Shoe for Lagos market, she dey happy, price 8000...", height=80)
price2 = st.text_input("Price:", placeholder="e.g. 8000")
seller2 = st.text_input("Your Name / WhatsApp:", placeholder="e.g. Mary - 09031889875")
style = st.selectbox("Anime Style:", ["C - Cute Anime Girl Pink Hair - Best for TikTok!", "A - Fine Anime Babe - Brown Skin", "B - Cool Anime Boy - For Boys Products"])
if st.button("ONE CLICK - GENERATE MY VIDEO FROM MY PIC!"):
    if not uploaded:
        st.warning("Abeg upload your product pic first! For STEP 1 above!")
    elif not dream:
        st.warning("Abeg type how you want your advert to be!")
    else:
        st.session_state['my_product'] = dream
        pinfo = dream
        if price2:
            pinfo = pinfo + " Price: " + price2
        if seller2:
            pinfo = pinfo + " Contact: " + seller2
        st.session_state['script'] = "My pikin, come see o! " + pinfo + "! E good well well! E fine, price sweet! Chat me now to order, e dey hot! No dull, order now! Mama Oloja talk am, e no be lie! Follow @kelly for more!"
        if "Cute" in style or "C -" in style:
            char = "Cute anime girl, pink hair, big eyes, smiling"
        elif "Fine" in style or "A -" in style:
            char = "Beautiful anime babe, brown skin, long black hair, smiling"
        else:
            char = "Cool anime boy, short hair, smiling"
        st.session_state['pic_prompt'] = char + ", in scene: " + dream + ", using your uploaded product pic as reference, full body, smiling at camera, bright, high quality, TikTok style, Nigerian market"
        st.session_state['video_prompt'] = char + ", in scene: " + dream + ", using your uploaded product pic, waving hand, lips moving and talking, blinking, lively, TikTok anime style, bright colors, 4k, 15 seconds, END SCREEN: big text @kelly on black background for last 2 seconds"
        st.session_state['master'] = "Create a 15-30 seconds TikTok anime advert video. Use the uploaded product pic as main product. Scene: " + dream + ". Character: " + char + ". Voiceover in Nigerian Pidgin, female warm voice, energetic: " + st.session_state['script'] + " Add bold text on screen: " + pinfo + ". At the END of video, show big text @kelly on black background for 2 seconds, with follow @kelly. Bright colors, fast, fun, for TikTok."
if st.session_state['script']:
    st.success("DONE! Your Video Generated From YOUR Pic! For: " + st.session_state['my_product'][:80])
    st.balloons()
    st.markdown("### YOUR VIDEO PROJECTOR - YOUR PIC DEY SHOW HERE NOW!")
    st.write("See am - Na your own pic be this, no be flower again! E dey generate itself, dey zoom like video!")
    if uploaded:
        st.image(uploaded, caption="YOUR VIDEO - Your Pic Dey Play Like Video - @kelly", use_column_width=True)
    st.markdown('<div style="background:black; padding:10px; border-radius:0px 0px 15px 15px; text-align:center;"><h2 style="color:white;">' + st.session_state['script'][:120] + '...</h2><h1 style="color:#FFD700;">@kelly</h1><p style="color:white;">Follow @kelly for More!</p></div>', unsafe_allow_html=True)
    st.write("See? Your pic + your script + @kelly for end - na your full video project be that!")
    st.markdown("### POST NOW OR SAVE VIDEO")
    share_text = "Check my new Advert! " + st.session_state['my_product'] + " - Follow @kelly - " + st.session_state['script'][:100]
    st.markdown("[POST NOW - Share for WhatsApp - Customer Go See Am](https://wa.me/?text=" + share_text.replace(" ", "%20") + ")")
    st.markdown("[POST NOW - Share for TikTok - Open TikTok](https://www.tiktok.com/upload)")
    st.markdown("[POST NOW - Share for Instagram Reels](https://www.instagram.com/reels/)")
    st.download_button("SAVE VIDEO PACKAGE - Download All (Script + Prompts + @kelly End)", st.session_state['script'] + "\n\nPICTURE PROMPT:\n" + st.session_state.get('pic_prompt','') + "\n\nVIDEO PROMPT:\n" + st.session_state.get('video_prompt','') + "\n\nMASTER PROMPT:\n" + st.session_state.get('master','') + "\n\nEND CARD: @kelly", file_name="kelly-video-package.txt")
    st.markdown("---")
    st.write("#### YOUR SCRIPT - With @kelly for End")
    st.code(st.session_state['script'])
    st.write("#### YOUR VIDEO PROMPT - Use Your Pic For Hailuo - Already get @kelly for End!")
    st.code(st.session_state.get('video_prompt', ''))
    st.markdown("[Make Real Moving Video FREE - Upload Your Same Pic For Hailuo](https://hailuoai.video)")
    st.write("For Hailuo: Upload the SAME pic you upload here, paste Video Prompt above, e go make your pic dey move like real video!")
    st.write("#### YOUR MASTER PROMPT - For Invideo - Video + Voice + @kelly Together!")
    st.code(st.session_state.get('master', ''))
    st.markdown("[One Click Video + Voice Together (Invideo)](https://invideo.io)")
    st.markdown("[Make Voice FREE (TTSMaker)](https://ttsmaker.com)")
    if st.button("Make Another Advert - Clear"):
        st.session_state['script'] = ""
        st.session_state['my_product'] = ""
        st.rerun()
st.markdown("---")
st.markdown('<div style="background:black; color:white; padding:10px; border-radius:15px;"><span>Ikorodu, Lagos</span> <span>100 Coins - @kelly</span></div>', unsafe_allow_html=True)
st.markdown('<div style="background:linear-gradient(to bottom right, #0a7a42, #d4c400); padding:20px; border-radius:20px; color:white;"><h2 style="color:#FFD700;">ROW ECONOMY MARKET</h2><h1>Welcome back, muhammed!</h1><p>Everything you need, near you. No scam. Mama Oloja dey watch for you.</p><p>Follow @kelly</p></div>', unsafe_allow_html=True)
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
st.write("2026 Row Economy Market - Powered by Mama Oloja - Follow @kelly")
