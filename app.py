import streamlit as st
import urllib.parse

W='2348116911722'

# --- COLORS ---
c1='<style>'
c2='.stApp{background:#fdf6e3;}'
c3='h1{color:#8B4513;}'
c4='h2{color:#228B22;}'
c5='div.stButton>button{background:#228B22;color:white;}'
c6='</style>'
st.markdown(c1+c2+c3+c4+c5+c6, unsafe_allow_html=True)

st.title('Row Economy')
st.write('Drum Food Calabash Cloth Hut Event Garage Car')

s=st.selectbox('State',['Abuja','Lagos','Kano','Rivers','Kaduna'])
a=st.text_input('Area','Wuse')

t1,t2,t3,t4,t5=st.tabs(['Food','Event','Cloth','Car','Square'])

with t1:
    st.subheader('Food - Drum Beat')
    p=st.number_input('People',1,500,10,key='f')
    tot=p*1500
    st.write(f'Total: N{tot}')
    txt='Food '+str(p)+' '+a+' '+s
    q=urllib.parse.quote(txt)
    lk='https://wa.me/'+W+'?text='+q
    st.link_button('Order Food',lk)

with t2:
    st.subheader('Event - Hut Vibe')
    ev=st.text_input('Event','Concert')
    pr=st.number_input('Ticket',500,50000,2000,key='e')
    qty=st.number_input('Qty',1,20,1,key='eq')
    tot2=pr*qty
    st.write(f'Total: N{tot2}')
    txt2='Event '+ev+' '+a+' '+s
    q2=urllib.parse.quote(txt2)
    lk2='https://wa.me/'+W+'?text='+q2
    st.link_button('Buy Ticket',lk2)

with t3:
    st.subheader('Cloth - Calabash Style')
    cl=st.selectbox('Cloth',['Shirt','Native','Hijab','Ankara'])
    sz=st.selectbox('Size',['M','L','XL','XXL'])
    txt3='Cloth '+cl+' '+sz+' '+a+' '+s
    q3=urllib.parse.quote(txt3)
    lk3='https://wa.me/'+W+'?text='+q3
    st.link_button('Buy Cloth',lk3)

with t4:
    st.subheader('Car - Garage Verified')
    st.info('Law Protected - Must Verify')
    
    car=st.selectbox('Car',['Corolla','Sienna','Hiace','Camry'])
    chassis=st.text_input('Chassis VIN')
    ct=st.selectbox('Cert',['CAC','License','NIN'])
    cert=st.file_uploader('Upload cert')
    
    ag1=st.checkbox('Car not stolen - papers genuine')
    ag2=st.checkbox('Row is marketplace only')
    ag3=st.checkbox('Report to Police if fake')
    
    st.link_button('Check Police CMR','https://cmris.npf.gov.ng')
    
    if cert and ag1 and ag2 and ag3 and chassis!='':
        st.success('GREEN VERIFIED DEALER')
        txt4='Car '+car+' '+chassis+' Verified '+a+' '+s
        q4=urllib.parse.quote(txt4)
        lk4='https://wa.me/'+W+'?text='+q4
        st.link_button('Submit For Approval',lk4)
    else:
        st.error('Upload cert + 3 ticks + VIN')

with t5:
    st.subheader('Village Square')
    st.write('Drum - Food Sharing')
    st.write('Calabash - Cloth Display')
    st.write('Hut - Event Stage')
    st.write('Garage - Verified Cars')
    vid=st.file_uploader('Post video')
    if vid:
        st.video(vid)
        st.success('Village Posted!')

st.divider()
st.caption('Row Economy - Verified Marketplace - Abuja')
st.caption('Verify chassis at cmris.npf.gov.ng')
st.caption('Report: 08116911722 - Law Protected')
