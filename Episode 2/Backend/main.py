from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, Student

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Database Connected"}