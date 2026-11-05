import streamlit as st
if 'g' not in st.session_state:
    st.session_state.g=[]
if 'p' not in st.session_state:
    st.session_state.p='Home'
st.title('Row Economy Market')
st.write('Buy Cheap. Sell Fast.')
q=st.text_input('Ask Mama Oloja')
if st.session_state.p=='Home':
    st.subheader('Categories')
    a,b,c,d=st.columns(4)
    a.write('Perfume')
    b.write('Clothes')
    c.write('Phones')
    d.write('Food')
    e,f,g,h=st.columns(4)
    e.write('Car Mart')
    f.write('Services')
    g.write('Tickets')
    h.write('Chat')
    st.subheader('Featured')
    st.success('Horlance - VERIFIED')
    st.write('Car AC Repair')
    st.write('Osun and Oyo')
    st.link_button('Chat on WhatsApp','https://wa.me/2349046044472')
    st.subheader('New Goods')
    for x in st.session_state.g:
        st.info(x[0])
        st.link_button('Chat Seller','https://wa.me/'+x[1])
    st.subheader('Sell - FREE')
    nm=st.text_input('Your Name')
    pd=st.text_input('Product')
    pr=st.text_input('Price')
    wa=st.text_input('WhatsApp')
    go=st.button('POST FOR FREE')
    if go:
        t=nm+' - '+pd+' - N'+pr
        w='234'+wa[1:] if len(wa)==11 else wa
        st.session_state.g.append((t,w))
        st.success('Posted!')
        st.rerun()
if st.session_state.p=='Shop':
    st.subheader('Shop')
    for x in st.session_state.g:
        st.info(x[0])
if st.session_state.p=='Orders':
    st.subheader('Orders')
    st.write('Check WhatsApp for orders')
if st.session_state.p=='Profile':
    st.subheader('Profile')
    st.write(len(st.session_state.g))
nav=st.segmented_control('Menu',['Home','Shop','Orders','Profile'])
if nav:
    st.session_state.p=nav
    st.rerun()
