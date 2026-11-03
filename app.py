import streamlit as st
import requests
import uuid

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
HEADERS = {"apikey": KEY, "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

st.set_page_config(page_title="Row Economy Market", layout="wide")
st.title("Row Economy Market - PERMANENT")

tab1, tab2 = st.tabs(["Market", "Sell"])

with tab1:
    st.subheader("Products")
    try:
        r = requests.get(f"{URL}/rest/v1/products?select=*&order=id.desc", headers=HEADERS, timeout=20)
        if r.status_code == 200:
            products = r.json()
            if not products:
                st.info("No products yet")
            else:
                cols = st.columns(3)
                for i, p in enumerate(products):
                    with cols[i % 3]:
                        img = p.get("image_url","")
                        if img:
                            if img.endswith((".mp4",".mov",".webm")):
                                st.video(img)
                            else:
                                st.image(img, use_container_width=True)
                        st.write(f"**{p.get('name','')}** - ₦{p.get('price','')}")
                        st.caption(p.get("description",""))
                        wa = p.get("whatsapp","")
                        if wa:
                            st.link_button("Chat Seller", f"https://wa.me/{wa}?text=Hi I want {p.get('name','')}")
                        st.divider()
        else:
            st.error(f"Failed to load: {r.text}")
    except Exception as e:
        st.error(f"Error: {e}")

with tab2:
    st.subheader("Post Product + Pic/Video")
    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0)
    desc = st.text_area("Description")
    whatsapp = st.text_input("WhatsApp 234...")
    seller = st.text_input("Shop Name")
    up_file = st.file_uploader("Upload Picture or Video DIRECTLY from phone", type=["jpg","jpeg","png","mp4","mov","webm"])

    if st.button("Post Product"):
        if not name or not whatsapp:
            st.warning("Fill product name and WhatsApp!")
        else:
            image_url = ""
            if up_file is not None:
                try:
                    ext = up_file.name.split(".")[-1]
                    fname = f"{uuid.uuid4()}.{ext}"
                    # Upload to storage bucket
                    storage_headers = {"apikey": KEY, "Authorization": f"Bearer {KEY}", "Content-Type": up_file.type}
                    up_res = requests.post(f"{URL}/storage/v1/object/product-images/{fname}", headers=storage_headers, data=up_file.getvalue(), timeout=30)
                    if up_res.status_code in [200,201]:
                        image_url = f"{URL}/storage/v1/object/public/product-images/{fname}"
                    else:
                        st.error(f"Storage upload failed: {up_res.text}. Did you create bucket 'product-images' as PUBLIC?")
                        st.stop()
                except Exception as e:
                    st.error(f"Upload error: {e}")
                    st.stop()
            
            data = {"name": name, "price": price, "description": desc, "whatsapp": whatsapp, "seller_name": seller, "image_url": image_url}
            try:
                post_r = requests.post(f"{URL}/rest/v1/products", headers=HEADERS, json=data, timeout=20)
                if post_r.status_code in [200,201]:
                    st.success("✅ Product posted permanently!")
                    st.balloons()
                else:
                    st.error(f"Failed: {post_r.text}")
            except Exception as e:
                st.error(f"Error: {e}")
