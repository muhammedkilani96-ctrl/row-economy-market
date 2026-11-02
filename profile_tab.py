import streamlit as st
from database import get_adverts
import base64

def show(area, state):
    st.subheader("Your Profile")
    st.write(f"Location: **{area}, {state}**")
    st.write("Businesses you posted:")
    
    ads = get_adverts()
    my_ads = [a for a in ads if a]  # for now show all (later filter by phone)
    
    if not my_ads:
        st.info("You never post yet. Go Advertise tab!")
        return
        
    for i, ad in enumerate(reversed(my_ads)):
        if ad.get("image"):
            try:
                st.image(base64.b64decode(ad["image"]), width=200)
            except:
                pass
        st.write(f"{ad.get('business')} - {ad.get('what')} - N{ad.get('price')} - {ad.get('category')}")
        if st.button(f"Delete this", key=f"del{i}"):
            ads.remove(ad)
            st.success("Deleted! Reboot to see.")
            st.rerun()
        st.divider()
