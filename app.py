import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="ROW Market",
    layout="wide"
)
st.header("ROW Economy Market - Abuja")

SHEET_CSV = st.secrets.get("SHEET_CSV", "")
WEBAPP_URL = st.secrets.get("WEBAPP_URL", "")

def clean_phone(p):
    s = str(p).strip()
    s = s.replace(" ", "")
    s = s.replace("-", "")
    s = s.replace("+", "")
    if s.endswith(".0"):
        s = s[:-2]
    if s.startswith("0"):
        s = "234" + s[1:]
    out = ""
    for c in s:
        if c.isdigit():
            out = out + c
    return out

def show_price(p):
    try:
        f = float(str(p).replace(",", ""))
        return str(int(f))
    except:
        return str(p)

def show_phone(p):
    s = str(p).strip()
    if s.endswith(".0"):
        s = s[:-2]
    return s

def load_products():
    if not SHEET_CSV:
        return pd.DataFrame()
    try:
        df = pd.read_csv(SHEET_CSV, dtype=str)
        df = df.fillna("")
        df.columns = [c.strip().lower() for c in df.columns]
        if "name" not in df.columns:
            return pd.DataFrame()
        df = df[df["name"].str.strip() != ""]
        df = df.drop_duplicates(
            subset=["name", "price", "location"],
            keep="last"
        )
        return df.reset_index(drop=True)
    except Exception as e:
        st.error("Load error: " + str(e))
        return pd.DataFrame()

products = load_products()

# MAP
st.subheader("LIVE MAP")
st.map(
    pd.DataFrame(
        {"lat": [9.066], "lon": [7.483]}
    )
)
if not products.empty:
    if "lat" in products.columns:
        mdf = products.copy()
        mdf["lat"] = pd.to_numeric(
            mdf["lat"], errors="coerce"
        )
        mdf["lon"] = pd.to_numeric(
            mdf["lon"], errors="coerce"
        )
        mdf = mdf.dropna(subset=["lat", "lon"])
        if not mdf.empty:
            st.map(mdf[["lat", "lon"]])

# SEARCH
st.subheader("Search by Location")
loc_search = st.text_input(
    "Type location e.g Wuse, Garki, Lagos",
    key="loc_search"
)
show_products = products
if loc_search:
    if not products.empty:
        mask = products["location"].str.contains(
            loc_search, case=False, na=False
        )
        show_products = products[mask]
        if show_products.empty:
            st.warning("No product for " + loc_search)
        else:
            st.success(
                "Found " + str(len(show_products))
            )

if show_products.empty:
    st.info("No products yet.")
else:
    rev = show_products.iloc[::-1]
    for _, row in rev.iterrows():
        nm = row.get("name", "")
        pr = row.get("price", "")
        loc = row.get("location", "")
        ph = row.get("phone", "")
        if str(ph).strip() == "":
            ph = row.get("whatsapp", "")
        title = "**" + str(nm) + " - N"
        title = title + show_price(pr)
        title = title + " - " + str(loc) + "**"
        st.write(title)
        st.write(str(loc))
        cl = clean_phone(ph)
        if cl:
            link = "https://wa.me/" + cl
            link = link + "?text=Hi, I want " + str(nm)
            btn = "WhatsApp " + show_phone(ph)
            st.link_button(btn, link)
        st.divider()

# ASK AI
st.subheader("Ask AI - Find Product")
if "q" not in st.session_state:
    st.session_state.q = ""
if "notfound" not in st.session_state:
    st.session_state.notfound = False

ai_q = st.text_input(
    "What do you need? e.g I need chicken",
    value=st.session_state.q,
    key="ai_input"
)
if st.button("Ask AI"):
    st.session_state.q = ai_q
    q = ai_q.lower().strip()
    stop = ["i", "need", "want", "for", "a", "an", "the"]
    words = []
    for w in q.split():
        if w not in stop:
            if len(w) > 2:
                words.append(w)
    found = pd.DataFrame()
    if words:
        if not products.empty:
            mask2 = pd.Series([False] * len(products))
            for w in words:
                m = products.astype(str).apply(
                    lambda x: x.str.contains(
                        w, case=False, na=False
                    )
                ).any(axis=1)
                m = m.reset_index(drop=True)
                mask2 = mask2 | m
            found = products[mask2]
    if not found.empty:
        st.session_state.notfound = False
        st.success("AI found " + str(len(found)))
        for _, r in found.iterrows():
            t2 = "**" + str(r.get("name", ""))
            t2 = t2 + " - N" + show_price(r.get("price", ""))
            t2 = t2 + " - " + str(r.get("location", "")) + "**"
            st.write(t2)
    else:
        st.session_state.notfound = True
        st.warning("Sorry, no " + ai_q + " yet.")

if st.session_state.notfound:
    st.subheader("Wait For It")
    w_name = st.text_input("Your Name", key="w_name")
    w_phone = st.text_input(
        "Your WhatsApp Number", key="w_phone"
    )
    if st.button("Notify Me on WhatsApp"):
        try:
            if WEBAPP_URL:
                data = {
                    "name": ai_q,
                    "price": "",
                    "location": "WAITLIST",
                    "phone": w_phone,
                    "whatsapp": w_phone,
                    "lat": "",
                    "lon": "",
                    "buyer_name": w_name
                }
                requests.post(
                    WEBAPP_URL, json=data, timeout=10
                )
            st.success("Saved! We will notify you.")
        except Exception as e:
            st.error("Could not save: " + str(e))

# POST
st.subheader("Post Product - Show on Map")
p_name = st.text_input(
    "Product Name e.g Beans 50kg", key="p_name"
)
p_price = st.text_input(
    "Price e.g 56588", key="p_price"
)
p_loc = st.text_input(
    "Location e.g Wuse, Abuja", key="p_loc"
)
p_phone = st.text_input(
    "Your WhatsApp Number", key="p_phone"
)
if st.button("Post Product"):
    if not p_name:
        st.warning("Fill Name, Price, Location")
    elif not p_price:
        st.warning("Fill Name, Price, Location")
    elif not p_loc:
        st.warning("Fill Name, Price, Location")
    else:
        try:
            if WEBAPP_URL:
                data2 = {
                    "name": p_name,
                    "price": p_price,
                    "location": p_loc,
                    "phone": p_phone,
                    "whatsapp": p_phone,
                    "lat": 9.066,
                    "lon": 7.483
                }
                requests.post(
                    WEBAPP_URL, json=data2, timeout=10
                )
            st.success("Posted! Refresh to see it.")
        except Exception as e:
            st.error("Could not post: " + str(e))
