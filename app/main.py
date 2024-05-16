from fastapi import FastAPI

import requests

app =FastAPI()

@app.get("/")

def read_root():
    URL = "http://swopenapi.seoul.go.kr/api/subway/427a53796b6d696e37344f6451594a/xml/realtimeStationArrival/0/5/%EC%84%9C%EC%9A%B8"
#����ö �ǽð� �������� �ҷ�����

#http://swopenapi.seoul.go.kr/api/subway/427a53796b6d696e37344f6451594a/xml/realtimePosition/0/5/1%ED%98%B8%EC%84%A0
#����ö �ǽð� ���� ��ġ����

    contents = requests.get(URL).text

    return {"message": contents}

@app.get("/home")
def home():
    return {"message": "home!"}


@app.get("/subway/{station_name}")
async def get_subway_info(station_name: str):
    try:
        api_key = "427a53796b6d696e37344f6451594a"  # �߱޹��� API Ű�� ���⿡ �Է��մϴ�.
        url = f"http://swopenapi.seoul.go.kr/api/subway/427a53796b6d696e37344f6451594a/xml/realtimeStationArrival/0/5/{station_name}"
        
        # ���� ���� ������ ���� API�� ��û�� �����ϴ�.
        response = requests.get(url)
        response.raise_for_status()  # ������ �߻��ϸ� ���ܸ� �߻���ŵ�ϴ�.

        subway_info = response.content  # API ������ ���̳ʸ� �������� �����ɴϴ�.
        return subway_info  # Ŭ���̾�Ʈ���� ����ö ������ ��ȯ�մϴ�.
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Error fetching subway data") from e