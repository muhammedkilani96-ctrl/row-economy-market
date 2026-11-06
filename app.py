import streamlit as st
import random

st.set_page_config(page_title="ROW Economy Market - Video Anime", page_icon="🎬", layout="wide")

if 'coins' not in st.session_state:
    st.session_state['coins'] = 100
if 'script' not in st.session_state:
    st.session_state['script'] = ""
if 'paid' not in st.session_state:
    st.session_state['paid'] = False
if 'video_prompt' not in st.session_state:
    st.session_state['video_prompt'] = ""

# ===== 🎬 VIDEO ANIME - TOP - RED BANNER =====
st.markdown("""
<div style="background:#ff2d55; padding:20px; border-radius:15px; text-align:center; color:white;">
<h1 style="color:white;">🎬 MAMA OLOJA VIDEO ANIME</h1>
<h3 style="color:white;">Real Video - Girl Dey Move, Mouth Dey Talk!</h3>
<p>Generate FREE, Download Video Package na ₦200 ONLY!</p>
<p>Pay to Opay 8116911722 - Kilani Muhammed Opeyemi</p>
</div>
""", unsafe_allow_html=True)

st.write("### 👀 SEE SAMPLE VIDEO ANIME - How Your Video Go Look")
st.write("This na sample - Your own video go get your product + your voice!")
# SAMPLE VIDEO - Replace this link with your own video later
st.video("https://cdn.coverr.co/videos/coverr-anime-girl-looking-at-the-camera-1585/1080p.mp4")
st.caption("Sample: Cute Anime Girl talking - Your video go be like this, but with your product!")

st.markdown("---")
st.write("### 🎯 STEP 1 - PICK YOUR PRODUCT (FREE)")

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
style = st.selectbox("Anime Girl Style:", [
    "C - Cute Anime Girl Pink Hair - Best for TikTok!",
    "A - Fine Anime Babe - Brown Skin",
    "B - Cool Anime Boy - For Boys Products"
])

if st.button("✨ Generate My Video Advert (FREE Preview)"):
    if "Black Rapture" in prod:
        st.session_state['script'] = "My pikin, come see o! Black Rapture don land! E dey smell like money, e dey last all day! Chat me now to order. Mama Oloja talk am, e no be lie!"
    elif "Rolex" in prod:
        st.session_state['script'] = "My pikin, see Rolex Watch! E go make you look like big boy! Price na 10,000 only, with box! Chat me now, no dull!"
    elif "Face Serum" in prod:
        st.session_state['script'] = "My pikin, your face go glow! Face Serum na 4,000 only! E go clear your face, make you shine! Chat Blessing now!"
    else:
        st.session_state['script'] = f"My pikin, come see o! {prod}! E good well well, price sweet! Chat me now to order. Mama Oloja recommend am!"
    # VIDEO PROMPTS
    if "Cute" in style or "C -" in style:
        char = "Cute anime girl, pink hair, big eyes, smiling, Nigerian market background"
    elif "Fine" in style or "A -" in style:
        char = "Beautiful anime babe, brown skin, long black hair, smiling, Nigerian market background"
    else:
        char = "Cool anime boy, short hair, smiling, holding product, Nigerian market background"
    st.session_state['video_prompt'] = f"{char}, holding {prod}, waving hand, lips moving and talking, blinking, lively, TikTok anime style, bright colors, 4k"
    st.session_state['pic_prompt'] = f"{char}, holding {prod}, full body, smiling at camera, bright, high quality, TikTok style"

if st.session_state['script']:
    st.success("✅ Preview Ready! - Script + Video Prompt Ready!")
    st.write("**🎙️ Your Mama Oloja Script:**")
    st.write(st.session_state['script'])
    st.write(f"**Style:** {style}")
    st.info("Preview na FREE. To unlock Video Package (Picture Prompt + Video Prompt + Voice Steps), pay ₦200 below.")
    st.markdown("---")
    st.subheader("💰 STEP 2 - Pay ₦200 To Unlock VIDEO Package")
    st.write("**Opay Number: 8116911722**")
    st.write("**Name: Kilani Muhammed Opeyemi**")
    st.write("**Amount: ₦200**")
    st.write("**Narration: Video Anime - Your Name**")
    ref = st.text_input("Enter Your Opay Name + Reference:", placeholder="e.g. MARY - 200")
    if st.button("✅ I Don Pay ₦200 - Unlock Video Package"):
        if ref:
            st.session_state['paid'] = True
            st.success("Payment received! Video Package don unlock!")
        else:
            st.warning("Abeg enter Opay name + reference first.")
    if st.session_state['paid']:
        st.markdown("### 🎉 YOUR REAL VIDEO ANIME PACKAGE - DO AM IN 3 MINS!")
        st.balloons()
        st.markdown("#### 🖼️ STEP A - MAKE ANIME PICTURE (FREE)")
        st.write("Copy this prompt, go Bing Create / Perchance, paste am, download picture:")
        st.code(st.session_state.get('pic_prompt', ''))
        st.markdown("[🖼️ Click Here - Make Picture FREE (Bing Create)](https://www.bing.com/images/create)")
        st.markdown("---")
        st.markdown("#### 🎥 STEP B - MAKE VIDEO FROM PICTURE (FREE)")
        st.write("Go Hailuo AI, upload picture wey you just make, paste this Video Prompt:")
        st.code(st.session_state.get('video_prompt', ''))
        st.markdown("[🎥 Click Here - Make Video FREE (Hailuo AI)](https://hailuoai.video)")
        st.markdown("[🎥 Alternative - Make Video FREE (Kling AI)](https://klingai.com)")
        st.write("Wait 1 min, Download Video! Girl go dey move, mouth go dey talk!")
        st.markdown("---")
        st.markdown("#### 🎙️ STEP C - ADD MAMA OLOJA VOICE")
        st.write("Copy script below, go TTSMaker, paste am, Voice: Female Warm, Speed 0.9x, Download MP3:")
        st.code(st.session_state['script'])
        st.download_button("📜 Download Script", st.session_state['script'], file_name="mama-oloja-script.txt")
        st.markdown("[🎙️ Click Here - Make Voice FREE (TTSMaker)](https://ttsmaker.com)")
        st.markdown("---")
        st.markdown("#### 🎬 STEP D - JOIN VIDEO + VOICE (FREE)")
        st.write("Go CapCut App (for phone), Import Video + Voice, Export, Post for TikTok / WhatsApp Status!")
        st.markdown("[🎬 Download CapCut FREE](https://www.capcut.com)")
        st.write("💬 **Need Help Make Video?** Chat us: https://wa.me/2348116911722 - We go help you make am for ₦500 extra!")
    else:
        st.warning("🔒 Video Package Locked - Pay ₦200 to Opay 8116911722 to unlock Picture Prompt + Video Prompt + Voice Steps.")

st.markdown("---")

# ===== REST OF APP =====
st.markdown("""
<div style="background:black; color:white; padding:10px; border-radius:15px; display:flex; justify-content:space-between;">
<span>📍 Ikorodu, Lagos</span><span>🪙 100 Coins • 🛒 0</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:linear-gradient(to bottom right, #0a7a42, #d4c400); padding:20px; border-radius:20px; color:white;">
<h2 style="color:#FFD700;">✦ ROW ECONOMY MARKET ✦</h2>
<h1>Welcome back,<br>muhammed! 👋</h1>
<p>Everything you need, near you. No scam.<br>Mama Oloja dey watch for you.</p>
<p>⭐ 4.9 Rating
