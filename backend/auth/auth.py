import os
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

# Cargar clave secreta desde variables de entorno o usar una por defecto
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")  # Usa una clave segura en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Configuración de Hashing de Contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Esquema de autenticación OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Simulación de base de datos de usuarios (Reemplazar con MongoDB)
fake_users_db = {
    "usuario": {
        "username": "usuario",
        "full_name": "Usuario Ejemplo",
        "email": "usuario@example.com",
        "hashed_password": pwd_context.hash("password123"),
        "disabled": False,
    }
}

# Función para verificar la contraseña ingresada con la almacenada (hash)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Función para obtener un usuario de la base de datos simulada
def get_user(db: Dict[str, Any], username: str) -> Optional[Dict[str, Any]]:
    return db.get(username)

# Función para autenticar usuario (verifica usuario y contraseña)
def authenticate_user(db: Dict[str, Any], username: str, password: str) -> Optional[Dict[str, Any]]:
    user = get_user(db, username)
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user

# Función para crear un token de acceso JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Dependencia para obtener el usuario actual a partir del token de autenticación
async def get_current_user(token: str = Depends(oauth2_scheme)) -> Dict[str, Any]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username)
    if user is None:
        raise credentials_exception
    return user

# Dependencia para verificar si el usuario está activo
async def get_current_active_user(current_user: Dict[str, Any] = Depends(get_current_user)) -> Dict[str, Any]:
    if current_user.get("disabled"):
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return current_user

# Función para actualizar la contraseña de un usuario
def update_user_password(username: str, new_password: str) -> bool:
    user = get_user(fake_users_db, username)
    if user:
        user["hashed_password"] = pwd_context.hash(new_password)
        return True
    return False
