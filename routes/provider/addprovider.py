
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.connection import get_session
from model.provider import provider
from schemas.provider import ProviderCreate
from security.auth import get_current_user
from model.user import User

router = APIRouter()

@router.post("/add", response_model=provider)
def create_provider(provider: ProviderCreate, session: Session = Depends(get_session),current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Only admins can add providers.")
    try:
    
        db_provider = provider.from_orm(provider)
        session.add(db_provider)
        session.commit()
        session.refresh(db_provider)
        return db_provider
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating provider: {str(e)}")