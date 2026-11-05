import streamlit as st
st.set_page_config(page_title='Row Market')
if 'g' not in st.session_state: st.session_state.g=[]
if 'p' not in st.session_state: st.session_state.p='Home'
if 'chat' not in st.session_state: st.session_state.chat=[]
st.title('Row Market')
st.write('Row Economy Market')
st.write('Buy Cheap. Sell Fast.')
q=st.text_input('Ask Mama Oloja - What are you looking for?')
ql=q.lower()
st.subheader('Mama Oloja Replies:')
if q=='': st.write('Mama: Welcome my dear, ask me for rice, perfume, phone, car.')
if 'rice' in ql: st.write('Mama: Rice is hot now. Check Food category. Good price is N80000 to N95000 per bag in Abuja.')
if 'perfume' in ql: st.write('Mama: Perfume plenty. Original ones start N15000. Avoid too cheap ones, they are fake my dear.')
if 'phone' in ql: st.write('Mama: Phones plenty in Shop. Ask seller for receipt and test before you pay.')
if 'car' in ql: st.write('Mama: For Car AC, go to Horlance. He is verified. Call 09046044472.')
if 'horlance' in ql: st.write('Mama: Horlance is verified. Car AC repair in Osun and Oyo. Very good man.')
if 'price' in ql: st.write('Mama: Tell me what product, I will tell you the real market price. No cheating here.')
if 'hello' in ql or 'hi' in ql: st.write('Mama: Hello my dear, welcome to Row Market. What do you want to buy today?')
if 'cheap' in ql: st.write('Mama: Row Market is for cheap price. Search below, you will see best price.')
if 'sell' in ql: st.write('Mama: To sell, scroll down to Sell FREE, fill form, post. Buyers will chat you on WhatsApp.')
s=st.text_input('Type here to search...')
s=s.lower()
nav=st.segmented_control('Menu', ['Home','Shop','Orders','Profile'])
if nav: st.session
