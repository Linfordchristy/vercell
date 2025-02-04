# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "the health check is succesfull"
