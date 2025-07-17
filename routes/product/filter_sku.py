from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select
from database.connection import get_session
from model.product import Product
from typing import Optional, List

router = APIRouter()

@router.get("/filter_sku", response_model=List[Product])
def get_products(
    sku: Optional[str] = Query(None),
    session: Session = Depends(get_session)
):
    query = select(Product)
    if sku:
        query = query.where(Product.sku == sku)
    return session.exec(query).all()