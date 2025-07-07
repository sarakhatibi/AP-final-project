from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.connection import get_session
from model.provider import Provider

router = APIRouter()

@router.get("/providers/", response_model=list[Provider])
def read_providers(session: Session = Depends(get_session)):
    try:
        providers = session.exec(select(Provider)).all()
        return providers
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching providers: {str(e)}")