import streamlit as st
from supabase import create_client
import pandas as pd
import uuid, random

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
st.markdown(f"<div style='background:#0a2a15;padding:12px;border-radius:10px;color:#4ade80;font-weight:bold'>Welcome {phone} | Bal N500000 | ⭐ 5.0 Seller</div>", unsafe_allow_html=True)

try: products = supabase.table("products").select("*").order("created_at", desc=True).execute().data
except: products = []
try: lives = supabase.table("live_sessions").select("*").eq("is_live", True).execute().data
except: lives = []
try: comments = supabase.table("live_comments").select("*").order("created_at", desc=True).limit(20).execute().data
except: comments = []
try: gifts = supabase.table("live_gifts").select("*").order("created_at", desc=True).limit(10).execute().data
except: gifts = []

# Find cheapest price
cheapest = min([p.get('price',999999) for p in products]) if products else 0

tabs = st.tabs(["Home","LIVE MARKET","POST PRODUCT","GO LIVE","MAP","SECURITY","SOS","CHAT","Wallet"])

with tabs[0]:
    st.title("ROW ECONOMY SUPER")
    people = st.number_input("People", 1, 1000, 10)
    st.success(f"Total: ₦{people*1000}")

with tabs[1]:
    st.markdown("# 🔴 LIVE MARKETPLACE")
    if not products:
        st.info("No products yet")
    cols = st.columns(2)
    for i, p in enumerate(products):
        with cols[i%2]:
            with st.container(border=True):
                # Show 3 pics if exists
                imgs = [p.get('image_url'), p.get('image_url2'), p.get('image_url3')]
                imgs = [x for x in imgs if x]
                if imgs:
                    st.image(imgs, width=150)
                if p.get('video_url'):
                    st.video(p['video_url'])
                
                # Cheapest badge
                is_cheapest = p.get('price',0) == cheapest and cheapest != 0
                if is_cheapest:
                    st.markdown("<span style='background:#22c55e;color:white;padding:3px 8px;border-radius:10px;font-size:12px'>🔥 Cheapest in Abuja</span>", unsafe_allow_html=True)
                
                st.markdown(f"**{p.get('name')}** - ₦{p.get('price',0)}")
                st.caption(p.get('description',''))
                st.markdown(f"⭐ {p.get('rating',5.0)} | {random.randint(5,120)} sold")
                
                c1,c2 = st.columns(2)
                if c1.button("Buy", key=f"buy{p['id']}"):
                    st.toast("Order placed!")
                    # Rating popup
                    st.session_state[f"rate_{p['id']}"] = True
                if c2.button("Chat Seller", key=f"chat{p['id']}"):
                    st.link_button("WhatsApp", f"https://wa.me/2348116911722")
                
                if st.session_state.get(f"rate_{p['id']}"):
                    stars = st.slider("Rate seller", 1, 5, 5, key=f"star{p['id']}")
                    if st.button("Submit Rating", key=f"ratebtn{p['id']}"):
                        supabase.table("products").update({"rating": stars}).eq("id", p['id']).execute()
                        st.success("Rated!")
                        st.rerun()

with tabs[2]:
    st.title("Post Product - PRO")
    st.info("Add up to 3 pics + 1 video + description = more sales")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("Product Name*")
        price = st.number_input("Price N*", value=1000, min_value=0)
        desc = st.text_area("Description*")
        pic1 = st.file_uploader("Pic 1* - Main", type=['jpg','png','jpeg'])
        pic2 = st.file_uploader("Pic 2 - Optional", type=['jpg','png','jpeg'])
        pic3 = st.file_uploader("Pic 3 - Optional", type=['jpg','png','jpeg'])
        video = st.file_uploader("Video - Optional (10 sec)", type=['mp4','mov'])
        
        if st.form_submit_button("Post", type="primary"):
            if not name or not desc or not pic1:
                st.error("Name, Description, Pic 1 are compulsory")
            else:
                def upload(f):
                    if not f: return None
                    fname = f"{uuid.uuid4()}_{f.name}"
                    supabase.storage.from_("product_images").upload(fname, f.getvalue())
                    return supabase.storage.from_("product_images").get_public_url(fname)
                
                url1 = upload(pic1)
                url2 = upload(pic2)
                url3 = upload(pic3)
                vurl = upload(video)
                
                supabase.table("products").insert({
                    "name":name,"price":price,"description":desc,
                    "image_url":url1,"image_url2":url2,"image_url3":url3,"video_url":vurl
                }).execute()
                st.success("Posted with pics!"); st.rerun()

with tabs[3]:
    st.title("🔴 GO LIVE")
    if lives:
        st.markdown(f"**{len(lives)} LIVE NOW - {random.randint(12,200)} viewers**")
        for lv in lives:
            st.write(f"🔴 {lv['phone']} - {lv['title']} - 👁️ {random.randint(12,250)} watching")
    
    st.divider()
    st.subheader("Live Chat")
    chat_msg = st.text_input("Say something in live...")
    if st.button("Send Chat"):
        if lives:
            supabase.table("live_comments").insert({"live_phone":lives[0]['phone'],"sender_phone":phone,"message":chat_msg}).execute()
            st.rerun()
    for c in comments:
        st.write(f"**{c['sender_phone']}**: {c['message']}")
    
    st.divider()
    st.subheader("Send Coin Gift 🎁")
    gcol = st.columns(4)
    for idx, (gname, coins) in enumerate([("🌹 Rose",10),("🔥 Fire",50),("🦁 Lion",100),("💎 Diamond",500)]):
        with gcol[idx]:
            if st.button(f"{gname} {coins}", key=f"gift{gname}"):
                if lives:
                    supabase.table("live_gifts").insert({"live_phone":lives[0]['phone'],"sender_phone":phone,"gift":gname,"coins":coins}).execute()
                    st.balloons()
                    st.toast(f"Sent {gname}!")
    
    st.divider()
    cam = st.camera_input("Your camera")
    title = st.text_input("Live Title", "Selling in Wuse")
    if st.button("Start Live", type="primary"):
        supabase.table("live_sessions").insert({"phone":phone,"title":title,"is_live":True}).execute()
        st.rerun()
    if st.button("End Live"):
        supabase.table("live_sessions").delete().eq("phone",phone).execute()
        st.rerun()

with tabs[4]:
    st.title("SNAP MAP")
    st.map(pd.DataFrame({'lat':[9.0765,9.08,9.09],'lon':[7.3986,7.40,7.42]}), zoom=12)

with tabs[5]:
    st.title("SECURITY MAP")
    st.map(pd.DataFrame({'lat':[6.5244,7.3775,9.0765],'lon':[3.3792,3.9470,7.3986]}), zoom=5)

with tabs[6]:
    st.title("SOS")
    if st.button("SEND SOS", type="primary", use_container_width=True):
        st.error("SOS SENT!")

with tabs[7]:
    st.title("CHAT")
    st.text_input("Message")

with tabs[8]:
    st.title("Wallet")

if st.button("Logout"):
    st.session_state.logged = False
    st.rerun()
