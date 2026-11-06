import streamlit as st
import random

st.set_page_config(page_title="ROW Economy Market", page_icon="🛍️", layout="wide")

# ===== ANIME ADVERT - TOP - ALWAYS SHOW =====
st.markdown("### 🎬 MAMA OLOJA ANIME ADVERT - ₦200 ONLY!")
st.write("Pay to Opay 8116911722 - Kilani Muhammed Opeyemi")

prod = st.selectbox("Pick product:", ["Black Rapture - 4000 - Mary", "Face Serum - 4000 - Blessing", "Rolex Watch - 10000 - Arinfe", "Lip Combo - 6000 - Arinfe"])
if st.button("✨ Generate FREE Preview"):
    if "Black Rapture" in prod:
        st.session_state['script'] = "My pikin, come see o! Black Rapture don land! E dey smell like money! Chat me now!"
    elif "Face Serum" in prod:
        st.session_state['script'] = "My pikin, your face go glow! Face Serum na 4000 only! Chat Blessing now!"
    else:
        st.session_state['script'] = f"My pikin, come see o! {prod}! E good well well! Chat me now! Mama Oloja talk am!"

if st.session_state.get('script'):
    st.code(st.session_state['script'])
    st.write("**Pay ₦200 to Opay 8116911722 - Kilani Muhammed Opeyemi**")
    ref = st.text_input("Enter Opay Name + Ref:", placeholder="e.g. MARY - 200")
    if st.button("✅ I Don Pay ₦200 - Unlock"):
        if ref:
            st.session_state['paid'] = True
            st.success("Unlocked!")
    if st.session_state.get('paid'):
        st.download_button("📜 Download Script", st.session_state['script'], file_name="script.txt")
        st.write("Voice: Go ttsmaker.com, paste script, Female Warm, Speed 0.9x")
        st.balloons()
    else:
        st.warning("🔒 Locked - Pay ₦200 to Opay 8116911722")

st.markdown("---")
st.markdown("### 👋 Welcome back, muhammed! - Rest of your app go continue from here - Mama Oloja, Shop, etc go dey below after you paste full code")
