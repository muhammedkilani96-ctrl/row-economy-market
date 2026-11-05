import streamlit as st
if "cat" not in st.session_state:
    st.session_state.cat="All"
if "goods" not in st.session_state:
    st.session_state.goods=[]
st.title("Row Market")
st.write("Row Market Abuja - FREE")
q=st.text_input("Ask Mama Oloja")
s=st.text_input("Type here to search")
st.subheader("Categories")
a,b,c,d=st.columns(4)
if a.button("Perfume"):
    st.session_state.cat="Perfume"
if b.button("Clothes"):
    st.session_state.cat="Clothes"
if c.button("Phones"):
    st.session_state.cat="Phones"
if d.button("Food"):
    st.session_state.cat="Food"
a2,b2,c2,d2=st.columns(4)
if a2.button("Car Mart"):
    st.session_state.cat="Car"
if b2.button("Services"):
    st.session_state.cat="Services"
if c2.button("Tickets"):
    st.session_state.cat="Tickets"
if d2.button("Chat Rooms"):
    st.session_state.cat="Chat"
st.write("Category:")
st.write(st.session_state.cat)
st.subheader("Featured Listing")
st.write("Horlance Auto Cooling Ltd")
st.write("VERIFIED")
st.write("Car AC Repair")
st.write("Osun & Oyo State")
st.write("WhatsApp 09046044472")
u="https://wa.me/2349046044472"
st.link_button("Chat on WhatsApp",u)
st.write("Mama Oloja AI:")
st.write("Welcome my dear, I can help")
st.write("you find best price.")
st.subheader("Sell FREE")
nm=st.text_input("Your Name")
pd=st.text_input("Product Name")
pr=st.text_input("Price")
ct1=["Perfume","Clothes","Phones","Food"]
ct2=["Car","Services","Tickets","Chat"]
ct3=ct1+ct2
ct=st.selectbox("Category",ct3)
if st.button("Post Good"):
    item=nm+" - "+pd+" - N"+pr+" - "+ct
    st.session_state.goods.append(item)
    st.write("Posted! Thank you")
st.subheader("Shop")
st.write("Total Goods:")
st.write(len(st.session_state.goods))
for g in st.session_state.goods:
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
        st.write("---")
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
pn=st.text_input("Profile Name")
if st.button("Save Profile"):
    st.write("Profile Saved:")
    st.write(pn)
st.subheader("Share Row Market")
w="https://wa.me/?text=RowMarketAbuja"
st.link_button("Share on WhatsApp",w)
st.write("Row Market Abuja FREE")
st.write("Post goods FREE")
st.write("Chat FREE")
