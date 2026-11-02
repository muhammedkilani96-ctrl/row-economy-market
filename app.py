import streamlit as st
import urllib.parse

W='2348116911722'

st.title('Row')
st.write('Food Event Cloth Car')

s=st.selectbox('State',['Lagos','Abuja','Kano','Rivers'])
a=st.text_input('Area','Wuse')

t1,t2,t3,t4,t5=st.tabs(['Food','Event','Cloth','Car','Square'])

with t1:
    p=st.number_input('People',1,500,10,key='f')
    tot=p*1500
    st.write(tot)
    txt='Food '+str(p)+' '+a+' '+s
    q=urllib.parse.quote(txt)
    lk='https://wa.me/'+W+'?text='+q
    st.link_button('Order Food',lk)

with t2:
    ev=st.text_input('Event','Concert')
    pr=st.number_input('Ticket',500,50000,2000,key='e')
    qty=st.number_input('Qty',1,20,1,key='eq')
    tot2=pr*qty
    st.write(tot2)
    txt2='Event '+ev+' '+a+' '+s
    q2=urllib.parse.quote(txt2)
    lk2='https://wa.me/'+W+'?text='+q2
    st.link_button('Buy Ticket',lk2)

with t3:
    cl=st.selectbox('Cloth',['Shirt','Native','Hijab'])
    sz=st.selectbox('Size',['M','L','XL'])
    pr3=st.number_input('Price',1000,20000,5000,key='c')
    txt3='Cloth '+cl+' '+sz+' '+a+' '+s
    q3=urllib.parse.quote(txt3)
    lk3='https://wa.me/'+W+'?text='+q3
    st.link_button('Buy Cloth',lk3)

with t4:
    st.write('Car Verified Only')
    car=st.selectbox('Car',['Corolla','Sienna','Hiace'])
    pr4=st.number_input('Car Price',5000,5000000,20000,key='car')
    ct=st.selectbox('Cert',['CAC','License','NIN'])
    cert=st.file_uploader('cert')
    if cert:
        st.success('Cert OK Verified')
        txt4='Car '+car+' '+ct+' Verified '+a+' '+s
        q4=urllib.parse.quote(txt4)
        lk4='https://wa.me/'+W+'?text='+q4
        st.link_button('Submit Car',lk4)
    else:
        st.error('Upload cert first')

with t5:
    st.write('Village Square')
    st.write('Drum Food')
    st.write('Calabash Cloth')
    st.write('Hut Event')
    st.write('Garage Car Verified')
    vid=st.file_uploader('video')
    if vid:
        st.video(vid)
        st.success('Posted')
