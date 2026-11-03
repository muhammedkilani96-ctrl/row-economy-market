import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title='ROW SUPER', layout='centered')

if 'products' not in st.session_state:
    st.session_state.products=[]
if 'lives' not in st.session_state:
    st.session_state.lives=[]

if 'user' not in st.session_state:
    st.title('ROW ECONOMY SUPER MARKET')
    phone=st.text_input('Phone')
    pwd=st.text_input('Password', type='password')
    if st.button('LOGIN'):
        if phone.strip()=='08116911722' and pwd.strip().lower()=='kilani247':
            st.session_state.user=phone.strip()
            st.rerun()
        else:
            st.error('Use 08116911722 / kilani247')
    st.stop()

st.title('ROW ECONOMY SUPER')
st.success('Welcome '+st.session_state.user)

t1,t2,t3,t4=st.tabs(['LIVE MARKET','POST PRODUCT','GO LIVE','MAP'])

with t1:
    st.header('LIVE MARKET')
    search=st.text_input('Search')
    for lv in st.session_state.lives[::-1]:
        st.warning('LIVE: '+lv['title'])
    st.divider()
    plist=st.session_state.products[::-1]
    if search:
        plist=[p for p in plist if search.lower() in p['name'].lower()]
    if len(plist)==0:
        st.write('No products yet')
    for p in plist:
        st.subheader(p['name']+' - N'+str(p['price']))
        st.write(p['desc'])
        st.write('Seller: '+p['phone']+' | '+p['time'])
        st.link_button('Chat Seller', 'https://wa.me/'+p['phone'])
        if p.get('img'):
            try:
                st.image(p['img'], width=200)
            except:
                pass
        st.divider()

with t2:
    st.header('POST PRODUCT')
    pname=st.text_input('Name *', key='pn')
    pprice=st.number_input('Price', value=1000, key='pp')
    pdesc=st.text_area('Description', key='pd')
    pphone=st.text_input('WhatsApp', value='08116911722', key='ph')
    pimg=st.text_input('Image Link (optional)', key='pi')
    if st.button('POST NOW', type='primary'):
        if pname.strip()=='':
            st.error('Enter name')
        else:
            st.session_state.products.append({'name':pname,'price':pprice,'desc':pdesc,'phone':pphone,'img':pimg,'time':datetime.now().strftime('%H:%M')})
            st.success('Posted! Check LIVE MARKET')
            st.balloons()
            st.snow()

with t3:
    st.header('GO LIVE')
    ltitle=st.text_input('Live Title', key='lt')
    c1,c2=st.columns(2)
    with c1:
        if st.button('START LIVE', type='primary'):
            if ltitle:
                st.session_state.lives.append({'title':ltitle,'user':st.session_state.user,'time':datetime.now().strftime('%H:%M')})
                st.success('YOU ARE LIVE!')
                st.balloons()
    with c2:
        if st.button('END LIVE'):
            st.session_state.lives=[]
            st.warning('Ended')

with t4:
    st.header('ABUJA MAP')
    df=pd.DataFrame({'lat':[9.06+random.uniform(-0.05,0.05) for _ in range(15)],'lon':[7.48+random.uniform(-0.05,0.05) for _ in range(15)]})
    st.map(df)
    st.write('Products: '+str(len(st.session_state.products)))
    st.write('Live: '+str(len(st.session_state.lives)))
    if st.button('Logout'):
        del st.session_state.user
        st.rerun()
