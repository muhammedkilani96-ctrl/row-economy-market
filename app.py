import streamlit as st
st.set_page_config(page_title='Row Market')
if 'g' not in st.session_state: st.session_state.g=[]
if 'chat' not in st.session_state: st.session_state.chat=[]
if 'p' not in st.session_state: st.session_state.p='Home'
p=st.session_state.p
st.title('Row Market')
st.write('Buy Cheap. Sell Fast.')
st.write('Abuja, Nigeria')
nav=st.segmented_control('Menu', ['Home','Shop','Sell','Chat','Orders','Profile'])
if nav: st.session_state.p=nav
if nav: st.rerun()
p=st.session_state.p
q=st.text_input('Ask Mama Oloja')
ql=q.lower()
if p=='Home': st.subheader('Mama Oloja Replies:')
if p=='Home' and q=='': st.write('Mama: Welcome my dear')
if p=='Home' and 'rice' in ql: st.write('Mama: Rice N
