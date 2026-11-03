import streamlit as st, requests
def c(x):
 s=str(x).replace("\n","").replace("\r","").replace(" ","").replace("\t","").strip().strip('"').strip("'")
 return s
st.title("ROW Economy Market")
URL=c(st.secrets["SUPABASE_URL"])
KEY=c(st.secrets["SUPABASE_KEY"])
h={"apikey":KEY,"Authorization":f"Bearer {KEY}"}
u=URL+"/rest/v1/markets?select=*"
try:
 r=requests.get(u,headers=h,timeout=20)
 r.raise_for_status()
 st.success("Connected!")
 st.dataframe(r.json())
except Exception as e:
 st.error(e)
 st.write(URL)
