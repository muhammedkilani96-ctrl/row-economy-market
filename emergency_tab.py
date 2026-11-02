import streamlit as st
from datetime import datetime
import json, os

SOS_FILE="sos_alerts.json"

def get_sos():
    if not os.path.exists(SOS_FILE): return []
    try: return json.loads(open(SOS_FILE).read())
    except: return []

def show(area,state):
    st.title("🚨 EMERGENCY SOS - NIGERIA")
    st.markdown("""
    <div style='background:red;padding:15px;border-radius:15px;text-align:center;color:white;font-weight:bold;font-size:18px'>
    ⚠️ IN DANGER? PRESS SOS NOW ⚠️
    </div>
    """, unsafe_allow_html=True)
    
    st.caption(f"Your Location: {area}, {state} | Time: {datetime.now().strftime('%H:%M:%S')}")
    
    # Nearest security based on state
    POLICE_NUMBERS={
        "FCT Abuja":"08032003913 - FCT Police",
        "Lagos":"08057000001 - Lagos Police",
        "Kano":"08032600299 - Kano Police",
        "Rivers":"08032003514 - Rivers Police",
        "Default":"112 - Emergency Toll Free"
    }
    
    nearest=POLICE_NUMBERS.get(state, POLICE_NUMBERS["Default"])
    
    c1,c2=st.columns(2)
    with c1:
        st.subheader("🚨 SOS ACTIONS")
        if st.button("🚨 SEND SOS TO POLICE + NANS", use_container_width=True):
            sos=get_sos()
            sos.append({
                "name":st.session_state.user_name,
                "phone":st.session_state.user_phone,
                "area":area,
                "state":state,
                "time":str(datetime.now()),
                "status":"ALERT SENT"
            })
            open(SOS_FILE,"w").write(json.dumps(sos))
            st.error(f"🚨 SOS SENT! Location {area}, {state} shared to:")
            st.write(f"✅ Police Zone - {nearest}")
            st.write(f"✅ NANS HQ Abuja - 0800-NANS-HELP")
            st.write(f"✅ Nearest Task Force")
            st.balloons()
            
        if st.button("📍 SHARE LIVE LOCATION", use_container_width=True):
            st.link_button("Share on WhatsApp", f"https://wa.me/2348116911722?text=🚨 EMERGENCY! I need help at {area}, {state}. Name: {st.session_state.user_name} Phone: {st.session_state.user_phone} Time: {datetime.now()}", use_container_width=True)
        
        if st.button("📞 CALL POLICE NOW", use_container_width=True):
            st.link_button(f"Call {nearest}", f"tel:{nearest.split(' - ')[0]}", use_container_width=True)
    
    with c2:
        st.subheader("🛡️ NEAREST HELP")
        st.write(f"""
        **Your State:** {state}
        **Nearest Police:** {nearest}
        **NANS HQ:** Zone 6 Abuja - 09-123456
        **EFCC:** 0800-EFCC-NIG
        **NDLEA:** 0800-NDLEA-HELP
        **FRSC:** 122
        **Emergency:** 112 / 767
        """)
        st.map(pd.DataFrame([{"lat":9.0667, "lon":7.4833}]), latitude="lat", longitude="lon")
    
    st.divider()
    st.subheader("Recent SOS (Admin Only)")
    if st.session_state.user_phone=="2348116911722":
        for s in get_sos()[-10:][::-1]:
            st.write(f"🚨 {s['time'][11:16]} - {s['name']} - {s['area']}, {s['state']} - {s['phone']}")
            st.link_button(f"Respond to {s['name']}", f"https://wa.me/{s['phone']}", key=f"sos{s['time']}")
    else:
        st.caption("Only CEO can see all SOS. Your SOS is private to security.")
    
    st.warning("This button alerts real security. Use only for real emergency. Fake alert = offence under Nigerian law.")

# Need pandas import
import pandas as pd
