import streamlit as st
if 'goods' not in st.session_state:
    st.session_state.goods=[]
if 'page' not in st.session_state:
    st.session_state.page='Home'
def to_wa(n):
    r=''
    for c in n:
        if c.isdigit():
            r=r+c
    if len(r)==11 and r[0]=='0':
        r='234'+r[1:]
    if len(r)==10:
        r='234'+r
    return r
h1='<div style="background:#00A651">'
h2='<div style="padding:18px">'
h3='<h1 style="color:white">K&K Market</h1>'
h4='</div></div>'
st.markdown(h1+h2+h3+h4, unsafe_allow_html=True)
q=st.text_input('Ask Mama Oloja - What are you looking for?')
if st.session_state.page=='Home':
    t1='<div style="display:flex">'
    t2='<b>Categories</b><span> See all ></span>'
    t3='</div>'
    st.markdown(t1+t2+t3, unsafe_allow_html=True)
    c1='<div style="background:#FFD6E8">'
    c2='🧴 Perfume</div>'
    st.markdown(c1+c2, unsafe_allow_html=True)
    c3='<div style="background:#CDE7FF">'
    c4='👕 Clothes</div>'
    st.markdown(c3+c4, unsafe_allow_html=True)
    c5='<div style="background:#CDE7FF">'
    c6='📱 Phones</div>'
    st.markdown(c5+c6, unsafe_allow_html=True)
    c7='<div style="background:#FFE0B8">'
    c8='🍲 Food</div>'
    st.markdown(c7+c8, unsafe_allow_html=True)
    c9='<div style="background:#FFE0B8">'
    c10='🚗 Car Mart</div>'
    st.markdown(c9+c10, unsafe_allow_html=True)
    c11='<div style="background:#C8FFC8">'
    c12='💼 Services</div>'
    st.markdown(c11+c12, unsafe_allow_html=True)
    c13='<div style="background:#FFC8C8">'
    c14='🎟️ Tickets</div>'
    st.markdown(c13+c14, unsafe_allow_html=True)
    c15='<div style="background:#B8F0E8">'
    c16='💬 Chat Rooms</div>'
    st.markdown(c15+c16, unsafe_allow_html=True)
    cat=st.selectbox('Filter', ['All','Food','Clothes','Phones'])
    st.subheader('Featured Listing')
    f1='<div style="background:white">'
    f2='<b>Horlance Auto Cooling Ltd</b>'
    f3='<span> ✅ VERIFIED</span>'
    f4='</div>'
    st.markdown(f1+f2+f3+f4, unsafe_allow_html=True)
    st.write('Car AC Repair')
    st.write('Osun & Oyo State')
    st.write('WhatsApp 09046044472')
    st.link_button('Chat on WhatsApp', 'https://wa.me/2349046044472')
    st.subheader('New Goods')
    for x in st.session_state.goods:
        st.info(x[0])
        st.link_button('Chat Seller', 'https://wa.me/'+x[1])
    m1='<div style="background:#D6FFD6">'
    m2='Welcome my dear, I can help you find best price'
    m3='</div>'
    st.markdown(m1+m2+m3, unsafe_allow_html=True)
    st.subheader('Sell - FREE')
    nm=st.text_input('Your Name')
    pd=st.text_input('Product Name')
    pr=st.text_input('Price')
    wa=st.text_input('Your WhatsApp Number')
    go=st.button('POST MY GOODS FOR FREE')
    if go:
        t=nm+' - '+pd+' - N'+pr
        st.session_state.goods.append((t,to_wa(wa)))
        st.success('Posted!')
        st.balloons()
        st.rerun()
if st.session_state.page=='Shop':
    st.subheader('Shop')
    st.info('Horlance - Car AC - N25000')
    st.link_button('Chat', 'https://wa.me/2349046044472')
    for x in st.session_state.goods:
        st.info(x[0])
if st.session_state.page=='Orders':
    st.subheader('Orders')
    for x in st.session_state.goods:
        st.info(x[0])
if st.session_state.page=='Profile':
    st.subheader('Profile')
    st.write(len(st.session_state.goods))
st.markdown('---')
nav=st.segmented_control('Menu', ['Home','Shop','Orders','Profile'])
if nav=='Home':
    st.session_state.page='Home'
    st.rerun()
if nav=='Shop':
    st.session_state.page='Shop'
    st.rerun()
if nav=='Orders':
    st.session_state.page='Orders'
    st.rerun()
if nav=='Profile':
    st.session_state.page='Profile'
    st.rerun()
