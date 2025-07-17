
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database.connection import get_session
from model.provider import provider
from security.auth import get_current_user
from model.user import User


router = APIRouter()

def get_db(): 
    with get_session() as session: 
        yield session

@router.delete("/delete/{provider_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_provider(provider_id: int, session: Session = Depends(get_session),current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Only admins can delete providers.")
    provider = session.get(provider, provider_id)
    if not provider:
        raise HTTPException(status_code=404, detail="Provider not found")
    session.delete(provider)
    session.commit()
    return