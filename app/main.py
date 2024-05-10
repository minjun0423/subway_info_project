from fastapi import FastAPI

import requests

app =FastAPI()

@app.get("/")
#def root():
#    return {"message": "Hello Root!"}

def read_root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&metroCd=11&cityCd=110&bizCd=C&apiKey=69viVTSCMlJ552B9O243czcn718eth0C5691acbA&returnType=json"

    contents = requests.get(URL).text

    return {"message": contents}

@app.get("/home")
def home():
    return {"message": "home!"}