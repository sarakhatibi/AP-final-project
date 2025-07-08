from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.connection import get_session
from model.provider import provider
from schemas.provider import ProviderUpdate

router = APIRouter()

@router.put("/providers/{provider_id}", response_model=provider)
def update_provider(
    provider_id: int,
    provider_update: ProviderUpdate,
    session: Session = Depends(get_session)
):
    provider = session.get(provider, provider_id)
    if not provider:
        raise HTTPException(status_code=404, detail="Provider not found")

    provider_data = provider_update.dict(exclude_unset=True)
    for key, value in provider_data.items():
        setattr(provider, key, value)

    session.add(provider)
    session.commit()
    session.refresh(provider)
    return provider