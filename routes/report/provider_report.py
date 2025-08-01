from fastapi import APIRouter, Depends
from sqlmodel import Session
from database.connection import get_db
from utils.score import calculate_provider_score
from fastapi import HTTPException

router = APIRouter()

@router.get("/provider_score/{provider_id}")
def score(provider_id: int, session: Session = Depends(get_db)):
    result = calculate_provider_score(provider_id, session)

    if result is None:
        raise HTTPException(status_code=404, detail="تأمین‌کننده یافت نشد")

    return {"provider_id": provider_id, "delivery_score": result}
