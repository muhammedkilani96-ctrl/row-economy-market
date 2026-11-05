import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime
import time
st.set_page_config(page_title='Row Economy Market', layout='wide', initial_sidebar_state='collapsed')
SHEET_ID = '1w8P3SQiChShHPQzShpgznR-lay-awTHmu_x-VHI9IU8E'
if 'my_orders' not in st.session_state: st.session_state.my_orders = []
if 'seller_inbox' not in st.session_state: st.session_state.seller_inbox = []
if 'local_goods' not in st.session_state: st.session_state.local_goods = []
if 'page' not in st.session_state: st.session_state.page = 'Home'
if 'cat' not in st.session_state: st.session_state.cat = 'All'
if 'my_name' not in st.session_state: st.session_state.my_name = ''
if 'buyer_phone_temp' not in st.session_state: st.session_state.buyer_phone_temp = ''
if 'referral_count' not in st.session_state: st.session_state.referral_count = 0
if 'verified_sellers' not in st.session_state: st.session_state.verified_sellers = ['Horlance Auto Cooling Ltd', 'Mama Ada']
if 'chat_msgs' not in st.session_state: st.session_state.chat_msgs = [{'room':'General','user':'Mama Ada','msg':'Welcome to Row Economy Market','time':'09:12'}]
if 'online_users' not in st.session_state: st.session_state.online_users = ['Mama Ada','Horlance Auto','Tunde']
if 'escrow_balance' not in st.session_state: st.session_state.escrow_balance = 0
if 'my_earnings' not in st.session_state: st.session_state.my_earnings = 0
PAYSTACK_LINK = 'https://paystack.shop/rowmarket'
BANK_NAME = 'OPay / GTB'
ACCOUNT_NAME = 'Row Economy Market - Horlance'
ACCOUNT_NUMBER = '9046044472'
COMMISSION = 0.05
@st.cache_data(ttl=30)
def load_sheet(sid):
    try:
        url = 'https://docs.google.com/spreadsheets/d/' + sid + '/export?format=csv'
        df = pd.read_csv(url)
        return df.dropna(subset=['Item'])
    except:
        return pd.DataFrame()
def get_goods():
    goods = []
    df = load_sheet(SHEET_ID)
    for _, r in df.iterrows():
        try:
            nm = str(r.get('Name',''))
            it = str(r.get('Item',''))
            pr = int(float(r.get('Price',0)))
            ct = str(r.get('Category',''))
            lc = str(r.get('Location','Abuja'))
            ph = str(r.get('Phone','2349046044472'))
            im = str(r.get('Image','https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600'))
            vf = str(r.get('Verified','')).upper() == 'TRUE'
            goods.append({'name':nm,'item':it,'price':pr,'cat':ct,'loc':lc,'phone':ph,'img':im,'verified':vf})
        except:
            pass
    goods = st.session_state.local_goods + goods
    if len(goods) == 0:
        goods = [
            {'name':'Horlance Auto Cooling Ltd','item':'Car AC Repair','price':25000,'cat':'Car','loc':'Osun & Oyo State','img':'https://images.unsplash.com/photo-1625047509168-a7026f36de04?w=600','phone':'2349046044472','verified':True},
            {'name':'Mama Ada','item':'Bag of Rice 50kg','price':85000,'cat':'Food','loc':'Wuse 2, Abuja','img':'https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600','phone':'2349046044472','verified':True},
            {'name':'Tunde Perfumes','item':'Oud Perfume 100ml','price':15000,'cat':'Perfume','loc':'Garki, Abuja','img':'https://images.unsplash.com/photo-1541643600914-78b084683601?w=600','phone':'2349046044472','verified':False},
            {'name':'Chidi Phones','item':'iPhone 12 - Neatly Used','price':280000,'cat':'Phones','loc':'Wuse 2, Abuja','img':'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600','phone':'2349046044472','verified':False},
            {'name':'Aisha Fashion','item':'Ankara Gown','price':25000,'cat':'Clothes','loc':'Gwarinpa, Abuja','img':'https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=600','phone':'2349046044472','verified':False},
        ]
    return goods
def delivery_fee(loc):
    if 'Wuse' in loc: return 1500
    if 'Garki' in loc: return 1500
    if 'Gwarinpa' in loc: return 2000
    if 'Osun' in loc or 'Oyo' in loc: return 3000
    return 2500
def deal_price(p):
    return int(p * 0.88)
def seller_avatar(name):
    if 'Mama' in name or 'Aisha' in name: return 'https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=100'
    if 'Horlance' in name: return 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100'
    return 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100'
