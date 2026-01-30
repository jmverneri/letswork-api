from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from app.database import engine
from passlib.context import CryptContext

router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    # 🔹 Paso 1: truncar password a 72 caracteres para evitar error
    password = data.password[:72]

    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT id, email, password_hash FROM users WHERE email = :email"),
            {"email": data.email}
        ).fetchone()

    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not pwd_context.verify(password, result.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "status": "ok",
        "user": {
            "id": result.id,
            "email": result.email
        }
    }

