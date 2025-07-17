
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from model.order import Order
from schemas.order import OrderCreate, OrderRead, OrderUpdate
from database.connection import get_session

router = APIRouter()


@router.get("/getbyid/{order_id}", response_model=OrderRead)
def get_order(order_id: int, session: Session = Depends(get_session)):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

