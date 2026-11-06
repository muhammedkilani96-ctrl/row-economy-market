# ===== MAMA OLOJA ANIME ADVERT - ₦200 PAYWALL - NO TABS VERSION =====
# Owner: Kilani Muhammed Opeyemi - Opay 8116911722

st.markdown("### 🎬 Mama Oloja Anime Advert")
st.write("Generate FREE, Download na **₦200** only! Pay to Kilani Muhammed Opeyemi")

all_products = [
    "Black Rapture - ₦4000 - Mary - 09031889875",
    "Black Rapture - ₦4000 - Arinfe - 090915907990",
    "Face Serum - ₦4000 - Blessing - 07052528772",
    "Rolex Watch - ₦10000 - Arinfe - 090915907990",
    "Lip Combo - ₦6000 - Arinfe - 090915907990",
    "Jersey Scarf - ₦3500 - Arinfe - 090915907990",
    "Yum Yum Combo - ₦12000 - Arinfe - 090915907990",
]
chosen = st.selectbox("Pick your product:", all_products, key="anime_prod")
anime_style = st.selectbox("Anime Style:", ["C - Cute Anime Girl (Pink)", "A - Fine Anime Babe", "B - Cool Anime Boy"], key="anime_style")

if st.button("✨ Generate My Advert (FREE Preview)", key="anime_gen"):
    st.session_state['advert_ready'] = True
    if "Black Rapture" in chosen:
        st.session_state['script'] = "My pikin, come see o! Black Rapture don land! E dey smell like money, e dey last all day! Chat me now to order. Mama Oloja talk am, e no be lie!"
    elif "Rolex" in chosen:
        st.session_state['script'] = "My pikin, see Rolex Watch! E go make you look like big boy! Price na 10,000 only, with box! Chat me now, no dull!"
    elif "Face Serum" in chosen:
        st.session_state['script'] = "My pikin, your face go glow! Face Serum na 4,000 only! E go clear your face, make you shine! Chat Blessing now!"
    else:
        st.session_state['script'] = f"My pikin, come see o! {chosen}! E good well well, price sweet! Chat me now to order. Mama Oloja recommend am!"

if st.session_state.get('advert_ready'):
    st.success("Preview Ready!")
    st.code(st.session_state['script'])
    st.write(f"Style: {anime_style}")
    st.info("Preview na FREE. To download, pay ₦200 below.")
    st.markdown("---")
    st.subheader("💰 Pay ₦200 To Unlock Download")
    st.write("**Opay Number: 8116911722**")
    st.write("**Name: Kilani Muhammed Opeyemi**")
    st.write("**Amount: ₦200**")
    st.write("**Narration: Anime Advert - Your Name**")
    pay_ref = st.text_input("Enter Your Opay Name + Reference:", placeholder="e.g. MARY - 200", key="anime_pay")
    if st.button("✅ I Don Pay ₦200 - Unlock", key="anime_unlock"):
        if pay_ref:
            st.session_state['paid'] = True
            st.success("Payment received! Download don unlock!")
        else:
            st.warning("Abeg enter your Opay name + reference first.")
    if st.session_state.get('paid'):
        st.markdown("### 🎉 YOUR VIDEO PACKAGE - DOWNLOAD NOW")
        st.download_button("📜 Download Mama Oloja Script", st.session_state['script'], file_name="mama-oloja-script.txt", key="anime_dl")
        st.write("🎙️ **Voice:** Go ttsmaker.com, paste script, Voice: Female Warm, Speed 0.9x, Download MP3")
        st.write("🖼️ **Anime Picture:** Use Cute Anime Girl picture")
        st.write("🎬 **Video:** Join Picture + Voice for OpenCut, Post for TikTok!")
        st.write("💬 **Need Help?** Chat us: https://wa.me/2348116911722")
        st.balloons()
    else:
        st.warning("🔒 Download Locked - Pay ₦200 to Opay 8116911722 to unlock.")

st.markdown("---")
