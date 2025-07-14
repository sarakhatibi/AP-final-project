from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.connection import get_session
from model.user import User
from schemas.user import UserUpdate   
from security.auth import get_current_user

router = APIRouter()

def get_db(): 
    with get_session() as session: 
        yield session

@router.put("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate, session: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
 if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Only admins can edit users.")
 user = session.get(User, user_id)
 if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
 user.full_name = user_update.full_name
 user.email = user_update.email
 user.username = user_update.username
 user.password=user_update.password
 session.add(user)
 session.commit()
 session.refresh(user)
 return {"msg": "User updated successfully", "user": user}