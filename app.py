import streamlit as st
import urllib.parse

W='2348116911722'

st.title('Row')
st.write('Verified Market')

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
    txt3='Cloth '+cl+' '+sz+' '+a+' '+s
    q3=urllib.parse.quote(txt3)
    lk3='https://wa.me/'+W+'?text='+q3
    st.link_button('Buy Cloth',lk3)

with t4:
    st.subheader('Car - Law Protected')
    st.info('Must upload cert + agree')
    
    car=st.selectbox('Car',['Corolla','Sienna','Hiace'])
    chassis=st.text_input('Chassis Number')
    pr4=st.number_input('Price',5000,5000000,20000,key='car')
    
    st.write('Step 1: Upload Cert')
    ct=st.selectbox('Cert Type',['CAC','License','NIN+Paper'])
    cert=st.file_uploader('Upload cert')
    
    st.write('Step 2: Law Check')
    agree1=st.checkbox('I confirm car not stolen, papers genuine')
    agree2=st.checkbox('I agree Row is only marketplace, not owner')
    agree3=st.checkbox('I agree details go to Police if fake')
    
    st.link_button('Check if stolen - Police CMR','https://cmris.npf.gov.ng')
    
    if cert and agree1 and agree2 and agree3 and chassis!='':
        st.success('VERIFIED - Ready to post')
        txt4='Car '+car+' Chassis '+chassis+' Verified '+a+' '+s
        q4=urllib.parse.quote(txt4)
        lk4='https://wa.me/'+W+'?text='+q4
        st.link_button('Submit for Admin Approval',lk4)
        st.write('Badge: GREEN VERIFIED DEALER')
    else:
        st.error('Complete all: cert + 3 ticks + chassis')
        st.button('Submit',disabled=True)

with t5:
    st.write('Village Square')
    st.write('Garage - Verified Only')
    vid=st.file_uploader('video')
    if vid:
        st.video(vid)
        st.success('Posted')

st.divider()
st.caption('Disclaimer: Row is marketplace only. Verify chassis at cmris.npf.gov.ng before buying.')
st.caption('Report stolen car: 08116911722')
