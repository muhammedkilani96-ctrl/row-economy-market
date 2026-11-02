import streamlit as st
import urllib.parse

st.set_page_config(page_title="ROW ECONOMY - Everything", page_icon="🛒", layout="wide")

st.markdown("<style>.stButton>button{background:#16a34a;color:white;border-radius:8px;width:100%;font-weight:bold;}</style>", unsafe_allow_html=True)

if "products" not in st.session_state:
    st.session_state.products = [
        {"name": "iPhone 12 UK Used 128GB", "price": "₦250k", "loc": "Ogbomoso", "cat": "Phones", "phone": "2348100000000", "desc":"BH 89%"},
        {"name": "Mama Gold Rice 50kg", "price": "₦75k", "loc": "Ilorin", "cat": "Groceries", "phone": "2348100000000", "desc":"Stone free"},
    ]
if "requests" not in st.session_state:
    st.session_state.requests = []
if "services" not in st.session_state:
    st.session_state.services = [
        {"name":"Afeez Haircut Studio","skill":"Barber","price":"₦2k / cut","loc":"Ogbomoso","phone":"2348100000000","desc":"Home service available, LAUTECH area"},
        {"name":"Queens Beauty Salon","skill":"Hair Dresser","price":"₦5k / Braids","loc":"Ilorin","phone":"2348100000000","desc":"Braids, Wigs, Lashes"},
        {"name":"Baba T Painter","skill":"Painter","price":"₦15k / room","loc":"Abuja","phone":"2348100000000","desc":"House painting, POP, Screeding"},
    ]

st.title("🛒 ROW ECONOMY")
st.caption("Market + Services - Ogbomoso | Ilorin | Abuja | Nigeria")

tab1, tab2, tab3 = st.tabs(["🛒 MARKET", "🙏 REQUESTS", "✂️ SERVICES - Barber, Hair, Painter"])

# TAB 1 MARKET
with tab1:
    with st.expander("➕ SELL PRODUCT - Post FREE"):
        with st.form("sell", clear_on_submit=True):
            n = st.text_input("Product Name *")
            c1,c2 = st.columns(2)
            with c1: p = st.text_input("Price *")
            with c2: cat = st.selectbox("Category", ["Phones","Groceries","Vehicles","Fashion","Electronics","Others"])
            c3,c4 = st.columns(2)
            with c3: loc = st.selectbox("Location", ["Ogbomoso","Ilorin","Abuja","Nationwide"])
            with c4: ph = st.text_input("WhatsApp *", placeholder="080...")
            desc = st.text_area("Desc")
            if st.form_submit_button("🚀 Post Product"):
                if n and p and ph:
                    cl = ''.join(filter(str.isdigit, ph))
                    if cl.startswith('0'): cl='234'+cl[1:]
                    st.session_state.products.append({"name":n,"price":p,"loc":loc,"cat":cat,"phone":cl,"desc":desc})
                    st.success("Product posted!"); st.balloons()
    search = st.text_input("🔍 Search product")
    for prod in reversed(st.session_state.products):
        if search.lower() in prod['name'].lower():
            with st.container(border=True):
                st.write(f"**{prod['name']}** - {prod['price']} | {prod['loc']}")
                st.caption(prod['desc'])
                msg=urllib.parse.quote(f"Hello, I saw {prod['name']} on ROW ECONOMY")
                st.link_button("💬 Buy on WhatsApp", f"https://wa.me/{prod['phone']}?text={msg}")

# TAB 2 REQUESTS
with tab2:
    with st.form("req", clear_on_submit=True):
        item = st.text_input("What do you need? *")
        c1,c2 = st.columns(2)
        with c1: bud = st.text_input("Budget")
        with c2: loc = st.selectbox("Your Location", ["Ogbomoso","Ilorin","Abuja","Nationwide"])
        ph = st.text_input("Your WhatsApp *")
        if st.form_submit_button("📢 Post Request"):
            if item and ph:
                cl=''.join(filter(str.isdigit, ph))
                if cl.startswith('0'): cl='234'+cl[1:]
                st.session_state.requests.append({"item":item,"budget":bud,"loc":loc,"phone":cl,"raw":ph})
                st.success("Request posted!")
    for r in reversed(st.session_state.requests):
        with st.container(border=True):
            st.write(f"NEED: {r['item']} - {r['budget']} | {r['loc']}")
            msg=urllib.parse.quote(f"I have {r['item']} for you - ROW ECONOMY")
            st.link_button(f"✅ I Have It - {r['raw']}", f"https://wa.me/{r['phone']}?text={msg}")

# TAB 3 SERVICES - NEW!
with tab3:
    st.subheader("✂️ Find Artisans Near You")
    st.write("Barbers, Hairdressers, Painters, Fashion Designers...")

    with st.expander("➕ REGISTER YOUR SERVICE - Barber, Hairdresser, Painter, etc - FREE", expanded=True):
        with st.form("service_form", clear_on_submit=True):
            s_name = st.text_input("Your Business Name / Your Name *", placeholder="e.g. Afeez Barber Shop")
            c1,c2 = st.columns(2)
            with c1:
                s_skill = st.selectbox("What do you do? *", ["Barber - Hair Baba","Hair Dresser - Hair Plaiting","Painter","Fashion Designer - Tailor","Makeup Artist","Nail Tech","Others"])
            with c2:
                s_price = st.text_input("Price / Rate *", placeholder="e.g. ₦2k per cut, ₦10k per room")
            c3,c4 = st.columns(2)
            with c3:
                s_loc = st.selectbox("Your
