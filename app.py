import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import time

st.set_page_config(
    page_title="Row Economy Market",
    layout="wide"
)

SHEET_ID = "1w8P3SQiChShHPQzShpgznR-lay-awTHmu_x-VHI9IU8E"
ADMIN_CODE = "ROW123"

if "my_orders" not in st.session_state:
    st.session_state.my_orders = []
if "seller_inbox" not in st.session_state:
    st.session_state.seller_inbox = []
if "local_goods" not in st.session_state:
    st.session_state.local_goods = []
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "cat" not in st.session_state:
    st.session_state.cat = "All"
if "my_name" not in st.session_state:
    st.session_state.my_name = ""
if "buyer_phone_temp" not in st.session_state:
    st.session_state.buyer_phone_temp = ""
if "referral_count" not in st.session_state:
    st.session_state.referral_count = 0
if "verified_sellers" not in st.session_state:
    st.session_state.verified_sellers = []
    st.session_state.verified_sellers.append("Horlance Auto Cooling Ltd")
    st.session_state.verified_sellers.append("Mama Ada")
if "chat_msgs" not in st.session_state:
    st.session_state.chat_msgs = []
    st.session_state.chat_msgs.append(
        {"room": "General", "user": "Mama Ada",
         "msg": "Welcome to Row Economy Market"}
    )
if "online_users" not in st.session_state:
    st.session_state.online_users = ["Mama Ada", "Horlance Auto", "Tunde"]
if "escrow_balance" not in st.session_state:
    st.session_state.escrow_balance = 0
if "my_earnings" not in st.session_state:
    st.session_state.my_earnings = 0

PAYSTACK_LINK = "https://paystack.shop/rowmarket"
BANK_NAME = "OPay / GTB"
ACCOUNT_NAME = "Row Economy Market - Horlance"
ACCOUNT_NUMBER = "9046044472"
COMMISSION = 0.05

@st.cache_data(ttl=30)
def load_sheet(sid):
    try:
        url = "https://docs.google.com/spreadsheets/d/"
        url = url + sid + "/export?format=csv"
        df = pd.read_csv(url)
        return df.dropna(subset=["Item"])
    except:
        return pd.DataFrame()

