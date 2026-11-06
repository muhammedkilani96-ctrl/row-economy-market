# ===== ANIME ADVERT - TOP BANNER - ALWAYS VISIBLE =====
st.markdown("""
<div style="background:#ff2d55; padding:15px; border-radius:15px; text-align:center; color:white;">
<h2>🎬 MAMA OLOJA ANIME ADVERT - ₦200 ONLY!</h2>
<p>Make Anime Video For Your Product - Pay ₦200 to Opay 8116911722</p>
</div>
""", unsafe_allow_html=True)

if st.button("🎬 CLICK HERE - Make My Anime Advert - ₦200", key="top_anime_btn"):
    st.session_state['show_anime'] = True

if st.session_state.get('show_anime'):
    st.header("🎬 Mama Oloja Anime Advert")
    prod_name = st.text_input("Product Name:", value="Face Serum", key="top_prod")
    prod_price = st.text_input("Price:", value="4000", key="top_price")
    prod_phone = st.text_input("Your WhatsApp:", value="07052528772", key="top_phone")
    
    if st.button("✨ Generate FREE Preview", key="top_gen"):
        st.session_state['anime_script_top'] = f"My pikin, come see o! {prod_name} don land! Price na {prod_price} only! Chat me for {prod_phone} now! Mama Oloja talk am!"
    
    if st.session_state.get('anime_script_top'):
        st.code(st.session_state['anime_script_top'])
        st.write("**Pay ₦200 to: Opay 8116911722 - Kilani Muhammed Opeyemi**")
        pay_ref = st.text_input("Enter Opay Name + Ref:", key="top_pay")
        if st.button("✅ I Don Pay ₦200 - Unlock", key="top_unlock"):
            if pay_ref:
                st.session_state['anime_paid_top'] = True
                st.success("Unlocked!")
        if st.session_state.get('anime_paid_top'):
            st.download_button("📜 Download Script", st.session_state['anime_script_top'], file_name="mama-oloja-script.txt", key="top_dl")
            st.write("Voice: Go ttsmaker.com, paste script, Female Warm, Speed 0.9x")
            st.balloons()
