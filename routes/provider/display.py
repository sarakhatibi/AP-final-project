
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from database.connection import get_session
from model.provider import provider

router = APIRouter()

@router.get("/providers/", response_model=list[provider])
def read_providers(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    try:
        offset = (page - 1) * limit
        query = select(provider).offset(offset).limit(limit)
        providers = session.exec(query).all()
        if not providers:
            raise HTTPException(status_code=404, detail="هیچ تأمین‌کننده‌ای در این صفحه پیدا نشد.")
        return providers
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching providers: {str(e)}")