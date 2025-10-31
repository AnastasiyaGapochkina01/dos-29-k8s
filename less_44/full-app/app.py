from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "postgres-service")
DB_NAME = os.getenv("DB_NAME", "testdb")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        row = result.fetchone()
        return {"message": "Hello from FastAPI with Postgres", "db_response": row[0]}
