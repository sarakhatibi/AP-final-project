from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database.connection import get_db
from model.user import User, UserRead, UserCreate, UserUpdate, UserLogin

router = APIRouter(tags=["Users"])

@router.get("/users", response_model=list[UserRead])
def get_all_users(session: Session = Depends(get_db)):
 users = session.exec(select(User)).all()
 return users
