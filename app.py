import streamlit as st
st.set_page_config(page_title='Row Market')
if 'g' not in st.session_state:
    st.session_state.g=[]
if 'p' not in st.session_state:
    st.session_state.p='Home'
st.title('Row Market')
st.write('Row Economy Market')
st.write('Buy Cheap. Sell Fast.')
q=st.text_input('Ask Mama Oloja - What are you looking for?')
s=st.text_input('Type here to search...')
s=s.lower()
if st.session_state.p=='Home':
    st.subheader('Categories - See all')
    a,b,c,d=st.columns(4)
    a.write('Perfume')
    b.write('Clothes')
    c.write('Phones')
    d.write('Food')
    e,f,g,h=st.columns(4)
    e.write('Car Mart')
    f.write('Services')
    g.write('Tickets')
    h.write('Chat Rooms')
    st.subheader('Featured Listing - See all')
    if s=='' or 'horlance' in s or 'car' in s or 'ac' in s:
        st.write('Horlance Auto Cooling Ltd - VERIFIED')
        st.write('Car AC Repair')
        st.write('Osun and Oyo State')
        st.write('WhatsApp 09046044472')
        st.link_button('Chat on WhatsApp', 'https://wa.me/2349046044472')
    st.subheader('New Goods')
    found=False
    for x in st.session_state.g:
       
