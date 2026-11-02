import streamlit as st
import database, explore_tab, advertise_tab, live_tab, chats_tab, profile_tab
from datetime import date

st.set_page_config(page_title="Row Economy Market Wuse 2 LIVE", layout="centered", page_icon="🛒")

if "ads_today" not in st.session_state: st.session_state.ads_today = 0
if "ads_date" not in st.session_state: st.session_state.ads_date = str(date.today())
if "paid_unlock" not in st.session_state: st.session_state.paid_unlock = 0
if "live_gifts" not in st.session_state: st.session_state.live_gifts = 0
if "live_comments" not in st.session_state: st.session_state.live_comments = []

STATES = ["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","FCT Abuja","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nasarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara"]

st.title("ROW ECONOMY MARKET Wuse 2 🔴 LIVE")
st.caption("Food | Cloth | Car | Ticket | Live Selling | Gifting - 10 FREE Ads")
st.write("WhatsApp: 08116911722 | Link: https://row-economy-market.streamlit.app")

state = st.selectbox("State", STATES, index=14)
area = st.text_input("Area / Town", "Wuse 2")
st.markdown(f"""<div style="background:#00FF7F; padding:10px; border-radius:10px; color:black; font-weight:bold">📍 You dey for {area}, {state} - LIVE NOW</div>""", unsafe_allow_html=True)

tabs = st.tabs(["🏠 Home","🔍 Explore","🔴 LIVE","📢 Advertise","💬 Chats","👤 Profile"])

with tabs[0]:
    st.subheader("Cooking Calculator")
    people = st.number_input("Number of people",1,500,10)
    meal = st.selectbox("Meal",["Spaghetti","Rice","Indomie","Full Package"])
    spag=(people+3)//4; rice=(people+4)//5
    prices={"Spaghetti":1000,"Rice":1500,"Indomie":350}
    if meal=="Spaghetti": needs={"Spaghetti":spag}
    elif meal=="Rice": needs={"Rice":rice}
    elif meal=="Indomie": needs={"Indomie":people}
    else: needs={"Rice":rice,"Spaghetti":spag}
    total=sum(prices[k]*v for k,v in needs.items())
    for k,v in needs.items(): st.metric(f"{k} x {v}", f"N{prices[k]*v}")
    st.write(f"### Total: N{total}")
    st.link_button(f"Order {area}", f"https://wa.me/2348116911722?text=Food {people} {meal} N{total} {area} {state}", use_container_width=True)

with tabs[1]: explore_tab.show(area,state)
with tabs[2]: live_tab.show(area,state)
with tabs[3]: advertise_tab.show(area,state)
with tabs[4]: chats_tab.show(area,state)
with tabs[5]: profile_tab.show(area,state)
