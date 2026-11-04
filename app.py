import streamlit as st
from supabase import create_client
import pandas as pd
from datetime import date

st.set_page_config(page_title="ROW Economy Market", layout="wide")
st.title("ROW Economy Market - Live Prices")

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

# Load data
@st.cache_data(ttl=60)
def load_all():
    markets = supabase.table("markets").select("*").order("name").execute().data
    products = supabase.table("products").select("*").order("name").execute().data
    prices = supabase.table("market_prices").select("*, markets(name), products(name, unit)").order("date_recorded", desc=True).execute().data
    return markets, products, prices

markets, products, prices = load_all()

tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🏪 Manage", "💰 Add Price"])

with tab1:
    st.subheader("Compare Prices Across Markets")
    if not products:
        st.info("Add products in Manage tab first")
    else:
        prod_names = {p['name']: p['id'] for p in products}
        sel = st.selectbox("Select Product", list(prod_names.keys()))
        if sel:
            pid = prod_names[sel]
            filtered = [p for p in prices if p['product_id'] == pid]
            if not filtered:
                st.warning(f"No prices yet for {sel}")
            else:
                df = pd.DataFrame([{
                    "Market": f["markets"]["name"] if f.get("markets") else f["market_id"],
                    "Price (₦)": f["price"],
                    "Date": f["date_recorded"]
                } for f in filtered])
                st.bar_chart(df.set_index("Market")["Price (₦)"])
                st.dataframe(df, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Add Market")
        with st.form("add_market", clear_on_submit=True):
            m_name = st.text_input("Market Name")
            m_loc = st.text_input("Location")
            if st.form_submit_button("Add Market") and m_name:
                supabase.table("markets").insert({"name": m_name, "location": m_loc}).execute()
                st.cache_data.clear()
                st.rerun()
        st.write("Markets:")
        for m in markets:
            c1,c2 = st.columns([4,1])
            c1.write(f"{m['name']} - {m.get('location','')}")
            if c2.button("X", key=f"m{m['id']}"):
                supabase.table("markets").delete().eq("id", m['id']).execute()
                st.cache_data.clear()
                st.rerun()
    with col2:
        st.subheader("Add Product")
        with st.form("add_product", clear_on_submit=True):
            p_name = st.text_input("Product Name e.g. Rice")
            p_unit = st.text_input("Unit", value="bag")
            if st.form_submit_button("Add Product") and p_name:
                supabase.table("products").insert({"name": p_name, "unit": p_unit}).execute()
                st.cache_data.clear()
                st.rerun()
        st.write("Products:")
        for p in products:
            c1,c2 = st.columns([4,1])
            c1.write(f"{p['name']} ({p['unit']})")
            if c2.button("X", key=f"p{p['id']}"):
                supabase.table("products").delete().eq("id", p['id']).execute()
                st.cache_data.clear()
                st.rerun()

with tab3:
    st.subheader("Record New Price")
    if not markets or not products:
        st.info("Add at least 1 market and 1 product in Manage tab")
    else:
        with st.form("add_price", clear_on_submit=True):
            m_opt = {m['name']: m['id'] for m in markets}
            p_opt = {p['name']: p['id'] for p in products}
            sel_m = st.selectbox("Market", list(m_opt.keys()))
            sel_p = st.selectbox("Product", list(p_opt.keys()))
            price_val = st.number_input("Price (₦)", min_value=0.0, step=100.0)
            date_val = st.date_input("Date", value=date.today())
            if st.form_submit_button("Save Price"):
                supabase.table("market_prices").insert({
                    "market_id": m_opt[sel_m],
                    "product_id": p_opt[sel_p],
                    "price": price_val,
                    "date_recorded": str(date_val)
                }).execute()
                st.cache_data.clear()
                st.success(f"Saved {sel_p} at {sel_m} = ₦{price_val}")
                st.rerun()
