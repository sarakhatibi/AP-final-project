from fastapi import APIRouter, Query, Depends, HTTPException
from sqlmodel import Session, select
from typing import Optional
from model.product import Product
from database.connection import get_session

router = APIRouter()

@router.get("/products")
def get_products(
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    session: Session = Depends(get_session)  
):
    query = select(Product)

    if min_price is not None:
        query = query.where(Product.price >= min_price)
    if max_price is not None:
        query = query.where(Product.price <= max_price)

    products = session.exec(query).all()
    if not products:
        raise HTTPException(
            status_code=404,
            detail="هیچ کالایی در بازه‌ی قیمتی مشخص‌شده پیدا نشد."
        )

    return products