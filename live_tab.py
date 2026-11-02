import streamlit as st
import base64
from datetime import datetime

def show(area, state):
    st.subheader("🔴 ROW LIVE - Sell Live, Get Gifted!")
    
    if "live_gifts" not in st.session_state:
        st.session_state.live_gifts = 0
    if "live_comments" not in st.session_state:
        st.session_state.live_comments = []
    
    # --- START LIVE ---
    with st.expander("🎥 START YOUR LIVE - Sell Now", expanded=True):
        live_title = st.text_input("Live Title e.g Selling Ankara - 50% off Wuse 2")
        product = st.text_input("Wetin you dey sell for this live?")
        price = st.number_input("Price for live", 0, 1000000, 5000)
        go_live = st.checkbox("I'M LIVE NOW 🔴")
        if go_live:
            st.success(f"LIVE: {live_title} | {area} - {len(st.session_state.live_comments)} watching")
    
    if not go_live:
        st.info("Tick 'I'M LIVE' to start")
        return

    # LIVE SCREEN
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown(f"""
        <div style="background:black; color:#39FF14; padding:20px; border-radius:15px; border:3px solid #39FF14; text-align:center">
        <h2>🔴 LIVE - {live_title}</h2>
        <p>📍 {area}, {state} | 🪘 {st.session_state.live_gifts} Gifts | 👁️ 24 watching</p>
        <p style="font-size:50px">📹 LIVE VIDEO HERE</p>
        <p>Upload short clip as live demo</p>
        </div>
        """, unsafe_allow_html=True)
        live_video = st.file_uploader("Upload live demo video (15sec)", type=["mp4","mov"], key="live_vid")
        if live_video:
            st.video(live_video)
        
        st.link_button(f"💬 BUY NOW N{price} - WhatsApp", f"https://wa.me/2348116911722?text=I want {product} from LIVE N{price}", use_container_width=True)

    with col2:
        st.write("### 🎁 Gifts")
        st.metric("Total Cowries", f"{st.session_state.live_gifts} 🪘")
        
        g1, g2, g3 = st.columns(3)
        with g1:
            if st.button("🌹 Rose\nN50"):
                st.session_state.live_gifts += 5
                st.balloons()
        with g2:
            if st.button("🪘 Drum\nN100"):
                st.session_state.live_gifts += 10
        with g3:
            if st.button("👑 Crown\nN500"):
                st.session_state.live_gifts += 50
                st.snow()
        
        st.divider()
        st.write("### 💬 Live Chat")
        chat = st.text_input("Comment", key="chat_input")
        if st.button("Send"):
            if chat:
                st.session_state.live_comments.append(f"{datetime.now().strftime('%H:%M')} - {chat}")
        for c in reversed(st.session_state.live_comments[-10:]):
            st.write(c)

    st.divider()
    st.caption("Seller cashout: 1 Cowrie = N10 | 100 Cowries = N1000 | Withdraw via WhatsApp")
