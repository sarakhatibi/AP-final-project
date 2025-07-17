from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List, Optional
from model.product import Product
from schemas.product import ProductRead
from database.connection import get_session

router = APIRouter()

def get_db():
    with get_session() as session:
        yield session

@router.get("/filter_name", response_model=List[ProductRead])
def read_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    name: Optional[str] = None,
    session: Session = Depends(get_db)
):
   
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail="page و limit باید عددی بزرگ‌تر از صفر باشند.")

   
    offset = (page - 1) * limit

    query = select(Product)
    if name:
        query = query.where(Product.name.contains(name))

    products = session.exec(query.offset(offset).limit(limit)).all()

    
    if not products:
        raise HTTPException(status_code=404, detail="هیچ محصولی در این صفحه پیدا نشد.")

    
    return products