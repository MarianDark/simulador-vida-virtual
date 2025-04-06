from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from models.user import UserCreate, UserInDB
from auth.auth import authenticate_user, create_access_token
from db import user_collection
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

    # Verificar si el usuario está autenticado
    if not current_user:
        raise HTTPException(status_code=401, detail="No autenticado")

    # Devolver la información del usuario autenticado
    return current_user 
@router.put("/auth/update", response_model=UserInDB)
async def update_user(user: UserCreate, current_user: UserInDB = Depends(authenticate_user)):
    # Verificar si el usuario está autenticado
    if not current_user:
        raise HTTPException(status_code=401, detail="No autenticado")

    # Actualizar la información del usuario
    hashed_password = pwd_context.hash(user.password)
    user_data = user.dict()
    user_data["hashed_password"] = hashed_password
    del user_data["password"]

    result = await user_collection.update_one({"username": current_user.username}, {"$set": user_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="No se pudo actualizar el usuario")

    updated_user = await user_collection.find_one({"username": current_user.username})
    return updated_user
@router.delete("/auth/delete", response_model=dict)
async def delete_user(current_user: UserInDB = Depends(authenticate_user)):
    # Verificar si el usuario está autenticado
    if not current_user:
        raise HTTPException(status_code=401, detail="No autenticado")

    # Eliminar el usuario
    result = await user_collection.delete_one({"username": current_user.username})
    if result.deleted_count == 0:
        raise HTTPException(status_code=400, detail="No se pudo eliminar el usuario")

    return {"detail": "Usuario eliminado correctamente"}
    # El código parece estar bien estructurado y cubre las operaciones básicas de autenticación y gestión de usuarios.
    # Sin embargo, hay un par de cosas que podrían mejorarse o añadirse:

    # 1. Importar las dependencias necesarias si no están ya importadas:
    # from fastapi import APIRouter, Depends, HTTPException
    # from passlib.context import CryptContext
    # from .models import UserCreate, UserInDB
    # from .auth import authenticate_user, create_access_token
    # from .database import user_collection

    # 2. Asegurarse de que el contexto de contraseña esté definido:
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # 3. Asegurarse de que el router esté definido:
    # router = APIRouter()

    # 4. Asegurarse de que las funciones auxiliares como authenticate_user y create_access_token estén definidas y funcionando correctamente.

    # 5. Asegurarse de que los modelos UserCreate y UserInDB estén definidos correctamente en el archivo models.py.

    # 6. Asegurarse de que la colección user_collection esté correctamente configurada en el archivo database.py.

    # Si todos estos puntos están cubiertos, el código debería funcionar correctamente.
