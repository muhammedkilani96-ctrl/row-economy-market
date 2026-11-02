import streamlit as st
from database import get_adverts
import base64

def show(area, state):
    st.subheader(f"Explore {area}")
    
    search = st.text_input("Search product e.g jollof")
    
    ads = get_adverts()
    if not ads:
        st.info("No adverts yet. Be first to post!")
        return
    
    # Filter
    if search:
        ads = [a for a in ads if search.lower() in a.get("what","").lower() or search.lower() in a.get("business","").lower() or search.lower() in a.get("category","").lower()]
    
    st.write(f"{len(ads)} found")
    
    for i, ad in enumerate(reversed(ads)):
        if ad.get("image"):
            try:
                st.image(base64.b64decode(ad["image"]), width=300)
            except:
                pass
        st.write(f"**{ad.get('business')}** - {ad.get('what')} ({ad.get('category','Other')}) - N{ad.get('price')}")
        st.link_button(f"Chat on WhatsApp", f"https://wa.me/{ad.get('whatsapp')}?text=Hi, I saw {ad.get('what')} on Row Economy", key=f"wa_{i}")
        st.divider()
