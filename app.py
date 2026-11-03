import streamlit as st
st.set_page_config(page_title="Row Economy Market")
st.info("We accept Naira, USDT, BTC")
tab1, tab2, tab3 = st.tabs(["Market","Sell","My Shop"])
with tab1:
    st.write("Search product")
    st.text_input("Search")
    st.success("Market is working! Add Supabase secrets to show products")
with tab2:
    st.write("Post Product - Add secrets to enable")
with tab3:
    st.write("My Shop")
