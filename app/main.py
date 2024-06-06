from fastapi import FastAPI #최종

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/subway")
def subway_info():
    return {"지하철 테스트"}