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
st.success(f"Welcome {phone} | 3:03 AM - Battery 8% - Let's fix!")

try: products = supabase.table("products").select("*").order("created_at", desc=True).execute().data
except: products = []
try: lives = supabase.table("live_sessions").select("*").eq("is_live", True).execute().data
except: lives = []

tabs = st.tabs(["LIVE MARKET","POST PRODUCT","GO LIVE","MAP","Wallet"])

with tabs[0]:
    st.markdown("# 🔴 LIVE MARKETPLACE")
    if not products:
        st.info("No products yet - Be first!")
    for p in products:
        with st.container(border=True):
            if p.get('image_url'):
                st.image(p['image_url'], width=250)
            st.write(f"**{p.get('name')}** - ₦{p.get('price',0)}")
            st.caption(p.get('description','No description'))

with tabs[1]:
    st.title("Post Product - Compulsory Pic + Desc")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("Product Name*")
        price = st.number_input("Price*", value=1000)
        desc = st.text_area("Description* - Compulsory")
        pic = st.file_uploader("Product Picture* - COMPULSORY (JPG, PNG)", type=['jpg','png','jpeg'])
        
        if st.form_submit_button("Post 🔴", type="primary"):
            if not name or not desc or not pic:
                st.error("❌ Name + Description + Pic are COMPULSORY!")
            else:
                try:
                    fname = f"{uuid.uuid4()}_{pic.name}"
                    # Upload to bucket (if bucket missing, it will still save without pic)
                    try:
                        supabase.storage.from_("product_images").upload(fname, pic.getvalue())
                        image_url = supabase.storage.from_("product_images").get_public_url(fname)
                    except:
                        image_url = None
                        st.warning("Bucket not created yet - posting without image URL, but saving product")
                    
                    data = {"name": name, "price": price, "description": desc}
                    if image_url:
                        data["image_url"] = image_url
                    
                    supabase.table("products").insert(data).execute()
                    st.success("✅ POSTED! Check LIVE MARKET")
                    st.balloons()
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
                    st.info("If error says 'description', RUN THE SQL ABOVE AGAIN and wait 20 sec")

with tabs[2]:
    st.title("🔴 GO LIVE - Coin Gifts")
    cols = st.columns(4)
    if cols[0].button("🌹 Rose 10"): st.balloons(); st.toast("Rose sent!")
    if cols[1].button("🔥 Fire 50"): st.balloons(); st.toast("Fire sent!")
    if cols[2].button("🦁 Lion 100"): st.balloons(); st.toast("Lion sent!")
    if cols[3].button("💎 Diamond 500"): st.balloons(); st.toast("Diamond sent!")
    
    st.divider()
    cam = st.camera_input("Go Live Camera")
    title = st.text_input("Live Title", "Selling in Wuse - Send Coins!")
    if st.button("Start Live", type="primary"):
        supabase.table("live_sessions").insert({"phone":phone,"title":title,"is_live":True}).execute()
        st.success("LIVE! People can send you coins")
        st.rerun()

with tabs[3]:
    st.title("SNAP MAP")
    st.map(pd.DataFrame({'lat':[9.0765,9.08,9.09],'lon':[7.3986,7.40,7.42]}))

with tabs[4]:
    st.title("Wallet")
    st.metric("Balance","₦500,000")
    st.metric("Coins","5000")

if st.button("Logout"):
    st.session_state.logged = False
    st.rerun()
