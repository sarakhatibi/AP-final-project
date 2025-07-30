
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.order import Order
from database.connection import get_db
from schemas.order import OrderCreate
from datetime import datetime

router = APIRouter()

@router.post("/add")
def create_order(order_data: OrderCreate, session: Session = Depends(get_db)):
    try:
        new_order = Order(**order_data.dict())
        session.add(new_order)
        session.commit()
        session.refresh(new_order)
        return {"message": "Order created successfully", "order": new_order}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"خطا در ثبت سفارش: {str(e)}")