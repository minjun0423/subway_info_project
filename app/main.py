from fastapi import FastAPI

import requests

app =FastAPI()

@app.get("/")
#def root():
#    return {"message": "Hello Root!"}

def read_root():
    URL = "http://swopenAPI.seoul.go.kr/api/subway/427a53796b6d696e37344f6451594a/xml/realtimeStationArrival/0/5/¼­¿ï"

    contents = requests.get(URL).text

    return {"message": contents}

@app.get("/home")
def home():
    return {"message": "home!"}