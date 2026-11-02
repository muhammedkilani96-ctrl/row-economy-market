import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy", layout="centered")

if 'ads' not in st.session_state:
    st.session_state.ads = 0

WHATSAPP = "2348116911722"
NUM = "08116911722"

STATES = ["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","FCT Abuja","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nasarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara"]

st.title("Row Economy Market")
st.write("Nigeria Super Market")
st.caption(f"WhatsApp {NUM} Free {st.session_state.ads}/10")

state = st.selectbox("Select State", STATES, index=14)
area = st.text_input("Your Area / Town", "Wuse")

st.success(f"Location: {area}, {state}")

tab1, tab2, tab3 = st.tabs(["Food","Events","Clothes"])

with tab1:
    people = st.number_input("People",1,500,10,key="f1")
    meal = st.selectbox("Meal",["Spaghetti","Rice","Indomie","Full"],key="f2")
    spag = (people+3)//4
    rice = (people+4)//5
    if meal == "Spaghetti":
        needs = {"Spaghetti": spag}
    elif meal == "Rice":
        needs = {"Rice": rice}
    elif meal == "Indomie":
        needs = {"Indomie": people}
    else:
        needs = {"Rice": rice, "Spaghetti": spag}
    prices = {"Spaghetti":1000,"Rice":1500,"Indomie":350}
    total = 0
    for k,v in needs.items():
        total += prices[k]*v
        st.metric(f"{k} x {v}", f"N{prices[k]*v}")
    st.write(f"Total N{total}")
    msg = f"Food {people} {meal} N{total} Location {area} {state}"
    link = "https://wa.me/" + WHATSAPP + "?text="
