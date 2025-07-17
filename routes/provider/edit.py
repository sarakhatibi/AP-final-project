from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.connection import get_session
from model.provider import Provider
from schemas.provider import ProviderUpdate
from security.auth import get_current_user
from model.user import User


router = APIRouter()


@router.put("/edit/{provider_id}", response_model=Provider)
def update_provider(
    provider_id: int,
    provider_update: ProviderUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Only admins can edit providers.")
    providerobg = session.get(Provider, provider_id)
    if not providerobg:
        raise HTTPException(status_code=404, detail="Provider not found")

    provider_data = provider_update.dict(exclude_unset=True)
    for key, value in provider_data.items():
        setattr(providerobg, key, value)

    session.add(providerobg)
    session.commit()
    session.refresh(providerobg)
    return providerobg