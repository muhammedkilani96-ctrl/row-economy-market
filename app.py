import streamlit as st
st.set_page_config(page_title='Row Market')
if 'g' not in st.session_state:
    st.session_state.g=[]
if 'p' not in st.session_state:
    st.session_state.p='Home'
h1='<div style="background:#00A651">'
h2='<h1 style="color:white">Row Market</h1>'
h3='<p style="color:white">Row Economy Market</p>'
h4='<p style="color:white">Buy Cheap. Sell Fast.</p></div>'
st.markdown(h1+h2+h3+h4, unsafe_allow_html=True)
q=st.text_input('Ask Mama Oloja - What are you looking for?')
s=st.text_input('Type here to search...')
if st.session_state.p=='Home':
    st.subheader('Categories - See all >')
    a,b,c,d=st.columns(4)
    c1='<div style="background:#FFD6E8">'
    c2='🧴<br>Perfume</div>'
    a.markdown(c1+c2, unsafe_allow_html=True)
    c3='<div style="background:#CDE7FF">'
    c4='👕<br>Clothes</div>'
    b.markdown(c3+c4, unsafe_allow_html=True)
    c5='<div style="background:#CDE7FF">'
    c6='📱<br>Phones</div>'
    c.markdown(c5+c6, unsafe_allow_html=True)
    c7='<div style="background:#FFE0B8">'
    c8='🍲<br>Food</div>'
    d.markdown(c7+c8, unsafe_allow_html=True)
    e,f,g,h=st.columns(4)
    c9='<div style="background:#FFE0B8">'
    c10='🚗<br>Car Mart</div>'
    e.markdown(c9+c10, unsafe_allow_html=True)
    c11='<div style="background:#C8FFC8">'
    c12='💼<br>Services</div>'
    f.markdown(c11+c12, unsafe_allow_html=True)
    c13='<div style="background:#FFC8C8">'
    c14='🎟️<br>Tickets</div>'
    g.markdown(c13+c14, unsafe_allow_html=True)
    c15='<div style="background:#B8F0E8">'
    c16='💬<br>Chat Rooms</div>'
    h.markdown(c15+c16, unsafe_allow_html=True)
    st.subheader('Featured Listing - See all >')
    f1='<div style="background:white">'
    f2='<b>Horlance Auto Cooling Ltd</b>'
    f3=' ✅ VERIFIED</div>'
    st.markdown(f1+f2+f3, unsafe_allow_html=True)
    st.write('🔧 Car AC Repair')
    st.write('📍 Osun & Oyo State')
    st.write('🟢 WhatsApp 09046044472')
    st.link_button('Chat on WhatsApp', 'https://wa.me/2349046044472')
    st.subheader('New Goods')
    for x in st.session_state.g:
        st.info(x[0])
        st.link_button('Chat Seller', 'https://wa.me/'+x[1])
    m1='<div style="background:#D6FFD6">'
    m2='Welcome my dear, I can help you find best price'
    m3='</div>'
    st.markdown(m1+m2+m3, unsafe_allow_html=True)
    st.subheader('Sell - FREE')
    st.write('Post in 30 seconds. Buyer chats you.')
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
    st.subheader('Shop - Row Market')
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
    st.write('Row Market - Abuja, Nigeria')
    st.write('Total goods:')
    st.write(len(st.session_state.g))
    for x in st.session_state.g:
        st.info(x[0])
nav=st.segmented_control('Menu', ['Home','Shop','Orders','Profile'])
if nav:
    st.session_state.p=nav
    st.rerun()
