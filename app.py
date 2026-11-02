import streamlit as st
import urllib.parse

WHATSAPP='2348116911722'

st.title('Row')
st.write('Market')

s=st.selectbox('State',['Lagos','Abuja','Kano'])
a=st.text_input('Area','Wuse')

t1,t2=st.tabs(['Food','Cars'])

with t1:
    p=st.number_input('People',1,500,10)
    tot=p*1500
    st.write(tot)
    txt='Food '+str(p)+' '+a+' '+s
    lk='https://wa.me/'+WHATSAPP+'?text='+urllib.parse.quote(txt)
    st.link_button('Order',lk)

with t2:
    st.write('Car Verified')
    car=st.selectbox('Car',['Corolla','Sienna'])
    pr=st.number_input('Price',5000,5000000,20000)
    st.write('Upload cert')
    cert=st.file_uploader('cert')
    if cert:
        st.success('OK Verified')
        txt2='Car '+car+' '+a+' '+s+' Verified'
        lk2='https://wa.me/'+WHATSAPP+'?text='+urllib.parse.quote(txt2)
        st.link_button('Submit',lk2)
    else:
        st.error('Upload cert')
