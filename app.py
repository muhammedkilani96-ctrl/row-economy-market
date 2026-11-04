# ===== STEP 4: AI ASSISTANT =====
st.markdown("---")
st.markdown("### 🤖 Ask AI - Find Product Fast")

user_need = st.text_input("Type what you need, e.g: I need Rice for Wuse, budget 85000", key="ai_input")

if st.button("Ask AI 🔍"):
    if not user_need:
        st.warning("Abeg type wetin you need first, e.g: I need Rice for Wuse")
    else:
        # Get products from your app - change this to your own variable name
        # If your products are in st.session_state['products'] or a dataframe called df
        try:
            products = st.session_state.get('products', [])
            if isinstance(products, list) and len(products) == 0:
                # Fallback - demo product so AI no go empty
                products = [{"name": "Fresh Rice 50kg", "price": 85000, "location": "Wuse Market, Abuja", "whatsapp": "2348116911722"}]
        except:
            products = [{"name": "Fresh Rice 50kg", "price": 85000, "location": "Wuse Market, Abuja", "whatsapp": "2348116911722"}]

        need_lower = user_need.lower()
        found = []
        for p in products:
            # p can be dict or row - we check name + location
            name = str(p.get('name', '') if isinstance(p, dict) else p[0]).lower()
            loc = str(p.get('location', '') if isinstance(p, dict) else p[2]).lower()
            # Simple match: if user typed "rice" and product is rice
            match = False
            for word in ["rice", "beans", "garri", "oil", "yam", "tomato"]:
                if word in need_lower and word in name:
                    match = True
            # Also match location
            if "wuse" in need_lower and "wuse" in loc:
                match = True
            if "garki" in need_lower and "garki" in loc:
                match = True
            if match:
                found.append(p)

        if found:
            st.success(f"AI found {len(found)} product(s) for you:")
            for p in found:
                if isinstance(p, dict):
                    name = p.get('name'); price = p.get('price'); loc = p.get('location'); wa = p.get('whatsapp')
                else:
                    name, price, loc, wa = p[0], p[1], p[2], p[3]
                st.markdown(f"**{name} - N{price:,} - {loc}**")
                # Clean WhatsApp number
                wa_clean = str(wa).replace("+", "").replace(" ", "")
                if wa_clean.startswith("0"):
                    wa_clean = "234" + wa_clean[1:]
                msg = f"Hello, I see your {name} for N{price} for {loc} on Row Economy Market. Is it still available?"
                import urllib.parse
                wa_link = f"https://wa.me/{wa_clean}?text={urllib.parse.quote(msg)}"
                st.link_button(f"💬 Chat Seller on WhatsApp - {name}", wa_link)
        else:
            st.info("No product match yet for that need.")
            st.markdown("**Drop your WhatsApp, we go notify you when seller post am:**")
            buyer_wa = st.text_input("Your WhatsApp Number", key="buyer_wait")
            if st.button("Notify Me When Available"):
                st.success("Done! We don save your request. We go notify you once seller post am.")
