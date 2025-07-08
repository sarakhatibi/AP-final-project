from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.connection import get_session
from model.user import User
from schemas.user import UserUpdate   

router = APIRouter()

def get_db(): 
    with get_session() as session: 
        yield session

@router.put("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate, session: Session = Depends(get_db)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.full_name = user_update.full_name
    user.email = user_update.email
    user.username = user_update.username
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"msg": "User updated successfully", "user": user}