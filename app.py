import streamlit as st
st.set_page_config(page_title="Row Economy")
if "goods" not in st.session_state:
    st.session_state.goods=[]
if "page" not in st.session_state:
    st.session_state.page="Home"
if "cat" not in st.session_state:
    st.session_state.cat="All"

h1 = """<div style="background:#00A651;padding:18px;border-radius:0 0 25px 25px;color:white;text-align:center"><b style="font-size:28px">ROW ECONOMY</b><p>Nigeria Sweetest Market</p></div>"""
st.markdown(h1, unsafe_allow_html=True)

q=st.text_input("Ask", placeholder="Ask Mama Oloja - What are you looking for?")
if q:
    qq=q.lower()
    if "car" in qq or "ac" in qq or "cool" in qq:
        st.success("Mama found: Horlance Auto Cooling - Car AC Repair - Osun & Oyo")
    elif "rice" in qq:
        st.success("Mama found: Mama T - Bag of Rice - N45000 - Abuja")
    elif "perfume" in qq or "cloth" in qq or "phone" in qq or "food" in qq:
        st.success("Mama found: Check Categories below for "+q)
    else:
        st.info("Mama dey find: "+q+" - No seller yet, be the first to post it below!")

st.markdown("### Categories")
cat = """<div style="display:flex;flex-wrap:wrap;gap:8px;text-align:center;font-size:13px">
<div style="width:23%"><div style="background:#FDE7F3;padding:14px;border-radius:18px">🧴</div>Perfume</div>
<div style="width:23%"><div style="background:#E0F2FE;padding:14px;border-radius:18px">👕</div>Clothes</div>
<div style="width:23%"><div style="background:#DBEAFE;padding:14px;border-radius:18px">📱</div>Phones</div>
<div style="width:23%"><div style="background:#FEF3C7;padding:14px;border-radius:18px">🍲</div>Food</div>
<div style="width:23%"><div style="background:#FFEDD5;padding:14px;border-radius:18px">🚗</div>Car Mart</div>
<div style="width:23%"><div style="background:#DCFCE7;padding:14px;border-radius:18px">💼</div>Services</div>
<div style="width:23%"><div style="background:#FCE7F3;padding:14px;border-radius:18px">🎟️</div>Tickets</div>
<div style="width:23%"><div style="background:#DCFCE7;padding:14px;border-radius:18px">💬</div>Chat Rooms</div>
</div>"""
st.markdown(cat, unsafe_allow_html=True)

choice=st.selectbox("Tap to Choose Category - It Will Work Now", ["All","Perfume","Clothes","Phones","Food","Car Mart","Services","Tickets","Chat Rooms"])
st.session_state.cat=choice
if choice!="All":
    st.success("Showing: "+choice)
    if choice=="Car Mart":
        st.info("Horlance Auto Cooling Ltd - Car AC Repair - See below")
    elif choice=="Food":
        st.info("Mama T - Bag of Rice - N45000 - See below")
    else:
        st.info("No seller yet for "+choice+" - Post it FREE below and be first!")

if st.session_state.page=="Profile":
    st.markdown("### Profile")
    st.info("Your Profile - ROW ECONOMY")
    st.write("Name: Guest User")
    st.write("Location: Nigeria")
    st.write("You have posted: "+str(len(st.session_state.goods))+" goods")
    if st.button("Back to Home"):
        st.session_state.page="Home"
        st.rerun()

elif st.session_state.page=="Orders":
    st.markdown("### Orders")
    if len(st.session_state.goods)==0:
        st.info("No orders yet. Post your goods below!")
    else:
        for g in st.session_state.goods:
            st.success("Order: "+g)

elif st.session_state.page=="Shop":
    st.markdown("### Shop - All Goods")
    st.success("Horlance Auto Cooling - Car AC Repair - N25000")
    st.success("Mama T - Bag of Rice - N45000")
    for g in st.session_state.goods:
        st.success(g)

else:
    st
