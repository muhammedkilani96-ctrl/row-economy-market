import streamlit as st
import json, hashlib, random, pandas as pd
st.set_page_config(page_title='ROW ECONOMY', layout='centered')
def load(f,d):
 try: return json.loads(open(f).read())
 except: return d
def save(f,d):
 open(f,'w').write(json.dumps(d))
def hp(p):
 return hashlib.sha256(p.encode()).hexdigest()
u=load('users.json',{})
u['08116911722']={'pw':hp('Kilani247')}
save('users.json',u)
w=load('wallets.json',{})
if w.get('08116911722',0)<1000:
 w['08116911722']=500000
 save('wallets.json',w)
if 'user' not in st.session_state:
 st.title('ROW ECONOMY SUPER')
 st.info('Login 08116911722 / Kilani247')
 ph=st.text_input('Phone')
 pw=st.text_input('Password',type='password')
 if st.button('Login'):
  us=load('users.json',{})
  if ph in us and us[ph]['pw']==hp(pw):
   st.session_state.user=ph
   st.rerun()
 st.stop()
bal=load('wallets.json',{}).get(st.session_state.user,0)
tabs=st.tabs(['Home','SNAP MAP','SECURITY','SOS','CHAT','Wallet'])
with tabs[0]:
 st.metric('People',10)
 st.metric('Wallet',f'N{bal}')
with tabs[1]:
 st.title('SNAP MAP')
 df=pd.DataFrame({'lat':[9.06+random.uniform(-0.03,0.03) for _ in range(30)],'lon':[7.48+random.uniform(-0.03,0.03) for _ in range(30)]})
 st.map(df)
with tabs[2]:
 st.title('SECURITY MAP')
 df2=pd.DataFrame({'lat':[9.0765,9.0579,6.5244],'lon':[7.4851,7.4951,3.3792]})
 st.map(df2)
 st.write('NANS HQ, Police HQ, Zone 2')
with tabs[3]:
 if st.button('SEND SOS'): st.error('SOS SENT')
 st.link_button('Call 112','tel:112')
with tabs[4]:
 chats=load('global_chat.json',[])
 for c in chats[-20:]: st.write(f"{c['name']}: {c['msg']}")
 m=st.text_input('Msg')
 if st.button('Send'):
  chats.append({'name':st.session_state.user,'msg':m})
  save('global_chat.json',chats)
  st.rerun()
with tabs[5]:
 st.title(f'N{bal}')
 st.image(f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={st.session_state.user}')
 if st.button('Logout'):
  del st.session_state.user
  st.rerun()
