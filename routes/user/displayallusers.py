from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database.connection import get_session
from model.user import User
from schemas.user import  UserRead, UserCreate, UserUpdate, UserLogin

router = APIRouter(tags=["Users"])

def get_db(): 
    with get_session() as session: 
        yield session

@router.get("/users", response_model=list[UserRead])
def get_all_users(session: Session = Depends(get_db)):
 users = session.exec(select(User)).all()
 return users
