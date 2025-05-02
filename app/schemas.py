from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# Used for request body when signing up
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# Used when returning user data
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


# Request body for adding/updating an expense
class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: Optional[str] = None


# Response schema
class ExpenseResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    category: str
    description: Optional[str] = None
    timestamp: datetime

    class Config:
        orm_mode = True
