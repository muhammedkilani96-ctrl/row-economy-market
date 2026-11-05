import streamlit as st
if "cat" not in st.session_state:
    st.session_state.cat="All"
if "goods" not in st.session_state:
    st.session_state.goods=[]
if "photos" not in st.session_state:
    st.session_state.photos=[]
if "orders" not in st.session_state:
    st.session_state.orders=[]
if "msgs" not in st.session_state:
    st.session_state.msgs=[]
if "page" not in st.session_state:
    st.session_state.page="Home"
css="<style>"
css+="[data-testid='stHorizontalBlock']"
css+="{flex-wrap:nowrap !important}"
css+="</style>"
st.markdown(css,unsafe_allow_html=True)
head="<div style='background:#16a34a;"
head+="padding:20px 10px;"
head+="border-radius:0 0 20px 20px;"
head+="text-align:center'>"
head+="<h1 style='color:white;margin:0'>"
head+="Row Market</h1>"
head+="<p style='color:white'>"
head+="Row Market Abuja - FREE</p></div>"
st.markdown(head,unsafe_allow_html=True)
q=st.text_input("Search",key="q1")
q=st.text_input("Ask Mama",key="q2")
s=q
st.markdown('<h3>Categories</h3>',unsafe_allow_html=True)
a,b=st.columns(2)
if a.button("Perfume",key="c1"):
    st.session_state.cat="Perfume"
if b.button("Clothes",key="c2"):
    st.session_state.cat="Clothes"
c,d=st
