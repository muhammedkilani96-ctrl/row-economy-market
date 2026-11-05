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
st.markdown('<div style="background-color:#16a34a;padding:12px">',unsafe_allow_html=True)
st.markdown('<h1 style="color:white">Row Market</h1>',unsafe_allow_html=True)
st.markdown('<p style="color:white">Row Market Abuja - FREE</p>',unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)
q=st.text_input("Ask Mama Oloja",key="q1")
s=st.text_input("Type here to search",key="s1")
st.subheader("Categories")
a,b=st.columns(2)
if a.button("Perfume",key="c1"):
    st.session_state.cat="Perfume"
if b.button("Clothes",key="c2"):
    st.session_state.cat="Clothes"
a2,b2=st.columns(2)
if a2.button("Phones",key="c3"):
    st.session_state.cat="Phones"
if b2.button("Food",key="c4"):
    st.session_state.cat="Food"
a3,b3=st.columns(2)
if a3.button("Car Mart",key="c5"):
    st.session_state.cat="Car"
if b3.button("Services",key="c6"):
    st.session_state.cat="Services"
a4,b4=st.columns(2)
if a4.button("Tickets",key="c7"):
    st.session_state.cat="Tickets"
if b4.button("Chat Rooms",key="c8"):
    st.session_state.cat="Chat"
st.write("Category:")
st.write(st.session_state.cat)
st.subheader("Featured Listing")
st.write("Horlance Auto Cooling Ltd")
st.write("VERIFIED - Car AC Repair")
st.write("Osun & Oyo State")
st.write("WhatsApp 09046044472")
u="https://wa.me/2349046044472"
st.link_button("Chat on WhatsApp",u)
st.write("Mama Oloja AI:")
st.write("Welcome my dear, I can help")
st.write("you find best price.")
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
        st.write(g)
        ph=st.session_state.photos[idx]
        if ph is not None:
            st.image(ph)
        k="ord"+str(idx)
        if st.button("Order This",key=k):
            st.session_state.orders.append(g)
            st.write("Order Added!")
        st.write("---")
st.subheader("My Orders")
st.write("Total Orders:")
st.write(len(st.session_state.orders))
for o in st.session_state.orders:
    st.write(o)
if len(st.session_state.orders)>0:
    st.link_button("Order on WhatsApp",u)
st.subheader("Chat Rooms")
rm=st.selectbox("Chat Room",ct3,key="rm1")
cm=st.text_input("Chat Message",key="cm1")
if st.button("Send Chat",key="send1"):
    m=rm+" : "+cm
    st.session_state.msgs.append(m)
    st.write("Sent!")
for m in st.session_state.msgs:
    ml=m.lower()
    rl=rm.lower()
    if rl in ml:
        st.write(m)
st.subheader("Mama Answers")
ql=q.lower()
if "rice" in ql:
    st.write("Rice N80000 Abuja best price")
if "perfume" in ql:
    st.write("Perfume N15000")
if "car" in ql:
    st.write("Car go Horlance")
    st.write("09046044472")
if "phone" in ql:
    st.write("Phone test first")
if "food" in ql:
    st.write("Food fresh daily")
if "clothes" in ql:
    st.write("Clothes new stock")
if "hello" in ql:
    st.write("Mama Welcome dear")
if "hi" in ql:
    st.write("Mama Welcome dear")
st.subheader("My Profile")
pn=st.text_input("Profile Name",key="pn1")
if st.button("Save Profile",key="save1"):
    st.write("Profile Saved:")
    st.write(pn)
st.subheader("Share Row Market")
w="https://wa.me/?text=RowMarketAbuja"
st.link_button("Share on WhatsApp",w)
st.write("Row Market Abuja FREE")
st.write("Post goods FREE")
st.write("Chat FREE")
