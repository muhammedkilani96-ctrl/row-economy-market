if st.button("Pay with Paystack 💳"):
    st.link_button("Click to Pay ₦"+str(total), f"https://paystack.shop/pay/yourlink?amount={total*100}")
    st.success("Payment link ready! After pay, I go confirm.")
