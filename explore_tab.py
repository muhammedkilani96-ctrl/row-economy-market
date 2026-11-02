search = st.text_input("Search")
ads = [a for a in get_adverts() if search.lower() in a['what'].lower()]
