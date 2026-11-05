import streamlit as st
import urllib.parse
st.set_page_config(page_title="Row Economy")
if "goods" not in st.session_state:
    st.session_state.goods=[]
if "page" not in st.session_state:
    st.session_state.page="Home"
if "notes" not in st.session_state:
    st.session_state.notes=[]

def to_wa(num):
    n="".join([c for c in num if c.isdigit()])
    if len(n)==11 and n.startswith("0"):
        return "234"+n[1:]
    if len(n)==10:
        return "234"+n
    return n

def wa_link(seller_wa, product):
    msg="Hello, I want to buy:
