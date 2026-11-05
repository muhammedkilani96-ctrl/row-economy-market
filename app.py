import streamlit as st, urllib.parse as u
st.set_page_config(page_title="Row Economy", layout="wide")
st.markdown("<style>header{visibility:hidden} .block-container{padding:0!important} .stApp{background:white}</style>", unsafe_allow_html=True)
if "g" not in st.session_state:
    st.session_state.g=["Horlance Auto Cooling Ltd|Car AC Repair|25000|Osun & Oyo State|09046044472|Car Mart|YES","Mama T|Bag of Rice|45000|Abuja|09046044472|Food|YES"]
cat_now=st.query_params.get("cat","All")
st.markdown("<div style='background:#00A651;padding:16px 14px 28px;border-radius:0 0 28px 28px;color:white;display:flex;justify-content:space-between;align-items:center'><span>☰</span><b style='font-size:25px'>ROW ECONOMY</b><span style='background:#FF8A00;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center'>👤</span></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#00A651;font-weight:bold'>Nigeria Sweetest Market</p>", unsafe_allow_html=True)
search=st.text_input("S", placeholder="Ask Mama Oloja - What are you looking for?", label_visibility="collapsed")
st.markdown("<div style='display:flex;justify-content:space-between;padding:10px 14px'><b>Categories</b><a href='?cat=All' style='color:#00A651;text-decoration:none'>See all ></a></div>", unsafe_allow_html=True)
st.markdown("<div style='display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px;padding:0 14px'><a href='?cat=Perfume' style='text-decoration:none'><div style='background:#FFE4F1;border-radius:16px;padding:14px;text-align:center;font-size:28px'>🧴</div><p style='text-align:center;color:#111;font-size:13px'>Perfume</p></a><a href='?cat=Clothes' style='text-decoration:none'><div style='background:#D6EAF8;border-radius:16px;padding:14px;text-align:center;font-size:28px'>👕</div><p style='text-align:center;color:#111;font-size:13px'>Clothes</p></a><a href='?cat=Phones' style='text-decoration:none'><div style='background:#D6EAF8;border-radius:16px;padding:14px;text-align:center;font-size:28px'>📱</div><p style='text-align:center;color:#111;font-size:13px'>Phones</p></a><a href='?cat=Food' style='text-decoration:none'><div style='background:#FFE8CC;border-radius:16px;padding:14px;text-align:center;font-size:28px'>🍲</div><p style='text-align:center;color:#111;font-size:13px'>Food</p></a></div>", unsafe_allow_html=True)
st.markdown("<div style='display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px;padding:10px 14px'><a href='?cat=Car Mart' style='text-decoration:none'><div style='background:#FFE8CC;border-radius:16px;padding:14px;text-align:center;font-size:28px'>🚗</div><p style='text-align:center;color:#111;font-size:13px'>Car Mart</p></a><a href='?cat=Services' style='text-decoration:none'><div style='background:#D5F5E3;border-radius:16px;padding:14px;text-align:center;font-size:28px'>💼</div><p style='text-align:center;color:#111;font-size:13px'>Services</p></a><a href='?cat=Tickets' style='text-decoration:none'><div style='background:#FADBD8;border-radius:16px;padding:14px;text-align:center;font-size:28px'>🎟️</div><p style='text-align:center;color:#111;font-size:13px'>Tickets</p></a><a href='?cat=Chat Rooms' style='text-decoration:none'><div style='background:#D5F5E3;border-radius:16px;padding:14px;text-align:center;font-size:28px'>💬</div><p style='text-align:center;color:#111;font-size:13px'>Chat Rooms</p></a></div>", unsafe_allow_html=True)
st.markdown("<div style='display:flex;justify-content:space-between;padding:8px 14px'><b>Featured Listing</b><span style='color:#00A651'>See all ></span></div>", unsafe_allow_html=True)
all_goods=st.session_state.g
for line in all_goods:
    p=line.split("|")
    seller,name,price,loc,wa,cat,ver=p[0],p[1],p[2],p[3],p[4],p[5],p[6]
    skip=False
    if cat_now!="All" and cat!=cat_now:
        skip=True
    if search and search.lower() not in name.lower():
        skip=True
    if skip:
        continue
    msg=u.quote("Hello "+seller+", I saw your "+name)
    link="https://wa.me/234"+wa[1:]+"?text="+msg
    img="https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=400"
    if "AC" not in name:
        img="https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400"
    card="<div style='background:white;margin:0 14px 16px;padding:16px;border-radius:20px;box-shadow:0 4px 16px #EDEDED'>"
    card+="<div style='text-align:right'><span style='background:#00A651;color:white;padding:5px 12px;border-radius:20px;font-size:12px'>VERIFIED</span></div>"
    card+="<div style='display:flex;gap:12px'><div style='flex:1'><b>"+seller+"</b><p>Product: "+name+" - <b style='color:#00A651'>N"+price+"</b></p><p>Location: "+loc+"</p><p>WhatsApp: "+wa+"</p></div>"
    card+="<img src='"+img+"' style='width:140px;height:130px;object-fit:cover;border-radius:14px'></div>"
    card+="<a href='"+link+"' style='display:block;background:#00A651;color:white;text-align:center;padding:12px;border-radius:14px;text-decoration:none;font-weight:bold;margin-top:12px'>Chat on WhatsApp</a></div>"
    st.markdown(card, unsafe_allow_html=True)
st.markdown("<div style='display:flex;gap:8px;padding:0 14px'><div style='text-align:center'><div style='font-size:36px'>👩🏾</div><span style='background:#00A651;color:white;font-size:10px;padding:3px 7px;border-radius:10px'>Mama Oloja AI</span></div><div style='background:#D5F5E3;border-radius:18px;padding:12px;flex:1'>Welcome my dear, I can help you find the best price in the market.</div></div>", unsafe_allow_html=True)
q=st.text_input("Ask Mama", placeholder="Ask Mama Oloja...", label_visibility="collapsed")
if q:
    st.success("Mama Oloja: I found "+q+" for you above.")
st.markdown("<div style='padding:16px'><b>Sell - FREE for First 10</b><br>1 Name 2 WhatsApp 3 Location 4 Pictures 5 Price</div>", unsafe_allow_html=True)
with st.form("f"):
    n1=st.text_input("1. Your Name")
    n2=st.text_input("2. WhatsApp")
    n3=st.selectbox("3. Location", ["Abuja","Osun & Oyo State","Ogbomoso","Ilorin","Lagos"])
    n4=st.selectbox("Category", ["Food","Phones","Clothes","Perfume","Car Mart","Services","Tickets","Chat Rooms"])
    n5=st.text_input("5. Product Name")
    n6=st.text_input("5. Price - e.g. 25000")
    pic=st.file_uploader("4. Upload Picture", type=["jpg","png"])
    if pic:
        st.image(pic)
    go=st.form_submit_button("POST MY GOODS FOR FREE")
    if go:
        if n1=="" or n2=="":
            st.error("Fill Name and WhatsApp")
        elif n5=="":
            st.error("Fill Product Name")
        else:
            new=n1+"|"+n5+"|"+n6+"|"+n3+"|"+n2+"|"+n4+"|NO"
            st.session_state.g.append(new)
            st.success("Done! Your goods are LIVE!")
            st.balloons()
            st.rerun()
st.markdown("<div style='background:white;display:flex;justify-content:space-around;padding:12px;border-top:1px solid #eee'><span>Home</span><span>Shop</span><span>Orders</span><span>Profile</span></div>", unsafe_allow_html=True)
