import streamlit as st
import urllib.parse

st.set_page_config(page_title="ROW ECONOMY - Everything Market", page_icon="🛒", layout="wide")

st.markdown("""
<style>
.main {background: #f8fff8;}
.stButton>button {background: #16a34a; color: white; border-radius: 8px; width: 100%;}
</style>
""", unsafe_allow_html=True)

# HEADER
col1, col2 = st.columns([1,5])
with col1:
    st.markdown("## 🛒")
with col2:
    st.title("ROW ECONOMY")
    st.caption("Everything Market - Ogbomoso | Ilorin | Abuja | Nationwide")

# SESSION STATE FOR REQUESTS
if "requests" not in st.session_state:
    st.session_state.requests = []

tab1, tab2 = st.tabs(["🛒 MARKET - Buy Anything", "🙏 REQUESTS - I Need Something"])

# === TAB 1: MARKET ===
with tab1:
    st.subheader("🛒 Everything Market")
    
    # Filters from your screenshot
    c1, c2, c3 = st.columns(3)
    with c1:
        search = st.text_input("🔍 Search product", placeholder="iPhone, Rice, Car...")
    with c2:
        loc_filter = st.selectbox("📍 Filter by Location", ["All", "Ogbomoso", "Ilorin", "Abuja", "Nationwide"])
    with c3:
        cat_filter = st.selectbox("📦 Filter by Category", ["All", "Phones", "Groceries", "Vehicles", "Fashion", "Others"])

    # Sample products
    products = [
        {"name": "iPhone 12 UK Used 128GB", "price": "₦250,000", "loc": "Ogbomoso", "cat": "Phones", "phone": "2348100000000"},
        {"name": "Mama Gold Rice 50kg", "price": "₦75,000", "loc": "Ilorin", "cat": "Groceries", "phone": "2348100000000"},
        {"name": "Toyota Corolla 2010", "price": "₦3,200,000", "loc": "Abuja", "cat": "Vehicles", "phone": "2348100000000"},
    ]

    for p in products:
        if (loc_filter == "All" or p["loc"] == loc_filter) and (cat_filter == "All" or p["cat"] == cat_filter) and (search.lower() in p["name"].lower() or search == ""):
            with st.container(border=True):
                col_a, col_b = st.columns([3,1])
                with col_a:
                    st.write(f"**{p['name']}**")
                    st.write(f"{p['price']} | 📍 {p['loc']} | {p['cat']}")
                with col_b:
                    msg = urllib.parse.quote(f"Hello, I saw {p['name']} for {p['price']} on ROW ECONOMY")
                    wa_link = f"https://wa.me/{p['phone']}?text={msg}"
                    st.link_button("💬 Buy via WhatsApp", wa_link)

# === TAB 2: REQUEST SPACE ===
with tab2:
    st.subheader("🙏 Request Space - Tell us what you need")
    st.info("No see wetin you dey find? Post your need, sellers go contact you!")

    with st.form("request_form", clear_on_submit=True):
        r_item = st.text_input("What do you need? *", placeholder="e.g. iPhone 11 64GB, Shop for rent in Ogbomoso")
        r_budget = st.text_input("Your Budget", placeholder="e.g. ₦150k - 180k")
        r_loc = st.selectbox("Your Location", ["Ogbomoso", "Ilorin", "Abuja", "Nationwide", "Other"])
        r_phone = st.text_input("Your WhatsApp Number *", placeholder="08012345678")
        r_desc = st.text_area("More details", placeholder="Describe exactly what you want...")
        submitted = st.form_submit_button("📢 Post My Request")

        if submitted:
            if r_item and r_phone:
                st.session_state.requests.append({
                    "item": r_item, "budget": r_budget, "loc": r_loc, "phone": r_phone, "desc": r_desc
                })
                st.success("✅ Request Posted! Sellers will chat you on WhatsApp.")
                st.balloons()
            else:
                st.error("Please fill item and WhatsApp number")

    st.divider()
    st.write(f"### 📋 Live Requests ({len(st.session_state.requests)})")
    
    if not st.session_state.requests:
        st.caption("No requests yet. Be the first to post!")
    else:
        for req in reversed(st.session_state.requests):
            with st.container(border=True):
                st.write(f"**NEED: {req['item']}**")
                st.write(f"💰 Budget: {req['budget']} | 📍 {req['loc']}")
                if req['desc']:
                    st.write(f"📝 {req['desc']}")
                clean_phone = ''.join(filter(str.isdigit, req['phone']))
                if clean_phone.startswith('0'):
                    clean_phone = '234' + clean_phone[1:]
                msg = urllib.parse.quote(f"Hello, I saw your request for {req['item']} on ROW ECONOMY. I have it!")
                wa_link = f"https://wa.me/{clean_phone}?text={msg}"
                st.link_button(f"✅ I Have This - Chat {req['phone']}", wa_link)

st.divider()
st.caption("ROW ECONOMY © 2026 - Buy & Sell Anything, Request Anything")
