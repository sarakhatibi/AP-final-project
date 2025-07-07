from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.order import Order
from database.connection import get_session
router = APIRouter()
@router.delete("/orders/{order_id}")
def delete_order(order_id: int, session: Session = Depends(get_session)):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    session.delete(order)
    session.commit()

    return {"message": "Order deleted successfully."}
