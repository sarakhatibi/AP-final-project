
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from model.order import Order
from database.connection import get_db

router = APIRouter()

@router.post("/add")
def create_order(order: Order, session: Session = Depends(get_db)):
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