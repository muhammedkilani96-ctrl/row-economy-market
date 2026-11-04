import streamlit as st
from supabase import create_client
import pandas as pd
import uuid

st.set_page_config(
    page_title="ROW ECONOMY",
    layout="wide"
)

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(URL, KEY)

st.markdown(
    "<style>.block-container{max-width:700px;"
    "margin:auto;} .stButton>button{width:100%;"
    "height:48px;border-radius:12px;"
    "font-weight:600;} footer{visibility:hidden;}"
    "#MainMenu{visibility:hidden;}</style>",
    unsafe_allow_html=True
)

if 'logged' not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    st.title("ROW ECONOMY")
    st.caption("Abuja Live Marketplace")
    with st.container(border=True):
        phone = st.text_input(
            "Phone",
            value="08116911722"
        )
        pwd = st.text_input(
            "Password",
            type="password",
            value="Kilani247"
        )
        if st.button(
            "Login",
            type="primary",
            use_container_width=True
        ):
            if phone.strip() == "08116911722":
                if pwd.strip().lower() == "kilani247":
                    st.session_state.logged = True
                    st.session_state.phone = phone
                    st.rerun()
                else:
                    st.error("Wrong login")
            else:
                st.error("Wrong login")
    st.stop()

phone = st.session_state.phone
st.markdown(f"Welcome {phone} | Coins 5000 | Abuja")
st.divider()

try:
    products = supabase.table(
        "products"
    ).select("*").order(
        "created_at",
        desc=True
    ).execute().data
except Exception:
    products = []

try:
    lives = supabase.table(
        "live_sessions"
    ).select("*").eq(
        "is_live", True
    ).execute().data
except Exception:
    lives = []

tabs = st.tabs(
    ["LIVE MARKET",
     "POST PRODUCT",
     "GO LIVE",
     "MAP",
     "Wallet"]
)

# LIVE MARKET
with tabs[0]:
    st.markdown("## LIVE MARKETPLACE")
    search = st.text_input(
        "Search",
        placeholder="Search rice, yam, oil..."
    )
    cat_list = [
        "All",
        "Food",
        "Fashion",
        "Electronics",
        "Other"
    ]
    cat = st.selectbox(
        "Category",
        cat_list
    )
    filtered = products
    if search:
        filtered = [
            p for p in filtered
            if search.lower() in str(
                p.get('name', '')
            ).lower()
        ]
    if not filtered:
        st.info("No product yet.")
    cols = st.columns(2)
    for i, p in enumerate(filtered):
        with cols[i % 2]:
            with st.container(border=True):
                if p.get('image_url'):
                    st.image(
                        p['image_url'],
                        use_container_width=True
                    )
                st.markdown(
                    f"**{p.get('name', 'No name')}**"
                )
                st.markdown(
                    f"### N{p.get('price', 0):,}"
                )
                st.caption(
                    str(p.get('description', ''))[:80]
                )
                st.markdown("Star 5.0 | Wuse Market")
                b1, b2 = st.columns(2)
                with b1:
                    if st.button(
                        "Buy Now",
                        key=f"buy{p['id']}",
                        type="primary"
                    ):
                        st.balloons()
                with b2:
                    msg = f"Hello I want {p.get('name')}"
                    st.link_button(
                        "WhatsApp",
                        f"https://wa.me/2348116911722?text={msg}"
                    )

# POST PRODUCT
with tabs[1]:
    st.markdown("## Post Product")
    st.info("Pic + Description compulsory")
    with st.form("post_form", clear_on_submit=True):
        name = st.text_input("Product Name*")
        price = st.number_input(
            "Price (N)*",
            value=1000,
            min_value=0
        )
        desc = st.text_area("Description*")
        pic = st.file_uploader(
            "Product Picture*",
            type=['jpg', 'png', 'jpeg']
        )
        if st.form_submit_button(
            "Post Product",
            type="primary",
            use_container_width=True
        ):
            if not name or not desc or not pic:
                st.error("Name + Desc + Pic needed!")
            else:
                try:
                    fname = f"{uuid.uuid4()}_{pic.name}"
                    supabase.storage.from_(
                        "product_images"
                    ).upload(
                        fname,
                        pic.getvalue()
                    )
                    image_url = supabase.storage.from_(
                        "product_images"
                    ).get_public_url(fname)
                    supabase.table(
                        "products"
                    ).insert(
                        {
                            "name": name,
                            "price": price,
                            "description": desc,
                            "image_url": image_url
                        }
                    ).execute()
                    st.success("Posted!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")

# GO LIVE
with tabs[2]:
    st.markdown("## GO LIVE - Earn Coins")
    if lives:
        st.success("LIVE NOW - 124 watching")
    st.markdown("### Send Coin Gift")
    g1, g2 = st.columns(2)
    with g1:
        if st.button("Rose - 10"):
            st.balloons()
    with g2:
        if st.button("Fire - 50"):
            st.balloons()
    g3, g4 = st.columns(2)
    with g3:
        if st.button("Lion - 100"):
            st.balloons()
    with g4:
        if st.button("Diamond - 500"):
            st.balloons()
    st.divider()
    st.markdown("### Your Live Camera")
    cam = st.camera_input("Take Photo")
    title = st.text_input(
        "Live Title",
        "Selling in Wuse - Send Coins!"
    )
    s1, s2 = st.columns(2)
    with s1:
        if st.button("Start Live", type="primary"):
            supabase.table(
                "live_sessions"
            ).insert(
                {
                    "phone": phone,
                    "title": title,
                    "is_live": True
                }
            ).execute()
            st.rerun()
    with s2:
        if st.button("End Live"):
            supabase.table(
                "live_sessions"
            ).delete().eq(
                "phone", phone
            ).execute()
            st.rerun()

# MAP
with tabs[3]:
    st.markdown("## SNAP MAP - Abuja")
    st.map(
        pd.DataFrame(
            {
                'lat': [9.0765, 9.08, 9.09],
                'lon': [7.3986, 7.40, 7.42]
            }
        ),
        zoom=12
    )
    st.markdown("### SOS")
    if st.button(
        "SEND SOS - I NEED HELP",
        type="primary",
        use_container_width=True
    ):
        st.error("SOS Sent to Security")

# WALLET
with tabs[4]:
    st.markdown("## Wallet")
    w1, w2 = st.columns(2)
    with w1:
        st.metric("Naira Balance", "N500,000")
    with w2:
        st.metric("Coins", "5000")

st.divider()
if st.button("Logout", use_container_width=True):
    st.session_state.logged = False
    st.rerun()
