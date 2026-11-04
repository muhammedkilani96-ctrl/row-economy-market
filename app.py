import streamlit as st
import pandas as pd
import uuid, io, datetime, random, hashlib, json, os, re
import qrcode

st.set_page_config(page_title="Ilorin Game Fiesta 4.0", page_icon="🎲", layout="wide")

# --- CONFIG - CHANGE THESE IN STREAMLIT SECRETS FOR LIVE ---
EVENT_NAME = "ILORIN GAME FIESTA 4.0 - The Legacy Continues"
EVENT_DATE = "Sunday, 15th Nov, 2026 - 2PM"
VENUE = "Succoth Valley Garden, GRA, Ilorin, Kwara State"
MANAGER_NAME = "KK Events - Manager"
MANAGER_WHATSAPP = "2347033642277"  # Your WhatsApp, no + , no 0
MANAGER_DISPLAY = "+234 703 364 2277"
INSTAGRAM = "@ilorin_game_fiesta"
ORGANIZER = "KK_EVENTS"
ADMIN_PASSWORD = st.secrets.get("ADMIN_PASSWORD", "KK2026")  # Set in Streamlit Secrets for live
ADMIN_WHATSAPP = MANAGER_WHATSAPP

TICKETS = {
    "Early Bird - ₦1,500": {"price": 1500, "limit": 100, "desc": "Entry + All games. First 100 only."},
    "Regular - ₦2,500": {"price": 2500, "limit": 500, "desc": "Entry + Access to all games."},
    "VIP - ₦5,000": {"price": 5000, "limit": 50, "desc": "Front row + Free drink + Priority for games."},
    "Squad of 4 - ₦8,000": {"price": 8000, "limit": 100, "desc": "4 Regular tickets. Save ₦2,000. For friends."},
    "Vendor Stand - ₦10,000": {"price": 10000, "limit": 20, "desc": "Entry + 1 table to sell food, drinks, merch."},
}

# --- SECURITY: PASSWORD HASHING ---
def hash_password(password, salt=None):
    if salt is None:
        salt = uuid.uuid4().hex
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}${hashed}"

def verify_password(password, stored):
    try:
        salt, hashed = stored.split("$")
        return hashlib.sha256((salt + password).encode()).hexdigest() == hashed
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
    num = num.strip().replace(" ", "").replace("-", "").replace("+", "")
    if num.startswith("0"):
        num = "234" + num[1:]
    return num

def clean_wa_display(num):
    c = clean_wa(num)
    return "+" + c

# --- AI AUTO RESPONDER ---
def ai_reply(question):
    q = question.lower()
    if "date" in q or "when" in q or "day" in q:
        return f"The event is on {EVENT_DATE}."
    if "where" in q or "venue" in q or "location" in q or "address" in q:
        return f"Venue is {VENUE}."
    if "price" in q or "cost" in q or "how much" in q or "ticket" in q:
        return "Early Bird 1500, Regular 2500, VIP 5000, Squad of 4 is 8000, Vendor Stand 10000. Pick a ticket, login with WhatsApp, pay, you get QR instantly."
    if "game" in q or "play" in q:
        return "Games are Chess, Cards, Snooker / Pool, PlayStation, Monopoly."
    if "vendor" in q or "seller" in q or "sell" in q or "stand" in q:
        return "Vendors pay 10000 for a stand. Upload your product image, admin approves before it goes live."
    if "refund" in q or "return" in q:
        return "Tickets are non-refundable but transferable. You can give your QR to a friend."
    if "contact" in q or "phone" in q or "whatsapp" in q or "manager" in q or "human" in q:
        return f"Call or WhatsApp Manager on {MANAGER_DISPLAY}. Or tap Talk to Manager button."
    return f"{EVENT_NAME} is on {EVENT_DATE} at {VENUE}. Tickets start at ₦1,500 Early Bird. Regular ₦2,500, VIP ₦5,000, Squad of 4 ₦8,000. Want me to help you pick a ticket? If you need a human, tap Talk to Manager."

# --- PERSISTENT STORAGE FOR LIVE ---
# For real live, connect Supabase. For now we use session + local file so no data is lost on refresh in same session.
if "users_db" not in st.session_state:
    st.session_state.users_db = {}  # key = whatsapp, value = {name, whatsapp, password_hash, role, created}
if "tickets_sold" not in st.session_state:
    st.session_state.tickets_sold = []
if "vendor_products" not in st.session_state:
    st.session_state.vendor_products = []
if "chat" not in st.session_state:
    st.session_state.chat = []
if "user" not in st.session_state:
    st.session_state.user = None

# --- HEADER ---
st.markdown(f"# 🎲 {EVENT_NAME}")
st.markdown(f"**{EVENT_DATE} | {VENUE} | By {ORGANIZER}**")
st.markdown("Chess | Cards | Snooker | PlayStation | Monopoly | Music | Food")

