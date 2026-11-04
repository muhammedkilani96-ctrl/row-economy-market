import streamlit as st
import pandas as pd
import uuid, io, datetime, hashlib, re
import qrcode
from urllib.parse import quote

st.set_page_config(page_title="Ilorin Game Fiesta 4.0", page_icon="🎲", layout="wide")

EVENT_NAME = "ILORIN GAME FIESTA 4.0 - The Legacy Continues"
EVENT_DATE = "Sunday, 15th Nov, 2026 - 2PM"
VENUE = "Succoth Valley Garden, GRA, Ilorin, Kwara State"
MANAGER_NAME = "KK Events - Manager"
MANAGER_WHATSAPP = "2347033642277"
MANAGER_DISPLAY = "+234 703 364 2277"
INSTAGRAM = "@ilorin_game_fiesta"
ORGANIZER = "KK_EVENTS"
ADMIN_PASSWORD = st.secrets.get("ADMIN_PASSWORD", "KK2026")

TICKETS = {
    "Early Bird - ₦1,500": {"price": 1500, "limit": 100, "desc": "Entry + All games. First 100 only."},
    "Regular - ₦2,500": {"price": 2500, "limit": 500, "desc": "Entry + Access to all games."},
    "VIP - ₦5,000": {"price": 5000, "limit": 50, "desc": "Front row + Free drink + Priority for games."},
    "Squad of 4 - ₦8,000": {"price": 8000, "limit": 100, "desc": "4 Regular tickets. Save ₦2,000. For friends."},
    "Vendor Stand - ₦10,000": {"price": 10000, "limit": 20, "desc": "Entry + 1 table to sell food, drinks, merch."},
}

def hash_password(password, salt=None):
    if salt is None:
        salt = uuid.uuid4().hex
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return salt + "$" + hashed

def verify_password(password, stored):
    try:
        parts = stored.split("$")
        salt = parts[0]
        hashed = parts[1]
        check = hashlib.sha256((salt + password).encode()).hexdigest()
        return check == hashed
    except:
        return False

def is_strong_password(pwd):
    if len(pwd) < 8:
        return False, "Password must be at least 8 characters."
    if not re.search(r"[0-9]", pwd):
        return False, "Password must contain at least 1 number."
    if not re.search(r"[A-Za-z]", pwd):
        return False, "Password must contain at least 1 letter."
    return True, "Strong password."

def clean_wa(num):
    n = num.strip().replace(" ", "").replace("-", "").replace("+", "")
    if n.startswith("0"):
        n = "234" + n[1:]
    return n

def wa_link(number, message):
    return "https://wa.me/" + number + "?text=" + quote(message)

def ai_reply(question):
    q = question.lower()
    if "date" in q or "when" in q or "day" in q:
        return "The event is on " + EVENT_DATE + "."
    if "where" in q or "venue" in q or "location" in q or "address" in q:
        return "Venue is " + VENUE + "."
    if "price" in q or "cost" in q or "how much" in q or "ticket" in q:
        return "Early Bird 1500, Regular 2500, VIP 5000, Squad of 4 is 8000, Vendor Stand 10000. Pick a ticket, login with WhatsApp, pay, you get QR instantly."
    if "game" in q or "play" in q:
        return "Games are Chess, Cards, Snooker / Pool, PlayStation, Monopoly."
    if "vendor" in q or "seller" in q or "sell" in q or "stand" in q:
        return "Vendors pay 10000 for a stand. Upload your product image, admin approves before it goes live."
    if "refund" in q or "return" in q:
        return "Tickets are non-refundable but transferable. You can give your QR to a friend."
    if "contact" in q or "phone" in q or "whatsapp" in q or "manager" in q or "human" in q:
        return "Call or WhatsApp Manager on " + MANAGER_DISPLAY + ". Or tap Talk to Manager button."
    return EVENT_NAME + " is on " + EVENT_DATE + " at " + VENUE + ". Tickets start at 1500 Early Bird. Regular 2500, VIP 5000, Squad of 4 8000. Want me to help you pick a ticket? If you need a human, tap Talk to Manager."

if "users_db" not in st.session_state:
    st.session_state.users_db = {}
if "tickets_sold" not in st.session_state:
    st.session_state.tickets_sold = []
if "vendor_products" not in st.session_state:
    st.session_state.vendor_products = []
if "chat" not in st.session_state:
    st.session_state.chat = []
if "user" not in st.session_state:
    st.session_state.user = None

st.markdown("# 🎲 " + EVENT_NAME)
st.markdown("**" + EVENT_DATE + " | " + VENUE + " | By " + ORGANIZER + "**")
st.markdown("Chess | Cards | Snooker | PlayStation | Monopoly | Music | Food")

manager_msg = "Hello Manager, I have a question about Ilorin Game Fiesta 4.0"
st.markdown("[💬 Talk To Manager Directly On WhatsApp](" + wa_link(MANAGER_WHATSAPP, manager_msg) + ")")
st.caption("Manager: " + MANAGER_NAME + " - " + MANAGER_DISPLAY + " | Instagram: " + INSTAGRAM)

