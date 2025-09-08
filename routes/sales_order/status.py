from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database.connection import get_db
from model.order import OrderStatus
from schemas.sales_order import StatusUpdate
from model.sales_order import OrderItem

router = APIRouter()

@router.get("/status/{order_id}")
def get_order_status(order_id: int, db: Session = Depends(get_db)):
    order = db.exec(select(OrderItem).where(OrderItem.id == order_id)).first()
    if not order:
        raise HTTPException(status_code=404, detail="سفارش پیدا نشد.")

    return {
        "product_id": order.product_id,
        "quantity": order.quantity,
        "unit_price": order.unit_price,
        "status": order.status
    }