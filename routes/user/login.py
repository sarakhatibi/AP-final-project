from fastapi import APIRouter, Depends,HTTPException,status 
from sqlmodel import Session, select 
from database.connection import get_db 
from schemas.user import UserCreate
from schemas.user import UserLogin
from model.user import User
from security.hash import hash_password,verify_password
from security.jwt import create_access_token



router = APIRouter()
@router.post("/login")
def login(credentials: UserLogin, session: Session = Depends(get_db)):
    user = session.exec(select(User).where(User.username == credentials.username)).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="نام کاربری یا رمز اشتباه است")
    
    token = create_access_token({"sub": str(user.id), "role": user.role})
    return {
    "access_token": token,
    "token_type": "bearer",
    "role": user.role  }