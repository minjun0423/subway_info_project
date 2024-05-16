from fastapi import FastAPI

import requests

app =FastAPI()

@app.get("/")

def read_root():
    URL = "http://swopenapi.seoul.go.kr/api/subway/427a53796b6d696e37344f6451594a/xml/realtimeStationArrival/0/5/%EC%84%9C%EC%9A%B8"
#지하철 실시간 도착정보 불러오기

#http://swopenapi.seoul.go.kr/api/subway/427a53796b6d696e37344f6451594a/xml/realtimePosition/0/5/1%ED%98%B8%EC%84%A0
#지하철 실시간 열차 위치정보

    contents = requests.get(URL).text

    return {"message": contents}

@app.get("/home")
def home():
    return {"message": "home!"}


@app.get("/subway/{station_name}")
async def get_subway_info(station_name: str):
    try:
        api_key = "427a53796b6d696e37344f6451594a"  # 발급받은 API 키를 여기에 입력합니다.
        url = f"http://swopenapi.seoul.go.kr/api/subway/427a53796b6d696e37344f6451594a/xml/realtimeStationArrival/0/5/{station_name}"
        
        # 서울 열린 데이터 광장 API로 요청을 보냅니다.
        response = requests.get(url)
        response.raise_for_status()  # 오류가 발생하면 예외를 발생시킵니다.

        subway_info = response.content  # API 응답을 바이너리 형식으로 가져옵니다.
        return subway_info  # 클라이언트에게 지하철 정보를 반환합니다.
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Error fetching subway data") from e