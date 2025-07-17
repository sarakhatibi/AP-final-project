from fastapi import Path
from fastapi import APIRouter, Depends, HTTPException
from model.order import Order
from sqlmodel import Session
from database.connection import get_session


router = APIRouter()
@router.put("/update/{order_id}", response_model=Order)
def update_order(order_id: int, updated_order: Order, session: Session = Depends(get_session)):
    existing_order = session.get(Order, order_id)
    if not existing_order:
        raise HTTPException(status_code=404, detail="Order not found")

    for field, value in updated_order.dict().items():
        setattr(existing_order, field, value)

    session.add(existing_order)
    session.commit()
    session.refresh(existing_order)

    return existing_order