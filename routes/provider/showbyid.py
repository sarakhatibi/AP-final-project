
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.connection import get_session
from model.provider import Provider
from security.auth import get_current_user
from model.user import User
from schemas.provider import ProviderRead

router = APIRouter()

@router.get("/showbyid/{provider_id}", response_model=ProviderRead)
def read_single_provider(
    provider_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="دسترسی غیرمجاز. فقط ادمین‌ها می‌توانند اطلاعات تأمین‌کننده را ببینند.")
    
    provider_data = session.get(Provider, provider_id)

    if not provider_data:
        raise HTTPException(status_code=404, detail="تأمین‌کننده‌ای با این شناسه یافت نشد.")
    
    return provider_data