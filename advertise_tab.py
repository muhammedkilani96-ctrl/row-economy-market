import streamlit as st
from database import add_advert
import base64
from datetime import datetime, date
def show(area,state):
    st.subheader("Advertise")
    if st.session_state.ads_date != str(date.today()):
        st.session_state.ads_today=0; st.session_state.paid_unlock=0; st.session_state.ads_date=str(date.today())
    total_allowed=10+st.session_state.paid_unlock
    left=total_allowed-st.session_state.ads_today
    if left>0:
        if st.session_state.ads_today<10: st.success(f"FREE Left: {10-st.session_state.ads_today}/10")
        else: st.info(f"Paid Left: {left}")
    else:
        st.error("Limit reached! Pay N200")
        c1,c2=st.columns(2)
        c1.link_button("💳 Paystack N200", "https://paystack.com/pay/row-economy-200", use_container_width=True)
        c2.link_button("💬 WhatsApp Pay", "https://wa.me/2348116911722?text=I don pay N200 for extra ad", use_container_width=True)
        code=st.text_input("Enter code ROW200")
        if st.button("Unlock"):
            if code.startswith("ROW"): st.session_state.paid_unlock+=1; st.rerun()
        return
    with st.form("ad"):
        b=st.text_input("Business Name"); w=st.text_area("Wetin you sell?"); p=st.number_input("Price",0,10000000,2000)
        wa=st.text_input("WhatsApp e.g 23480..."); cat=st.selectbox("Category",["Food","Cloth","Car","Ticket","Service","Other"])
        img=st.file_uploader("Image",type=["jpg","png","jpeg"])
        if st.form_submit_button("Post Ad"):
            b64=base64.b64encode(img.read()).decode() if img else None
            add_advert({"business":b,"what":w,"price":p,"whatsapp":wa,"category":cat,"area":area,"state":state,"image":b64,"date":str(datetime.now())})
            st.session_state.ads_today+=1; st.success("Posted!"); st.balloons()
