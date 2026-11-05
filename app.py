import streamlit as st
if 'goods' not in st.session_state:
    st.session_state.goods=[]
if 'page' not in st.session_state:
    st.session_state.page='Home'
if 'cat' not in st.session_state:
    st.session_state.cat='All'
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
st.markdown(
 '<h1 style="color:white;'
 'background:#00A651;'
 'padding:18px;border-radius:0 0 25px 25px">'
 'K&K Market</h1>',
 unsafe_allow_html=True)
q=st.text_input(
 'Ask Mama Oloja',
 placeholder='What are you looking for today?')
if st.session_state.page=='Home':
    st.subheader('Categories')
    def catbtn(e,l):
        st.markdown(
         '<div style="font-size:28px;'
         'text-align:center">'+e+'</div>',
         unsafe_allow_html=True)
        if st.button(l,key='c'+l):
            st.session_state.cat=l
            st.session_state.page='Shop'
            st.rerun()
    a,b,c,d=st.columns(4)
    with a:
        catbtn('🧴','Perfume')
    with b:
        catbtn('👕','Clothes')
    with c:
        catbtn('📱','Phones')
    with d:
        catbtn('🍲','Food')
    e,f,g,h=st.columns(4)
    with e:
        catbtn('🚗','Car Mart')
    with f:
        catbtn('💼','Services')
    with g:
        catbtn('🎟️','Tickets')
    with h:
        catbtn('💬','Chat Rooms')
    st.subheader('Featured Listing')
    st.success('Horlance Auto Cooling Ltd - VERIFIED')
    st.write('🔧 Car AC Repair')
    st.write('📍 Osun & Oyo State')
    st.write('🟢 WhatsApp 09046044472')
    st.link_button(
     '💬 Chat on WhatsApp',
     'https://wa.me/2349046044472')
    st.subheader('New Goods')
    shown=[]
    for x in st.session_state.goods:
        if q.lower() in x[0].lower():
            shown.append(x)
    if q=='':
        shown=st.session_state.goods
    if len(shown)==0:
        st.write
