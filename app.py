import streamlit as st
if "cat" not in st.session_state:
    st.session_state.cat="All"
if "goods" not in st.session_state:
    st.session_state.goods=[]
if "photos" not in st.session_state:
    st.session_state.photos=[]
if "orders" not in st.session_state:
    st.session_state.orders=[]
if "msgs" not in st.session_state:
    st.session_state.msgs=[]
if "page" not in st.session_state:
    st.session_state.page="Home"
st.markdown('<style>[data-testid="stHorizontalBlock"]{flex-wrap:nowrap !important;gap:8px !important}[data-testid="column"]{min-width:0 !important;flex:1 !important}div.stButton>button{width:100% !important;padding:12px 2px !important;font-size:14px !important;border-radius:14px !important;white-space:nowrap !important}</style>',unsafe_allow_html=True)
st.markdown('<div style="background:#16a34a;padding:20px 10px;border-radius:0 0 20px 20px;text-align:center"><h1 style="color:white;margin:0;font-size:32px">Row Market</h1><p style="color:white;margin:5px 0 0 0">Row Market Abuja - FREE</p></div>',unsafe_allow_html=True)
q=st.text_input("Search",placeholder="Ask Mama Oloja - What are you looking for today?",key="q1",label_visibility="collapsed")
s=q
st.markdown('<h3>Categories</h3>',unsafe_allow_html=True)
a,b=st.columns(2)
if a.button("Perfume",key="c1"):
    st.session_state.cat="Perfume"
if b.button("Clothes",key="c2"):
    st.session_state.cat="Clothes"
c,d=st.columns(2)
if c.button("Phones",key="c3"):
    st.session_state.cat="Phones"
if d.button("Food",key="c4"):
    st.session_state.cat="Food"
e,f=st.columns(2)
if e.button("Car Mart",key="c5"):
    st.session_state.cat="Car"
if f.button("Services",key="c6"):
    st.session_state.cat="Services"
g,h=st.columns(2)
if g.button("Tickets",key="c7"):
    st.session_state.cat="Tickets"
if h.button("Chat Rooms",key="c8"):
    st.session_state.cat="Chat"
st.write("Category:")
st.write(st.session_state.cat)
st.markdown('<div style="background:white;padding:14px;border-radius:16px;box-shadow:0 2px 10px #eee"><div style="text-align:right"><span style="background:#16a34a;color:white;padding:4px 10px;border-radius:20px;font-size:12px">VERIFIED</span></div><h4>Horlance Auto Cooling Ltd</h4><p>Car AC Repair</p><p>Osun & Oyo State</p><p>WhatsApp 09046044472</p></div>',unsafe_allow_html=True)
u="https://wa.me/2349046044472"
st.link_button("Chat on WhatsApp",u)
st.markdown('<div style="background:#dcfce7;padding:12px;border-radius:16px">Mama Oloja AI: Welcome my dear, I can help you find the best price.</div>',unsafe_allow_html=True)
st.subheader("Sell FREE")
nm=st.text_input("Your Name",key="nm1")
pd=st.text_input("Product Name",key="pd1")
pr=st.text_input("Price",key="pr1")
ct1=["Perfume","Clothes","Phones","Food"]
ct2=["Car","Services","Tickets","Chat"]
ct3=ct1+ct2
ct=st.selectbox("Category