def open_cat(cat_name):
    st.session_state.cat = cat_name
    st.session_state.page = 'Category'
    st.rerun()
st.markdown('<style>header{visibility:hidden !important}.block-container{padding-top:0px !important;padding-left:0px !important;padding-right:0px !important;padding-bottom:140px !important;max-width:100% !important}div.stButton > button{width:100% !important;background:#16A34A !important;color:white !important;border-radius:14px !important;padding:16px 10px !important;border:none !important;font-weight:700 !important;font-size:16px !important;box-shadow:0 4px 12px rgba(22,163,74,0.25) !important}div.stButton > button:hover{background:#15803D !important}div.stLinkButton > a{width:100% !important;background:#16A34A !important;color:white !important;border-radius:14px !important;text-align:center !important;font-weight:700 !important;padding:12px !important}input{border-radius:12px !important}div[data-testid="stExpander"]{border-radius:16px !important;border:1px solid #E5E7EB !important}div[data-testid="stSegmentedControl"] button{border-radius:20px !important;padding:10px 12px !important}div[data-testid="stSegmentedControl"] button[data-testid="stSegmentedControlButton-selected"]{background:#16A34A !important;color:white !important}</style>', unsafe_allow_html=True)
st.markdown('<div style="background:#16A34A;border-radius:0 0 28px 28px;padding:16px 18px 22px 18px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 4px 20px rgba(0,0,0,0.12)"><div><h1 style="color:white;margin:0;font-size:25px;line-height:1">Row Economy</h1><p style="color:#BBF7D0;margin:2px 0 0 0;font-size:13px">Market - Buy & Sell Free</p></div><div style="background:white;width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px;box-shadow:0 2px 10px rgba(0,0,0,0.15)">👤</div></div>', unsafe_allow_html=True)
buyer_name = st.session_state.my_name
buyer_phone = st.session_state.buyer_phone_temp
page = st.session_state.page
current_cat = st.session_state.cat
CAT_INFO = {
    'Food': {'emoji':'🍲','color':'#F97316','title':'Food Market','desc':'Rice, Garri, Oil, Fresh Food','usage':'See ONLY Food products. Post your Food here.'},
    'Phones': {'emoji':'📱','color':'#3B82F6','title':'Phones Market','desc':'iPhone, Samsung, Accessories','usage':'See ONLY Phones. Post your Phone here.'},
    'Perfume': {'emoji':'🧴','color':'#EC4899','title':'Perfume Market','desc':'Oud, Designer Perfumes','usage':'See ONLY Perfumes. Post your Perfume here.'},
    'Clothes': {'emoji':'👕','color':'#3B82F6','title':'Clothes Market','desc':'Ankara, Gowns, Shirts','usage':'See ONLY Clothes. Post your Clothes here.'},
    'Car': {'emoji':'🚗','color':'#F97316','title':'Car Mart','desc':'Car AC, Repairs, Car Sales','usage':'See ONLY Cars. Post your Car service here.'},
    'Services': {'emoji':'💼','color':'#16A34A','title':'Services Market','desc':'Plumber, Electrician, Hair','usage':'See ONLY Services. Post your Service here.'},
    'Tickets': {'emoji':'🎟️','color':'#EC4899','title':'Tickets Market','desc':'Event, Flight, Bus Tickets','usage':'See ONLY Tickets. Post your Ticket here.'},
    'Chat': {'emoji':'💬','color':'#10B981','title':'Chat Rooms','desc':'Talk to Sellers','usage':'Chat with sellers and Mama Oloja.'},
}
def show_category_page(cat_name):
    info = CAT_INFO.get(cat_name, {'emoji':'🛒','color':'#16A34A','title':cat_name,'desc':'','usage':''})
    st.markdown('<div style="background:' + info['color'] + ';border-radius:0 0 28px 28px;padding:22px 16px;text-align:center;color:white"><h1 style="margin:0;font-size:30px">' + info['emoji'] + ' ' + info['title'] + '</h1><p style="margin:6px 0 0 0">' + info['desc'] + '</p><p style="margin:4px 0 0 0;font-size:13px;opacity:0.9">Row Economy Market - ' + cat_name + ' ONLY</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="padding:12px 16px 0 16px"><p style="color:#6B7280;font-size:13px;margin:0">USAGE: ' + info['usage'] + '</p></div>', unsafe_allow_html=True)
    if st.button('⬅ Back to Home - See All Categories', key='back_home_' + cat_name):
        st.session_state.page = 'Home'
        st.session_state.cat = 'All'
        st.rerun()
    st.caption('USAGE: Back button takes you to Home categories.')
    search_in_cat = st.text_input('Search in ' + cat_name + ' only', key='search_in_' + cat_name)
    st.caption('USAGE: Type to find product inside ' + cat_name + ' only.')
    st.markdown('<div style="background:#FFF7ED;border:2px dashed #16A34A;border-radius:20px;padding:16px;margin:12px 16px"><h3 style="margin:0">POST YOUR ' + cat_name.upper() + ' PRODUCT - FREE</h3><p style="margin:6px 0 0 0;color:#6B7280">Your product will show ONLY in ' + cat_name + ' page. People who press ' + cat_name + ' will see you.</p></div>', unsafe_allow_html=True)
    with st.expander('TAP TO POST IN ' + cat_name.upper() + ' - USAGE: Fill form to sell in ' + cat_name, expanded=False):
        p_name = st.text_input('Your Name', value=buyer_name, key='post_name_' + cat_name)
        p_item = st.text_input('What are you selling in ' + cat_name + '?', key='post_item_' + cat_name)
        p_price = st.number_input('Price (Naira)', min_value=0, key='post_price_' + cat_name)
        p_loc = st.text_input('Location', key='post_loc_' + cat_name)
        p_phone = st.text_input('Your WhatsApp', value=buyer_phone, key='post_phone_' + cat_name)
        uploaded = st.file_uploader('Upload Photo - USAGE: Show your real product', type=['jpg','png','jpeg'], key='post_photo_' + cat_name)
        p_img_link = st.text_input('OR Paste Photo Link', key='post_img_' + cat_name)
        img_to_use = 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600'
        if uploaded is not None: st.image(uploaded, caption='Your photo preview', width=200)
        if p_img_link: img_to_use = p_img_link
        if st.button('POST IN ' + cat_name.upper() + ' NOW', key='post_now_' + cat_name):
            if p_name and p_item and p_price > 0:
                is_ver = p_name in st.session_state.verified_sellers
                st.session_state.local_goods.insert(0, {'name':p_name,'item':p_item,'price':int(p_price),'cat':cat_name,'loc':p_loc or 'Abuja','phone':p_phone or '2349046044472','img':img_to_use,'verified':is_ver})
                st.success('Posted in ' + cat_name + '! People who press ' + cat_name + ' will see you now!')
                st.balloons()
                st.rerun()
            else: st.error('Fill Name, Product, Price - all 3 are needed.')
    all_goods = get_goods()
    filtered = []
    for g in all_goods:
        if g['cat'].lower().strip() != cat_name.lower().strip(): continue
        if search_in_cat and search_in_cat.lower() not in (g['item'] + g['name'] + g['loc']).lower(): continue
        filtered.append(g)
    st.markdown('<div style="background:#EFF6FF;border-radius:12px;padding:12px;margin:12px 16px"><b>Showing ' + str(len(filtered)) + ' products in ' + cat_name + ' - ONLY ' + cat_name + '</b></div>', unsafe_allow_html=True)
    if len(filtered) == 0:
        st.info('No products in ' + cat_name + ' yet. Be the first to post in ' + cat_name + ' above!')
    st.subheader('Swipe - ' + cat_name)
    st.caption('USAGE: Swipe left / right to see ' + cat_name + ' products quickly.')
    if len(filtered) > 0:
        cards = ''
        for g in filtered:
            cards += '<div style="min-width:76vw;max-width:76vw;background:white;border-radius:20px;overflow:hidden;box-shadow:0 4px 20px #ddd;flex-shrink:0"><img src="' + g['img'] + '" style="width:100%;height:220px;object-fit:cover"><div style="padding:14px"><b>' + g['name'] + '</b><p>' + g['item'] + '</p><p style="color:#16A34A;font-weight:800">N' + str(deal_price(g['price'])) + '</p></div></div>'
        st.markdown('<div style="display:flex;overflow-x:auto;gap:12px;padding:8px 16px">' + cards + '</div>', unsafe_allow_html=True)
    st.subheader('All ' + cat_name + ' Products')
    st.caption('USAGE: Each card = 1 seller. Seller pic = round face. Tap ORDER to buy safely with Escrow.')
    delivery_loc = st.selectbox('Your Delivery Area - USAGE: Choose where rider will deliver', ['Wuse 2, Abuja','Garki, Abuja','Gwarinpa, Abuja','Osun & Oyo','Abuja','Pickup Only'], key='delivery_' + cat_name)
    payment = st.selectbox('Pay with - USAGE: Escrow = safest, we hold money', ['Escrow - Paystack (Safest)','Pay on Delivery (Cash)','Bank Transfer to Row Economy Market'], key='payment_' + cat_name)
    if payment == 'Bank Transfer to Row Economy Market': st.markdown('<div style="background:#F0FDF4;border:1px solid #16A34A;border-radius:12px;padding:12px;margin:0 16px">Transfer: ' + BANK_NAME + ' - ' + ACCOUNT_NAME + ' - ' + ACCOUNT_NUMBER + '<br>USAGE: Transfer then send receipt on WhatsApp.</div>', unsafe_allow_html=True)
    if 'Escrow' in payment: st.link_button('Pay Safely via Escrow - USAGE: Pay online, we hold money', PAYSTACK_LINK)
    for idx, g in enumerate(filtered):
        is_ver = g['name'] in st.session_state.verified_sellers or g['verified']
        badge_txt = 'VERIFIED' if is_ver else 'New Seller'
        fee = delivery_fee(delivery_loc)
        base = deal_price(g['price'])
        discount = 500 if st.session_state.referral_count >= 3 else 0
        total = base + (0 if base >= 100000 else fee) - discount
        if total < 0: total = 0
        comm = int(total * COMMISSION)
        seller_gets = int(total * (1 - COMMISSION))
        avatar = seller_avatar(g['name'])
        st.markdown('<div style="background:white;border-radius:20px;overflow:hidden;box-shadow:0 4px 20px #eee;margin:12px 16px"><img src="' + g['img'] + '" style="width:100%;height:280px;object-fit:cover"><div style="padding:16px"><div style="display:flex;gap:10px;align-items:center"><img src="' + avatar + '" style="width:52px;height:52px;border-radius:50%;object-fit:cover;border:2px solid #16A34A"><div><b>' + g['name'] + '</b> - ' + badge_txt + '<br><span style="font-size:12px;color:#666">Seller in ' + g['cat'] + ' - ' + g['loc'] + '</span></div></div><p style="margin:12px 0 4px 0;font-size:17px;font-weight:600">' + g['item'] + '</p><p style="color:#16A34A;font-weight:800;font-size:22px;margin:4px 0">N' + str(base) + ' <span style="font-size:13px;color:#999;text-decoration:line-through">N' + str(g['price']) + '</span></p><p style="margin:0;color:#374151">Total with delivery: <b>N' + str(total) + '</b></p><p style="font-size:12px;color:#3B82F6;margin:4px 0 0 0">Escrow: N' + str(comm) + ' to Market, Seller gets N' + str(seller_gets) + '</p></div></div>', unsafe_allow_html=True)
        if st.button('Chat Seller - USAGE: Talk to seller before you buy', key='chat_' + cat_name + '_' + str(idx)):
            st.session_state.page = 'Profile'
            st.rerun()
        if st.button('ORDER NOW - Escrow N' + str(total) + ' - USAGE: Buy safely, we hold money', key='order_' + cat_name + '_' + str(idx) + '_' + g['item'][:5]):
            if not buyer_name or not buyer_phone: st.error('Set Name + WhatsApp on Home page first - open Your Details on Home.')
            else:
                order = {'buyer':buyer_name,'buyer_phone':buyer_phone,'seller':g['name'],'seller_phone':g['phone'],'item':g['item'],'price':base,'total':total,'delivery':delivery_loc,'payment':payment,'status':'Pending','tracking':'Pending - Waiting Seller','time':datetime.now().strftime('%H:%M %d %b'),'commission':comm,'seller_gets':seller_gets}
                st.session_state.my_orders.append(order)
                st.session_state.seller_inbox.append(order)
                st.session_state.escrow_balance += total
                st.success('Order placed in ' + cat_name + '! Escrow held. Seller will reply YES / NO.')
                st.balloons()
        notify_msg = 'Hello ' + g['name'] + ', Row Economy Market NEW ORDER in ' + cat_name + ': ' + g['item'] + ' Total N' + str(total) + ' Buyer ' + buyer_name + ' - ' + buyer_phone + '. Reply YES / NO.'
        notify_link = 'https://wa.me/' + g['phone'] + '?text=' + urllib.parse.quote(notify_msg)
        st.link_button('Notify Seller on WhatsApp - USAGE: Tell seller you ordered', notify_link)
        st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)
if page == 'Home':
    st.markdown('<div style="background:linear-gradient(90deg,#EF4444,#F97316);color:white;border-radius:16px;padding:16px;margin:14px 16px;text-align:center;box-shadow:0 4px 16px rgba(239,68,68,0.25)"><b>DEAL OF THE DAY - 12% OFF</b><br>Use
