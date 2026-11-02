import streamlit as st
import urllib.parse

st.set_page_config(page_title="Row Economy", layout="centered")

if 'ads' not in st.session_state:
    st.session_state.ads = 0

WHATSAPP = "2348116911722"
NUM = "08116911722"

STATES = ["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","FCT Abuja","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nasarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara"]

# AFRICAN STYLE CSS - NOT TIKTOK
st.markdown("""
<style>
.village-card {
  border: 4px solid #8B4513;
  border-radius: 25px;
  padding: 15px;
  background: #FFF8DC;
  margin: 10px 0;
  box-shadow: 3px 3px 10px #888;
}
.drum { background: linear-gradient(#D2B48C, #8B4513); color: white; border-radius: 50% 50% 20% 20%; }
.calabash { background: #DEB887; border-radius: 60% 60% 20% 20%; }
.hut { background: repeating-linear-gradient(45deg, #FFD700, #FF8C00); }
</style>
""", unsafe_allow_html=True)

st.title("ROW ECONOMY VILLAGE SQUARE")
st.caption("Connect - Sell - Celebrate - Officially African")
st.write(f"WhatsApp {NUM} | Free Ads {st.session_state.ads}/10")

state = st.selectbox("Select State", STATES, index=14)
area = st.text_input("Your Area / Town", "Wuse")
st.success(f"Location: {area}, {state}")

tab1, tab2, tab3, tab4 = st.tabs(["Food", "Events", "Clothes", "Village Square"])

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
    msg = f"Food {people} {meal} N{total} {area} {state}"
    link = "https://wa.me/" + WHATSAPP + "?text=" + urllib.parse.quote(msg)
    st.link_button("Order via Village", link, use_container_width=True)

with tab2:
    event = st.text_input("Event Name","Concert")
    venue = st.text_input("Venue","Hall")
    price = st.number_input("Ticket Price",500,100000,2000,key="e1")
    qty = st.number_input("Qty",1,20,1,key="e2")
    total_t = price*qty
    st.write(f"Total N{total_t}")
    msg2 = f"Ticket {qty} for {event} {area} {state} N{total_t}"
    link2 = "https://wa.me/" + WHATSAPP + "?text=" + urllib.parse.quote(msg2)
    st.link_button("Buy from Village", link2, use_container_width=True)

with tab3:
    cloth = st.selectbox("Item",["Shirt","Native","Hijab","Trouser","Shoe","Cap"],key="c0")
    size = st.selectbox("Size",["S","M","L","XL","XXL"],key="c1")
    c_price = st.number_input("Price",1000,100000,5000,key="c2")
    c_qty = st.number_input("How many",1,20,1,key="c3")
    total_c = c_price*c_qty
    st.write(f"{cloth} {size} x {c_qty} N{total_c}")
    msg3 = f"Cloth {cloth} {size} x {c_qty} N{total_c} {area} {state}"
    link3 = "https://wa.me/" + WHATSAPP + "?text=" + urllib.parse.quote(msg3)
    st.link_button("Buy from Village", link3, use_container_width=True)

with tab4:
    st.subheader("VILLAGE SQUARE - Video Ads")
    st.write("Our own design - No copy TikTok!")
    
    # 3 African styled video stalls
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="village-card drum">', unsafe_allow_html=True)
        st.write("DRUM STALL")
        st.write("Food Seller")
        st.write("Mama Ife, Lagos")
        vid1 = st.file_uploader("Upload Food Video", type=["mp4"], key="v1")
        if vid1:
            st.video(vid1)
        st.write("Jollof by Mama Ife")
        st.write("124 Cowries")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:
        st.markdown('<div class="village-card calabash">', unsafe_allow_html=True)
        st.write("CALABASH STALL")
        st.write("Cloth Seller")
        st.write("Ade, Abuja")
        vid2 = st.file_uploader("Upload Cloth Video", type=["mp4"], key="v2")
        if vid2:
            st.video(vid2)
        st.write("Ankara by Ade")
        st.write("98 Cowries")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c3:
        st.markdown('<div class="village-card hut">', unsafe_allow_html=True)
        st.write("HUT STALL")
        st.write("Event Seller")
        st.write("Chika, Ibadan")
        vid3 = st.file_uploader("Upload Event Video", type=["mp4"], key="v3")
        if vid3:
            st.video(vid3)
        st.write("Wedding by Chika")
        st.write("76 Cowries")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()
    st.write("How it works:")
    st.write("1. Seller uploads 15 sec video")
    st.write("2. Video appears inside Drum/Calabash/Hut")
    st.write("3. Buyer clicks Cowrie to order via WhatsApp")

st.divider()
with st.form("ad"):
    name = st.text_input("Shop Name")
    cat = st.selectbox("Category",["Food","Event","Cloth","Video"])
    item = st.text_area("What you sell")
    ok = st.form_submit_button("Post to Village Square")
    if ok:
        if st.session_state.ads < 10:
            st.session_state.ads += 1
            st.success(f"Posted to {area}, {state}! Left {10-st.session_state.ads}")
        else:
            st.error("Pay N200 to continue selling")
