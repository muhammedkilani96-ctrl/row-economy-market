import streamlit as st
st.set_page_config(page_title='K&K Market')
if 'g' not in st.session_state:
    st.session_state.g=[]
if 'p' not in st.session_state:
    st.session_state.p='Home'
st.markdown('<h1 style="background:#00A651">K&K Market</h1>', unsafe_allow_html=True)
q=st.text_input('Ask Mama Oloja - What are you looking for today?')
s=st.text_input('Type here to search...')
if st.session_state.p=='Home':
    st.subheader('Categories - See all >')
    a,b,c,d=st.columns(4)
    a.write('🧴')
    a.write('Perfume')
    b.write('👕')
    b.write('Clothes')
    c.write('📱')
    c.write('Phones')
    d.write('🍲')
    d.write('Food')
    e,f,g,h=st.columns(4)
    e.write('🚗')
    e.write('Car Mart')
    f.write('💼')
    f.write('Services')
    g.write('🎟️')
    g.write('Tickets')
    h.write('💬')
    h.write('Chat Rooms')
    st.subheader('Featured Listing - See all >')
    st.write('Horlance Auto Cooling Ltd - VERIFIED')
    st.write('Car AC Repair')
    st.write('Osun & Oyo State')
    st.write('WhatsApp 09046044472')
    st.link_button('Chat on WhatsApp', 'https://wa.me/2349046044472')
    st.subheader('New Goods')
    for x in st.session_state.g:
        st.info(x[0])
        st.link_button('Chat Seller', 'https://wa.me/'+x[1])
    st.write('Welcome my dear, I can help you find best price')
    st.subheader('Sell - FREE')
    nm=st.text_input('Your Name')
    pd=st.text_input('Product Name')
    pr=st.text_input('Price')
    wa=st.text_input('Your WhatsApp Number')
    cg=st.selectbox('Category', ['Food','Clothes','Phones','Perfume','Car Mart','Services','Tickets'])
    go=st.button('POST MY GOODS FOR FREE')
    if go:
        t=nm+' - '+pd+' - N'+pr+' - '+cg
        w='234'+wa[1:] if len(wa)==11 else wa
        st.session_state.g.append((t,w))
        st.success('Posted!')
        st.balloons()
        st.rerun()
if st.session_state.p=='Shop':
    st.subheader('Shop')
    st.info('Horlance - Car AC - N25000')
    st.link_button('Chat', 'https://wa.me/2349046044472')
    for x in st.session_state.g:
        st.info(x[0])
        st.link_button('Chat Seller', 'https://wa.me/'+x[1])
if st.session_state.p=='Orders':
    st.subheader('Orders')
    st.write('Check WhatsApp for orders')
    for x in st.session_state.g:
        st.info(x[0])
if st.session_state.p=='Profile':
    st.subheader('Profile')
    st.write('K&K Market - Abuja, Nigeria')
    st.write('Total goods:')
    st.write(len(st.session_state.g))
    for x in st.session_state.g:
        st.info(x[0])
nav=st.segmented_control('Menu', ['Home','Shop','Orders','Profile'])
if nav:
    st.session_state.p=nav
    st.rerun()
