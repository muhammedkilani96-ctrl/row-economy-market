import streamlit as st
from database import get_adverts
import base64
from datetime import datetime

def show(area, state):
    st.subheader(f"Explore {area}")
    
    col1, col2 = st.columns([2,1])
    with col1:
        search = st.text_input("Search product e.g jollof", key="search_exp")
    with col2:
        cat_filter = st.selectbox("Category", ["All","Food","Cloth","Car","Service","Other"], key="cat_exp")
    
    ads = get_adverts()
    if not ads:
        st.info("No adverts yet. Be first to post!")
        return
    
    # Filter
    if search:
        ads = [a for a in ads if search.lower() in a.get("what","").lower() or search.lower() in a.get("business","").lower()]
    if cat_filter != "All":
        ads = [a for a in ads if a.get("category","Other")==cat_filter]
    
    st.write(f"**{len(ads)} found**")
    
    if "chats" not in st.session_state:
        st.session_state.chats = []
    
    for i, ad in enumerate(reversed(ads)):
        with st.container():
            if ad.get("image"):
                try:
                    st.image(base64.b64decode(ad["image"]), width=300)
                except:
                    pass
            st.markdown(f"### {ad.get('business')}")
            st.write(f"{ad.get('what')} | {ad.get('category','Other')} | **N{ad.get('price')}** | {ad.get('area')}")
            
            c1, c2 = st.columns(2)
            with c1:
                if st.link_button(f"💬 Chat on WhatsApp", f"https://wa.me/{ad.get('whatsapp')}?text=Hi {ad.get('business')}, I saw {ad.get('what')} on Row Economy Market", key=f"wa_{i}_{ad.get('what')}"):
                    pass
            with c2:
                if st.button(f"Save to Chats", key=f"save_{i}"):
                    st.session_state.chats.append({
                        "business": ad.get('business'),
                        "what": ad.get('what'),
                        "whatsapp": ad.get('whatsapp'),
                        "time": datetime.now().strftime("%H:%M %d-%b")
                    })
                    st.success("Saved to Chats tab!")
            st.divider()
