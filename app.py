for line in st.session_state.goods:
    p = line.split("|")
    seller = p[0]
    name = p[1
    price = p[2]
    loc = p[3]
    wa = p[4]
    cat = p[5]
    ver = p[6]
    skip = False
    if cat_now != "All" and cat != cat_now:
        skip = True
    if search and search.lower() not in name.lower() and search.lower() not in seller.lower():
        skip = True
    if skip:
        continue
    msg = urllib.parse.quote("Hello " + seller + ", I saw your " + name)
    link = "https://wa.me/234" + wa[1:] + "?text=" + msg
    img = "https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?w=400"
    if "AC" not in name:
        img = "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400"
    card = "<div style='background:white;margin:0 14px 16px 14px;padding:16px;border-radius:20px;box-shadow:0 4px 16px #EDEDED'>"
    card = card + "<div style='text-align:right'><span style='background:#00A651;color:white;padding:5px 12px;border-radius:20px;font-size:12px;font-weight:bold'>VERIFIED</span></div>"
    card = card + "<div style='display:flex;gap:12px'><div style='flex:1'><b style='font-size:17px;color:#111'>" + seller + "</b>"
    card = card + "<p style='color:#333;margin:8px 0'>Product: " + name + " - <b style='color:#00A651'>N" + price + "</b></p>"
    card = card + "<p style='color:#666;margin:6px 0'>Location: " + loc + "</p>"
    card = card + "<p style='color:#666;margin:6px 0'>WhatsApp: " + wa + "</p></div>"
    card = card + "<img src='" + img + "' style='width:140px;height:130px;object-fit:cover;border-radius:14px'>"
    card = card + "</div>"
    card = card + "<a href='" + link + "' style='display:block;background:#00A651;color:white;text-align:center;padding:12px;border-radius:14px;text-decoration:none;font-weight:bold;margin-top:12px;font-size:16px'>Chat on WhatsApp</a></div>"
    st.markdown(card, unsafe_allow_html=True)
