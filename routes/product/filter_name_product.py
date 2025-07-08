from fastapi import APIRouter, Depends, HTTPException 
from sqlmodel import Session, select 
from typing import List, Optional 
from datetime import datetime 
 
from model.product import Product
from schemas.prudct import ProductCreate, ProductRead, ProductUpdate 
from database.connection import get_session 
 
router = APIRouter() 
def get_db(): 
    with get_session() as session: 
        yield session
@router.get("/", response_model=List[ProductRead]) 
def read_products(skip: int = 0, limit: int = 100, name: Optional[str] = None, session: Session = Depends(get_db)): 
    query = select(Product) 
    if name: 
        query = query.where(Product.name.contains(name)) 
    products = session.exec(query.offset(skip).limit(limit)).all() 
    return products