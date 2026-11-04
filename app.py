import streamlit as st
from supabase import create_client

st.set_page_config(page_title="ROW Economy Market")
st.title("ROW Economy Market")

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

st.success("Connected!")

# Add Market
st.subheader("Add New Market")
with st.form("add", clear_on_submit=True):
    name = st.text_input("Market Name")
    location = st.text_input("Location")
    ok = st.form_submit_button("Add Market")
    if ok and name:
        supabase.table("markets").insert({"name": name, "location": location}).execute()
        st.success("Added!")
        st.rerun()

st.divider()
st.subheader("All Markets")

data = supabase.table("markets").select("*").execute()
rows = data.data

if not rows:
    st.info("No markets yet")
else:
    for r in rows:
        c1, c2, c3 = st.columns([3, 3, 1])
        c1.write(r["name"])
        c2.write(r.get("location", ""))
        if c3.button("Delete", key=str(r["id"])):
            supabase.table("markets").delete().eq("id", r["id"]).execute()
            st.rerun()
