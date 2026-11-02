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
    pr=st.number_input('Ticket',500,50000,2000,key='
