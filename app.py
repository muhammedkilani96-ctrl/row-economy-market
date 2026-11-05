import streamlit as st
st.set_page_config(page_title='Row Economy Market')
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
h2='<div style="padding:20px;border-radius:25px">'
h3='<h1 style="color:white">Row Economy Market</h1>'
h4='<p style="color:white">Buy Cheap. Sell Fast. Chat on WhatsApp.</p>'
h5='</div></div>'
st.markdown(h1+h2+h3+h4+h5, unsafe_allow_html=True)
q=st.text_input('Ask Mama Oloja - What are you looking for today?')
if st.session_state.page=='Home':
    st.markdown('<b>Categories - See all ></b>', unsafe_allow_html=True)
    r1='<table><tr><td style="background:#FFD6E8">'
    r2='🧴<br>Perfume</td>'
    r3='<td style="background:#CDE7FF">👕<br>Clothes</td>'
    r4='<td style="background:#CDE7FF">📱<br>Phones</td>'
    r5='<td style="background:#FFE0B8">🍲<br>Food</td></tr>'
    r6='<tr><td style="background:#FFE0B8">🚗<br>Car Mart</td>'
    r7='<td style="background:#C8FFC8">💼<br>Services</td>'
    r8='<td style="background:#FFC8C8">🎟️<br>Tickets</td>'
    r9='<td style="background:#B8F0E8">💬<br>Chat Rooms</td>'
    r10='</tr></table>'
    st.markdown(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10, unsafe_allow_html=True)
    cat=st.selectbox('Filter by Category', ['All','Perfume','Clothes','Phones','Food','Car Mart','Services','Tickets','Chat Rooms'])
    st.subheader('Featured Listing - See all >')
    f1='<div style="background:white">'
    f2='<b>Horlance Auto Cooling Ltd</b>'
    f3='<span> ✅ VERIFIED</span>'
    f4='</div>'
    st.markdown(f1+f2+f3+f4, unsafe_allow_html=True)
    st.write('Car AC Repair - Osun & Oyo State')
    st.write('WhatsApp 09046044472')
    st.link_button('Chat on WhatsApp', 'https://wa.me/2349046044472')
    st.subheader('New Goods')
    st.write('Tap Chat Seller to buy on WhatsApp')
    for x in st.session_state.goods:
        st.info(x[0])
        st.link_button('Chat Seller', 'https://wa.me/'+x[1])
    m1='<div style="background:#D6FFD6">'
    m2='Welcome my dear, I can help you find best price'
    m3='</div>'
    st.markdown(m1+m2+m3, unsafe_allow_html=True)
    st.subheader('Sell - FREE')
    st.write('Post in 30 seconds.
