import streamlit as st
if 'goods' not in st.session_state:
    st.session_state.goods=[]
if 'page' not in st.session_state:
    st.session_state.page='Home'
def to_wa(n):
    r=''
    for c in n:
        if c.isdigit():
            r=r+c
    if len(r)==11 and r[0]=='0':
        r='234'+r[1:]
    if len(r)==10:
        r='234'+r
    return r
# HEADER
st.markdown('<div style="background:#00A651;'
 'padding:18px 12px 30px 12px;'
 'border-radius:0 0 25px 25px;'
 'display:flex;'
 'justify-content:space-between;'
 'align-items:center">'
 '<div style="color:white;font-size:28px">☰</div>'
 '<h1 style="color:white;margin:0">'
 'K&K Market</h1>'
 '<div style="background:#FF7A00;'
 'width:45px;height:45px;'
 'border-radius:50%;text-align:center;'
 'font-size:28px">👤</div></div>',
 unsafe_allow_html=True)
# SEARCH
q=st.text_input(
