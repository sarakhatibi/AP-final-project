from fastapi import APIRouter, Depends, HTTPException 
from sqlmodel import Session, select 
from typing import List, Optional 
from datetime import datetime 
from model.product import Product
from schemas.product import ProductCreate, ProductRead, ProductUpdate 
from database.connection import get_session 
from security.auth import get_current_user
from model.user import User
 
router = APIRouter() 
 

def get_db(): 
    with get_session() as session: 
        yield session 
 

@router.post("/", response_model=ProductRead) 
def create_product(product: ProductCreate, session: Session = Depends(get_db),current_user: User = Depends(get_current_user)): 
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Only admins can create products.")
    db_product = Product.from_orm(product) 
    session.add(db_product) 
    session.commit() 
    session.refresh(db_product) 
    return db_product
