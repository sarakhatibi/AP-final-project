from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from model.product import Product
from database.connection import get_db
from typing import List
from schemas.product import LowStockAlert

router = APIRouter()
@router.get("/low-stock", response_model=List[LowStockAlert])
def get_low_stock_products(
    session: Session = Depends(get_db),
    
):
  

    products = session.exec(select(Product).where(Product.quantity < 5)).all()

    alerts = [
        LowStockAlert(
            name=p.name,
            sku=p.sku,
            quantity=p.quantity,
            min_threshold=p.min_threshold,
            alert=f"'{p.name}' موجودی کمی دارد ({p.quantity} عدد باقی‌مانده)"
        )
        for p in products
    ]

    return alerts