import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title='ROW ECONOMY SUPER', layout='wide')

# --- STORAGE ---
if 'products' not in st.session_state:
    st.session_state.products = []
if 'lives' not in st.session_state:
    st.session_state.lives = []
if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- LOGIN ---
if 'user' not in st.session_state:
    st.title('ROW ECONOMY SUPER MARKET')
    st.subheader('Abuja No.1 Live Market')
    c1,c2 = st.columns(2)
    with c1:
        phone = st.text_input('Phone Number')
        pwd = st.text_input('Password', type='password')
        if st.button('LOGIN / REGISTER', type='primary'):
            if phone.strip() == '08116911722' and pwd.strip().lower() == 'kilani247':
                st.session_state.user = phone.strip()
