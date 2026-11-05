import streamlit as st
st.set_page_config(page_title="Row Economy")
if "goods" not in st.session_state:
    st.session_state.goods=[]
h1 = """<div style="background:#00A651;padding:18px;border-radius:0 0 25px 25px;color:white;text-align:center"><b style="font-size:28px">ROW ECONOMY</b><p>Nigeria Sweetest Market</p></div>"""
st.markdown(h1, unsafe_allow_html=True)
q=st.text_input("Ask", placeholder="Ask Mama Oloja - What are you looking for?")
if q:
    st.info("Mama dey find: "+q)
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
st.markdown("### Featured Listing")
f1 = """<div style="background:white;padding:16px;border-radius:20px;box-shadow:0 4px 16px #EDEDED"><span style="background:#00A651;color:white;padding:4px 10px;border-radius:20px;float:right">VERIFIED</span><b>Horlance Auto Cooling Ltd</b><p>🔧 Car AC Repair</p><p>📍 Osun & Oyo State</p><p>💬 WhatsApp 09046044472</p><p style="font-size:50px;text-align:center">🚗❄️</p><a href="https://wa.me/2349046044472" style="display:block;background:#00A651;color:white;text-align:center;padding:12px;border-radius:12px;text-decoration:none"><b>Chat on WhatsApp</b></a></div>"""
st.markdown(f1, unsafe_allow_html=True)
m1 = """<div style="display:flex;gap:8px;margin-top:12px"><div style="text-align:center">👩🏾<br><span style="font-size:10px">Mama Oloja AI</span></div><div style="background:#D1FAE5;padding:12px;border-radius:18px;flex:1">Welcome my dear, I can help you find the best price in the market. <span style="float:right;font-size:11px">🕐 now</span></div></div>"""
st.markdown(m1, unsafe_allow_html=True)
c2 = """<div style="background:white;padding:16px;border-radius:20px;box-shadow:0 4px 16px #EDEDED"><b>Mama T</b><p>Bag of Rice - <b>N45000</b></p><p>Abuja - 09046044472</p><p>Pay: <b>Transfer Before Delivery</b></p><p>Delivery: <b>Pickup Only</b></p></div>"""
st.markdown(c2, unsafe_allow_html=True)
st.link_button("Chat Mama T", "https://wa.me/2349046044472")
st.markdown("### New Goods")
for g in st.session_state.goods:
    st.success(g)
st.markdown("### Sell - FREE")
n1=st.text_input("Your Name")
n5=st.text_input("Product Name")
n6=st.text_input("Price")
n7=st.selectbox("Payment", ["Pay on Delivery","Transfer Before Delivery"])
n8=st.selectbox("Delivery", ["Pickup Only","Delivery Available"])
if st.button("POST MY GOODS FOR FREE"):
    if n1=="" or n5=="":
        st.warning("Fill Name and Product first")
    else:
        txt=n1+" - "+n5+" - N"+n6
        st.session_state.goods.append(txt)
        st.success("Posted! "+txt)
        st.balloons()
b1 = """<div style="background:white;padding:12px;border-radius:20px 20px 0 0;box-shadow:0 -2px 10px #EDEDED;display:flex;text-align:center"><div style="flex:1;color:#00A651">🏠<br><b>Home</b></div><div style="flex:1;color:grey">🏪<br>Shop</div><div style="flex:1;color:grey">📋<br>Orders</div><div style="flex:1;color:grey">👤<br>Profile</div></div>"""
st.markdown(b1, unsafe_allow_html=True)
