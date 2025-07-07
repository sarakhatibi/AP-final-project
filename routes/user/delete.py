from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from database.connection import get_db
from model.user import User  

router = APIRouter()

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, session: Session = Depends(get_db)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return