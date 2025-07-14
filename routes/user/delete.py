from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from database.connection import get_session
from model.user import User  
from security.auth import get_current_user

router = APIRouter()

def get_db(): 
    with get_session() as session: 
        yield session

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, session: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Only admins can delete users.")

    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return