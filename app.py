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
if p=="Home": st.subheader("Mama Oloja")
if p=="Home" and q=="": st.write("Mama Welcome my dear")
if p=="Home" and "rice" in ql: st.write("Mama Rice N80000 to N95000")
if p=="Home" and "perfume" in ql: st.write("Mama Perfume from N15000")
if p=="Home" and "phone" in ql: st.write("Mama Test phone before pay")
if p=="Home" and "car" in ql: st.write("Mama Go to Horlance")
if p=="Home" and "verified" in ql: st.write("Mama Verified is N5000")
if p=="Home": st.subheader("Categories")
if p=="Home": a,b=st.columns(2)
if p=="Home": a.write("Perfume")
if p=="Home": b.write("Clothes")
if p=="Home": c,d=st.columns(2)
if p=="Home": c.write("Phones")
if p=="Home": d.write("Food")
if p=="Home": st.subheader("Featured")
if p=="Home": st.write("Horlance VERIFIED")
if p=="Home": st.write("Car AC Repair")
if p=="Home": st.write("Osun and Oyo")
if p=="Home": st.write("09046044472")
if p=="Home": st.link_button("Chat WhatsApp", "https://wa.me/2349046044472")
s=st.text_input("Search here")
s=s.lower()
lo=st.text_input("Min Price e.g 0")
hi=st.text_input("Max Price e.g 100000")
if lo=="": lo="0"
if hi=="": hi="99999999"
if lo.isdigit()==
