import json, os
DB_FILE="adverts.json"
def get_adverts():
    if not os.path.exists(DB_FILE): return []
    try: return json.loads(open(DB_FILE).read())
    except: return []
def add_advert(ad):
    ads=get_adverts(); ads.insert(0,ad)
    open(DB_FILE,"w").write(json.dumps(ads))
