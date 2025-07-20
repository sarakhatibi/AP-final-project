from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database.connection import get_db
from model.order import OrderItem, OrderStatus

router = APIRouter()

@router.put("/status/{order_id}")
def update_order_status(order_id: int, new_status: OrderStatus, db: Session = Depends(get_db)):
    order = db.exec(select(OrderItem).where(OrderItem.id == order_id)).first()
    if not order:
        raise HTTPException(status_code=404, detail="سفارش پیدا نشد.")
    
    OrderItem.status = new_status
    db.add(OrderItem)
    db.commit()
    db.refresh(OrderItem)
    
    return {"message": "وضعیت سفارش با موفقیت تغییر کرد", "order_id": order_id, "new_status": OrderItem.status}