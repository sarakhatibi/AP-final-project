from fastapi import APIRouter, Depends, HTTPException 
from sqlmodel import Session, select 
from typing import List, Optional 
from datetime import datetime 
from database.connection import get_db
from model.product import Product
from schemas.product import ProductCreate, ProductRead, ProductUpdate 
router = APIRouter() 
 

@router.get("/filter_id/{product_id}", response_model=ProductRead) 
def read_product(product_id: int, session: Session = Depends(get_db)): 
    product = session.get(Product, product_id) 
    if not product: 
        raise HTTPException(status_code=404, detail="Product not found") 
    return product
