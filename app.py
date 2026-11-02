import streamlit as st
import urllib.parse

st.set_page_config(page_title="ROW ECONOMY Market", page_icon="🛒", layout="wide")

if 'products' not in st.session_state:
    st.session_state.products = [
        {"name":"iPhone 12 UK Used","price":250000,"location":"Ogbomoso","category":"Phones","vendor":"Muhammed","phone":"2348012345678","desc":"Neat UK used, battery 92%"},
        {"name":"Rice 50kg Bag","price":55000,"location":"Ilorin","category":"Food","vendor":"Alhaja","phone":"2348012345678","desc":"Mama Gold, clean"},
        {"name":"Benz GLK 2010","price":4500000,"location":"Abuja","category":"Cars","vendor":"Kelly","phone":"2348012345678","desc":"Registered, full option"},
    ]

st.title("🛒 ROW ECONOMY - Everything Market")
st.caption("Buy & Sell Anything - Ogbomoso | Ilorin | Abuja | Nationwide")

with st.sidebar:
    st.header("➕ Sell Something")
    with st.form("sell"):
        name = st.text_input("Product Name")
        price = st.number_input("Price (₦)", min_value=0)
        location = st.selectbox("Location", ["Ogbomoso","Ilorin","Abuja","Lagos","Others"])
        category = st.selectbox("Category", ["Phones","Food","Cars","Fashion","Electronics","Property","Others"])
        vendor = st.text_input("Your Name")
        phone = st.text_input("WhatsApp Number (234...)")
        desc = st.text_area("Description")
        submit = st.form_submit_button("Post Product")
        if submit and name and price:
            st.session_state.products.insert(0, {"name":name,"price":price,"location":location,"category":category,"vendor":vendor,"phone":phone,"desc":desc})
            st.success(f"{name} posted!")

col1, col2, col3 = st.columns(3)
with col1:
    search = st.text_input("🔍 Search product")
with col2:
    loc_filter = st.selectbox("📍 Filter by Location", ["All","Ogbomoso","Ilorin","Abuja","Lagos","Others"])
with col3:
    cat_filter = st.selectbox("📦 Filter by Category", ["All","Phones","Food","Cars","Fashion","Electronics","Property","Others"])

filtered = st.session_state.products
if search:
    filtered = [p for p in filtered if search.lower() in p['name'].lower()]
if loc_filter != "All":
    filtered = [p for p in filtered if p['location'] == loc_filter]
if cat_filter != "All":
    filtered = [p for p in filtered if p['category'] == cat_filter]

st.write(f"**{len(filtered)} Products Found**")

cols = st.columns(3)
for i, p in enumerate(filtered):
    with cols[i % 3]:
        st.markdown(f"**{p['name']}**\n💰 ₦{p['price']:,} | 📍 {p['location']} | 👤 {p['vendor']}")
        msg = f"Hello {p['vendor']}, I want to buy {p['name']} for ₦{p['price']:,} on ROW ECONOMY. Location: {p['location']}"
        wa_link = f"https://wa.me/{p['phone']}?text={urllib.parse.quote(msg)}"
        st.link_button(f"💬 Buy {p['name']}", wa_link)
        st.divider()