def get_goods():
    goods = []
    df = load_sheet(SHEET_ID)
    for _, r in df.iterrows():
        try:
            nm = str(r.get("Name", ""))
            it = str(r.get("Item", ""))
            pr = int(float(r.get("Price", 0)))
            ct = str(r.get("Category", ""))
            lc = str(r.get("Location", "Abuja"))
            ph = str(r.get("Phone", "2349046044472"))
            im = str(r.get("Image", ""))
            if im == "" or im == "nan":
                im = "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600"
            sp = str(r.get("SellerPic", ""))
            if sp == "" or sp == "nan":
                sp = "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100"
            vf = str(r.get("Verified", "")).upper() == "TRUE"
            goods.append(
                {"name": nm, "item": it, "price": pr,
                 "cat": ct, "loc": lc, "phone": ph,
                 "img": im, "seller_pic": sp, "verified": vf}
            )
        except:
            pass
    goods = st.session_state.local_goods + goods
    if len(goods) == 0:
        goods.append(
            {"name": "Horlance Auto Cooling Ltd",
             "item": "Car AC Repair",
             "price": 25000, "cat": "Car",
             "loc": "Osun & Oyo State",
             "img": "https://images.unsplash.com/photo-1625047509168-a7026f36de04?w=600",
             "phone": "2349046044472", "verified": True,
             "seller_pic": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100"}
        )
        goods.append(
            {"name": "Mama Ada",
             "item": "Bag of Rice 50kg",
             "price": 85000, "cat": "Food",
             "loc": "Wuse 2, Abuja",
             "img": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600",
             "phone": "2349046044472", "verified": True,
             "seller_pic": "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=100"}
        )
        goods.append(
            {"name": "Tunde Perfumes",
             "item": "Oud Perfume 100ml",
             "price": 15000, "cat": "Perfume",
             "loc": "Garki, Abuja",
             "img": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=600",
             "phone": "2349046044472", "verified": False,
             "seller_pic": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100"}
        )
        goods.append(
            {"name": "Chidi Phones",
             "item": "iPhone 12 - Neatly Used",
             "price": 280000, "cat": "Phones",
             "loc": "Wuse 2, Abuja",
             "img": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600",
             "phone": "2349046044472", "verified": False,
             "seller_pic": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100"}
        )
        goods.append(
            {"name": "Aisha Fashion",
             "item": "Ankara Gown",
             "price": 25000, "cat": "Clothes",
             "loc": "Gwarinpa, Abuja",
             "img": "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=600",
             "phone": "2349046044472", "verified": False,
             "seller_pic": "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=100"}
        )
    return goods

def delivery_fee(loc):
    if "Wuse" in loc:
        return 1500
    if "Garki" in loc:
        return 1500
    if "Gwarinpa" in loc:
        return 2000
    if "Osun" in loc or "Oyo" in loc:
        return 3000
    return 2500

def deal_price(p):
    return int(p * 0.88)

def open_cat(cat_name):
    st.session_state.cat = cat_name
    st.session_state.page = "Category"
    st.rerun()

st.title("Row Economy Market")
st.caption("Buy and Sell Free - Escrow Protected")
st.divider()

buyer_name = st.session_state.my_name
buyer_phone = st.session_state.buyer_phone_temp
page = st.session_state.page
current_cat = st.session_state.cat

CAT_DESC = {
    "Food": "Rice, Garri, Oil, Fresh Food",
    "Phones": "iPhone, Samsung, Accessories",
    "Perfume": "Oud, Designer Perfumes",
    "Clothes": "Ankara, Gowns, Shirts",
    "Car": "Car AC, Repairs, Car Sales",
    "Services": "Plumber, Electrician, Hair",
    "Tickets": "Event, Flight, Bus Tickets",
    "Chat": "Talk to Sellers",
}

def show_category_page(cat_name):
    st.header(cat_name + " Market")
    st.caption("Row Economy Market - " + cat_name + " ONLY")
    st.caption("USAGE: You see ONLY " + cat_name + " here.")
    st.caption("DESC: " + CAT_DESC.get(cat_name, ""))
    if st.button("Back to Home - See All Categories"):
        st.session_state.page = "Home"
        st.session_state.cat = "All"
        st.rerun()
    st.caption("USAGE: Back button goes to Home.")
    search_in_cat = st.text_input("Search in " + cat_name + " only")
    st.caption("USAGE: Type to find inside " + cat_name + " only.")
    st.subheader("POST YOUR " + cat_name.upper() + " PRODUCT - FREE")
    st.caption("USAGE: Your product shows ONLY in " + cat_name + " page.")
    with st.expander("TAP TO POST IN " + cat_name.upper()):
        p_name = st.text_input("Your Name", value=buyer_name)
        p_item = st.text_input("What are you selling in " + cat_name + "?")
        p_price = st.number_input("Price (Naira)", min_value=0)
        p_loc = st.text_input("Location")
        p_phone = st.text_input("Your WhatsApp", value=buyer_phone)
        st.write("STEP 1 - Product Photo")
        uploaded = st.file_uploader("Upload Product Photo", type=["jpg", "png", "jpeg"])
        p_img_link = st.text_input("OR Paste Product Photo Link")
        img_to_use = "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600"
        if uploaded is not None:
            st.image(uploaded, caption="Product preview", width=200)
        if p_img_link:
            img_to_use = p_img_link
        st.write("STEP 2 - YOUR FACE / SHOP PIC (NEW)")
        st.caption("USAGE: Buyers trust sellers they can see.")
        st.caption("Paste your face photo link, or upload below.")
        seller_uploaded = st.file_uploader("Upload Your Face / Shop Photo", type=["jpg", "png", "jpeg"], key="seller_pic_" + cat_name)
        seller_pic_link = st.text_input("OR Paste Your Face Photo Link", key="seller_link_" + cat_name)
        seller_pic_to_use = "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100"
        if seller_uploaded is not None:
            st.image(seller_uploaded, caption="Your face preview", width=100)
        if seller_pic_link:
            seller_pic_to_use = seller_pic_link
        if st.button("POST IN " + cat_name.upper() + " NOW"):
            if p_name and p_item and p_price > 0:
                is_ver = p_name in st.session_state.verified_sellers
                st.session_state.local_goods.insert(
                    0,
                    {"name": p_name, "item": p_item,
                     "price": int(p_price), "cat": cat_name,
                     "loc": p_loc or "Abuja",
                     "phone": p_phone or "2349046044472",
                     "img": img_to_use,
                     "seller_pic": seller_pic_to_use,
                     "verified": is_ver}
                )
                st.success("Posted in " + cat_name + "!")
                st.success("Your face pic will show on your product.")
                st.balloons()
                st.rerun()
            else:
                st.error("Fill Name, Product, Price - all 3 needed.")
    all_goods = get_goods()
    filtered = []
    for g in all_goods:
        if g["cat"].lower().strip() != cat_name.lower().strip():
            continue
        if search_in_cat:
            txt = g["item"] + g["name"] + g["loc"]
            if search_in_cat.lower() not in txt.lower():
                continue
        filtered.append(g)
    st.info("Showing " + str(len(filtered)) + " products in " + cat_name + " - ONLY " + cat_name)
    if len(filtered) == 0:
        st.write("No products in " + cat_name + " yet.")
        st.write("Be the first to post in " + cat_name + " above!")
    st.subheader("All " + cat_name + " Products")
    st.caption("USAGE: Each card = 1 seller. Tap ORDER to buy with Escrow.")
    delivery_loc = st.selectbox(
        "Your Delivery Area",
        ["Wuse 2, Abuja", "Garki, Abuja", "Gwarinpa, Abuja",
         "Osun & Oyo", "Abuja", "Pickup Only"]
    )
    st.caption("USAGE: Choose where rider will deliver.")
    payment = st.selectbox(
        "Pay with",
        ["Escrow - Paystack (Safest)",
         "Pay on Delivery (Cash)",
         "Bank Transfer to Row Economy Market"]
    )
    st.caption("USAGE: Escrow = safest, we hold money.")
    if payment == "Bank Transfer to Row Economy Market":
        st.success("Transfer: " + BANK_NAME)
        st.success("Name: " + ACCOUNT_NAME)
        st.success("Number: " + ACCOUNT_NUMBER)
    if "Escrow" in payment:
        st.link_button("Pay Safely via Escrow", PAYSTACK_LINK)
    for idx, g in enumerate(filtered):
        st.divider()
        st.image(g["img"], width=350)
        st.caption("Product photo above")
        st.image(g.get("seller_pic", ""), width=80)
        st.caption("Seller face / shop pic above - Buy from real people")
        st.subheader(g["item"])
        st.write("Seller: " + g["name"])
        if g["name"] in st.session_state.verified_sellers or g["verified"]:
            st.success("VERIFIED Seller")
        else:
            st.write("New Seller - Ask Admin to verify")
        st.write("Category: " + g["cat"])
        st.write("Location: " + g["loc"])
        fee = delivery_fee(delivery_loc)
        base = deal_price(g["price"])
        discount = 0
        if st.session_state.referral_count >= 3:
            discount = 500
        total = base + fee - discount
        if base >= 100000:
            total = base - discount
        if total < 0:
            total = 0
        comm = int(total * COMMISSION)
        seller_gets = int(total - comm)
        st.write("Old Price: N" + str(g["price"]))
        st.write("Deal Price: N" + str(base))
        st.write("Total with delivery: N" + str(total))
        st.caption("Escrow: N" + str(comm) + " to Market.")
        st.caption("Seller gets: N" + str(seller_gets))
        if st.button("Chat Seller - Talk before you buy", key="chat_" + cat_name + "_" + str(idx)):
            st.session_state.page = "Profile"
            st.rerun()
        if st.button("ORDER NOW - Escrow N" + str(total), key="order_" + cat_name + "_" + str(idx)):
            if not buyer_name or not buyer_phone:
                st.error("Set Name + WhatsApp on Home first.")
            else:
                order = {
                    "buyer": buyer_name,
                    "buyer_phone": buyer_phone,
                    "seller": g["name"],
                    "seller_phone": g["phone"],
                    "item": g["item"],
                    "price": base,
                    "total": total,
                    "delivery": delivery_loc,
                    "payment": payment,
                    "status": "Pending",
                    "tracking": "Pending - Waiting Seller",
                    "commission": comm,
                    "seller_gets": seller_gets,
                }
                st.session_state.my_orders.append(order)
                st.session_state.seller_inbox.append(order)
                st.session_state.escrow_balance += total
                st.success("Order placed in " + cat_name + "!")
                st.success("Escrow held. Seller will reply YES / NO.")
                st.balloons()
        msg = "Hello " + g["name"]
        msg = msg + ", Row Economy Market NEW ORDER in "
        msg = msg + cat_name + ": " + g["item"]
        msg = msg + " Total N" + str(total)
        msg = msg + " Buyer " + buyer_name + " - " + buyer_phone
        msg = msg + ". Reply YES / NO."
        link = "https://wa.me/" + g["phone"]
        link = link + "?text=" + urllib.parse.quote(msg)
        st.link_button("Notify Seller on WhatsApp", link)
        st.caption("USAGE: Tell seller you ordered.")

if page == "Home":
    st.success("DEAL OF THE DAY - 12% OFF - Use code ROW12")
    with st.expander("Your Details - Tap to set Name and WhatsApp"):
        st.caption("USAGE: Set your name once. Orders and Chat use this name.")
        my_name_input = st.text_input("Your Name", value=st.session_state.my_name)
        if my_name_input and my_name_input != st.session_state.my_name:
            st.session_state.my_name = my_name_input
            if my_name_input not in st.session_state.online_users:
                st.session_state.online_users.append(my_name_input)
            st.rerun()
        buyer_phone_input = st.text_input("Your WhatsApp Number", value=st.session_state.buyer_phone_temp)
        st.session_state.buyer_phone_temp = buyer_phone_input
        st.write("Referral invites: " + str(st.session_state.referral_count))
        st.caption("Invite 3 friends, get N500 off.")
        if st.button("I Invited a Friend +1"):
            st.session_state.referral_count += 1
            st.rerun()
        st.caption("USAGE: Tap after you invite a friend.")
        st.write("You are: " + (st.session_state.my_name or "Guest"))
    search_q = st.text_input("Search - Ask Mama Oloja")
    st.caption("USAGE: Type Rice, iPhone, Perfume to find it fast.")
    st.header("Categories")
    st.write("Tap any button - it opens its OWN page with ONLY that category.")
    st.info("HOW TO USE: 1. Tap category 2. See ONLY that category 3. Tap ORDER 4. Tap Back to Home")
    if st.button("Perfume - Tap to see ONLY Perfumes"):
        open_cat("Perfume")
    st.caption("Perfume: Oud, Designer Perfumes")
    if st.button("Clothes - Tap to see ONLY Clothes"):
        open_cat("Clothes")
    st.caption("Clothes: Ankara, Gowns, Shirts")
    if st.button("Phones - Tap to see ONLY Phones"):
        open_cat("Phones")
    st.caption("Phones: iPhone, Samsung")
    if st.button("Food - Tap to see ONLY Food"):
        open_cat("Food")
    st.caption("Food: Rice, Garri, Oil")
    if st.button("Car Mart - Tap to see ONLY Cars"):
        open_cat("Car")
    st.caption("Car Mart: Car AC, Repairs")
    if st.button("Services - Tap to see ONLY Services"):
        open_cat("Services")
    st.caption("Services: Plumber, Hair, Makeup")
    if st.button("Tickets - Tap to see ONLY Tickets"):
        open_cat("Tickets")
    st.caption("Tickets: Events, Flights")
    if st.button("Chat Rooms - Tap to chat with sellers"):
        open_cat("Chat")
    st.caption("Chat Rooms: Talk to Mama Oloja")
    st.header("Preview")
    st.caption("USAGE: Quick preview. Tap Open Page for full market.")
    all_goods = get_goods()
    for g in all_goods[:3]:
        st.image(g["img"], width=350)
        st.write(g["name"] + " - " + g["item"] + " - " + g["cat"])
        st.write("Price: N" + str(deal_price(g["price"])))
        if st.button("Open " + g["cat"] + " Page", key="open_" + g["cat"] + "_" + g["item"][:4]):
            open_cat(g["cat"])

if page == "Category":
    show_category_page(current_cat)

if page == "Shop":
    st.header("Shop")
    st.caption("USAGE: Shop = Home. Tap Go Home to see categories.")
    if st.button("Go Home"):
        st.session_state.page = "Home"
        st.rerun()

if page == "Orders":
    st.header("My Orders + Tracking")
    st.caption("USAGE: See what you ordered. When delivered, tap Confirm to release Escrow.")
    if len(st.session_state.my_orders) == 0:
        st.info("No orders yet. Go Home, tap Category, tap ORDER NOW.")
    for oi, o in enumerate(st.session_state.my_orders):
        st.divider()
        st.write("Item: " + o["item"])
        st.write("Seller: " + o["seller"])
        st.write("Total: N" + str(o.get("total", o["price"])))
        st.write("Tracking: " + o.get("tracking", ""))
        st.write("Status: " + o["status"])
        if o["status"] == "Available":
            if st.button("Confirm Delivery - Release Escrow", key="confirm_" + str(oi)):
                st.session_state.escrow_balance -= o.get("total", 0)
                st.session_state.my_earnings += o.get("commission", 0)
                o["status"] = "Delivered"
                o["tracking"] = "Delivered - Escrow Released"
                st.success("Delivered! Escrow released.")
                st.rerun()
    st.header("Seller Inbox")
    st.caption("USAGE: Seller, type your WhatsApp to see orders for you.")
    st.caption("Tap YES if you have it, NO if sold out.")
    seller_check = st.text_input("Your Seller WhatsApp")
    if seller_check:
        inbox = []
        for o in st.session_state.seller_inbox:
            if seller_check in o["seller_phone"]:
                inbox.append(o)
        if len(inbox) == 0:
            st.info("No orders for this number yet.")
        for j, o in enumerate(inbox):
            st.divider()
            st.write("NEW ORDER Buyer: " + o["buyer"])
            st.write("Wants: " + o["item"])
            st.write("Total: N" + str(o.get("total", o["price"])))
            st.write("Tracking: " + o.get("tracking", ""))
            if st.button("YES I Have It", key="yes_" + str(j)):
                o["status"] = "Available"
                o["tracking"] = "Packed - Waiting Rider"
                for mo in st.session_state.my_orders:
                    if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                        mo["status"] = "Available"
                        mo["tracking"] = "Packed - Waiting Rider"
                st.rerun()
            if st.button("NO Sold Out", key="no_" + str(j)):
                o["status"] = "Sold Out"
                o["tracking"] = "Sold Out"
                for mo in st.session_state.my_orders:
                    if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                        mo["status"] = "Sold Out"
                        mo["tracking"] = "Sold Out"
                st.rerun()
            if o["status"] == "Available":
                if st.button("Rider Picked Up", key="rider_" + str(j)):
                    o["tracking"] = "On The Way - Rider Picked Up"
                    for mo in st.session_state.my_orders:
                        if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                            mo["tracking"] = "On The Way - Rider Picked Up"
                    st.rerun()
                if st.button("Mark Delivered", key="deliv_" + str(j)):
                    o["tracking"] = "Delivered - Waiting Buyer Confirmation"
                    for mo in st.session_state.my_orders:
                        if mo["item"] == o["item"] and mo["buyer"] == o["buyer"]:
                            mo["tracking"] = "Delivered - Waiting Buyer Confirmation"
                    st.rerun()

if page == "Profile":
    st.header("Profile + Chat")
    st.caption("USAGE: See your name, escrow, earnings. Chat below.")
    st.write("Name: " + (buyer_name or "Guest"))
    st.write("Phone: " + (buyer_phone or "No number"))
    st.write("Escrow Held: N" + str(st.session_state.escrow_balance))
    st.write("Your Earnings: N" + str(st.session_state.my_earnings))
    st.write("Online: " + ", ".join(st.session_state.online_users))
    if st.button("Go to Home to Set Name"):
        st.session_state.page = "Home"
        st.rerun()
    if st.checkbox("Auto-refresh chat", value=True):
        time.sleep(8)
        st.rerun()
    tab1, tab2 = st.tabs(["General", "DM"])
    with tab1:
        st.caption("USAGE: Chat with everyone here.")
        for m in st.session_state.chat_msgs:
            if m["room"] == "General":
                st.write(m["user"] + ": " + m["msg"])
        msg = st.text_input("Type message")
        if st.button("Send"):
            if not buyer_name:
                st.error("Go Home, set Name first.")
            elif msg:
                st.session_state.chat_msgs.append(
                    {"room": "General", "user": buyer_name, "msg": msg}
                )
                st.rerun()
    with tab2:
        st.caption("USAGE: Private chat with one person.")
        dm_with = st.selectbox("Chat with", st.session_state.online_users)
        dm_room = "DM_" + dm_with
        for m in st.session_state.chat_msgs:
            if m["room"] == dm_room:
                st.write(m["user"] + ": " + m["msg"])
        dm_msg = st.text_input("DM message")
        if st.button("Send DM"):
            if not buyer_name:
                st.error("Go Home, set Name first.")
            elif dm_msg:
                st.session_state.chat_msgs.append(
                    {"room": dm_room, "user": buyer_name, "msg": dm_msg}
                )
                st.rerun()

if page == "Admin":
    st.header("Admin Panel - Row Economy Market")
    st.caption("USAGE: Only YOU as owner can open this. Control sellers and orders.")
    admin_input = st.text_input("Enter Admin Code", type="password")
    if admin_input == "":
        st.info("Enter code to unlock Admin. Your code is ROW123. Change it in code later.")
    elif admin_input != ADMIN_CODE:
        st.error("Wrong code. Try again.")
    else:
        st.success("Welcome Admin - Horlance")
        st.write("Escrow Held: N" + str(st.session_state.escrow_balance))
        st.write("Your Earnings: N" + str(st.session_state.my_earnings))
        st.write("Total Orders: " + str(len(st.session_state.my_orders)))
        st.write("Total Products: " + str(len(get_goods())))
        st.subheader("All Orders - Admin Control")
        st.caption("USAGE: See every order. Delete fake orders.")
        for oi, o in enumerate(st.session_state.my_orders):
            st.divider()
            st.write("Buyer: " + o["buyer"] + " - " + o.get("buyer_phone", ""))
            st.write("Seller: " + o["seller"])
            st.write("Item: " + o["item"] + " - N" + str(o.get("total", o["price"])))
            st.write("Status: " + o["status"] + " - " + o.get("tracking", ""))
            if st.button("Delete This Order", key="admin_del_order_" + str(oi)):
                st.session_state.my_orders.pop(oi)
                st.rerun()
        st.subheader("All Products - Admin Control")
        st.caption("USAGE: Delete fake products. Verify good sellers.")
        all_g = get_goods()
        for gi, g in enumerate(all_g):
            st.divider()
            st.image(g["img"], width=200)
            st.write(g["name"] + " - " + g["item"] + " - " + g["cat"])
            st.write("Price: N" + str(g["price"]) + " - " + g["loc"])
            if g["name"] in st.session_state.verified_sellers:
                st.success("VERIFIED")
            else:
                st.write("Not Verified")
            if st.button("Verify This Seller", key="admin_verify_" + str(gi)):
                if g["name"] not in st.session_state.verified_sellers:
                    st.session_state.verified_sellers.append(g["name"])
                st.success(g["name"] + " is now VERIFIED")
                st.rerun()
            if st.button("Delete This Product", key="admin_del_prod_" + str(gi)):
                found = False
                for lg in list(st.session_state.local_goods):
                    if lg["item"] == g["item"] and lg["name"] == g["name"]:
                        st.session_state.local_goods.remove(lg)
                        found = True
                if not found:
                    st.info("Demo product - cannot delete demo. Delete from Google Sheet.")
                else:
                    st.success("Deleted")
                st.rerun()
        st.subheader("Verified Sellers List")
        st.write(", ".join(st.session_state.verified_sellers))

st.divider()
st.write("You are on: " + page)
st.caption("USAGE: Home = Categories, Shop = Home, Orders = Your orders, Profile = Chat, Admin = Owner only")
nav = st.segmented_control(
    "Nav",
    ["Home", "Shop", "Orders", "Profile", "Admin"],
    selection_mode="single",
    default="Home" if page == "Category" else page,
    label_visibility="collapsed"
)
if nav and nav != st.session_state.page:
    st.session_state.page = nav
    st.rerun()
st.link_button("Share Row Economy Market", "https://wa.me/?text=Check%20Row%20Economy%20Market%20-%20Post%20FREE")
st.caption("USAGE: Share app to friends on WhatsApp.")
