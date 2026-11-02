import streamlit as st
from database import add_advert
import base64
from datetime import datetime, date

def show(area, state):
    st.subheader("Advertise Your Business")

    if "ads_today" not in st.session_state:
        st.session_state.ads_today = 0
    if "ads_date" not in st.session_state:
        st.session_state.ads_date = str(date.today())
    if "paid_unlock" not in st.session_state:
        st.session_state.paid_unlock = 0

    if st.session_state.ads_date != str(date.today()):
        st.session_state.ads_today = 0
        st.session_state.paid_unlock = 0
        st.session_state.ads_date = str(date.today())

    total_allowed = 10 + st.session_state.paid_unlock
    free_left = total_allowed - st.session_state.ads_today

    if free_left > 0:
        if st.session_state.ads_today < 10:
            st.success(f"FREE Ads Left: {10 - st.session_state.ads_today}/10")
        else:
            st.info(f"Paid Ads Left: {free_left} (you paid for extra)")
    else:
        st.error("You don reach limit for today!")
        st.markdown("### Pay N200 to post more")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("💳 Pay N200 - Paystack (Auto)", "https://paystack.com/pay/row-economy-200", use_container_width=True)
            st.caption("Auto unlock after payment")
        with col2:
            st.link_button("💬 Pay via WhatsApp (Manual)", f"https://wa.me/2348116911722?text=I don pay N200 for extra ads for {area}", use_container_width=True)
            st.caption("Send proof on WhatsApp")
        
        code = st.text_input("Enter unlock code (Paystack gives code, or we give ROW200 after WhatsApp proof)")
        if st.button("Unlock with code"):
            if code == "ROW200" or code.startswith("ROW"):
                st.session_state.paid_unlock += 1
                st.success("Unlocked! 1 extra advert added")
                st.rerun()
            else:
                st.error("Invalid code")
        return

    with st.form("advert_form"):
        business = st.text_input("Business Name")
        what = st.text_area("Wetin you dey sell? e.g 2 VIP Tickets - Concert")
        price = st.number_input("Price N", 0, 10000000, 2000)
        whatsapp = st.text_input("WhatsApp e.g 2348012345678")
        category = st.selectbox("Category", ["Food","Cloth","Car","Ticket","Service","Other"])
        image = st.file_uploader("Product/Ticket Image", type=["jpg","png","jpeg"])
        submit = st.form_submit_button("Post Advert - FREE" if st.session_state.ads_today < 10 else f"Post Advert - Paid ({free_left-1} left)")
        if submit:
            if not business or not what:
                st.error("Fill business and what you sell")
            else:
                img_b64 = None
                if image:
                    img_b64 = base64.b64encode(image.read()).decode()
                add_advert({
                    "business": business, "what": what, "price": price,
                    "whatsapp": whatsapp, "category": category,
                    "area": area, "state": state, "image": img_b64,
                    "date": str(datetime.now())
                })
                st.session_state.ads_today += 1
                st.success(f"Posted! Total today {st.session_state.ads_today}/{total_allowed}")
                st.balloons()
