
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from database.connection import get_session
from model.provider import provider
from security.auth import get_current_user
from model.user import User


router = APIRouter()

@router.get("/providers/", response_model=list[provider])
def read_providers(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Only admins can see providers.")
    try:
        offset = (page - 1) * limit
        query = select(provider).offset(offset).limit(limit)
        providers = session.exec(query).all()
        if not providers:
            raise HTTPException(status_code=404, detail="هیچ تأمین‌کننده‌ای در این صفحه پیدا نشد.")
        return providers
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching providers: {str(e)}")