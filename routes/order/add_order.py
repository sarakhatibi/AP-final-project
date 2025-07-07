
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from models.order import Order
from database.connection import get_session

router = APIRouter()

@router.post("/orders/")
def create_order(order: Order, session: Session = Depends(get_session)):
    try:
        session.add(order)
        session.commit()
        session.refresh(order)
        return {
            "message": "Order created successfully.",
            "order": order
        }
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")