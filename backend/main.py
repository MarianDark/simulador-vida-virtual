from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth.auth import (
    get_current_user,
    authenticate_user,
    create_access_token,
    fake_users_db,
)
from routes.npc_routes import router as npc_router
from routes.user_routes import router as user_router
from routes.auth_routes import router as auth_router
from db import npc_collection

app = FastAPI()

# Incluir rutas del NPC, usuario y autenticación
app.include_router(npc_router)
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
async def home():
    return {"message": "Simulador de Vida Virtual con IA funcionando 🚀"}

# Endpoint de autenticación (Login con OAuth2)
@app.post("/auth/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")

    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

# Ruta protegida: Obtener usuario autenticado
@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

