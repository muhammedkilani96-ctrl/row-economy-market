import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="wide")

# --- Supabase ---
supabase = None
try:
    from supabase import create_client
    supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
except:
    supabase = None

def safe_load(table):
    if supabase is None:
        return []
    try:
        return supabase.table(table).select("*").execute().data or []
    except:
        return []

if "local_sellers" not in st.session_state:
    st.session_state.local_sellers = []

products = safe_load("products")
sellers = safe_load("sellers")
all_items = sellers + products + st.session_state.local_sellers

# --- HEADER ---
st.title("🛒 ROW ECONOMY")
st.caption("Anything you want to Buy & Sell — Goods + Services | Abuja • Ogbomoso • Ilorin • Nationwide")

# --- FILTERS ---
c1, c2, c3 = st.columns(3)
category = c1.selectbox("📦 Category", ["All", "Food & Groceries", "Phones & Gadgets", "Fashion", "Beauty & Services", "Home & Living", "Vehicles & Parts", "Building & Work", "Other Services"])
location = c2.selectbox("📍 Location", ["All", "Abuja", "Ogbomoso", "Ilorin", "Ibadan", "Lagos", "Port Harcourt", "Kano"])
search = c3.text_input("🔍 Search", placeholder="rice, iPhone, hair...")

filtered = all_items
if category != "All":
    filtered = [s for s in filtered if category.lower() in str(s.get("category","")).lower() or category.lower() in str(s).lower()]
if location != "All":
    filtered = [s for s in filtered if location.lower() in str(s.get("location","")).lower() or location.lower() in str(s).lower()]
if search:
    filtered = [s for s in filtered if search.lower() in str(s).lower()]

st.success(f"**{len(filtered)} products found**")

# --- PRODUCT GRID ---
if not filtered:
    st.info("No products yet. Be the first to list below!")
else:
    cols = st.columns(3)
    for i, s in enumerate(filtered):
        name = s.get("name") or s.get("title") or f"Product {i+1}"
        whatsapp = str(s.get("whatsapp") or "09046044472")
        price = s.get("price") or "Contact for price"
        cat = s.get("category") or "General"
        loc = s.get("location") or "Abuja"
        image = s.get("image") or s.get("image_url") or ""

        display_wa = "0" + whatsapp[3:] if whatsapp.startswith("234") else whatsapp
        clean = whatsapp[1:] if whatsapp.startswith("0") else whatsapp[3:] if whatsapp.startswith("234") else whatsapp
        msg = urllib.parse.quote(f"Hello, I saw {name} ({price}) on ROW ECONOMY. Still available?")
        wa_link = f"https://wa.me/234{clean}?text={msg}"

        with cols[i % 3]:
            if image:
                st.image(image, use_container_width=True)
            else:
                st.markdown(f"<div style='background:#f0f0f0;padding:30px;text-align:center;border-radius:12px;font-size:40px'>🛍️</div>", unsafe_allow_html=True)
            st.markdown(f"**{name}**")
            st.write(f"{cat} • 📍 {loc}")
            st.markdown(f"**{price}**")
            st.write(f"📞 {display_wa} | Slot {i+1} of 10")
            st.link_button("💬 Chat on WhatsApp", wa_link, use_container_width=True)
            st.write("---")

# --- ADD PRODUCT ---
st.divider()
st.header("➕ Sell Anything - Add Your Product")
st.write("Your product appears instantly. No admin needed.")

with st.form("add"):
    c1, c2 = st.columns(2)
    name = c1.text_input("Product / Business Name *", placeholder="e.g. Bag of Rice - Mama T")
    whatsapp = c2.text_input("WhatsApp Number *", placeholder="09046044472")
    c3, c4 = st.columns(2)
    category2 = c3.selectbox("Category", ["Food & Groceries", "Phones & Gadgets", "Fashion", "Beauty & Services", "Home & Living", "Vehicles & Parts", "Building & Work", "Other Services"])
    price2 = c4.text_input("Price", placeholder="₦45,000")
    c5, c6 = st.columns(2)
    location2 = c5.selectbox("Location", ["Abuja", "Ogbomoso", "Ilorin", "Ibadan", "Lagos", "Port Harcourt", "Kano"])
    image2 = c6.text_input("Image Link (optional)", placeholder="Paste image URL or leave empty")
    submit = st.form_submit_button("✅ List My Product - FREE", use_container_width=True)

    if submit:
        if not name or not whatsapp:
            st.error("Fill Name and WhatsApp")
        else:
            new = {"name": name, "whatsapp": whatsapp, "price": price2, "category": category2, "location": location2, "image": image2}
            st.session_state.local_sellers.append(new)
            if supabase:
                try:
                    supabase.table("sellers").insert({"name": name, "whatsapp": whatsapp}).execute()
                except:
                    pass
            st.success(f"🎉 {name} is now LIVE!")
            st.balloons()
            st.rerun()

st.caption("ROW ECONOMY - Built for Nigeria. Buy & Sell Anything.")
