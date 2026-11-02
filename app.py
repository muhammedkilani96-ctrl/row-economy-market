import streamlit as st
import urllib.parse

st.set_page_config(page_title="ROW ECONOMY - Everything Market", page_icon="🛒", layout="wide")

# THEME
st.markdown("""
<style>
.stButton>button {background: #16a34a; color: white; border-radius: 8px; width: 100%; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

# INIT DATA
if "products" not in st.session_state:
    st.session_state.products = [
        {"name": "iPhone 12 UK Used 128GB", "price": "₦250,000", "loc": "Ogbomoso", "cat": "Phones", "phone": "2348100000000", "desc":"Neat, BH 89%"},
        {"name": "Mama Gold Rice 50kg", "price": "₦75,000", "loc": "Ilorin", "cat": "Groceries", "phone": "2348100000000", "desc":"Stone free"},
        {"name": "Toyota Corolla 2010", "price": "₦3,200,000", "loc": "Abuja", "cat": "Vehicles", "phone": "2348100000000", "desc":"First body"},
    ]
if "requests" not in st.session_state:
    st.session_state.requests = []

# HEADER
st.title("🛒 ROW ECONOMY")
st.caption("Everything Market - Ogbomoso | Ilorin | Abuja | Nationwide")

tab1, tab2 = st.tabs(["🛒 MARKET - Buy Anything", "🙏 REQUESTS - I Need Something"])

# === TAB 1: MARKET + SELL FORM ===
with tab1:
    with st.expander("➕ SELL YOUR PRODUCT - Click to Post (FREE)", expanded=False):
        with st.form("sell_form", clear_on_submit=True):
            s_name = st.text_input("Product Name *", placeholder="e.g. iPhone 11 64GB Neat")
            c1, c2 = st.columns(2)
            with c1:
                s_price = st.text_input("Price *", placeholder="₦150,000")
            with c2:
                s_cat = st.selectbox("Category", ["Phones","Groceries","Vehicles","Fashion","Electronics","Others"])
            c3, c4 = st.columns(2)
            with c3:
                s_loc = st.selectbox("Location", ["Ogbomoso","Ilorin","Abuja","Nationwide"])
            with c4:
                s_phone = st.text_input("Your WhatsApp Number *", placeholder="08012345678")
            s_desc = st.text_area("Description", placeholder="Condition, size, etc...")
            s_img = st.file_uploader("Product Picture (optional)", type=['jpg','png','jpeg'])
            
            if st.form_submit_button("🚀 Post to Market"):
                if s_name and s_price and s_phone:
                    clean = ''.join(filter(str.isdigit, s_phone))
                    if clean.startswith('0'): clean = '234' + clean[1:]
                    st.session_state.products.append({
                        "name": s_name, "price": s_price, "loc": s_loc, 
                        "cat": s_cat, "phone": clean, "desc": s_desc
                    })
                    st.success(f"✅ {s_name} posted! Buyers will see it now.")
                    st.balloons()
                else:
                    st.error("Fill Name, Price, and WhatsApp!")

    st.divider()
    # FILTERS
    f1, f2, f3 = st.columns(3)
    with f1:
        search = st.text_input("🔍 Search product", placeholder="iPhone, Rice, Car...")
    with f2:
        loc_filter = st.selectbox("📍 Filter by Location", ["All", "Ogbomoso", "Ilorin", "Abuja", "Nationwide"])
    with f3:
        cat_filter = st.selectbox("📦 Filter by Category", ["All", "Phones", "Groceries", "Vehicles", "Fashion", "Electronics", "Others"])

    # SHOW PRODUCTS
    filtered = [p for p in st.session_state.products if 
                (loc_filter=="All" or p["loc"]==loc_filter) and
                (cat_filter=="All" or p["cat"]==cat_filter) and
                (search.lower() in p["name"].lower() or search=="")]
    
    st.write(f"**{len(filtered)} products found**")
    for p in reversed(filtered):
        with st.container(border=True):
            ca, cb = st.columns([3,1])
            with ca:
                st.write(f"**{p['name']}**")
                st.write(f"💰 {p['price']} | 📍 {p['loc']} | 📦 {p['cat']}")
                if p.get('desc'): st.caption(p['desc'])
            with cb:
                msg = urllib.parse.quote(f"Hello, I saw {p['name']} for {p['price']} on ROW ECONOMY. Is it available?")
                wa_link = f"https://wa.me/{p['phone']}?text={msg}"
                st.link_button("💬 Buy via WhatsApp", wa_link)

# === TAB 2: REQUEST SPACE ===
with tab2:
    st.subheader("🙏 Request Space")
    st.info("No see what you want? Post your need here!")
    with st.form("request_form", clear_on_submit=True):
        r_item = st.text_input("What do you need? *", placeholder="e.g. iPhone 11 64GB")
        rb1, rb2 = st.columns(2)
        with rb1:
            r_budget = st.text_input("Budget", placeholder="₦150k - 180k")
        with rb2:
            r_loc = st.selectbox("Your Location", ["Ogbomoso","Ilorin","Abuja","Nationwide"])
        r_phone = st.text_input("Your WhatsApp Number *", placeholder="08012345678")
        r_desc = st.text_area("More details")
        if st.form_submit_button("📢 Post My Request"):
            if r_item and r_phone:
                clean = ''.join(filter(str.isdigit, r_phone))
                if clean.startswith('0'): clean = '234' + clean[1:]
                st.session_state.requests.append({
                    "item": r_item, "budget": r_budget, "loc": r_loc, "phone": clean, "desc": r_desc, "raw_phone": r_phone
                })
                st.success("✅ Request Posted!")
            else:
                st.error("Fill item and phone")

    st.divider()
    for req in reversed(st.session_state.requests):
        with st.container(border=True):
            st.write(f"**NEED: {req['item']}** - 💰 {req['budget']} | 📍 {req['loc']}")
            if req['desc']: st.write(req['desc'])
            msg = urllib.parse.quote(f"Hello, I saw your request for {req['item']} on ROW ECONOMY. I have it!")
            st.link_button(f"✅ I Have It - Chat {req['raw_phone']}", f"https://wa.me/{req['phone']}?text={msg}")

st.caption("ROW ECONOMY © 2026 - Built by Muhammed at 3% battery 🔋")
