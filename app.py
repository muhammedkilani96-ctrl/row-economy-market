import streamlit as st, requests
def c(x):
 s=str(x)
 s=s.replace("\n","").replace("\r","").replace(" ","").replace("\t","").strip()
 s=s.strip('"').strip("'")
 s=s.replace('"""','').replace("'''",'')
 return s.strip()
st.title("ROW Economy Market")
URL=c(st.secrets["SUPABASE_URL"])
KEY=c(st.secrets["SUPABASE_KEY"])
st.write("URL clean:")
st.write(URL)
st.write("Length:", len(URL))
h={"apikey":KEY,"Authorization":f"Bearer {KEY}"}
u=URL+"/rest/v1/markets?select=*"
try:
 r=requests.get(u,headers=h,timeout=20)
 r.raise_for_status()
 st.success("Connected!")
 st.dataframe(r.json())
except Exception as e:
 st.error(e)
