
from fastapi import APIRouter, Depends, HTTPException 
from sqlmodel import Session, select 
from typing import List, Optional 
from datetime import datetime  
from model.product import Product, ProductCreate, ProductRead, ProductUpdate 
from database.connection import get_session 

router = APIRouter() 
def get_db(): 
    with get_session() as session: 
        yield session 

@router.put("/{product_id}", response_model=ProductRead) 
def update_product(product_id: int, product_update: ProductUpdate, session: Session = Depends(get_db)): 
    product = session.get(Product, product_id) 
    if not product: 
        raise HTTPException(status_code=404, detail="Product not found") 
    product_data = product_update.dict(exclude_unset=True) 
    for key, value in product_data.items(): 
        setattr(product, key, value) 
    session.add(product) 
    session.commit() 
    session.refresh(product) 
    return product