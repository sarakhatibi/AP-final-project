
from fastapi import APIRouter, Depends, HTTPException 
from sqlmodel import Session, select 
from typing import List, Optional 
from datetime import datetime 
from models.product import Product, ProductCreate, ProductRead, ProductUpdate 
from database.connection import get_session  
router = APIRouter() 
def get_db(): 
    with get_session() as session: 
        yield session 

@router.delete("/{product_id}") 
def delete_product(product_id: int, session: Session = Depends(get_db)): 
    product = session.get(Product, product_id) 
    if not product: 
        raise HTTPException(status_code=404, detail="Product not found") 
    session.delete(product) 
    session.commit() 
    return {"ok": True}