if not st.session_state.user:
    st.info("🔐 Login is required to buy tickets or sell. Your password is encrypted and safe.")
    tab_login, tab_register = st.tabs(["Login", "Register - New Account"])
    with tab_login:
        wa_login = st.text_input("WhatsApp Number", placeholder="07033642277", key="login_wa")
        pwd_login = st.text_input("Password", type="password", key="login_pwd")
        if st.button("Login Securely", use_container_width=True):
            wa_clean = clean_wa(wa_login)
            found = st.session_state.users_db.get(wa_clean)
            if not found:
                st.error("No account with this WhatsApp number. Please Register first.")
            elif verify_password(pwd_login, found["password_hash"]):
                st.session_state.user = found
                st.success("Welcome back " + found["name"] + "!")
                st.rerun()
            else:
                st.error("Wrong password. Try again.")
        st.markdown("---")
        st.markdown("Forgot Password?")
        wa_forgot = st.text_input("Enter your WhatsApp number to reset", key="forgot_wa")
        if st.button("Reset Password via WhatsApp"):
            if wa_forgot:
                wa_c = clean_wa(wa_forgot)
                if wa_c in st.session_state.users_db:
                    reset_msg = "Hello, I forgot my password for Ilorin Game Fiesta. My WhatsApp is +" + wa_c + ". Please help me reset."
                    st.markdown("[Click here to message Manager to reset your password](" + wa_link(MANAGER_WHATSAPP, reset_msg) + ")")
                    st.info("Manager will verify you on WhatsApp and reset your password.")
                else:
                    st.error("No account found for that number.")
    with tab_register:
        r_name = st.text_input("Full Name", key="reg_name")
        r_wa = st.text_input("WhatsApp Number", placeholder="07033642277", key="reg_wa")
        r_role = st.selectbox("I am a:", ["Buyer", "Seller / Vendor"])
        r_pwd = st.text_input("Create Safe Password - 8+ chars, with number", type="password", key="reg_pwd")
        r_pwd2 = st.text_input("Confirm Password", type="password", key="reg_pwd2")
        agree = st.checkbox("I agree to event rules. Tickets are non-refundable but transferable.")
        if st.button("Create My Account - Safe & Secure", use_container_width=True):
            if not r_name or not r_wa or not r_pwd:
                st.error("Fill name, WhatsApp number and password.")
            elif r_pwd != r_pwd2:
                st.error("Passwords do not match.")
            elif not agree:
                st.error("Please tick agree to continue.")
            else:
                ok, msg = is_strong_password(r_pwd)
                if not ok:
                    st.error(msg)
                else:
                    wa_c = clean_wa(r_wa)
                    if wa_c in st.session_state.users_db:
                        st.error("This WhatsApp number already has an account. Please Login.")
                    else:
                        new_user = {
                            "name": r_name, "whatsapp": wa_c,
                            "whatsapp_display": "+" + wa_c,
                            "password_hash": hash_password(r_pwd),
                            "role": r_role,
                            "created": str(datetime.datetime.now())
                        }
                        st.session_state.users_db[wa_c] = new_user
                        st.session_state.user = new_user
                        st.success("Account created safely for " + r_name + "! You are logged in.")
                        st.rerun()
    st.markdown("---")
    st.markdown("### 🤖 Ask AI - No Login Needed")
    q = st.text_input("Ask anything: How much is VIP? Where is venue?", key="public_q")
    if st.button("Ask AI"):
        if q:
            st.success(ai_reply(q))
    st.stop()

user = st.session_state.user
st.success("✅ Logged in as " + user["name"] + " - " + user["whatsapp_display"] + " | Role: " + user["role"])
c_logout, c_manager = st.columns([1, 1])
with c_logout:
    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()
with c_manager:
    m_msg = "Hello Manager, I am " + user["name"] + " - I need help with my ticket"
    st.markdown("[💬 Talk To Manager](" + wa_link(MANAGER_WHATSAPP, m_msg) + ")")

tab_market, tab_sell, tab_mytickets, tab_ai, tab_admin = st.tabs(["🎟️ Buy Tickets", "🛍️ Sell / Vendor Post", "🎫 My Tickets", "🤖 Ask AI / Manager", "📊 Admin"])

with tab_market:
    st.subheader("Choose Your Ticket")
    for t_name, info in TICKETS.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**" + t_name + "**")
            st.caption(info["desc"])
        with col2:
            qty = st.number_input("Qty for " + t_name, min_value=0, max_value=10, key="qty_" + t_name)
            if qty > 0:
                total = qty * info["price"]
                st.write("Total: ₦" + format(total, ","))
                if st.button("Pay ₦" + format(total, ",") + " - " + t_name, key="pay_" + t_name):
                    code = str(uuid.uuid4())[:8].upper()
                    st.session_state.tickets_sold.append({
                        "code": code, "ticket": t_name, "qty": qty,
                        "total": total, "buyer_name": user.get("name"),
                        "buyer_whatsapp": user.get("whatsapp"),
                        "date": str(datetime.datetime.now())
                    })
                    st.success("Payment Successful! Your Ticket Code: " + code)
                    st.info("Screenshot this code. Show QR at gate.")
                    qr = qrcode.make("ILORIN-GAME-FIESTA-" + code + "-" + user.get("whatsapp"))
                    buf = io.BytesIO()
                    qr.save(buf, format="PNG")
                    st.image(buf.getvalue(), width=200, caption="Ticket " + code)
                    share_msg = "I just bought " + t_name + " for Ilorin Game Fiesta! My code is " + code
                    st.markdown("[Send Ticket To My WhatsApp](" + wa_link(user.get("whatsapp"), share_msg) + ")")

