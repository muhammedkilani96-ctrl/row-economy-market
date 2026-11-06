import streamlit as st
import random
st.set_page_config(page_title="ROW - One Click Anime - @kelly", page_icon="🎬", layout="wide")
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
st.markdown('<div style="background:#ff2d55; padding:20px; border-radius:15px; text-align:center; color:white;"><h1 style="color:white;">ONE CLICK ANIME ADVERT - FREE!</h1><h3 style="color:white;">Type It - Click - Video Show - Post Now - @kelly for End!</h3><p>100% FREE FOR NOW - By @kelly</p></div>', unsafe_allow_html=True)
st.write("### TYPE EXACTLY HOW YOU WANT YOUR ADVERT VIDEO TO BE:")
st.write("Example: Fine girl dey sell Red Shoe for Lagos market, she dey happy, price 8000")
dream = st.text_area("Describe Your Advert Video Here:", placeholder="e.g. Fine girl dey sell Red Shoe for Lagos market, she dey happy, price 8000, customers dey rush am...", height=100)
price2 = st.text_input("Price (Optional):", placeholder="e.g. 8000")
seller2 = st.text_input("Your Name / WhatsApp (Optional):", placeholder="e.g. Mary - 09031889875")
style = st.selectbox("Anime Style:", ["C - Cute Anime Girl Pink Hair - Best for TikTok!", "A - Fine Anime Babe - Brown Skin", "B - Cool Anime Boy - For Boys Products"])
if st.button("ONE CLICK - GENERATE MY FULL ADVERT!"):
    if not dream:
        st.warning("Abeg type how you want your advert to be first!")
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
        st.session_state['pic_prompt'] = char + ", in scene: " + dream + ", full body, smiling at camera, bright, high quality, TikTok style, Nigerian market"
        st.session_state['video_prompt'] = char + ", in scene: " + dream + ", waving hand, lips moving and talking, blinking, lively, TikTok anime style, bright colors, 4k, 15 seconds, END SCREEN: big text @kelly on black background for last 2 seconds"
        st.session_state['master'] = "Create a 15-30 seconds TikTok anime advert video. Scene: " + dream + ". Character: " + char + ". Voiceover in Nigerian Pidgin, female warm voice, energetic: " + st.session_state['script'] + " Add bold text on screen: " + pinfo + ". At the END of video, show big text @kelly on black background for 2 seconds, with follow @kelly. Bright colors, fast, fun, for TikTok."
if st.session_state['script']:
    st.success("DONE! Your Video Ready! For: " + st.session_state['my_product'][:80])
    st.balloons()
    st.markdown("### YOUR VIDEO PROJECTOR - WATCH AM HERE!")
    st.markdown('<div style="background:black; padding:15px; border-radius:20px; text-align:center; color:white;"><h3 style="color:white;">NOW SHOWING - YOUR ADVERT</h3><p style="color:#FFD700;">' + st.session_state['my_product'] + '</p><p style="color:white;">Anime Girl Dey Talk Your Script...</p><div style="background:linear-gradient(to right, #ff2d55, #ff9a00); padding:40px; border-radius:15px;"><h1 style="color:white;">YOUR PRODUCT HERE</h1><p style="color:white;">' + st.session_state['script'][:120] + '...</p><h2 style="color:white;">Tap Play Below To Watch Sample</h2></div><p style="color:#FFD700; font-size:20px;">@kelly</p></div>', unsafe_allow_html=True)
    st.video("https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4")
    st.write("Above na sample player - Your real video from Hailuo go look like this, but with your product + your voice + @kelly for end!")
    st.markdown('<div style="background:#111; color:white; padding:20px; border-radius:15px; text-align:center;"><h1 style="color:white;">THANKS FOR WATCHING</h1><h1 style="color:#FFD700;">@kelly</h1><p>Follow @kelly for More!</p></div>', unsafe_allow_html=True)
    st.write("END CARD: Every video go end with @kelly like this! No forget am!")
    st.markdown("### POST NOW OR SAVE VIDEO")
    share_text = "Check my new Anime Advert! " + st.session_state['my_product'] + " - Follow @kelly - " + st.session_state['script'][:100]
    st.markdown("[POST NOW - Share for WhatsApp - Customer Go See Am](https://wa.me/?text=" + share_text.replace(" ", "%20") + ")")
    st.markdown("[POST NOW - Share for TikTok - Open TikTok](https://www.tiktok.com/upload)")
    st.markdown("[POST NOW - Share for Instagram Reels](https://www.instagram.com/reels/)")
    st.download_button("SAVE VIDEO PACKAGE - Download All (Script + Prompts + @kelly End)", st.session_state['script'] + "\n\nPICTURE PROMPT:\n" + st.session_state.get('pic_prompt','') + "\n\nVIDEO PROMPT:\n" + st.session_state.get('video_prompt','') + "\n\nMASTER PROMPT:\n" + st.session_state.get('master','') + "\n\nEND CARD: @kelly", file_name="kelly-video-package.txt")
    st.markdown("---")
    st.write("#### YOUR SCRIPT - For Voice - With @kelly for End")
    st.code(st.session_state['script'])
    st.write("#### YOUR PICTURE PROMPT")
    st.code(st.session_state.get('pic_prompt', ''))
    st.markdown("[Make Picture FREE (Bing)](https://www.bing.com/images/create)")
    st.write("#### YOUR VIDEO PROMPT - Already get @kelly for End!")
    st.code(st.session_state.get('video_prompt', ''))
    st.markdown("[Make Real Video FREE (Hailuo)](https://hailuoai.video)")
    st.write("#### YOUR MASTER PROMPT - Paste for Invideo - E Go Do Video + Voice + @kelly Together!")
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
