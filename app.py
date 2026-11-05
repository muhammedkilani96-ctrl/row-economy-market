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
q=st.text_input("Ask Mama Oloja")
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
if st.session_state.page=="Profile":
    st.markdown("### Profile")
    st.write("Posted goods:")
    st.write(len(st.session_state.goods))
elif st.session_state.page=="Orders":
    st.markdown("### Orders")
    if len(st.session_state.goods)==0:
        st.info("No orders yet")
    else:
        for it in st.session_state.goods:
            st.success(it[0])
            st.link_button("Chat Seller",
            wa_link(it[1], it[0]))
elif st.session_state.page=="Shop":
    st.markdown("### Shop - All Goods")
    st.success("Horlance - Car AC - N25000")
    st.link_button("Chat Horlance",
    wa_link("2349046044472", "x"))
    if st.button("Send Request to Horlance"):
        st.session_state.notes.append("Buyer wants Horlance")
        st.rerun()
    st.success("Mama T - Rice - N45000")
    st.link_button("Chat Mama T",
    wa_link("2349046044472", "x"))
    if st.button("Send Request to Mama T"):
        st.session_state.notes.append("Buyer wants Mama T Rice")
        st.rerun()
    for idx, it in enumerate(st.session_state.goods):
        st.success(it[0])
        st.link_button("Chat Seller",
        wa_link(it[1], it[0]), key="s"+str(idx))
        if st.button("Send Request", key="sr"+str(idx)):
            st.session_state.notes.append("Buyer wants: "+it[0])
            st.rerun()
else:
    st.markdown("### Featured")
    st.success("Horlance Auto Cooling - Car AC - N25000")
    st.link_button("Chat Horlance",
    wa_link("2349046044472", "x"))
    st.success("Mama T - Bag of Rice - N45000")
    st.link_button("Chat Mama T",
    wa_link("2349046044472", "x"))
    st.markdown("### New Goods")
    for idx, it in enumerate(st.session_state.goods):
        st.success(it[0])
        st.link_button("I Want This - Chat Seller",
        wa_link(it[1], it[0]), key="h"+str(idx))
        if st.button("Send Request", key="hr"+str(idx)):
            st.session_state.notes.append("Buyer wants: "+it[0])
            st.rerun()
st.markdown("### Sell - FREE")
nm=st.text_input("Your Name")
pd=st.text_input("Product Name")
pr=st.text_input("Price")
wa=st.text_input("Your WhatsApp Number")
pay=st.selectbox("Payment",
["Pay on Delivery", "Transfer Before"])
dlv=st.selectbox("Delivery",
["Pickup Only", "Delivery Available"])
if st.button("POST MY GOODS FOR FREE"):
    if nm=="" or pd=="" or wa=="":
        st.warning("Fill Name, Product, WhatsApp")
    else:
        txt=nm+" - "+pd+" - N"+pr
        txt=txt+" - "+pay+" - "+dlv
        st.session_state.goods.append((txt, to_wa(wa)))
        st.success("Posted! "+txt)
        st.balloons()
st.markdown("### Menu - Tap to Work")
n1, n2, n3, n4 = st.columns(4)
with n1:
    if st.button("Home"):
        st.session_state.page="Home"
        st.rerun()
with n2:
    if st.button("Shop"):
        st.session_state.page="Shop"
        st.rerun()
with n3:
    if st.button("Orders"):
        st.session_state.page="Orders"
        st.rerun()
with n4:
    if st.button("Profile"):
        st.session_state.page="Profile"
        st.rerun()
