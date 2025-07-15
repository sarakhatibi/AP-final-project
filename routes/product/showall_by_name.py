from sqlmodel import select, SQLModel, Session
from fastapi import APIRouter, Depends, HTTPException
from model.product import Product
from database.connection import get_session
router = APIRouter()
@router.get("/products")
def get_products(
    session: Session = Depends(get_session)
):
    query = select(Product).order_by(Product.name) 

    products = session.exec(query).all()

    if not products:
        raise HTTPException(
            status_code=404,
            detail="هیچ کالایی در دیتابیس پیدا نشد."
        )

    return products