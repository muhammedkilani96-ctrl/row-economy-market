# ============ MAMA OLOJA V4 - VERY EFFECTIVE SMART BRAIN ============
import re

# --- Mama's Full Product Knowledge ---
PRODUCTS_DB = [
    {"name": "Face Serum", "price": 4000, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "glow dull dark spot pimple uneven tone", "desc": "For glow, dark marks, dull skin"},
    {"name": "Ceramide Serum", "price": 5000, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "dry sensitive stressed dehydrated damaged barrier", "desc": "For dry, sensitive, stressed skin - restores barrier"},
    {"name": "Illuminating Serum 10% Niacinamide", "price": 5500, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "glow bright uneven dark spot pimple", "desc": "For glow, brightening, dark marks"},
    {"name": "Biore UV Sunscreen", "price": 5000, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen protect oily normal", "desc": "Light, everyday, no white cast"},
    {"name": "Nivea Sun Sensitive SPF50", "price": 9000, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen sensitive", "desc": "For sensitive skin, immediate protection"},
    {"name": "Skin Aqua SPF50+", "price": 10000, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen", "desc": "Super moisture, no white cast"},
    {"name": "La Roche-Posay Anthelios", "price": 17000, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "sun sunscreen sensitive pharmacy", "desc": "Pharmacy grade, best for sensitive"},
    {"name": "TONYMOLY Ceramide Toner", "price": 6000, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "dry toner sensitive", "desc": "Bouncy, soft, moisturized"},
    {"name": "Estelin Whitening Toner", "price": 8000, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "toner bright whitening uneven", "desc": "Brightening, uneven tone"},
    {"name": "Simple Soothing Toner", "price": 10000, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "toner sensitive", "desc": "Alcohol-free, for sensitive"},
    {"name": "Acwell Licorice Toner", "price": 10500, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "toner glow bright pimple", "desc": "Cleansing + Hydrating + Brightening"},
    {"name": "Nivea Men Lotion 400ml", "price": 5000, "cat": "Cosmetics", "seller": "Blessing", "phone": "07052528772", "for": "men man lotion dry body", "desc": "For men, fast absorb, no stickiness"},
    {"name": "AC Gas Recharge", "price": 0, "cat": "Services", "seller": "Horlance", "phone": "09046044472", "for": "ac car cool gas hot air", "desc": "Car AC gas recharge - ask price"},
    {"name": "Compressor Repair", "price": 0, "cat": "Services", "seller": "Horlance", "phone": "09046044472", "for": "ac car compressor noise cool", "desc": "Compressor repair & replacement"},
    {"name": "AC Leak Fixing", "price": 0, "cat": "Services", "seller": "Horlance", "phone": "09046044472", "for": "ac car leak gas", "desc": "Leak detection & fixing"},
    {"name": "Full AC Servicing", "price": 0, "cat": "Services", "seller": "Horlance", "phone": "09046044472", "for": "ac car servicing full", "desc": "Full AC system servicing"},
]

def mama_answer(q):
    q = q.lower().strip()
    # Find budget number: "5000", "5k", "10,000"
    budget = None
    nums = re.findall(r'(\d+)\s*k', q)
    if nums:
        budget = int(nums[0]) * 1000
    else:
        nums2 = re.findall(r'(\d{3,})', q.replace(",", ""))
        if nums2:
            budget = int(nums2[0])

    # 1. GREETING
    if any(w in q for w in ["hello", "hi", "good morning", "good afternoon", "how are you"]):
        return "🧕 Mama Oloja: Hello my pikin! Welcome to Row Economy Market. Wetin you dey find today? Tell me: 1) Product name 2) Your budget 3) Your area. E.g. 'I need serum under 5000 in Ikorodu' - I go help you sharp sharp!"

    # 2. FOOD - Jollof rice etc - WE DON'T HAVE YET - BE HONEST
    food_words = ["jollof", "rice", "food", "stew", "soup", "amala", "eba", "suya", "shawarma", "pizza", "burger", "chicken", "meat", "breakfast", "lunch", "eat", "hungry"]
    if any(w in q for w in food_words):
        return f"🧕 Mama Oloja: Ah! For '{q}' - Honest talk, we NO get food seller for Row Market YET. Na only Blessing (cosmetics) and Horlance (Car AC) we get now. BUT no worry! 👉 If you be food seller, join FREE now - 8 slots left! 👉 If you be buyer, tell me your area (Ikorodu? Osun?) and your budget, I go find food seller for you and add am. What area you dey?"

    # 3. CLOTHES / PHONES / SHOES - NOT YET
    if any(w in q for w in ["cloth", "dress", "shirt", "shoe", "sneaker", "bag", "wig", "hair"]):
        return f"🧕 Mama Oloja: For '{q}' - We no get clothes seller yet o. Na only cosmetics and Car AC we get. You want make I find clothes seller for you? Tell me your area + budget, or if YOU sell clothes, join FREE - 8 slots left! Tap 'Clothes' category to be first!"
    if any(w in q for w in ["phone", "iphone", "samsung", "laptop"]):
        return f"🧕 Mama Oloja: For '{q}' - We no get phone seller yet. Tell me which phone + your budget + your area, I go find am for you. Or if you sell phone, join FREE now!"

    # 4. CAR AC - Horlance
    if any(w in q for w in ["ac", "car", "cool", "horlance", "compressor", "gas"]):
        return "🧕 Mama Oloja: Ah! For Car AC, na Horlance be number 1! Dem dey Osun & Oyo State. Services: Gas Recharge, Compressor Repair, Leak Fixing, Full Servicing. Chat dem now - WhatsApp 09046044472, Call 09067551606. Tell dem Mama Oloja send you. Wetin be your car problem? Hot air? No gas? Noise?"

    # 5. SKIN CONCERN - PRESCRIBE
    if any(w in q for w in ["pimple", "acne", "dark spot", "dark mark"]):
        return "🧕 Mama Oloja: For pimple / dark spot, my pikin, do this: 1) Illuminating Serum ₦5,500 (for dark marks) 2) Acwell Toner ₦10,500 (for cleansing) 3) Biore Sunscreen ₦5,000 (MUST use, sun go darken am). Total if you take all 3: ₦21,000. If money small, start with Illuminating Serum ₦5,500 only. Chat Blessing - 07052528772. Tell her your skin type - oily or dry?"
    if "dry" in q:
        return "🧕 Mama Oloja: Dry skin? Take Ceramide Serum ₦5,000 + TONYMOLY Ceramide Toner ₦6,000 = ₦11,000. Dem go nourish and restore your skin. Avoid harsh soap. Chat Blessing - 07052528772"
    if "oily" in q:
        return "🧕 Mama Oloja: Oily skin? Take Face Serum ₦4,000 (light, no grease) + Biore Sunscreen ₦5,000 (light, no white cast). Total ₦9,000. Chat Blessing - 07052528772"
    if "sensitive" in q:
        return "🧕 Mama Oloja: Sensitive skin? Take Simple Soothing Toner ₦10,000 + Nivea Sun Sensitive ₦9,000 + Ceramide Serum ₦5,000. All gentle, no alcohol. Chat Blessing - 07052528772"

    # 6. SEARCH PRODUCTS BY KEYWORD + BUDGET
    matches = []
    for p in PRODUCTS_DB:
        # Check if any word in query matches product
        if any(word in p["name"].lower() or word in p["for"] for word in q.split() if len(word) > 2):
            if budget is None or p["price"] == 0 or p["price"] <= budget:
                matches.append(p)
    # Also direct category search
    if not matches:
        for p in PRODUCTS_DB:
            if any(w in q for w in p["name"].lower().split()):
                if budget is None or p["price"] == 0 or p["price"] <= budget:
                    matches.append(p)

    if matches:
        # Remove duplicates, sort by price
        seen = set(); uniq = []
        for m in matches:
            if m["name"] not in seen:
                seen.add(m["name"]); uniq.append(m)
        uniq = sorted(uniq, key=lambda x: x["price"])[:5]
        text = f"🧕 Mama Oloja: I find {len(uniq)} for you"
        if budget: text += f" under ₦{budget:,}"
        text += ":\n"
        for m in uniq:
            price_txt = f"₦{m['price']:,}" if m["price"] > 0 else "Chat for price"
            text += f"\n• {m['name']} - {price_txt} - {m['desc']} - {m['seller']} {m['phone']}"
        text += "\n\nWhich one you want? Tell me your budget and area, I go pick best one for you."
        return text

    # 7. BUDGET ONLY - "I have 5000"
    if budget:
        cheap = [p for p in PRODUCTS_DB if p["price"] > 0 and p["price"] <= budget]
        cheap = sorted(cheap, key=lambda x: x["price"])[:6]
        if cheap:
            text = f"🧕 Mama Oloja: With ₦{budget:,} you fit buy:\n"
            for m in cheap:
                text += f"\n• {m['name']} - ₦{m['price']:,} - {m['seller']} {m['phone']}"
            text += "\n\nWhich one you want? Chat seller now."
            return text

    # 8. PRICE / CHEAP / BEST
    if any(w in q for w in ["cheap", "cheapest", "affordable", "low price"]):
        return "🧕 Mama Oloja: Cheapest for you: Face Serum ₦4,000, Biore Sunscreen ₦5,000, Ceramide Serum ₦5,000, Nivea Men Lotion ₦5,000. All from Blessing - 07052528772. Which one you want?"
    if any(w in q for w in ["best", "recommend", "suggest"]):
        return "🧕 Mama Oloja: Best for most people: 1) Face Serum ₦4,000 (glow) 2) Biore Sunscreen ₦5,000 (protect) 3) TONYMOLY Toner ₦6,000 (soft skin). Tell me your skin concern - dry? oily? pimple? - I go recommend exact one for YOU."

    # 9. LOCATION
    if any(w in q for w in ["where", "location", "area", "ikorodu", "abuja", "lagos", "osun", "oyo"]):
        return "🧕 Mama Oloja: Blessing dey Ikorodu, Lagos / Abuja - 07052528772. Horlance dey Osun & Oyo - 09046044472. Where you dey? Tell me your area, I go tell you who near you."

    # 10. SELL / JOIN
    if any(w in q for w in ["sell", "seller", "join", "vendor", "shop"]):
        return "🧕 Mama Oloja: You want sell? Good! Join FREE for 1 month - Nov 6 to Dec 6 - 0% commission. 8 slots left. WhatsApp Admin, tell us wetin you sell + your area + your picture. We go verify you and add you. You fit sell food, clothes, phone, anything!"

    # 11. FALLBACK - NEVER USELESS - ASK 3 QUESTIONS
    return f"🧕 Mama Oloja: My pikin, I hear you - '{q}'. Help me help you well: 1) Wetin exactly you want? (serum, sunscreen, food, car AC, etc) 2) Your budget? (e.g. 5000) 3) Your area? (Ikorodu, Osun, Abuja?). Tell me those 3, I go give you exact answer + seller phone number. Or tap a Category below - Cosmetics = Blessing, Services = Horlance."

st.markdown("### 🧕 Ask Mama Oloja - She Sabi Everything Now")
st.markdown("Try: *'Jollof rice'* | *'I have pimple'* | *'I need serum under 5000'* | *'My car AC hot'*")
ask = st.text_input("Wetin you dey find?", placeholder="E.g. I need serum under 5000 in Ikorodu...")
if ask:
    st.success(mama_answer(ask))
    # Quick buttons to help
    col1, col2, col3 = st.columns(3)
    if col1.button("💄 Cosmetics"): st.session_state.category = "Cosmetics"; st.rerun()
    if col2.button("🧰 Car AC"): st.session_state.category = "Services"; st.rerun()
    if col3.button("💬 Chat Seller"): st.session_state.category = "Chat Rooms"; st.rerun()
