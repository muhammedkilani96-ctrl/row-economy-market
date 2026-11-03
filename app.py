with t3:
 st.title("GO LIVE - Sell Live!")
 st.write("Go live and sell like TikTok")
 title=st.text_input("Live Title e.g. Selling Fresh Tomatoes")
 ldesc=st.text_input("What are you selling today?")
 
 st.info("Click START LIVE - Buyers will see you as LIVE in LIVE MARKET")
 
 if st.button("🔴 START LIVE NOW"):
  if title:
   live_data={
    "user":st.session_state.user,
    "title":title,
    "desc":ldesc,
    "time":datetime.now().strftime("%H:%M:%S")
   }
   lives.append(live_data)
   save("lives.json",lives)
   st.success("YOU ARE NOW LIVE! 🔴")
   st.balloons()
  else:
   st.error("Add Live Title")
 
 st.divider()
 st.write("Upload product photo for live")
 photo=st.file_uploader("Live Product Photo")
 if photo:
  st.image(photo)
 
 if st.button("END MY LIVE"):
  lives=[l for l in lives if l['user']!=st.session_state.user]
  save("lives.json",lives)
  st.warning("Live Ended")
