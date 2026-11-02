import streamlit as st
import pandas as pd
import random
import re

st.set_page_config(page_title="Naija Market AI", page_icon="🛒", layout="wide")

if 'products' not in st.session_state:
    st.session_state.products=[
        {"name":"Rice 50kg","price":65000,"sold":45,"stock":20},
        {"name":"Indomie Carton","price":12000,"sold":50,"stock":100},
        {"name":"Groundnut Oil","price":4500,"sold":30,"stock":40},
        {"name":"Spaghetti","price":1000,"sold":12,"stock":50}
    ]
if 'cart' not in st.session_state:
    st.session_state.cart=[]
if 'ad_views' not in st.session_state:
    st.session_state.ad_views=0
if 'user_points' not in st.session_state:
    st.session_state.user_points=185

st.title("Naija Market AI")
st.caption("V2 Upgraded - 10 FREE | N200 extra | Ads N500")
st.divider()
st.subheader("Acting AI - Personal Shopper V2")

q=st.text_input("Customer:", placeholder="I want cook spaghetti for 10 people")
if q:
    low=q.lower()
    people=10
    m=re.search(r'(\d+)\s*people', low)
    if m:
        people=int(m.group(1))
    packs=max(1,(people+3)//4)
    if "spaghetti" in low:
        st.success(f"AI: For {people} people, you need {packs} packs Spaghetti + 1 Oil!")
        oil=next((p for p in st.session_state.products if "oil" in p["name"].lower()),None)
        spag=next((p for p in st.session_state.products if "spaghetti" in p["name"].lower()),None)
        sugg=[x for x in [oil,spag] if x]
    else:
        st.info(f"AI: Based on '{q}', I suggest:")
        sugg=random.sample(st.session_state.products,2)
    
    for s in sugg:
        qty=packs if "spaghetti" in s["name"].lower() and "spaghetti" in low else 1
        c1,c2=st.columns([3,1])
        with c1:
            st.write(f"**{s['name']}** - N{s['price']} x {qty} = N{s['price']*qty}")
        with c2:
            if st.button("Add to Cart", key=f"{s['name']}{random.randint(0,99999)}"):
                st.session_state.cart.append({**s,"qty":qty})
                st.session_state.user_points+=10
                st.success(f"Added {qty} x {s['name']}!")
                st.balloons()

if st.session_state.cart:
    st.divider()
    st.write("Your Cart:")
    df_cart=pd.DataFrame(st.session_state.cart)
    st.table(df_cart)
    total=sum([c['price']*c.get('qty',1) for c in st.session_state.cart])
    st.metric("TOTAL TO PAY", f"N{total}")
    if st.button("Checkout"):
        st.success("Order placed! Pay on delivery or via Paystack link.")

st.divider()
st.subheader("Advert Room - 10 Ads Free Per Day")
st.caption(f"Ads seen today: {st.session_state.ad_views}/10 FREE")
if st.button("View Advert"):
    st.session_state.ad_views+=1
    st.rerun()

st.divider()
st.subheader("Ranking")
df=pd.DataFrame(st.session_state.products).sort_values("sold", ascending=False)
st.dataframe(df, use_container_width=True)
