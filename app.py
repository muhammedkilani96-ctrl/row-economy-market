import streamlit as st
st.set_page_config(page_title="Row")
st.session_state.setdefault("g",[])
st.session_state.setdefault("c",[])
o=open("g.txt","a")
o.close()
r=open("g.txt")
txt=r.read()
r.close()
g2=txt.split("\n")
g2=[x for x in g2 if x]
g=st.session_state.g
len(g) in [0] and g.extend(g2)
o2=open("c.txt","a")
o2.close()
r2=open("c.txt")
txt2=r2.read()
r2.close()
c2=txt2.split("\n")
c2=[x for x in c2 if x]
c=st.session_state.c
len(c) in [0] and c.extend(c2)
st.title("Row Market")
st.write("Buy Cheap Sell Fast")
st.write("Abuja Nigeria")
q=st.text_input("Ask Mama")
st.write("Mama Welcome my dear")
st.write("Rice N80000 to N95000")
st.write("Perfume from N