with tab_sell:
    st.subheader("Seller - Post Product Before Publishing")
    st.caption("Upload image. Admin must approve before buyers see it.")
    pname = st.text_input("Product Name - e.g. Shawarma, Merch, Game Pad")
    pprice = st.number_input("Price (₦)", min_value=0)
    pdesc = st.text_area("Description")
    pimg = st.file_uploader("Upload Product Image", type=["jpg", "png", "jpeg"])
    if st.button("Submit For Review"):
        if pname and pprice and pimg:
            st.session_state.vendor_products.append({
                "name": pname, "price": pprice, "desc": pdesc,
                "seller": user.get("whatsapp"), "seller_name": user.get("name"),
                "status": "Pending", "image": pimg
            })
            st.success("Submitted! Waiting for Admin approval. It is saved as Pending.")
        else:
            st.error("Add name, price and image.")
    st.markdown("### Approved Products For Event")
    approved = [p for p in st.session_state.vendor_products if p["status"] == "Approved"]
    if not approved:
        st.info("No approved products yet. Once Admin approves, they show here.")
    for p in approved:
        st.image(p["image"], width=200)
        st.write("**" + p["name"] + "** - ₦" + format(p["price"], ",") + " - by " + p["seller_name"])
        st.caption(p["desc"])

with tab_mytickets:
    st.subheader("My Tickets")
    mine = [t for t in st.session_state.tickets_sold if t["buyer_whatsapp"] == user.get("whatsapp")]
    if not mine:
        st.info("You have no tickets yet. Buy one above.")
        st.markdown("[Need help? Talk To Manager On WhatsApp](" + wa_link(MANAGER_WHATSAPP, "Hello Manager, I need help buying ticket") + ")")
    else:
        st.dataframe(pd.DataFrame(mine))

with tab_ai:
    st.subheader("🤖 Ask AI - Or Talk To Manager")
    st.caption("AI answers instantly 24/7. If you want a human, tap Talk to Manager.")
    st.markdown("[💬 Talk To Manager Directly On WhatsApp - " + MANAGER_DISPLAY + "](" + wa_link(MANAGER_WHATSAPP, "Hello Manager, I need help with Ilorin Game Fiesta") + ")")
    for msg in st.session_state.chat:
        st.write("**You:** " + msg["q"])
        st.write("**AI:** " + msg["a"])
    user_q = st.text_input("Ask AI anything about Ilorin Game Fiesta", key="ai_q")
    if st.button("Send to AI"):
        if user_q:
            ans = ai_reply(user_q)
            st.session_state.chat.append({"q": user_q, "a": ans})
            st.rerun()
    c1, c2, c3 = st.columns(3)
    if c1.button("How much is VIP?"):
        st.session_state.chat.append({"q": "How much is VIP?", "a": ai_reply("How much is VIP?")})
        st.rerun()
    if c2.button("Where is venue?"):
        st.session_state.chat.append({"q": "Where is venue?", "a": ai_reply("Where is venue?")})
        st.rerun()
    if c3.button("What games?"):
        st.session_state.chat.append({"q": "What games?", "a": ai_reply("What games?")})
        st.rerun()

with tab_admin:
    st.subheader("Admin - You Control Everything")
    admin_pass = st.text_input("Admin Password", type="password")
    if admin_pass == ADMIN_PASSWORD:
        st.markdown("### Pending Vendor Products")
        for i, p in enumerate(st.session_state.vendor_products):
            if p["status"] == "Pending":
                st.image(p["image"], width=150)
                st.write(p["name"] + " - ₦" + format(p["price"], ",") + " by " + p["seller_name"] + " (+" + p["seller"] + ")")
                col1, col2 = st.columns(2)
                if col1.button("Approve", key="ap_" + str(i)):
                    st.session_state.vendor_products[i]["status"] = "Approved"
                    st.rerun()
                if col2.button("Reject", key="rj_" + str(i)):
                    st.session_state.vendor_products[i]["status"] = "Rejected"
                    st.rerun()
        st.markdown("### All Tickets Sold")
        if st.session_state.tickets_sold:
            df = pd.DataFrame(st.session_state.tickets_sold)
            st.dataframe(df)
            st.metric("Total Revenue", "₦" + format(df["total"].sum(), ","))
            st.metric("Tickets Sold", len(df))
            st.download_button("Download All Buyers WhatsApp Numbers", df.to_csv(index=False), "buyers.csv", "text/csv")
        else:
            st.info("No tickets sold yet.")
    elif admin_pass:
        st.error("Wrong password.")
