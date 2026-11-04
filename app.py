import streamlit as st
from supabase import create_client
import pandas as pd
import uuid

st.set_page_config(page_title="ROW ECONOMY SUPER", layout="wide")
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

if 'logged' not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    st.title("ROW ECONOMY SUPER")
    phone = st.text_input("Phone", value="08116911722")
    pwd = st.text_input("Password", type="password", value="Kilani247")
    if st.button("Login", type="primary"):
        if phone.strip() == "08116911722" and pwd.strip().lower() == "kilani247":
            st.session_state.logged = True
            st.session_state.phone = phone
            st.rerun()
        else:
            st.error("Wrong login")
    st.stop()

phone = st.session_state.phone
st.markdown(f"<div style='background:#0a2a15;padding:12px;border-radius:10px;color:#4ade80;font-weight:bold'>Welcome {phone} | Bal N500000</div>", unsafe_allow_html=True)

try: products = supabase.table("products").select("*").order("created_at", desc=True).execute().data
except: products = []
try: lives = supabase.table("live_sessions").select("*").eq("is_live", True).execute().data
except: lives = []

tabs = st.tabs(["Home","LIVE MARKET","POST PRODUCT","GO LIVE","MAP","SECURITY","SOS","CHAT","Wallet"])

with tabs[1]:
    st.markdown("# 🔴 LIVE MARKETPLACE")
    for p in products:
        with st.container(border=True):
            if p.get('image_url'):
                st.image(p['image_url'], width=200)
            st.write(f"**{p.get('name')}** - ₦{p.get('price',0)}")
            st.caption(p.get('description',''))

with tabs[2]:
    st.title("Post Product")
    st.info("Pic + Description compulsory")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("Product Name*")
        price = st.number_input("Price*", value=1000)
        desc = st.text_area("Description*")
        pic = st.file_uploader("Product Picture* - COMPULSORY", type=['jpg','png','jpeg'])
        
        if st.form_submit_button("Post", type="primary"):
            if not name or not desc or not pic:
                st.error("❌ Name, Description, and Pic are compulsory!")
            else:
                try:
                    # Upload pic
                    fname = f"{uuid.uuid4()}_{pic.name}"
                    supabase.storage.from_("product_images").upload(fname, pic.getvalue())
                    image_url = supabase.storage.from_("product_images").get_public_url(fname)
                    
                    # Insert
                    supabase.table("products").insert({
                        "name": name, 
                        "price": price, 
                        "description": desc, 
                        "image_url": image_url
                    }).execute()
                    st.success("✅ Posted! Go to LIVE MARKET")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
                    st.info("Fix: Run the SQL above, then try again")

with tabs[3]:
    st.title("GO LIVE - Coin Gifts")
    st.subheader("Send Gift 🎁")
    c1,c2,c3,c4 = st.columns(4)
    if c1.button("🌹 Rose 10"): st.balloons(); st.toast("Sent Rose!")
    if c2.button("🔥 Fire 50"): st.balloons(); st.toast("Sent Fire!")
    if c3.button("🦁 Lion 100"): st.balloons(); st.toast("Sent Lion!")
    if c4.button("💎 Diamond 500"): st.balloons(); st.toast("Sent Diamond!")
    
    st.divider()
    cam = st.camera_input("Camera")
    title = st.text_input("Live Title", "Selling in Wuse")
    if st.button("Start Live", type="primary"):
        try:
            supabase.table("live_sessions").insert({"phone":phone,"title":title,"is_live":True}).execute()
            st.success("LIVE!")
            st.rerun()
        except Exception as e:
            st.error(f"{e}")

with tabs[0]: st.title("Home"); people = st.number_input("People",1,1000,10); st.success(f"₦{people*1000}")
with tabs[4]: st.title("SNAP MAP"); st.map(pd.DataFrame({'lat':[9.0765,9.08],'lon':[7.3986,7.40]}))
with tabs[5]: st.title("SECURITY MAP"); st.map(pd.DataFrame({'lat':[6.5244,9.0765],'lon':[3.3792,7.3986]}))
with tabs[6]: st.title("SOS"); st.button("SEND SOS", type="primary")
with tabs[7]: st.title("CHAT")
with tabs[8]: st.title("Wallet"); st.metric("Balance","₦500,000")

if st.button("Logout"):
    st.session_state.logged = False
    st.rerun()
