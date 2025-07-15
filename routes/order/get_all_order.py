from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from model.order import Order
from schemas.order import OrderRead
from database.connection import get_session

router = APIRouter()

@router.get("/orders/", response_model=list[OrderRead])
def get_all_orders(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    offset = (page - 1) * limit
    query = select(Order).offset(offset).limit(limit)

    orders = session.exec(query).all()

    if not orders:
        raise HTTPException(status_code=404, detail="سفارشی در این صفحه پیدا نشد.")

    return orders

