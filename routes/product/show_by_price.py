from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from model.product import Product
from database.connection import get_session

router = APIRouter()

@router.get("/showbyprice")
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