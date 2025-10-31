from fastapi import FastAPI
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
version = os.getenv("APP_VERSION", "unknown")

@app.get("/")
async def read_root():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"version": version, "current_time": current_time}
