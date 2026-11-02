import streamlit as st
import urllib.parse

st.set_page_config(page_title="ROW ECONOMY", page_icon="shopping", layout="wide")

st.markdown("<style>.stButton>button{background:#16a34a;color:white;border-radius:8px;width:100%;font-weight:bold;}</style>", unsafe_allow_html=True)

if "products" not in st.session_state:
    st.session_state.products = [
        {"name": "iPhone 12 UK Used 128GB", "price": "250k", "loc": "Ogbomoso", "cat": "Phones", "phone": "2348100000000", "desc": "BH 89 percent"},
        {"name": "Mama Gold Rice 50kg", "price": "75k", "loc": "Ilorin", "cat": "Groceries", "phone": "2348100000000", "desc": "Stone free"},
    ]
if "requests" not in st.session_state:
    st.session_state.requests = []
if "services" not in st.session_state:
    st.session_state.services = [
        {"name": "Afeez Haircut Studio", "skill": "Barber", "price": "2k per cut", "loc": "Ogbomoso", "phone": "2348100000000", "raw": "08010000000", "desc": "Home service available"},
        {"name": "Queens Beauty Salon", "skill": "Hair Dresser", "price": "5k per braids", "loc": "Ilorin", "phone": "2348100000000", "raw": "08010000000", "desc": "Braids, Wigs, Lashes"},
        {"name": "Baba T Painter", "skill": "Painter", "price": "15k per room", "loc": "Abuja", "phone": "2348100000000", "raw": "08010000000", "desc": "House painting, POP"},
    ]

st.title("ROW ECONOMY")
st.caption("Market + Services - Ogbomoso | Ilorin | Abuja | Nigeria")

tab1, tab2, tab3 = st.tabs(["MARKET", "REQUESTS", "SERVICES - Barber Hair Painter"])

with tab1:
    with st.expander("SELL PRODUCT - Post FREE"):
        with st.form("sell", clear_on_submit=True):
            n = st.text_input("Product Name")
            p = st.text_input("Price")
            cat = st.selectbox("Category", ["Phones","Groceries","Vehicles","Fashion","Electronics","Others"])
            loc = st.selectbox("Location", ["Ogbomoso","Ilorin","Abuja","Nationwide"])
            ph = st.text_input("WhatsApp Number")
            desc = st.text_area("Description")
            if st.form_submit_button("Post Product"):
                if n and p and ph:
                    cl = "".join(filter(str.isdigit, ph))
                    if cl.startswith("0"):
                        cl = "234" + cl[1:]
                    st.session_state.products.append({"name": n, "price": p, "loc": loc, "cat": cat, "phone": cl, "desc": desc})
                    st.success("Product posted")
                    st.balloons()
    search = st.text_input("Search product")
    for prod in reversed(st.session_state.products):
        if search.lower() in prod["name"].lower():
            with st.container(border=True):
                st.write(f"{prod['name']} - {prod['price']} | {prod['loc']}")
                st.caption(prod["desc"])
                msg = urllib.parse.quote(f"Hello, I saw {prod['name']} on ROW ECONOMY")
                st.link_button("Buy on WhatsApp", f"https://wa.me/{prod['phone']}?text={msg}")

with tab2:
    with st.form("req", clear_on_submit=True):
        item = st.text_input("What do you need")
        bud = st.text_input("Budget")
        loc = st.selectbox("Your Location", ["Ogbomoso","Ilorin","Abuja","Nationwide"])
        ph = st.text_input("Your WhatsApp")
        if st.form_submit_button("Post Request"):
            if item and ph:
                cl = "".join(filter(str.isdigit, ph))
                if cl.startswith("0"):
                    cl = "234" + cl[1:]
                st.session_state.requests.append({"item": item, "budget": bud, "loc": loc, "phone": cl, "raw": ph})
                st.success("Request posted")
    for r in reversed(st.session_state.requests):
        with st.container(border=True):
            st.write(f"NEED: {r['item']} - {r['budget']} | {r['loc']}")
            msg = urllib.parse.quote(f"I have {r['item']} for you - ROW ECONOMY")
            st.link_button(f"I Have It - {r['raw']}", f"https://wa.me/{r['phone']}?text={msg}")

with tab3:
    st.subheader("Find Artisans Near You")
    with st.expander("REGISTER YOUR SERVICE - Barber, Hair Dresser, Painter - FREE", expanded=True):
        with st.form("service_form", clear_on_submit=True):
            s_name = st.text_input("Business Name")
            s_skill = st.selectbox("What do you do", ["Barber","Hair Dresser","Painter","Fashion Designer","Makeup Artist","Nail Tech","Others"])
            s_price = st.text_input("Price Rate", placeholder="2k per cut, 10k per room")
            s_loc = st.selectbox("Your Base", ["Ogbomoso","Ilorin","Abuja","Nationwide"])
            s_phone = st.text_input("Your WhatsApp Number")
            s_desc = st.text_area("About your work")
            if st.form_submit_button("List My Service"):
                if s_name and s_phone and s_desc:
                    cl = "".join(filter(str.isdigit, s_phone))
                    if cl.startswith("0"):
                        cl = "234" + cl[1:]
                    st.session_state.services.append({"name": s_name, "skill": s_skill, "price": s_price, "loc": s_loc, "phone": cl, "raw": s_phone, "desc": s_desc})
                    st.success(f"{s_name} listed")
                    st.balloons()
    
    f1, f2 = st.columns(2)
    with f1:
        skill_filter = st.selectbox("Filter by Skill", ["All","Barber","Hair Dresser","Painter","Fashion Designer","Makeup Artist","Nail Tech","Others"])
    with f2:
        loc_filter = st.selectbox("Filter Location", ["All","Ogbomoso","Ilorin","Abuja","Nationwide"])
    
    filtered_s = [s for s in st.session_state.services if (skill_filter=="All" or s["skill"]==skill_filter) and (loc_filter=="All" or s["loc"]==loc_filter)]
    
    st.write(f"{len(filtered_s)} Artisans found")
    for s in reversed(filtered_s):
        with st.container(border=True):
            st.write(f"{s['name']} - {s['skill']}")
            st.write(f"{s['price']} | {s['loc']}")
            st.caption(f"{s['desc']}")
            msg = urllib.parse.quote(f"Hello {s['name']}, I saw your {s['skill']} service on ROW ECONOMY")
            st.link_button(f"Book on WhatsApp - {s['raw']}", f"https://wa.me/{s['phone']}?text={msg}")

st.caption("ROW ECONOMY 2026 - By Muhammed")
