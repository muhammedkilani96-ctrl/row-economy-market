import streamlit as st
if 'goods' not in st.session_state:
    st.session_state.goods=[]
if 'page' not in st.session_state:
    st.session_state.page='Home'
if 'cat' not in st.session_state:
    st.session_state.cat='All'
def to_wa(num):
    n=''
    for c in num:
        if c.isdigit():
            n=n+c
    if len(n)==11:
        if n[0]=='0':
            n='234'+n[1:]
    if len(n)==10:
        n='234'+n
    return n
css='<style>'
css=css+'.stApp{background:#f7f7f7}'
css=css+'.block-container{padding-top:0px;padding-left:0px;padding-right:0px;padding-bottom:100px}'
css=css+'div[data-testid="stHorizontalBlock"]{flex-wrap:nowrap !important;gap:5px !important}'
css=css+'div[data-testid="column"]{min-width:0px !important;flex:1 !important}'
css=css+'.header{background:#00A651;padding:18px 12px 30px 12px;border-radius:0px 0px 25px 25px;display:flex;justify-content:space-between;align-items:center}'
css=css+'.header h1{color:white;margin:0px;font-size:28px}'
css=css+'.avatar{background:#FF7A00;width:45px;height:45px;border
