import streamlit as st
st.set_page_config(page_title='Row Market')
if 'g' not in st.session_state: st.session_state.g=[]
if 'chat' not in st.session_state: st.session_state.chat=[]
if 'p' not in st.session_state: st.session_state.p='Home'
st.markdown('<div style="background-color:#00A651;padding:15px;color:white">Row Market - Row Economy Market</div>', unsafe_allow_html=True)
st.markdown('<div style="background-color:#E8FFE8;padding:10px">Buy Cheap. Sell Fast. Abuja, Nigeria</div>', unsafe_allow_html=True)
nav=st.segmented_control('Menu', ['Home','Shop','Sell','Chat','Orders','Profile'])
if nav: st.session_state.p=nav
if nav: st.rerun()
if st.session_state.p=='Home': st.markdown('<div style="background-color:#D6FFD6;padding:10px">Mama Oloja Replies:</div>', unsafe_allow_html=True)
q=st.text_input('Ask Mama Oloja - What are you looking for?')
ql=q.lower()
if st.session_state.p=='Home' and q=='': st.write('Mama: Welcome my dear, ask me for rice, perfume, phone, car.')
if st.session_state.p=='Home' and 'rice' in ql: st.write('Mama: Rice is hot now. Check Food category. Good price is N80000 to N95000 per bag in Abuja.')
if st.session_state.p=='Home' and 'perfume' in ql: st.write('Mama: Perfume plenty. Original ones start N15000. Avoid too cheap ones, they are fake my dear.')
if st.session_state.p=='Home' and 'phone' in ql: st.write('Mama: Phones plenty in Shop. Ask seller for receipt and test before you pay.')
if st.session_state.p=='Home' and 'car' in ql: st.write('Mama: For Car AC, go to Horlance. He is verified. Call 09046044472.')
if st.session_state.p=='Home' and 'horlance' in ql: st.write('Mama: Horlance is verified. Car AC repair in Osun and Oyo. Very good man.')
if st.session_state.p=='Home' and 'verified' in ql: st.write('Mama: Verified means we checked the seller. Pay N5000 in Profile to get Verified badge.')
if st.session_state.p=='
