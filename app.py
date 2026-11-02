import streamlit as st
import urllib.parse
from datetime import datetime

USE_DB=False
supabase=None
BUCKET="Image"
try:
 from supabase import create_client
 URL=st.secrets["SUPABASE_URL"]
 KEY=st.secrets["SUPABASE_KEY"]
 BUCKET=st.secrets.get("BUCKET_NAME","Image")
 supabase=create_client(URL,KEY)
 USE_DB=True
except: USE_DB=False

st.set_page_config(page_title="ROW ECONOMY",page_icon="🛒",layout="wide")

def upload_image(file):
 if not USE_DB or not file: return None
 try:
  fname=f"{int(datetime.now().timestamp())}_{file.name}".replace(" ","_")
  supabase.storage.from_(BUCKET).upload(fname,file.getvalue(),{"content-type":file.type})
  return supabase.storage.from_(BUCKET).get_public_url(fname)
 except Exception as e:
  st.error(f"Upload: {e}")
  return None

def fetch(t):
 if USE_DB:
  try: return supabase.table(t).select("*").order("created_at",desc=True).execute().data
  except: return []
 else: return []

def insert(t,data):
 if USE_DB:
  try: supabase.table(t).insert(data).execute(); return True
  except Exception as e: st.error(e); return False
 else: return False

st.title("ROW ECONOMY 🛒")
st.caption(f"{'🟢 PERMANENT DB LIVE' if USE_DB else '🔴 Secrets missing'} | Image Bucket: {BUCKET}")

tab1,tab2,tab3,tab4=st.tabs(["MARKET","REQUESTS","SERVICES","CHAT"])

with tab1:
 with st.expander("SELL + PICTURE",expanded=True):
  with st.form("sell",clear_on_submit=True):
   n=st.text_input("Product Name *")
   p=st.text_input("Price *")
   cat=st.selectbox("Category",["Phones","Groceries","Vehicles","Fashion","Electronics","Others"])
   loc=st.selectbox("Location",["Ogbomoso","Ilorin","Abuja","Nationwide"])
   ph=st.text_input("WhatsApp *")
   desc=st.text_area("Description")
   img=st.file_uploader("Picture",type=['jpg','png','jpeg'])
   if st.form_submit_button("POST ✅"):
    if n and p and ph:
     cl="".join(filter(str.isdigit,ph)); 
     if cl.startswith("0"): cl="234"+cl[1:]
     iurl=upload_image(img)
     insert("products",{"name":n,"price":p,"loc":loc,"cat":cat,"phone":cl,"description":desc,"image_url":iurl})
     st.success("Posted permanently!")
    else: st.warning("Fill required")
 search=st.text_input("Search Market")
 for prod in fetch("products"):
  if search.lower() in prod.get("name","").lower():
   with st.container(border=True):
    if prod.get("image_url"): st.image(prod["image_url"],width=300)
    st.write(f"**{prod.get('name')}** - {prod.get('price')} | {prod.get('loc')}")
    st.caption(prod.get("description",""))
    m=urllib.parse.quote(f"Hello, I saw {prod.get('name')} on ROW ECONOMY")
    st.link_button(f"Buy {prod.get('phone')}",f"https://wa.me/{prod.get('phone')}?text={m}")

with tab2:
 with st.form("req",clear_on_submit=True):
  item=st.text_input("Need *"); bud=st.text_input("Budget"); loc=st.selectbox("Loc",["Ogbomoso","Ilorin","Abuja","Nationwide"],key="rl"); ph=st.text_input("WhatsApp *",key="rp")
  if st.form_submit_button("Post Request"):
   if item and ph:
    cl="".join(filter(str.isdigit,ph)); 
    if cl.startswith("0"): cl="234"+cl[1:]
    insert("requests",{"item":item,"budget":bud,"loc":loc,"phone":cl}); st.success("Posted!")
 for r in fetch("requests"):
  with st.container(border=True):
   st.write(f"🔎 {r.get('item')} | {r.get('budget')} | {r.get('loc')}")
   m=urllib.parse.quote(f"Hi, I saw your request for {r.get('item')}")
   st.link_button("Contact",f"https://wa.me/{r.get('phone')}?text={m}")

with tab3:
 with st.expander("SERVICE + PICTURE",expanded=True):
  with st.form("serv",clear_on_submit=True):
   sn=st.text_input("Business *"); sk=st.selectbox("Skill",["Barber","Hair Dresser","Painter","Fashion Designer","Makeup Artist","Nail Tech","Others"]); pr=st.text_input("Price"); sl=st.selectbox("Base",["Ogbomoso","Ilorin","Abuja","Nationwide"],key="sl"); sp=st.text_input("WhatsApp *",key="sp"); sd=st.text_area("About"); si=st.file_uploader("Work Pic",type=['jpg','png','jpeg'],key="si")
   if st.form_submit_button("List Service"):
    if sn and sp:
     cl="".join(filter(str.isdigit,sp)); 
     if cl.startswith("0"): cl="234"+cl[1:]
     iurl=upload_image(si)
     insert("services",{"name":sn,"skill":sk,"price":pr,"loc":sl,"phone":cl,"raw":sp,"description":sd,"image_url":iurl}); st.success("Listed!")
 for s in fetch("services"):
  with st.container(border=True):
   if s.get("image_url"): st.image(s["image_url"],width=300)
   st.write(f"**{s.get('name')}** - {s.get('skill')} | {s.get('price')}")
   st.caption(s.get("description",""))
   m=urllib.parse.quote(f"Hello {s.get('name')}, I saw your service on ROW ECONOMY")
   st.link_button(f"Book {s.get('raw','')}",f"https://wa.me/{s.get('phone')}?text={m}")

with tab4:
 chats=fetch("chats"); box=st.container(height=350)
 with box:
  for c in chats:
   with st.container(border=True): st.write(f"**{c.get('username')}** {c.get('loc')} {c.get('time','')}"); st.write(c.get("msg",""))
 with st.form("chat",clear_on_submit=True):
  c1,c2=st.columns(2)
  with c1: un=st.text_input("Name *")
  with c2: ul=st.selectbox("Loc",["Ogbomoso","Ilorin","Abuja","Others"])
  um=st.text_area("Message *")
  if st.form_submit_button("Send"):
   if un and um:
    now=datetime.now().strftime("%I:%M %p")
    insert("chats",{"username":un,"loc":ul,"msg":um,"time":now}); st.rerun()
