from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from model.product import Product
from database.connection import get_session
from schemas.product import ProductRead 
from typing import List


router = APIRouter()

@router.get("/showbyprice" ,response_model=List[ProductRead]
 )
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    offset = (page - 1) * limit
    query = select(Product).order_by(Product.price)
    products = session.exec(query.offset(offset).limit(limit)).all()
    if not products:
        raise HTTPException(status_code=404, detail="هیچ کالایی در دیتابیس پیدا نشد.")
    return products