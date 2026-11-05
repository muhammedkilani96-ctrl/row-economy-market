import streamlit as st
st.set_page_config(page_title="Row Market")
if "g" not in st.session_state: st.session_state.g=[]
if "chat" not in st.session_state: st.session_state.chat=[]
if "p" not in st.session_state: st.session_state.p="Home"
p=st.session_state.p
st.title("Row Market")
st.write("Buy Cheap Sell Fast")
nav=st.segmented_control("Menu", ["Home","Shop","Sell","Chat","Orders","Profile"])
if nav: st.session_state.p=nav
if nav: st.rerun()
p=st.session_state.p
q=st.text_input("Ask Mama Oloja")
ql=q.lower()
if p in ["Home"]: st.subheader("Mama Oloja")
if p in ["Home"] and q in [""]: st.write("Mama Welcome my dear")
if p in ["Home"] and "rice" in ql: st.write("Mama Rice N80000 to N95000")
if p in ["Home"] and "perfume" in ql: st.write("Mama Perfume from N15000")
if p in ["Home"] and "phone" in ql: st.write("Mama Test phone before pay")
if p in ["Home"] and "car" in ql: st.write("Mama Go to Horlance")
if p in ["Home"] and "verified" in ql: st.write("Mama Verified is N5000")
if p in ["Home"]: st.subheader("Categories")
if p in ["Home"]: a,b=st.columns(2)
if p in ["Home"]:
