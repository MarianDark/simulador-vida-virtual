from fastapi import APIRouter, Depends
from auth.auth import get_current_active_user
from models.user import UserInDB

router = APIRouter()

@router.get("/users/me", response_model=UserInDB)
async def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    return current_user
