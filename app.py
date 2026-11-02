import streamlit as st
import urllib.parse

st.set_page_config(page_title='Row', layout='centered')

WHATSAPP='2348116911722'

st.title('Row Economy')
st.write('Market for Nigeria')

state=st.selectbox('State',['Abia','Lagos','FCT Abuja','Kano','Rivers','Oyo'],index=2)
area=st.text_input('Area','Wuse')

tab1,tab2=st.tabs(['Food','Cars'])

with tab1:
    people=st.number_input('People',1,500,10)
    meal=st.selectbox('Meal',['Rice','Spaghetti'])
    total=people*1500
    st.write(total)
    txt='Food '+str(people)+' '+area+' '+state
    link='https://wa.me/'+WHATSAPP+'?text='+urllib.parse.quote(txt)
    st.link_button('Order',link)

with tab2:
    st.write('Cars - Need Certificate')
    car=st.selectbox('Car',['Corolla','Sienna','Hiace'])
    price=st.number_input('Price',5000,5000000,20000)
    cert=st.file_uploader('Upload CAC or License
