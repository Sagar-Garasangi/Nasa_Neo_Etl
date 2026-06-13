import requests
import pandas as pd
from datetime import datetime
import time 
import pyarrow
from config import host,password,api_key,user,db
url="https://api.nasa.gov/neo/rest/v1/feed"
records="near_earth_object"
df=[]
def extract(url,record,st_date,end_date,api):
    try:
        data=requests.get(url,params={"start_date":st_date,"end_date":end_date,"api_key":api_key},timeout=10)
        if(data.status_code==429):
            time.sleep(60)
        data.raise_for_status()
        if(data.status_code==200):
            data_json=data.json()
            if(not data_json):
             exit()
            neo = data_json["near_earth_objects"]
            for key,value in neo.items():
                df.extend(value)
        
    except requests.RequestException as e:
        print(f"failed extraction {e}")

extract(url,"near_earth_objects","2026-06-11","2026-06-11",api_key)
df_data=pd.json_normalize(df)
print(df_data.info())
