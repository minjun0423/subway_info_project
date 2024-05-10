from fastapi import FastAPI

import requests

app =FastAPI()

@app.get("/")
#def root():
#    return {"message": "Hello Root!"}

def read_root():
    URL = "http://swopenapi.seoul.go.kr/api/subway/427a53796b6d696e37344f6451594a/xml/realtimeStationArrival/0/5/%EC%84%9C%EC%9A%B8"
#지하철 실시간 도착정보

#http://swopenapi.seoul.go.kr/api/subway/427a53796b6d696e37344f6451594a/xml/realtimePosition/0/5/1%ED%98%B8%EC%84%A0
#지하철 실시간 열차 위치정보

    contents = requests.get(URL).text

    return {"message": contents}

@app.get("/home")
def home():
    return {"message": "home!"}