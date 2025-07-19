from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database.connection import get_db
from schemas.user import UserCreate
from model.user import User,Userwallet
from security.hash import hash_password


router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user_create: UserCreate, session: Session = Depends(get_db)):
    statement = select(User).where(
        (User.email == user_create.email) | (User.username == user_create.username)
    )
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered"
        )
    
    hashed = hash_password(user_create.password)
    new_user = User(
        full_name=user_create.full_name,
        email=user_create.email,
        username=user_create.username,
        hashed_password=hashed
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    new_wallet = Userwallet(id=new_user.id, userwallet=0.0)
    session.add(new_wallet)
    session.commit()
    session.refresh(new_wallet)
    return {"msg": "ثبت‌ نام موفق", "user_id": new_user.id}