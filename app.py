import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Naija Market AI", page_icon="🛒", layout="wide")

if 'products' not in st.session_state:
    st.session_state.products = [
        {"name": "Rice 50kg", "price": 65000, "sold": 45},
        {"name": "Indomie Carton", "price": 12000, "sold": 50},
        {"name": "Groundnut Oil", "price": 4500, "sold": 30},
    ]
if 'ad_views' not in st.session_state:
    st.session_state.ad_views = 0
if 'user_points' not in st.session_state:
    st.session_state.user_points = 85
if 'cart' not in st.session_state:
    st.session_state.cart = []

st.title("🛒 Naija Market AI — Shop + AI + Adverts + Ranking")
st.caption("10 Products FREE | AI Personal Shopper | Advert Space ₦500/week")

st.divider()
st.subheader("📦 Your Shop — 10-10-500 Rule")
product_count = len(st.session_state.products)
if product_count <= 10:
    st.success(f"✅ FREE PLAN: {product_count}/10 products — You dey enjoy free!")
else:
    extra = product_count - 10
    fee = ((extra + 9)//10) * 200
    st.warning(f"⚠️ You don pass free: {product_count} products. Extra: {extra} → Pay ₦{fee}")
    if st.button(f"Pay ₦{fee} to unlock", type="primary"):
        st.balloons()
        st.success("Payment successful!")

new_prod = st.text_input("Add product name")
new_price = st.number_input("Price ₦", min_value=100, value=1000)
if st.button("Add Product"):
    if new_prod and new_prod.strip():
        st.session_state.products.append({
            "name": new_prod.strip(),
            "price": new_price,
            "sold": random.randint(1, 10),
        })
        st.rerun()
    else:
        st.warning("Please enter a product name.")

st.dataframe(pd.DataFrame(st.session_state.products), use_container_width=True)

st.divider()
st.subheader("🤖 Acting AI — Personal Shopper")
customer_query = st.text_input("Customer: e.g., 'I need gift for my babe for 20k'")
if customer_query:
    if st.session_state.products:
        suggestions = random.sample(st.session_state.products, min(2, len(st.session_state.products)))
        st.info(f"🤖 AI: Based on '{customer_query}', I suggest:")
        for s in suggestions:
            st.write(f"- {s['name']} - ₦{s['price']}")
    else:
        st.info("No products yet. Add some products to get recommendations.")

st.divider()
st.subheader("📢 Advert Room — 10 Ads Free Per Day")
if st.session_state.ad_views < 10:
    st.caption(f"Ads seen today: {st.session_state.ad_views}/10 FREE")
    if st.button("View Advert"):
        st.session_state.ad_views += 1
        st.rerun()
else:
    st.info("🔒 You don see 10 adverts today — Come back tomorrow!")

st.divider()
c1, c2 = st.columns(2)
with c1:
    st.subheader("🏆 Weekly Sales Ranking")
    df_rank = pd.DataFrame(st.session_state.products).sort_values("sold", ascending=False)
    st.dataframe(df_rank, use_container_width=True)
with c2:
    st.subheader("👤 Avatar Ranking — VIP")
    st.metric("Your Points", st.session_state.user_points)
    if st.button("Simulate Buy (Gain 10 points)"):
        st.session_state.user_points += 10
        st.balloons()
        st.rerun()
