# File: app/main.py
from fastapi import FastAPI, Depends, HTTPException
from app.database import SessionLocal, get_db
from app import models
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os


app = FastAPI()


@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    # Try querying the user table (empty at first)
    users = db.query(models.User).all()
    return {"users_count": len(users)}


