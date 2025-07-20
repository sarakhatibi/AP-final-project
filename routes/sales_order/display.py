from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.connection import get_db
from model.order import OrderItem

router = APIRouter()

@router.get("/display/{user_id}")
def get_user_orders(user_id: int, db: Session = Depends(get_db)):
    orders = db.exec(select(OrderItem).where(OrderItem.user_id == user_id)).all()
    if not orders:
        raise HTTPException(status_code=404, detail="هیچ سفارشی برای این کاربر پیدا نشد.")
    
    return {"orders": orders}