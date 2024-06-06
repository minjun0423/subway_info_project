from fastapi import FastAPI #최종

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
