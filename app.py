df = load_data()
products = pd.DataFrame()
waitlist = pd.DataFrame()
if not df.empty and "location" in df.columns:
    products = df[df["location"].astype(str).str.upper() != "WAITLIST"].copy()
    waitlist = df[df["location"].astype(str).str.upper() == "WAITLIST"].copy()
    products = products.drop_duplicates(subset=["name", "price", "location"], keep="last")

st.header("LIVE MAP - Abuja")
st.map(pd.DataFrame({"lat": [9.066], "lon": [7.483]}))

if products.empty:
    st.info("No products yet. Be the first to post!")
else:
    for _, row in products.iloc[::-1].iterrows():
        nm = row.get("name", "")
        pr = row.get("price", "")
        loc = row.get("location", "")
        ph = row.get("phone", "")
        if pd.isna(ph) or str(ph) == "":
            ph = row.get("whatsapp", "")
        st.write("**" + str(nm) + " - N" + show_price(pr) + " - " + str(loc) + "**")
        st.write(str(loc))
        cl = clean_phone(ph)
        if cl:
            st.link_button("WhatsApp " + show_phone(ph), "https://wa.me/" + cl + "?text=Hi, I want " + str(nm))
        st.divider()
