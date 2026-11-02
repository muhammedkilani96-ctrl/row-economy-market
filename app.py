# ADVERT ROOM - FIXED PAYWALL
st.title("Advert Room - 10 Ads Free Per Day")

if "ad_count" not in st.session_state:
    st.session_state.ad_count = 0

if st.session_state.ad_count < 10:
    st.write(f"Ads seen today: {st.session_state.ad_count}/10 FREE")
    if st.button("View Advert"):
        st.session_state.ad_count += 1
        st.success("Ad watched! +1")
        st.rerun()
else:
    st.error(f"Ads seen today: {st.session_state.ad_count}/10 - FREE FINISHED!")
    st.write("Pay **N200** to continue watching ads today")
    if st.button("Pay N200 with Paystack"):
        # Paystack payment link here
        st.link_button("Pay Now", "https://paystack.com/pay/YOUR_LINK")
