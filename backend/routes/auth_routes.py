from fastapi import APIRouter, Depends, HTTPException, status
from db import user_collection
from models.user import UserCreate, UserInDB
from auth.auth import create_access_token, authenticate_user, pwd_context

router = APIRouter()

@router.post("/auth/register", response_model=UserInDB)
async def register_user(user: UserCreate):
    # Verificar si el usuario ya existe
    existing_user = await user_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    hashed_password = pwd_context.hash(user.password)
    user_data = user.dict()
    user_data["hashed_password"] = hashed_password
    del user_data["password"]

    result = await user_collection.insert_one(user_data)
    user_data["_id"] = str(result.inserted_id)

    return user_data

@router.post("/auth/login")
async def login(user_credentials: UserCreate):
    user = await authenticate_user(user_credentials.username, user_credentials.password)
    if not user:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
    
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
