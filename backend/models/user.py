from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    disabled: Optional[bool] = False

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str
