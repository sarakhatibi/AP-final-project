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
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
   
    offset = (page - 1) * limit

    query = select(Product)

    if min_price is not None:
        query = query.where(Product.price >= min_price)
    if max_price is not None:
        query = query.where(Product.price <= max_price)

   
    products = session.exec(query.offset(offset).limit(limit)).all()

    
    if not products:
        raise HTTPException(
            status_code=404,
            detail="محصولی در این صفحه یا بازه قیمتی یافت نشد."
        )

    
    return {
        "page": page,
        "limit": limit,
        "products": products
    }