import streamlit as st

st.set_page_config(page_title="K&K / ROW Economy Market", page_icon="🛍️", layout="wide")

st.title("🛍️ K&K / ROW Economy Market")
st.write("Powered by **Mama Oloja** 🧕 - She Knows All Prices! | Opay: 8116911722 - Kilani Muhammed Opeyemi")

# ===== PRODUCTS DATA =====
PRODUCTS = [
    {"name": "Black Rapture", "price": 4000, "seller": "Mary", "phone": "09031889875", "location": "Lagos", "cat": "Perfume", "desc": "Bold, long-lasting, smell like money"},
    {"name": "Black Rapture", "price": 4000, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Perfume", "desc": "Bold, long-lasting"},
    {"name": "Vintage Radio", "price": 10000, "seller": "Mary", "phone": "09031889875", "location": "Lagos", "cat": "Perfume", "desc": "Warm, vintage, Lattafa"},
    {"name": "Body Mist", "price": 4000, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Perfume", "desc": "Soft, sweet, everyday"},
    {"name": "Yum Yum Combo", "price": 12000, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Perfume", "desc": "Perfume + Body Spray, smell like ice cream"},
    {"name": "Musk Vanille", "price": 6000, "seller": "Mary", "phone": "09031889875", "location": "Lagos", "cat": "Perfume", "desc": "Vanilla sweet"},
    {"name": "Face Serum", "price": 4000, "seller": "Blessing", "phone": "07052528772", "location": "Abuja", "cat": "Beauty", "desc": "Clear face, glow"},
    {"name": "Ceramide Serum", "price": 5000, "seller": "Blessing", "phone": "07052528772", "location": "Abuja", "cat": "Beauty", "desc": "For dry skin"},
    {"name": "TONYMOLY Toner", "price": 6000, "seller": "Blessing", "phone": "07052528772", "location": "Abuja", "cat": "Beauty", "desc": "Tone + glow"},
    {"name": "Sunscreen", "price": 5000, "seller": "Blessing", "phone": "07052528772", "location": "Abuja", "cat": "Beauty", "desc": "Protect your skin"},
    {"name": "Lip Combo", "price": 6000, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Beauty", "desc": "Brown + Pink + Liner, girls love am"},
    {"name": "Rolex Watch", "price": 10000, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Watch", "desc": "Black strap, 3 designs, with box"},
    {"name": "Hand Chain", "price": 2000, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Jewelry", "desc": "Gold + Black LV"},
    {"name": "Gold Necklace", "price": 8000, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Jewelry", "desc": "Shine for owambe"},
    {"name": "Earrings", "price": 3000, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Jewelry", "desc": "Fine earrings"},
    {"name": "Jersey Scarf Plain", "price": 3500, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Scarf", "desc": "Soft, no slip, for hijab"},
    {"name": "Jersey Scarf Pattern", "price": 4000, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Scarf", "desc": "Stylish, for owambe"},
    {"name": "Tote Bag", "price": 6500, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Bag", "desc": "Big, strong bag"},
    {"name": "Real Man Spray", "price": 4500, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Perfume", "desc": "Fresh, Morning, Active - for men"},
    {"name": "Mini Perfume", "price": 3500, "seller": "Arinfe", "phone": "090915907990", "location": "Ibadan", "cat": "Perfume", "desc": "Small, sweet, carry anywhere"},
]

# ===== TABS =====
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["🛍️ Shop", "🛒 Cart + Pay", "❤️ Wishlist", "🎟️ Tickets + Delivery", "📊 Dashboard", "📝 Sell With Us", "🤖 Mama Oloja AI", "🎬 Anime Advert ₦200"])

# ===== TAB 1 - SHOP =====
with tab1:
    st.header("🛍️ Shop - All Products")
    search = st.text_input("🔍 Search product:", placeholder="e.g. Black Rapture, Rolex, Scarf")
    cat_filter = st.selectbox("Filter by Category:", ["All", "Perfume", "Beauty", "Watch", "Jewelry", "Scarf", "Bag"])
    loc_filter = st.selectbox("Filter by Location:", ["All", "Ibadan", "Lagos", "Abuja"])

    for p in PRODUCTS:
        if search and search.lower() not in p["name"].lower():
            continue
        if cat_filter != "All" and p["cat"] != cat_filter:
            continue
        if loc_filter != "All" and p["location"] != loc_filter:
            continue
        with st.container():
            st.write(f"**{p['name']}** - ₦{p['price']:,} | {p['seller']} - {p['location']} | {p['cat']}")
            st.write(p["desc"])
            wa_link = f"https://wa.me/234{p['phone'][1:]}?text=Hello {p['seller']}, I want {p['name']} - ₦{p['price']} from K&K Market"
            st.markdown(f"[💬 Buy via WhatsApp - {p['seller']}]({wa_link})")
            st.markdown("---")

# ===== TAB 2 - CART + PAY =====
with tab2:
    st.header("🛒 Cart + Pay - ₦200 Per Product For 30 Days (Seller Fee)")
    st.write("Buyer: Add to cart, pay to Kilani Muhammed Opeyemi - Opay 8116911722")
    st.write("Seller Fee: First 10 Sellers FREE, After that ₦200 per product for 30 days")
    st.info("To pay for your product listing, transfer ₦200 to Opay 8116911722 - Kilani Muhammed Opeyemi")

# ===== TAB 3 - WISHLIST =====
with tab3:
    st.header("❤️ Wishlist")
    st.write("Save products you like here. Click heart for your favourite product and come back later!")

# ===== TAB 4 - TICKETS + DELIVERY =====
with tab4:
    st.header("🎟️ Tickets + Delivery")
    st.write("**Tickets - VERIFIED - NO FAKE TICKET** - Digital Ticket + QR Code")
    st.write("**Delivery:** Ibadan ₦1,000 | Lagos ₦3,500 | Abuja - Ask Seller | Pickup FREE for Academy Ibadan")
    st.write("**Car Mart - VERIFIED:** Green Badge = VERIFIED DOCUMENTS, Yellow Badge = DOCUMENTS PENDING")
    st.warning("⚠️ Do not pay before inspection for Car Mart!")

# ===== TAB 5 - DASHBOARD =====
with tab5:
    st.header("📊 Dashboard - For CEO")
    st.write(f"Total Products: {len(PRODUCTS)}")
    st.write("Sellers: Arinfe (Ibadan), Mary (Lagos), Blessing (Abuja)")
    st.write("Anime Advert Downloads: Count your ₦200 payments for Opay 8116911722")

# ===== TAB 6 - SELL WITH US =====
with tab6:
    st.header("📝 Sell With Us - First 10 Sellers FREE!")
    st.write("After 10 sellers, ₦200 per product for 30 days. Pay to Opay 8116911722 - Kilani Muhammed Opeyemi")
    s_name = st.text_input("Your Name:")
    s_phone = st.text_input("Your WhatsApp Number:")
    s_prod = st.text_input("Product Name:")
    s_price = st.text_input("Price:")
    s_loc = st.text_input("Location:")
    if st.button("Submit To Sell"):
        st.success(f"Thank you {s_name}! Chat us on WhatsApp to confirm: https://wa.me/2348116911722 - Your product {s_prod} - ₦{s_price} go live after ₦200 payment!")

# ===== TAB 7 - MAMA OLOJA AI 2.0 =====
with tab7:
    st.header("🤖 Mama Oloja AI - Your Market Woman")
    st.write("Talk to me like you dey market! I sabi all products, prices, sellers, locations.")
    st.write("Try: *I get 5000* | *Gift for my girlfriend* | *I dey Ibadan* | *Which perfume sweet pass?* | *I want combo*")
    user_q = st.text_input("Ask Mama Oloja:", placeholder="e.g. I get 5000, wetin I fit buy?").lower()
    ask = st.button("💬 Ask Mama Oloja")
    q1, q2, q3, q4 = st.columns(4)
    if q1.button("I get ₦5,000"):
        user_q = "i get 5000"; ask = True
    if q2.button("Gift for Girlfriend"):
        user_q = "gift for girlfriend"; ask = True
    if q3.button("I dey Ibadan"):
        user_q = "i dey ibadan"; ask = True
    if q4.button("Best Perfume"):
        user_q = "best perfume"; ask = True

    if ask and user_q:
        if "5000" in user_q or "5k" in user_q:
            st.success("Mama Oloja: Ah! ₦5,000? You get plenty options my pikin!")
            st.write("**1. Hand Chain ₦2,000 + Mini Perfume ₦3,500 = ₦5,500** - Arinfe go give you discount!")
            st.write("**2. Body Mist ₦4,000 OR Black Rapture ₦4,000** - Both sweet, long-lasting!")
            st.write("**My Advice:** Buy **Black Rapture ₦4,000** from Mary - e get 20 reviews!")
        elif "girlfriend" in user_q or "babe" in user_q:
            st.success("Mama Oloja: For your girlfriend? You go make am happy! 💖")
            st.write("**Best Gift - Lip Combo ₦6,000** - Doneva Lipgloss Set - Girls dey love am!")
            st.write("**Sweet + Cheap - Hand Chain ₦2,000 + Mini Perfume ₦3,500 = ₦5,500** - She go think say you spend ₦10k!")
        elif "ibadan" in user_q:
            st.success("Mama Oloja: You dey Ibadan? Arinfe dey Academy, Ibadan! 🏠")
            st.write("**Arinfe Products:** Rolex ₦10k, Lip Combo ₦6k, Jersey Scarf ₦3.5k, Tote Bag ₦6.5k")
            st.write("**Delivery:** ₦1,000 only for Ibadan! Or Pickup FREE for Academy!")
        elif "perfume" in user_q and ("best" in user_q or "sweet" in user_q or "which" in user_q):
            st.success("Mama Oloja: Perfume matter? Make I compare for you! 👃")
            st.write("**For ₦4,000:** Black Rapture - 20 reviews, ⭐ 5.0 - BEST FOR ₦4k!")
            st.write("**For ₦6,000:** Arinfe Eau De Parfum OR Musk Vanille - Vanilla sweet")
            st.write("**For ₦10,000:** Vintage Radio - Warm, vintage, Premium!")
        elif "combo" in user_q:
            st.success("Mama Oloja: Combo? You sabi! You go save money! 🎁")
            st.write("**Combo 1 - Beauty Combo ₦8,000:** Lip Combo ₦6k + Hand Chain ₦2k")
            st.write("**Combo 2 - Perfume Combo ₦12,000:** Yum Yum Perfume + Suger Pink Spray")
            st.write("**Combo 3 - Full Owambe ₦15,500:** Gold Necklace ₦8k + Earrings ₦3k + Jersey Scarf ₦3.5k + Hand Chain ₦2k")
        else:
            st.success(f"Mama Oloja: You ask '{user_q}' - Make I help you!")
            st.write("Tell me: **Your budget?** (e.g. I get 5000) **Who you dey buy for?** (girlfriend, mama) **Where you dey?** (Ibadan, Lagos)")

# ===== TAB 8 - ANIME ADVERT + ₦200 PAYWALL - PERMANENT =====
with tab8:
    st.header("🎬 Mama Oloja Anime Advert - Permanent For All Sellers")
    st.write("Generate FREE, Download na **₦200** only! Mama Oloja voice + Anime Girl = Sell fast!")
    
    all_products = [f"{p['name']} - ₦{p['price']} - {p['seller']} - {p['phone']}" for p in PRODUCTS]
    chosen = st.selectbox("Pick your product:", all_products)
    anime_style = st.selectbox("Pick Anime Style:", ["C - Cute Anime Girl (Pink) - Best for Perfume/Beauty", "A - Fine Anime Babe - Best for Luxury", "B - Cool Anime Boy - Best for Watch/Men"])
    voice_style = st.selectbox("Pick Mama Oloja Voice:", ["Mama Oloja Pidgin (Funny) - Best!", "Mama Oloja English (Clear)", "Mama Oloja Yoruba Mix"])

    if st.button("✨ Generate My Advert (FREE Preview)"):
        st.session_state['advert_ready'] = True
        if "Black Rapture" in chosen:
            st.session_state['script'] = "My pikin, come see o! Black Rapture don land! E dey smell like money, e dey last all day! Chat me now to order. Mama Oloja talk am, e no be lie!"
        elif "Rolex" in chosen:
            st.session_state['script'] = "My pikin, see Rolex Watch! E go make you look like big boy! Price na 10,000 only, with box! Chat me now, no dull!"
        elif "Face Serum" in chosen:
            st.session_state['script'] = "My pikin, your face go glow! Face Serum na 4,000 only! E go clear your face, make you shine! Chat Blessing now!"
        else:
            st.session_state['script'] = f"My pikin, come see o! {chosen}! E good well well, price sweet! Chat me now to order. Mama Oloja recommend am!"

    if st.session_state.get('advert_ready'):
        st.success("Preview Ready! See your script:")
        st.code(st.session_state['script'])
        st.write(f"Style: {anime_style} | Voice: {voice_style}")
        st.info("Preview na FREE. To download full package, pay ₦200 below.")

        st.markdown("---")
        st.subheader("💰 Pay ₦200 To Unlock Download")
        st.write("**Pay to:**")
        st.write("**Opay Number: 8116911722**")
        st.write("**Name: Kilani Muhammed Opeyemi**")
        st.write("**Amount: ₦200**")
        st.write("**Narration: Anime Advert - Your Name**")

        pay_ref = st.text_input("Enter Your Opay Name + Reference after you pay:", placeholder="e.g. MARY - 200 - 12345")

        if st.button("✅ I Don Pay ₦200 - Unlock Download"):
            if pay_ref:
                st.session_state['paid'] = True
                st.success("Payment received! Download don unlock! Mama Oloja don bless your business!")
            else:
                st.warning("Abeg enter your Opay name + reference first.")

        if st.session_state.get('paid'):
            st.markdown("### 🎉 YOUR VIDEO PACKAGE - DOWNLOAD NOW")
            st.download_button("📜 Download Mama Oloja Script (TXT)", st.session_state['script'], file_name="mama-oloja-script.txt")
            st.write("🎙️ **Voice:** Go ttsmaker.com, paste script, Voice: Female Warm, Speed 0.9x, Download MP3")
            st.write("🖼️ **Anime Picture:** Use Cute Anime Girl picture as cover")
            st.write("🎬 **Video:** Join Picture + Voice for OpenCut, Post for TikTok!")
            st.write("💬 **Need Help?** Chat CEO: https://wa.me/2348116911722")
            st.balloons()
        else:
            st.warning("🔒 Download Locked - Pay ₦200 to Opay 8116911722 - Kilani Muhammed Opeyemi to unlock.")

    st.markdown("---")
    st.write("**New Seller? Your product no dey list?**")
    new_prod = st.text_input("New Product Name:")
    new_price = st.text_input("New Price:")
    new_phone = st.text_input("Your WhatsApp Number:")
    if st.button("Generate For New Product"):
        if new_prod:
            new_script = f"My pikin, come see o! {new_prod} don land! Price na {new_price} only! E good well well! Chat me for {new_phone} now to order. Mama Oloja talk am!"
            st.code(new_script)
            st.success("Done! Copy this script, pay ₦200 to 8116911722 to unlock download, then generate voice!")

st.markdown("---")
st.write("© 2026 K&K / ROW Economy Market - CEO: Kilani Muhammed Opeyemi | Opay: 8116911722 | Mama Oloja AI Inside")
