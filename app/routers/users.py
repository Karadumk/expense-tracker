import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import schemas, crud, database, auth
from datetime import timedelta

load_dotenv()
print(f"Raw ACCESS_TOKEN_EXPIRE_MINUTES: {os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')}")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/signup", response_model=schemas.Token)
def signup(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Check if username already exists
    existing_user = crud.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    # Check if email already exists
    existing_email = crud.get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    new_user = crud.create_user(db=db, user=user)
    access_token = auth.create_access_token(data={"sub": new_user.email})
    return {"access_token": access_token, "token_type": "bearer"}


# @router.post("/signup", response_model=schemas.UserOut)
# def signup(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
#     existing_user = crud.get_user_by_email(db, user.email)
#     if existing_user:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
#         )
#     new_user = crud.create_user(db, user)
#     return new_user


# @router.post("/login")
# def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
#     db_user = db.query(models.User).filter(models.User.email == user.email).first()
#     if not db_user:
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#     if not auth.verify_password(user.password, db_user.hashed_password):
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#     return {"message": "Login successful"}


@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = crud.get_user_by_email(db, email=form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
