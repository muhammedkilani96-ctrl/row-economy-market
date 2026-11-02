import streamlit as st
from database import get_adverts

def show(area, state):
    st.subheader("Your Chats")
    if "chats" not in st.session_state:
        st.session_state.chats = []
    
    if not st.session_state.chats:
        st.info("No chats yet. Go Explore and click WhatsApp to start chat!")
        st.write("When you click WhatsApp button, we save am here.")
        return
    
    for chat in reversed(st.session_state.chats):
        st.write(f"**{chat['business']}** - {chat['what']} - {chat['time']}")
        st.link_button(f"Continue chat", f"https://wa.me/{chat['whatsapp']}", key=f"c{chat['time']}")
        st.divider()
