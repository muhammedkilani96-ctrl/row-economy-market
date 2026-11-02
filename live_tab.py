import streamlit as st
from datetime import datetime
def show(area,state):
    st.subheader("🔴 ROW LIVE")
    live_title=st.text_input("Live Title", "Selling Ankara Wuse 2")
    product=st.text_input("Product for live"); price=st.number_input("Price",0,1000000,5000)
    go=st.checkbox("I'M LIVE NOW 🔴")
    if not go: st.info("Tick to start live"); return
    c1,c2=st.columns([2,1])
    with c1:
        st.markdown(f"<div style='background:black;color:#39FF14;padding:15px;border-radius:15px;text-align:center'>🔴 LIVE {live_title}<br>📍{area},{state} | Gifts {st.session_state.live_gifts}<br>📹 LIVE VIDEO</div>",unsafe_allow_html=True)
        vid=st.file_uploader("Upload live clip",type=["mp4"],key="live")
        if vid: st.video(vid)
        st.link_button(f"BUY N{price}", f"https://wa.me/2348116911722?text=I want {product} LIVE N{price}", use_container_width=True)
    with c2:
        st.metric("Cowries", f"{st.session_state.live_gifts} 🪘")
        if st.button("🌹 N50"): st.session_state.live_gifts+=5; st.balloons()
        if st.button("🪘 Drum N100"): st.session_state.live_gifts+=10
        if st.button("👑 Crown N500"): st.session_state.live_gifts+=50; st.snow()
        st.write("💬 Live Chat")
        chat=st.text_input("Comment",key="lc")
        if st.button("Send Chat"):
            if chat: st.session_state.live_comments.append(f"{chat}")
        for x in st.session_state.live_comments[-8:]: st.write(x)
