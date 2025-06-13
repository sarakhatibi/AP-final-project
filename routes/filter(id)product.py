from fastapi import APIRouter, Depends, HTTPException 
from sqlmodel import Session, select 
from typing import List, Optional 
from datetime import datetime 
 
from models.product import Product, ProductCreate, ProductRead, ProductUpdate 
from database.connection import get_session 
 
 
 

@router.get("/{product_id}", response_model=ProductRead) 
def read_product(product_id: int, session: Session = Depends(get_db)): 
    product = session.get(Product, product_id) 
    if not product: 
        raise HTTPException(status_code=404, detail="Product not found") 
    return product
