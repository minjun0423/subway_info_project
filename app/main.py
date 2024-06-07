from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import requests

API_KEY = "427a53796b6d696e37344f6451594a"  #서울시 오픈API 키
BASE_URL = "http://swopenapi.seoul.go.kr/api/subway"

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/subway", response_class=HTMLResponse)
def subway_info(request: Request):
    return templates.TemplateResponse("subway.html", {"request": request})

@app.post("/subway")
def search_station(station: str = Form(...)):
    return RedirectResponse(url=f"/subway/{station}")

@app.get("/subway/{station}")
def get_real_time_arrival_info(station: str):
    url = f"{BASE_URL}/{API_KEY}/json/realtimeStationArrival/0/5/{station}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json() #JSON 형식 변환 데이터
        
    processed_data = [] # 데이터 가공
    for arrival_info in data["realtimeArrivalList"]:
        station = arrival_info["statnNm"]
        train_line = arrival_info["trainLineNm"] #도착지 방면
        arvlMsg2 = arrival_info["arvlMsg2"] #첫번째도착메세지, (도착, 출발 , 진입 등)
        arvlMsg3 = arrival_info["arvlMsg3"] #두번째도착메세지, (종합운동장 도착,12분 후 (광명사거리) 등)
        updownline = arrival_info["updnLine"]
        barvlDt = arrival_info["barvlDt"]
        btrainNo = arrival_info["btrainNo"]
        subwayId = arrival_info["subwayId"]
        #cur_time = r.json()['datetime']
        #ordkey = arrival_info["ordkey"]

        processed_data.append({
            "열차번호": btrainNo,
            "호선": subwayId,
            "상하행선구분": updownline,
            "지하철 위치": arvlMsg3,
            "지하철 도착까지": arvlMsg2})
    return processed_data
