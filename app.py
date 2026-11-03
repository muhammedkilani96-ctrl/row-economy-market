import streamlit as st
import json, hashlib, random, pandas as pd
from datetime import datetime

st.set_page_config(page_title='ROW ECONOMY SUPER', layout='centered')

def load(f,d):
    try:
        return json.loads(open(f).read())
    except:
        return d

def save(f,data):
    open(f,'w').write(json.dumps(data))

def hp(p):
    return hashlib.sha256(p.encode()).hexdigest()

users=load('users.json',{})
users['08116911722']={'name':'CEO','pw':hp('Kilani247')}
save('users.json',users)

wallets=load('wallets.json',{})
if wallets.get('08116911722',0)<1000:
    wallets['08116911722']=500000
    save('wallets.json',wallets)

if 'user' not in st.session_state:
    st.title('ROW ECONOMY SUPER')
    st.info('Login 08116911722 / Kilani247')
    phone=st.text_input('
