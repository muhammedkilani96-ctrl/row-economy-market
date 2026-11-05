import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy Market", page_icon="🛒", layout="wide")

# --- Store ---
if "all_products" not in st.session_state:
    st.session_state.all_products = [
        {"seller": "Row Economy", "name": "Bag of Rice", "price": "₦45,000", "location": "Abuja", "whatsapp": "09046044472", "image": None, "video": None},
        {"seller": "Row Economy", "name": "Rice - Bulk", "price": "₦45,000/bag", "location": "Abuja", "whatsapp": "08116911722", "image": None, "video": None},
    ]

products = st.session_state.all_products

# --- HEADER ---
st.title("🛒 ROW ECONOMY")
st.caption("Buy & Sell ANYTHING - Clothes, Shoes, Hair, Food, Phones, Perfume, Cars")
st.success("🔥 TODAY ONLY - FREE FOR FIRST 10 SELLERS")

# --- FILTERS ---
c1, c2, c3 = st.columns(3)
loc_filter = c1.selectbox("📍 Location", ["All", "Abuja", "Ogbomoso", "Ilorin", "Ibadan", "Lagos", "Port Harcourt", "Kano"])
search = c2.text_input("🔍 Search", placeholder="rice, hair, iPhone...")
sort = c3.selectbox("Sort", ["Newest First", "Lowest Price", "Highest Price"])

filtered = products
if loc_filter != "All":
    filtered = [p for p in filtered if loc_filter.lower() in p["location"].lower()]
if search:
    filtered = [p for p in filtered if search.lower() in (p["name"] + p["seller"]).lower()]

st.write(f"**{len(filtered)} products found - {10 - len(set([p['seller'] for p in products]))} FREE slots left**")

# --- PRODUCT GRID - 10 PICTURES STYLE ---
if not filtered:
    st.info("No products yet. Be the first seller below!")
else:
    cols = st.columns(3)
    for i, p in enumerate(filtered):
        wa = str(p["whatsapp"])
        display_wa = "0" + wa[3:] if wa.startswith("234") else wa
        clean = wa[1:] if wa.startswith("0") else wa[3:] if wa.startswith("234") else wa
        msg = urllib.parse.quote(f"Hello {p['seller']}, I saw your {p['name']} ({p['price']}) on ROW ECONOMY. Still available?")
        link = f"https://wa.me/234{clean}?text={msg}"
        with cols[i % 3]:
            if p.get("image") is not None:
                st.image(p["image"], use_container_width=True)
            elif p.get("video") is not None:
                st.video(p["video"])
            else:
                st.markdown(f"<div style='background:#f0f0f0;padding:40px;text-align:center;border-radius:12px;font-size:40px'>🛍️</div>", unsafe_allow_html=True)
            st.markdown(f"**{p['name']}**")
            st.write(f"👤 {p['seller']} • 📍 {p['location']}")
            st.markdown(f"**{p['price']}**")
            st.write(f"📞 {display_wa}")
            st.link_button("💬 Chat on WhatsApp", link, use_container_width=True)
            st.write("---")

# --- SELLER FORM - MATCHES YOUR STATUS EXACTLY ---
st.divider()
st.header("➕ SELLER - Send Me Your Goods (FREE for First 10)")
st.write("Fill this like you would send me on WhatsApp. I will post it for you for FREE.")

with st.form("seller_form", clear_on_submit=False):
    st.subheader("1. Your Name")
    seller_name = st.text_input("Your Name *", placeholder="e.g. Mama T")
    st.subheader("2. Your WhatsApp Number")
    seller_wa = st.text_input("WhatsApp Number *", placeholder="09046044472")
    st.subheader("3. Your Location")
    seller_loc = st.selectbox("Your Location", ["Abuja", "Ogbomoso", "Ilorin", "Ibadan", "Lagos", "Port Harcourt", "Kano", "Other"])

    st.subheader("4. 10 Pictures / Videos of your goods")
    st.caption("Upload up to 10 pictures. One product per picture.")
    files = st.file_uploader("Upload Pictures / Videos (max 10)", type=["jpg", "jpeg", "png", "mp4", "mov"], accept_multiple_files=True)

    st.subheader("5. Price of each product")
    st.caption("If you upload 3 pictures, fill 3 names + prices below.")
    # Allow up to 10 products
    prod_names = []
    prod_prices = []
    for j in range(1, 11):
        col_a, col_b = st.columns([2, 1])
        pn = col_a.text_input(f"Product {j} Name", key=f"pn{j}", placeholder=f"Product {j} e.g. Bag of Rice" if j==1 else "")
        pp = col_b.text_input(f"Price {j}", key=f"pp{j}", placeholder="₦45,000" if j==1 else "")
        prod_names.append(pn)
        prod_prices.append(pp)

    submit = st.form_submit_button("✅ POST MY GOODS FOR FREE", use_container_width=True)

    if submit:
        if not seller_name or not seller_wa:
            st.error("Please fill Name and WhatsApp - No. 1 and 2")
        elif not any(prod_names):
            st.error("Please fill at least Product 1 Name + Price - No. 5")
        else:
            count = 0
            for idx, pn in enumerate(prod_names):
                if pn.strip():
                    price = prod_prices[idx] if prod_prices[idx] else "Contact for price"
                    img = None
                    vid = None
                    if files and idx < len(files):
                        f = files[idx]
                        if f.type.startswith("video"):
                            vid = f
                        else:
                            img = f
                    st.session_state.all_products.append({
                        "seller": seller_name, "name": pn, "price": price,
                        "location": seller_loc, "whatsapp": seller_wa,
                        "image": img, "video": vid
                    })
                    count += 1
            st.success(f"🎉 Done {seller_name}! {count} products posted for FREE. They are now LIVE above!")
            st.balloons()
            st.rerun()

st.caption("Row Economy - First 10 Sellers FREE. After that, paid slots.")
