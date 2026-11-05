import streamlit as st
if "goods" not in st.session_state:
    st.session_state.goods=[]
if "page" not in st.session_state:
    st.session_state.page="Home"
if "notes" not in st.session_state:
    st.session_state.notes=[]

def to_wa(num):
    n=""
    for c in num:
        if c.isdigit():
            n=n+c
    if len(n)==11:
        if n[0]=="0":
            n="234"+n[1:]
    if len(n)==10:
        n="234"+n
    return n

def wa_link(seller_wa, product):
    return "https://wa.me/"+seller_wa

st.markdown("## ROW ECONOMY")
st.markdown("Nigeria Sweetest Market")
st.markdown("---")

if len(st.session_state.notes)>0:
    st.warning("You have new buyer request")
    for nt in st.session_state.notes:
        st.warning(nt)
    if st.button("Clear Notifications"):
        st.session_state.notes=[]
        st.rerun()

q=st.text_input("Ask", "Ask Mama Oloja")
if q:
    qq=q.lower()
    if "car" in qq:
        st.success("Found: Horlance Car AC")
    elif "rice" in qq:
        st.success("Found: Mama T Rice N45000")
    else:
        st.info("Mama dey find: "+q)

st.markdown("### Categories")
st.write("Perfume | Clothes | Phones | Food")
st.write("Car Mart | Services | Tickets | Chat Rooms")

choice=st.selectbox("Tap Category",
["All","Perfume","Clothes","Phones",
"Food","Car Mart","Services",
"Tickets","Chat Rooms"])
if choice!="All":
    st.success("Showing: "+choice)
