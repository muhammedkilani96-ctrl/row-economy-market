import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy Market", layout="wide")

# --- Connect to Supabase, but don't crash if it fails ---
supabase = None
try:
    from supabase import create_client
    supabase = create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )
except Exception as e:
    supabase = None

def safe_load(table_name):
    """Load a table, return [] if table missing - never crash"""
    if supabase is None:
        return []
    try:
        res = supabase.table(table_name).select("*").execute()
        return res.data or []
    except:
        return []

products = safe_load("products")
sellers = safe_load("sellers")

# --- Header ---
st.title("Row Economy Market")

# --- Top Verified Seller (from products so it always works) ---
if products:
    top = products[0]
    whatsapp = top.get("whatsapp") or "09046044472"
    st.write(f"📞 WhatsApp: {whatsapp}")
    st.write("Slot 1 of 10 - First Verified Seller")
    msg = urllib.parse.quote("Hello, I want to buy from Row Economy Market")
    st.link_button("💬 Chat on WhatsApp", f"https://wa.me/234{whatsapp[1:]}?text={msg}")
else:
    st.write("📞 WhatsApp: 09046044472")
    st.write("Slot 1 of 10 - First Verified Seller")
    st.link_button("💬 Chat on WhatsApp", "https://wa.me/2349046044472?text=Hello")

st.divider()

# --- All Sellers ---
st.header("All Sellers in Market")

# Use sellers if we have them, otherwise use products as sellers
display_list = sellers if sellers else products

if not display_list:
    st.info("No sellers yet. Check back soon.")
else:
    for i, s in enumerate(display_list, 1):
        name = s.get("name") or s.get("title") or f"Seller {i}"
        whatsapp = s.get("whatsapp") or "09046044472"
        st.subheader(f"{name}")
        st.write(f"WhatsApp: {whatsapp} | Slot {i} of 10")
        msg = urllib.parse.quote(f"Hello {name}, I want to buy")
        st.link_button("💬 Chat on WhatsApp", f"https://wa.me/234{whatsapp[1:] if whatsapp.startswith('0') else whatsapp}?text={msg}")
        st.divider()
