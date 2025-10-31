from fastapi import FastAPI
import os

app = FastAPI()

GREETING = os.getenv('GREETING', 'Hello')
APP_VERSION = os.getenv('APP_VERSION', '1.0')

@app.get("/")
async def root():
    return {
        "message": f"{GREETING}, Kubernetes!",
        "version": APP_VERSION
    }
