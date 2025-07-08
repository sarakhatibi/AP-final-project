from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database.connection import get_session
from model import product
from typing import List

router = APIRouter()

@router.get("/low-stock", response_model=List[product])
def get_low_stock_products(session: Session = Depends(get_session)):
    query = select(product).where(product.quantity < product.min_threshold)
    results = session.exec(query).all()
    return results