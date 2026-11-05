import streamlit as st
st.set_page_config(page_title="Row Economy")
if "goods" not in st.session_state:
    st.session_state.goods=[]
if "page" not in st.session_state:
    st.session_state.page="Home"

def to_wa(num):
    n="".join([c for c in num if c.isdigit()])
    if len(n)==11 and n.startswith("0"):
        return "234"+n[1:]
    if len(n)==10:
        return "234"+n
    return n

top = """<div style="background:#00A651;padding:18px;border-radius:0 0 25px 25px;color:white;text-align:center"><b style="font-size:28px">ROW ECONOMY</b><p>Nigeria Sweetest Market</p></div>"""
st.markdown(top, unsafe_allow_html=True)

q=st.text_input("Ask", placeholder="Ask Mama Oloja - What are you looking for?")
if q:
    qq=q.lower()
    if "car" in qq or "ac" in qq:
        st.success("Mama found: Horlance Auto Cooling - Car AC Repair")
    elif "rice" in qq:
        st.success("Mama found: Mama T - Bag of Rice - N45000")
    else:
        st.info("Mama dey find: "+q)

st.markdown("### Categories")
catbox = """<div style="display:flex;flex-wrap:wrap;gap:8px;text-align:center;font-size:13px">
<div style="width:23%"><div style="background:#FDE7F3;padding:14px;border-radius:18px">🧴</div>Perfume</div>
<div style="width:23%"><div style="background:#E0F2FE;padding:14px;border-radius:18px">👕</div>Clothes</div>
<div style="width:23%"><div style="background:#DBEAFE;padding:14px;border-radius:18px">📱</div>Phones</div>
<div style="width:23%"><div style="background:#FEF3C7;padding:14px;border-radius:18px">🍲</div>Food</div>
<div style="width:23%"><div style="background:#FFEDD5;padding:14px;border-radius:18px">🚗</div>Car Mart</div>
<div style="width:23%"><div style="background:#DCFCE7;padding:14px;border-radius:18px">💼</div>Services</div>
<div style="width:23%"><div style="background:#FCE7F3;padding:14px;border-radius:18px">🎟️</div>Tickets</div>
<div style="width:23%"><div style="background:#DCFCE7;padding:14px;border-radius:18px">💬</div>Chat Rooms</div>
</div>"""
st.markdown(catbox, unsafe_allow_html=True)

choice=st.selectbox("Tap Category", ["All","Perfume","Clothes","Phones","Food","Car Mart","Services","Tickets","Chat Rooms"])
if choice!="All":
    st.success("Showing: "+choice)
    if choice=="Car Mart":
        st.info("Horlance Auto Cooling - Car AC Repair below")
    elif choice=="Food":
        st.info("Mama T - Bag of Rice - N45000 below")
    else:
        st.info("No seller yet for "+choice+" - Post FREE below!")

if st.session_state.page=="Profile":
    st.markdown("### Profile")
    st.write("Name: Guest User")
    st.write("Posted goods: "+str(len(st.session_state.goods)))
elif st.session_state.page=="Orders":
    st.markdown("### Orders")
    if len(st.session_state.goods)==0:
        st.info("No orders yet")
    else:
        for item in st.session_state.goods:
            st.success(item[0])
            st.link_button("Chat Seller on WhatsApp", "https://wa.me/"+item[1])
elif st.session_state.page=="Shop":
    st.markdown("### Shop - All Goods")
    st.success("Horlance - Car AC Repair - N25000")
    st.link_button("Chat Horlance on WhatsApp", "https://wa.me/2349046044472")
    st.success("Mama T - Bag of Rice - N45000")
    st.link_button("Chat Mama T on WhatsApp", "https://wa.me/2349046044472")
    for item in st.session_state.goods:
        st.success(item[0])
        st.link_button("Chat Seller on WhatsApp", "https://wa.me/"+item[1])
else:
    st.markdown("### Featured Listing")
    card1 = """<div style="background:white;padding:16px;border-radius:20px;box-shadow:0 4px 16px #EDEDED"><span style="background:#00A651;color:white;padding:4px 10px;border-radius:20px;float:right">VERIFIED</span><b>Horlance Auto Cooling Ltd</b><p>🔧 Car AC Repair</p><p>📍 Osun & Oyo State</p><p>💬 WhatsApp 09046044472</p><p style="font-size:50px;text-align:center">🚗❄️</p><a href="https://wa.me/2349046044472" style="display:block;background:#00A651;color:white;text-align:center;padding:12px;border-radius:12px;text-decoration:none"><b>Chat on WhatsApp</b></a></div>"""
    st.markdown(card1, unsafe_allow_html=True)
    mama = """<div style="display:flex;gap:8px;margin-top:12px"><div style="text-align:center">👩🏾<br><span style="font-size:10px">Mama Oloja AI</span></div><div style="background:#D1FAE5;padding:12px;border-radius:18px;flex:1">Welcome my dear, I can help you find the best price in the market. <span style="float:right;font-size:11px">🕐 now</span></div></div>"""
    st.markdown(mama, unsafe_allow_html=True)
    card2 = """<div style="background:white;padding:16px;border-radius:20px;box-shadow:0 4px 16px #EDEDED"><b>Mama T</b><p>Bag of Rice - <b>N45000</b></p><p>Abuja - 09046044472</p><p>Pay: <b>Transfer Before Delivery</b></p><p>Delivery: <b>Pickup Only</b></p></div>"""
    st.markdown(card2, unsafe_allow_html=True)
    st.link_button("Chat Mama T", "https://wa.me/2349046044472")
    st.markdown("### New Goods")
    for item in st.session_state.goods:
        st.success(item[0])
        st.link_button("Chat Seller on WhatsApp", "https://wa.me/"+item[1])

st.markdown("### Sell - FREE")
nm=st.text_input("Your Name")
pd=st.text_input("Product Name")
pr=st.text_input("Price")
wa=st.text_input("Your WhatsApp Number", placeholder="e.g. 09046044472")
pay=st.selectbox("Payment", ["Pay on Delivery","Transfer Before Delivery"])
dlv=st.selectbox("Delivery", ["Pickup Only","Delivery Available"])
if st.button("POST MY GOODS FOR FREE"):
    if nm=="" or pd=="" or wa=="":
        st.warning("Fill Name, Product and WhatsApp Number first")
    else:
        txt=nm+" - "+pd+" - N"+pr+" - WhatsApp "+wa+" - "+pay+" - "+dlv
        st.session_state.goods.append((txt, to_wa(wa)))
        st.success("Posted! "+txt)
        st.balloons()

st.markdown("### Menu - Tap to Work")
nav1,nav2,nav3,nav4=st.columns(4)
with nav1:
    if st.button("Home"):
        st.session_state.page="Home"
        st.rerun()
with nav2:
    if st.button("Shop"):
        st.session_state.page="Shop"
        st.rerun()
with nav3:
    if st.button("Orders"):
        st.session_state.page="Orders"
        st.rerun()
with nav4:
    if st.button("Profile"):
        st.session_state.page="Profile"
        st.rerun()
