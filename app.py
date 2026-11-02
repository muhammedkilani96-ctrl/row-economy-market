import streamlit as st

st.set_page_config(page_title="Row Economy")

st.markdown("""
<style>
.stApp{background:#000000 !important;}
h1{color:#00FF66 !important;}
h2,h3{color:#FFFFFF !important;}
p, label, div{color:#FFFFFF !important;}
</style>
""", unsafe_allow_html=True)

st.title("Row Economy")
st.write("Black Background - Green White Green")

st.success("App loaded - Black background working")

st.subheader("Advertise Here")
biz = st.text_input("Business Name", "Mama Food")
what = st.text_input("What you sell", "Jollof rice")
price = st.number_input("Price", 100, 1000000, 2000)

if st.button("Post Advert"):
    st.success("Posted")
    st.write(biz)
    st.write(what)
    st.write(price)
    st.balloons()

st.divider()
st.write("Featured Ads")
st.write("Fresh Yam - Kano - 5500")
st.write("Ankara GWG - Lagos - 12000")

st.link_button("WhatsApp Chat", "https://wa.me/2348116911722")
st.link_button("CMRIS Verify", "https://cmris.npf.gov.ng")

st.caption("Row Economy - Black + Green")
