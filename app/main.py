# File: app/main.py
from fastapi import FastAPI, Depends
from app.database import get_db
from app import models
from sqlalchemy.orm import Session
from app.routers import users


app = FastAPI()
app.include_router(users.router)


@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    # Try querying the user table (empty at first)
    users = db.query(models.User).all()
    return {"users_count": len(users)}


