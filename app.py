import streamlit as st
st.set_page_config(page_title='Row Market')
if 'g' not in st.session_state:
    st.session_state.g=[]
if 'p' not in st.session_state:
    st.session_state.p='Home'
h1='<div style="background:#00A651">'
h2='<h1 style="color:white">Row Market</h1>'
h3='<p style="color:white">Row Economy Market</p>'
h4='<p style="color:white">Buy Cheap. Sell Fast.</p></div>'
st.markdown(h1+h2+h3+h4, unsafe_allow_html=True)
q=st.text_input('Ask Mama Oloja - What are you looking for?')
s=st.text_input('Type here to search...')
s=s.lower()
if st.session_state.p=='Home':
    st.subheader('Categories - See all >')
    a,b,c,d=st.columns(4)
    c1='<div style="background:#FFD6E8">'
    c2='🧴<br>Perfume</div>'
    a.markdown(c1+c2, unsafe_allow_html=True)
    c3='<div style="background:#CDE7FF">'
    c4='👕<br>Clothes</div>'
    b.markdown(c3+c4, unsafe_allow_html=True)
    c5='<div style="background:#CDE7FF">'
    c6='📱<br>Phones</div>'
    c.markdown(c5+c6, unsafe_allow_html=True)
    c7='<div style="background:#FFE0B8">'
    c8='🍲<br>Food</div
