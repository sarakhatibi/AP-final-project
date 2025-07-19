from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from model.user import User, Uwallet
from security.auth import get_current_user
from schemas.user import User,Userwallet
from database.connection import get_db

router = APIRouter()

@router.post("/wallet_charge")
def charge_wallet(amount: float, session: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Mablagh bayad mosbat bashad")

    wallet = session.exec(select(Userwallet).where(Userwallet.id == current_user.id)).first()

    if not wallet:
        wallet = Userwallet(id=current_user.id, userwallet=amount)
        session.add(wallet)
    else:
        wallet.userwallet += amount
        session.add(wallet)

    session.commit()
    session.refresh(wallet)

    return {
        "message": "✅ Sharj wallet ba movafaghiyat anjam shod",
        "new_balance": wallet.userwallet
    }
