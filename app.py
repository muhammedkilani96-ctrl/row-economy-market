import streamlit as st
import requests

# --- FIX FOR PHONE PASTE BREAKING ---
def get_secret(name):
    try:
        raw = st.secrets[name]
    except:
        return ""
    # Remove all spaces, newlines, tabs that phone adds
    cleaned = str(raw).replace("\n","").replace("\r","").replace(" ","").replace("\t","").strip()
    # Remove any surrounding quotes if you accidentally pasted with extra quotes
    cleaned = cleaned.strip('"').strip("'").strip()
    # Re-add if needed? No, keep clean
    # If cleaning removed https://, restore - but our replace removed spaces only, not ://
    # Actually we removed spaces only, so :// safe. We did replace(" ","") only.
    # For URL we need to keep ://, so don't remove : or /
    return cleaned

# For URL we clean differently - keep :// 
def get_url_secret(name):
    try:
        raw = st.secrets[name]
    except:
        return ""
    s = str(raw).replace("\n","").replace("\r","").replace(" ","").replace("\t","").strip()
    s = s.strip('"').strip("'")
    return s

st.set_page_config(page_title="ROW Economy Market", layout="wide")
st.title("ROW Economy Market")

SUPABASE_URL = get_url_secret("SUPABASE_URL")
SUPABASE_KEY = get_secret("SUPABASE_KEY")

# Show debug - you can remove later
if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("Secrets not found! Go to Manage app -> Settings -> Secrets and paste them.")
    st.code('SUPABASE_URL = "https://erglyztemazyluaqlhwc.supabase.co"\nSUPABASE_KEY = "your
