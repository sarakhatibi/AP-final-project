from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from model.user import User, Userwallet
from security.auth import get_current_user
from database.connection import get_db
from schemas.user import WalletChargeRequest, UserwalletRead  

router = APIRouter()

@router.post("/wallet_charge", response_model=UserwalletRead)
def charge_wallet(
    data: WalletChargeRequest,
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    amount = data.amount
    if amount <= 0:
        raise HTTPException(status_code=400, detail="مبلغ باید بیشتر از صفر باشد")

    wallet = session.exec(select(Userwallet).where(Userwallet.id == current_user.id)).first()

    if not wallet:
        wallet = Userwallet(id=current_user.id, userwallet=amount)
        session.add(wallet)
    else:
        wallet.userwallet += amount
        session.add(wallet)

    session.commit()
    session.refresh(wallet)

    return wallet