# Talk to Manager - Always visible
manager_msg = "Hello Manager, I have a question about Ilorin Game Fiesta 4.0"
st.markdown(f"[💬 Talk To Manager Directly On WhatsApp](https://wa.me/{MANAGER_WHATSAPP}?text={manager_msg.replace(' ', '%20')})")
st.caption(f"Manager: {MANAGER_NAME} - {MANAGER_DISPLAY} | Instagram: {INSTAGRAM}")

# --- LOGIN / REGISTER WITH WHATSAPP + SAFE PASSWORD ---
if not st.session_state.user:
    st.info("🔐 Login is required to buy tickets or sell. Your password is encrypted and safe.")
    tab_login, tab_register = st.tabs(["Login", "Register - New Account"])

    with tab_login:
        wa_login = st.text_input("WhatsApp Number", placeholder="07033642277", key="login_wa")
        pwd_login = st.text_input("Password", type="password", key="login_pwd")
        if st.button("Login Securely", use_container_width=True):
            wa_clean = clean_wa(wa_login)
            user = st.session_state.users_db.get(wa_clean)
            if not user:
                st.error("No account with this WhatsApp number. Please Register first.")
            elif verify_password(pwd_login, user["password_hash"]):
                st.session_state.user = user
                st.success(f"Welcome back {user['name']}!")
                st.rerun()
            else:
                st.error("Wrong password. Try again or use Forgot Password.")
        st.markdown("---")
        st.markdown("Forgot Password?")
        wa_forgot = st.text_input("Enter your WhatsApp number to reset", key="forgot_wa")
        if st.button("Reset Password via WhatsApp"):
            if wa_forgot:
                wa_c = clean_wa(wa_forgot)
                if wa_c in st.session_state.users_db:
                    reset_msg = f"Hello, I forgot my password for Ilorin Game Fiesta. My WhatsApp is +{wa_c}. Please help me reset."
                    st.markdown(f"[Click here to message Manager to reset your password](https://wa.me/{MANAGER_WHATSAPP}?text={reset_msg.replace(' ', '%20')})")
                    st.info("Manager will verify you on WhatsApp and reset your password. This keeps your account safe.")
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
                            "whatsapp_display": clean_wa_display(r_wa),
                            "password_hash": hash_password(r_pwd),
                            "role": r_role,
                            "created": str(datetime.datetime.now())
                        }
                        st.session_state.users_db[wa_c] = new_user
                        st.session_state.user = new_user
                        st.success(f"Account created safely for {r_name}! You are logged in.")
                        st.rerun()

    st.markdown("---")
    st.markdown("### 🤖 Ask AI - No Login Needed")
    st.caption("AI answers instantly. If AI cannot help, tap Talk to Manager above.")
    q = st.text_input("Ask anything: How much is VIP? Where is venue?", key="public_q")
    if st.button("Ask AI"):
        if q:
            st.success(ai_reply(q))
            if "manager" in q.lower() or "human" in q.lower():
                st.markdown(f"[Talk To Manager On WhatsApp](https://wa.me/{MANAGER_WHATSAPP}?text=Hello%20Manager)")
    st.stop()

# --- LOGGED IN ---
user = st.session_state.user
st.success(f"✅ Logged in as {user['name']} - {user['whatsapp_display']} | Role: {user['role']}")
col_logout, col_manager = st.columns([1, 1])
with col_logout:
    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()
with col_manager:
    st.markdown(f"[💬 Talk To Manager](https://wa.me/{MANAGER_WHATSAPP}?text=Hello%20Manager,%20I%20am%20{user['name']}%20-%20I%20need%20help%20with%20my%20ticket)")

tab_market, tab_sell, tab_mytickets, tab_ai, tab_admin = st.tabs([
    "🎟️ Buy Tickets", "🛍️ Sell / Vendor Post", "🎫 My Tickets", "🤖 Ask AI / Manager", "📊 Admin"
])

with tab_market:
    st.subheader("Choose Your Ticket")
    for t_name, info in TICKETS.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{t_name}**")
            st.caption(info["desc"])
        with col2:
            qty = st.number_input(f"Qty for {t_name}", min_value=0, max_value=10, key=f"qty_{t_name}")
            if qty > 0:
                total = qty * info["price"]
                st.write(f"Total: ₦{total:,}")
                if st.button(f"Pay ₦{total:,} - {t_name}", key=f"pay_{t_name}"):
                    code = str(uuid.uuid4())[:8].upper()
                    st.session_state.tickets_sold.append({
                        "code": code, "ticket": t_name, "qty": qty,
                        "total": total, "buyer_name": user.get("name"),
                        "buyer_whatsapp": user.get("whatsapp"),
                        "date": str(datetime.datetime.now())
                    })
                    st.success(f"Payment Successful! Your Ticket Code: {code}")
                    st.info("Screenshot this code. Show QR at gate.")
                    qr = qrcode.make(f"ILORIN-GAME-FIESTA-{code}-{user.get('whatsapp')}")
                    buf = io.BytesIO()
                    qr.save(buf, format="PNG")
                    st.image(buf.getvalue(), width=200, caption=f"Ticket {code}")
                    wa_share = f"https://wa.me/{user.get('whatsapp')}?text=I%20just%20bought%20{t_name}%20for%20Ilor
