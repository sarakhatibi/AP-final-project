from fastapi import Path
from fastapi import APIRouter, Depends, HTTPException
from schemas.order import OrderUpdate,OrderRead
from sqlmodel import Session
from database.connection import get_db
from model.order import Order


router = APIRouter()
@router.put("/update/{order_id}", response_model=OrderRead)
def update_order(order_id: int, updated_order: OrderUpdate, session: Session = Depends(get_db)):
    existing_order = session.get(Order, order_id)
    if not existing_order:
        raise HTTPException(status_code=404, detail="Order not found")

    update_data = updated_order.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(existing_order, field, value)

    session.add(existing_order)
    session.commit()
    session.refresh(existing_order)

    return existing_order