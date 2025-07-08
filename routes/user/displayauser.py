from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database.connection import get_session
from model.user import User
from schemas.user import UserRead, UserCreate, UserUpdate, UserLogin

def get_db(): 
    with get_session() as session: 
        yield session

router = APIRouter (tags=["Users"])
@router.get("/users/{user_id}", response_model=UserRead)
def get_single_user(user_id: int, session: Session = Depends(get_db)):
 user = session.get(User, user_id)
 if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
           detail=f"User with ID {user_id} not found"
        )
 return user