import streamlit as st
import urllib.parse as u
import requests, json
st.set_page_config(page_title="Row Economy", layout="wide")
BUCKET="SzHmbyQQ1X1ns5LY4Qi8u9"
KV="https://kvdb.io/"+BUCKET+"/goods"
DEFAULT=[]
DEFAULT.append("Horlance Auto Cooling Ltd|Car AC Repair|25000|Osun & Oyo State|09046044472|Car Mart|YES")
DEFAULT.append("Mama T|Bag of Rice|45000|Abuja|09046044472|Food|YES")
def load_goods():
    try:
        r=requests.get(KV, timeout=5)
        if r.status_code==200 and len(r.text)>2:
            d=json.loads(r.text)
            if isinstance(d, list) and len(d)>0:
                return d
    except:
        pass
    return DEFAULT.copy()
def save_goods(data):
    try:
        requests.post(KV, data=json.dumps(data), timeout=5)
    except:
        pass
if "g" not in st.session_state:
    st.session_state.g=load_goods()
if "orders" not in st.session_state:
    st.session_state.orders=[]
page=st.query_params.get("page","Home")
cat_now=st.query_params.get("cat","All")
st.success("ROW ECONOMY - Nigeria Sweetest Market")
st.write("Page: "+page+" - SAVED FOREVER")
def show_card(line):
    p=line.split("|")
    seller=p[0]
    name=p[1]
    price=p[2]
    loc=p[3]
    wa=p[4]
    st.write("---")
    st.write("**"+seller+"** - VERIFIED")
    st.write("Product: "+name+" - **N"+price+"**")
    st.write("Location: "+loc+" | WhatsApp: "+wa)
    msg=u.quote("Hello "+seller+", I want "+name+" for N"+price)
    link="https://wa.me/234"+wa[1:]+"?text="+msg
    st.link_button("Chat on WhatsApp", link)
if page=="Shop":
    st.subheader("Shop - All Goods")
    s2=st.text_input("Search Shop", placeholder="Rice, AC...")
    for line in st.session_state.g:
        if s2=="" or s2.lower() in line.lower():
            show_card(line)
elif page=="Orders":
    st.subheader("My Orders")
    st.info("Orders are tracked on WhatsApp with seller.")
    if len(st.session_state.orders)==0:
        st.write("No orders yet. Go to Shop and order.")
    for o in st.session_state.orders:
        st.success(o)
    if st.button("I Made An Order"):
        st.session_state.orders.append("Order - Chat on WhatsApp")
        st.rerun()
elif page=="Profile":
    st.subheader("My Profile")
    pname=st.text_input("Your Name", value="Text seller")
    pwa=st.text_input("Your WhatsApp", value="09046044472")
    ploc=st.selectbox("Your Location", ["Abuja","Osun & Oyo State","Ogbomoso","Ilorin","Lagos"])
    if st.button("Save My Profile"):
        st.success("Saved! "+pname+" - "+ploc)
    st.write("My Listings:")
    for line in st.session_state.g:
        if pname.lower() in line.lower():
            show_card(line)
    st.write("Admin Help: WhatsApp 09046044472")
else:
    search=st.text_input("Search", placeholder="Ask Mama Oloja - What are you looking for?")
    st.subheader("Categories - Showing: "+cat_now)
    c1,c2,c3,c4=st.columns(4)
    with c1:
        st.link_button("Perfume", "?cat=Perfume&page=Home")
    with c2:
        st.link_button("Clothes", "?cat=Clothes&page=Home")
    with c3:
        st.link_button("Phones", "?cat=Phones&page=Home")
    with c4:
        st.link_button("Food", "?cat=Food&page=Home")
    d1,d2,d3,d4=st.columns(4)
    with d1:
        st.link_button("Car Mart", "?cat=Car Mart&page=Home")
    with d2:
        st.link_button("Services", "?cat=Services&page=Home")
    with d3:
        st.link_button("Tickets", "?cat=Tickets&page=Home")
    with d4:
        st.link_button("Chat Rooms", "?cat=Chat Rooms&page=Home")
    st.subheader("Featured Listing")
    shown=[]
    for line in st.session_state.g:
        p=line.split("|")
        ok_cat=(cat_now=="All" or p[5]==cat_now)
        ok_s=(search=="" or search.lower() in line.lower())
        if ok_cat and ok_s:
            shown.append(line)
    if len(shown)==0:
        st.info("No goods in "+cat_now+" yet. Be first to post!")
    for line in shown:
        show_card(line)
    st.subheader("Mama Oloja AI")
    st.write("Welcome my dear, I help you find best price.")
    q=st.text_input("Ask Mama", placeholder="Ask Mama... e.g. Rice, AC")
    if q:
        found=[l for l in st.session_state.g if q.lower() in l.lower()]
        if len(found)>0:
            f=found[0].split("|")
            st.success("Mama: Yes! "+f[1]+" is N"+f[2]+" from "+f[0]+" in "+f[3])
        else:
            st.warning("Mama: Sorry, no "+q+" yet. Post it!")
    st.subheader("Sell - FREE for First 10")
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
                save_goods(st.session_state.g)
                st.success("Done! LIVE and SAVED FOREVER!")
                st.balloons()
                st.rerun()
st.write("---")
b1,b2,b3,b4=st.columns(4)
with b1:
    st.link_button("Home", "?page=Home")
with b2:
    st.link_button("Shop", "?page=Shop")
with b3:
    st.link_button("Orders", "?page=Orders")
with b4:
    st.link_button("Profile", "?page=Profile")
