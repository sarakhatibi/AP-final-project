
from fastapi import APIRouter, Depends, HTTPException 
from sqlmodel import Session, select 
from typing import List, Optional 
from datetime import datetime 
from model.product import Product
from schemas.product import ProductCreate, ProductRead, ProductUpdate 
from database.connection import get_db
from security.auth import get_current_user
from model.user import User
router = APIRouter() 

@router.delete("/delete/{product_id}") 
def delete_product(product_id: int, session: Session = Depends(get_db),current_user: User = Depends(get_current_user)): 
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Only admins can delete products.")

    product = session.get(Product, product_id) 
    if not product: 
        raise HTTPException(status_code=404, detail="Product not found") 
    session.delete(product) 
    session.commit() 
    return {"ok": True}