import streamlit as st
from supabase import create_client
from datetime import date

st.set_page_config(page_title="ROW Economy Market", layout="wide")
st.title("ROW Economy Market - Live Prices")

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

def load_data():
    markets = supabase.table("markets").select("*").order("name").execute().data
    products = supabase.table("products").select("*").order("name").execute().data
    prices = supabase.table("market_prices").select("*, markets(name), products(name, unit)").order("created_at", desc=True).execute().data
    return markets, products, prices

markets, products, prices = load_data()

tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🏪 Manage", "💰 Add Price"])

with tab1:
    st.subheader("Compare Prices Across Markets")
    if not products:
        st.info("Add products in Manage tab")
    else:
        prod_list = [p['name'] for p in products]
        sel = st.selectbox("Select Product", prod_list, key="dash_prod")
        if sel:
            # find id
            pid = next(p['id'] for p in products if p['name']==sel)
            filtered = [f for f in prices if f['product_id']==pid]
            if not filtered:
                st.warning(f"No prices yet for {sel}")
            else:
                for f in filtered:
                    mname = f['markets']['name'] if f.get('markets') else "Unknown"
                    st.metric(mname, f"₦{f['price']}", f["date_recorded"])
                st.divider()
                st.dataframe(filtered, use_container_width=True)

with tab2:
    st.subheader("Add Market")
    with st.form("add_market", clear_on_submit=True):
        m_name = st.text_input("Market Name e.g. Wuse Market")
        m_loc = st.text_input("Location e.g. Abuja")
        if st.form_submit_button("Add Market") and m_name:
            supabase.table("markets").insert({"name": m_name, "location": m_loc}).execute()
            st.rerun()
    if markets:
        for m in markets:
            c1,c2 = st.columns([4,1])
            c1.write(f"{m['name']} - {m.get('location','')}")
            if c2.button("X", key=f"m{m['id']}"):
                supabase.table("markets").delete().eq("id", m['id']).execute()
                st.rerun()
    else:
        st.caption("No markets yet")

    st.divider()
    st.subheader("Add Product")
    with st.form("add_product", clear_on_submit=True):
        p_name = st.text_input("Product Name e.g. Rice")
        p_unit = st.selectbox("Unit", ["bag", "kg", "crate", "pcs"])
        if st.form_submit_button("Add Product") and p_name:
            supabase.table("products").insert({"name": p_name, "unit": p_unit}).execute()
            st.rerun()
    if products:
        for p in products:
            c1,c2 = st.columns([4,1])
            c1.write(f"{p['name']} ({p['unit']})")
            if c
