import streamlit as st
from database import add_advert, get_adverts
import base64
from datetime import datetime, date

def show(area, state):
    st.subheader("Advertise Your Business")
    
    # --- LIMIT LOGIC ---
    if "ads_today" not in st.session_state:
        st.session_state.ads_today = 0
    if "ads_date" not in st.session_state:
        st.session_state.ads_date = str(date.today())
    
    # reset new day
    if st.session_state.ads_date != str(date.today()):
        st.session_state.ads_today = 0
        st.session_state.ads_date = str(date.today())
    
    free_left = 10 - st.session_state.ads_today
    if free_left > 0:
        st.success(f"FREE Ads Left Today: {free_left}/10")
    else:
        st.warning("Free limit reached (10/10) today")
        st.info("Pay N200 to post more")
        # PAY BUTTON
        st.link_button("Pay N200 via WhatsApp to Unlock", f"https://wa.me/2348116911722?text=I want to pay N200 for extra advert on Row Economy Market", use_container_width=True)
        pay_code = st.text_input("Enter payment code after paying (we give you)", key="paycode")
        if pay_code != "ROW200" and free_left <= 0:
            st.error("Enter correct code to continue")
            return

    with st.form("advert_form"):
        business = st.text_input("Business Name e.g Mama Put")
        what = st.text_area("Wetin you dey sell?")
        price = st.number_input("Price N", 0, 10000000, 2000)
        whatsapp = st.text_input("WhatsApp Number e.g 23480...")
        category = st.selectbox("Category", ["Food","Cloth","Car","Ticket","Service","Other"])
        image = st.file_uploader("Upload product image", type=["jpg","png","jpeg"])
        
        submit = st.form_submit_button("Post Advert")
        if submit:
            if not business or not what:
                st.error("Fill business and what you sell")
            else:
                img_b64 = None
                if image:
                    img_b64 = base64.b64encode(image.read()).decode()
                add_advert({
                    "business": business,
                    "what": what,
                    "price": price,
                    "whatsapp": whatsapp,
                    "category": category,
                    "area": area,
                    "state": state,
                    "image": img_b64,
                    "date": str(datetime.now())
                })
                st.session_state.ads_today += 1
                st.success(f"Ad Posted! You don post {st.session_state.ads_today} today. Left {10 - st.session_state.ads_today} free")
                st.balloons()
