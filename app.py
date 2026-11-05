import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy Market", layout="wide")

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

# Load sellers + products, use session state for new ones too
if "local_sellers" not in st.session_state:
    st.session_state.local_sellers = []

products = safe_load("products")
sellers = safe_load("sellers")
all_sellers = sellers + products + st.session_state.local_sellers

# --- Header ---
st.title("🛒 Row Economy Market")
st.caption("Anything you want to Buy & Sell — Goods + Services")

# --- Search ---
search = st.text_input("🔍 Search anything", placeholder="rice, iPhone, hair, tailor...")
if search:
    all_sellers = [s for s in all_sellers if search.lower() in str(s).lower()]

# --- Sellers List ---
st.header(f"All Sellers in Market - {len(all_sellers)} / 10 Slots")

if not all_sellers:
    st.info("No sellers yet. Be the first to list below!")
else:
    for i, s in enumerate(all_sellers, 1):
        name = s.get("name") or s.get("title") or f"Seller {i}"
        whatsapp = str(s.get("whatsapp") or "09046044472")
        # Clean display: 234... -> 0...
        display_wa = whatsapp
        if display_wa.startswith("234"):
            display_wa = "0" + display_wa[3:]
        
        st.subheader(f"{name}")
        st.write(f"WhatsApp: {display_wa} | Slot {i} of 10")
        clean = whatsapp[1:] if whatsapp.startswith("0") else whatsapp[3:] if whatsapp.startswith("234") else whatsapp
        msg = urllib.parse.quote(f"Hello {name}, I saw you on Row Economy Market. Still available?")
        st.link_button("💬 Chat on WhatsApp", f"https://wa.me/234{clean}?text={msg}")
        st.divider()

# --- ADD YOUR PRODUCT FORM - THE BEST PART ---
st.divider()
st.header("➕ Want to Sell? Add Your Product Here")
st.write("Fill this, tap Submit, your product appears instantly. No need to contact admin.")

with st.form("add_seller"):
    c1, c2 = st.columns(2)
    name = c1.text_input("Your Business / Product Name *", placeholder="e.g. Rice - Mama T")
    whatsapp = c2.text_input("Your WhatsApp Number *", placeholder="09046044472")
    category = st.selectbox("Category", ["Food & Groceries", "Phones & Gadgets", "Fashion", "Beauty & Services", "Home & Living", "Vehicles & Parts", "Building & Work", "Other Services"])
    price = st.text_input("Price", placeholder="e.g. ₦45,000 / bag")
    location = st.selectbox("Location", ["Abuja", "Ogbomoso", "Ilorin", "Ibadan", "Lagos", "Port Harcourt", "Kano", "Other"])
    submitted = st.form_submit_button("✅ List My Product - FREE", use_container_width=True)

    if submitted:
        if not name or not whatsapp:
            st.error("Please fill Name and WhatsApp")
        else:
            new_item = {"name": name, "whatsapp": whatsapp, "title": name, "price": price, "category": category, "location": location}
            # Try Supabase first
            saved = False
            if supabase:
                try:
                    supabase.table("sellers").insert({"name": name, "whatsapp": whatsapp}).execute()
                    saved = True
                except:
                    pass
            # Always show instantly even if Supabase slow
            st.session_state.local_sellers.append(new_item)
            st.success(f"🎉 Done {name}! Your product is now LIVE in the market. Share the link!")
            st.balloons()
            st.rerun()

st.caption("Row Economy - Slot 1 of 10 is Premium. First 10 sellers get featured.")
