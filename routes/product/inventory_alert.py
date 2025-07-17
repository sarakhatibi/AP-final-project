from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database.connection import get_session
from model import product
from typing import List
from schemas.product import LowStockAlert



router = APIRouter()

@router.get("/low_stock", response_model=List[LowStockAlert])
def get_low_stock_products(session: Session = Depends(get_session)):
    query = select(product).where(product.quantity < product.min_threshold)
    results = session.exec(query).all()

    alerts = []
    for p in product:
        alerts.append(LowStockAlert(
            name=p.name,
            sku=p.sku,
            quantity=p.quantity,
            min_threshold=p.min_threshold,
                 alert=f"⚠ Stock below minimum threshold ({p.quantity} < {p.min_threshold})"
        ))

    return alerts