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
 

@router.post("/", response_model=ProductRead) 
def create_product(product: ProductCreate, session: Session = Depends(get_db)): 
    db_product = Product.from_orm(product) 
    session.add(db_product) 
    session.commit() 
    session.refresh(db_product) 
    return db_product
