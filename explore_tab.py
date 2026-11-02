import streamlit as st
from database import get_adverts
import base64
def show(area,state):
    st.subheader(f"Explore {area}, {state}")
    cat=st.selectbox("Filter",["All","Food","Cloth","Car","Ticket","Service","Other"])
    ads=get_adverts()
    filtered=[a for a in ads if (cat=="All" or a.get("category")==cat) and (state in a.get("state","") or area.lower() in a.get("area","").lower() or True)]
    if not filtered: st.info("No adverts yet. Be first to post!")
    for a in filtered:
        with st.container(border=True):
            if a.get("image"):
                try: st.image(base64.b64decode(a["image"]), use_container_width=True)
                except: pass
            st.write(f"**{a['business']}** - {a['category']}")
            st.write(a['what']); st.write(f"N{a['price']} | {a['area']}, {a['state']}")
            wa=a.get("whatsapp","2348116911722").replace("+","")
            st.link_button(f"Chat Seller", f"https://wa.me/{wa}?text=I see your {a['category']} for N{a['price']} in {a['area']}", use_container_width=True)
