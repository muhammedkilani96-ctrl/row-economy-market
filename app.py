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
st.markdown('<style>div.stButton>button{border-radius:14px;background:white;border:1px solid #e5e7eb;font-weight:600}div.stButton>button:hover{background:#dcfce7}</style>',unsafe_allow_html=True)
st.markdown('<div style="background:#16a34a;padding:16px 12px 20px 12px;border-radius:0 0 20px 20px">',unsafe_allow_html=True)
st.markdown('<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-size:24px;color:white">☰</span><span style="font-size:26px;font-weight:800;color:white">Row Market</span><span style="font-size:24px">👤</span></div>',unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)
q=st.text_input("Search",placeholder="Ask Mama Oloja - What are you looking for today?",key="q1",label_visibility="collapsed")
s=q
st.markdown('<div style="display:flex;justify-content:space-between;align-items:center"><h3 style="margin:0">Categories</h3><span style="color:#16a34a;font-weight:700">See all ></span></div>',unsafe_allow_html=True)
a,b,c,d=st.columns(4)
if a.button("Perfume",key="c1"):
    st.session_state.cat="Perfume"
if b.button("Clothes",key="c2"):
    st.session_state.cat="Clothes"
if c.button("Phones",key="c3"):
    st.session_state.cat="Phones"
if d.button("Food",key="c4"):
    st.session_state.cat="Food"
a2,b2,c2,d2=st.columns(4)
if a2.button("Car Mart",key="c5"):
    st.session_state.cat="Car"
if b2.button("Services",key="c6"):
    st.session_state.cat="Services"
if c2.button("Tickets",key="c7"):
    st.session_state.cat="Tickets"
if d2.button("Chat Rooms",key="c8"):
    st.session_state.cat="Chat"
st.write("Category:")
st.write(st.session_state.cat)
st.markdown('<div style="display:flex;justify-content:space-between;align-items:center"><h3 style="margin:0">Featured Listing</h3><span style="color:#16a34a;font-weight:700">See all ></span></div>',unsafe_allow_html=True)
st.markdown('<div style="background:white;padding:14px;border-radius:16px;box-shadow:0 2px 10px #eee">',unsafe_allow_html=True)
st.markdown('<div style="text-align:right"><span style="background:#16a34a;color:white;padding:4px 10px;border-radius:20px;font-size:12px">VERIFIED</span></div>',unsafe_allow_html=True)
st.markdown('<h4 style="margin:4px 0">Horlance Auto Cooling Ltd</h4>',unsafe_allow_html=True)
st.markdown('<p style="margin:2px 0">Car AC Repair</p>',unsafe_allow_html=True)
st.markdown('<p style="margin:2px 0">Osun & Oyo State</p>',unsafe_allow_html=True)
st.markdown('<p style="margin:2px 0">WhatsApp 09046044472</p>',unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)
u="https://wa.me/2349046044472"
st.link_button("Chat on WhatsApp",u)
st.markdown('<div style="background:#dcfce7;padding:12px;border-radius:16px">',unsafe_allow_html=True)
st.markdown('Mama Oloja AI: Welcome my dear, I can help you find the best price in the market. now',unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)
st.subheader("Sell FREE")
nm=st.text_input("Your Name",key="nm1")
pd=st.text_input("Product Name",key="pd1")
pr=st.text_input("Price",key="pr1")
ct1=["Perfume","Clothes","Phones","Food"]
ct2=["Car","Services","Tickets","Chat"]
ct3=ct1+ct2
ct=st.selectbox("Category",ct3,key="ct1")
pic=st.file_uploader("Add Photo",type=["jpg","png","jpeg"],key="pic1")
if pic is not None:
    st.image(pic)
if st.button("Post Good",key="post1"):
    item=nm+" - "+pd+" - N"+pr+" - "+ct
    st.session_state.goods.append(item)
    st.session_state.photos.append(pic)
    st.write("Posted! Thank you")
st.subheader("Shop")
st.write("Total Goods:")
st.write(len(st.session_state.goods))
for idx,g in enumerate(st.session_state.goods):
    gl=g.lower()
    sl=s.lower()
    ok=True
    if sl not in gl:
        ok=False
    if st.session_state.cat!="All":
        cl=st.session_state.cat.lower()
        if cl not in gl:
            ok=False
    if ok:
        st.markdown('<div style="background:white;padding:12px;border-radius:14px;box-shadow:0 1px 6px #eee">',unsafe_allow_html=True)
        st.write(g)
        ph=st.session_state.photos[idx]
        if ph is not None:
            st.image(ph)
        st.markdown('</div>',unsafe_allow_html=True)
        k="ord"+str(idx)
        if st.button("Order This",key=k):
            st.session_state.orders.append(g)
            st.write("Order Added!")
        st.write("---")
st
