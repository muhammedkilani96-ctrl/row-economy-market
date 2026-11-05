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
a='<div style="background:#00A651">'
b='<h1 style="color:white">K&K Market</h1>'
c='</div>'
st.markdown(a+b+c, unsafe_allow_html=True)
q=st.text_input('Ask Mama Oloja')
p=st.text_input('Search placeholder')
if st.session_state.page=='Home':
    st.subheader('Categories')
    g1='<div>🧴 Perfume | 👕 Clothes</div>'
    g2='<div>📱 Phones | 🍲 Food</div>'
    g3='<div>🚗 Car Mart | 💼 Services</div>'
    g4='<div>🎟️ Tickets | 💬 Chat Rooms</div>'
    st.markdown(g1, unsafe_allow_html=True)
    st.markdown(g2, unsafe_allow_html=True)
    st.markdown(g3, unsafe_allow_html=True)
    st.markdown(g4, unsafe_allow_html=True)
    cat=st.selectbox('Filter', ['All','Food','Clothes'])
    st.subheader('Featured Listing')
    st.success('Horlance Auto Cooling Ltd - VERIFIED')
    st.write('Car AC Repair')
    st.write('Osun & Oyo State')
    st.write('WhatsApp 09046044472')
    st.link_button('Chat on WhatsApp', 'https://wa.me/2349046044472')
    st.subheader('New Goods')
    for x in st.session_state.goods:
        st.info(x[0])
        st.link_button('Chat Seller', 'https://wa.me/'+x[1])
    st.info('Welcome my dear, I can help you find best price')
    st.subheader('Sell - FREE')
    nm=st.text_input('Your Name')
    pd=st.text_input('Product Name')
    pr=st.text_input('Price')
    wa=st.text_input('Your WhatsApp Number')
    go=st.button('POST MY GOODS FOR FREE')
    if go:
        t
