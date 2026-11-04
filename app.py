import streamlit as st
from supabase import create_client

# --- 1. Connection ---
st.set_page_config(page_title="ROW Economy Market", layout="centered")
st.title("ROW Economy Market")

try:
    URL = st.secrets["SUPABASE_URL"]
    KEY = st.secrets["SUPABASE_KEY"]
    supabase = create_client(URL, KEY)
    st.success("Connected!")
except Exception as e:
    st.error(f"Connection failed: {e}")
    st.stop()

# --- 2. Add Market Form ---
st.subheader("Add New Market")
with st.form("add_market", clear_on_submit=True):
    name = st.text_input("Market Name", placeholder="e.g. Wuse Market")
    location = st.text_input("Location", placeholder="e.g. Abuja")
    submitted = st.form_submit_button("Add Market")
    
    if submitted:
        if name.strip() == "":
            st.warning("Name cannot be empty")
        else:
            try:
                supabase.table("markets").insert({"name": name, "location": location}).execute()
                st.success(f"Added {name}!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()

# --- 3. List Markets ---
st.subheader("All Markets")
try:
    response = supabase.table("markets").select("*").order("name").execute()
    markets = response.data
    
    if not markets:
        st.info("No markets yet. Add one above!")
    else:
        for m in markets:
            col1, col2, col3 = st.columns([3, 3, 1])
            col1.write(f"**{m['name']}**")
            col2.write(m
