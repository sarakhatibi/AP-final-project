from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.connection import get_db
from model.user import User
from schemas.user import UserUpdate   
from security.auth import get_current_user
from security.hash import hash_password

router = APIRouter()

@router.put("/edit/{user_id},response_model=UserUpdateResponse")
def update_user(
    user_id: int,
    user_update: UserUpdate,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    
    if current_user.role != "admin" and current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Access denied")


    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    

    if user_update.full_name is not None:
        user.full_name = user_update.full_name
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.username is not None:
        user.username = user_update.username
    if user_update.password is not None and user_update.password.strip() != "":
        user.hashed_password = hash_password(user_update.password)

    session.add(user)
    session.commit()
    session.refresh(user)

    return {"msg": "User updated successfully", "user": user}
