from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models.order import Order
from schemas.order import OrderCreate, OrderRead, OrderUpdate
from database.connection import get_session

router = APIRouter()

@router.get("/orders/", response_model=list[OrderRead])
def get_all_orders(session: Session = Depends(get_session)):
    orders = session.exec(select(Order)).all()
    return orders

