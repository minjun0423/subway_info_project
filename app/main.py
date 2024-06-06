from fastapi import FastAPI #√÷¡æ

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
