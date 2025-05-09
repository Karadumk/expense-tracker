from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/signup", response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    existing_user = crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    new_user = crud.create_user(db, user)
    return new_user
