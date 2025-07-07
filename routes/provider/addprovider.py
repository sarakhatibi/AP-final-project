
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.connection import get_session
from models.provider import Provider, ProviderCreate

router = APIRouter()

@router.post("/providers/", response_model=Provider)
def create_provider(provider: ProviderCreate, session: Session = Depends(get_session)):
    try:
    
        db_provider = Provider.from_orm(provider)
        session.add(db_provider)
        session.commit()
        session.refresh(db_provider)
        return db_provider
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating provider: {str(e)}")