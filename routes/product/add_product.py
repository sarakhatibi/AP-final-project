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
 

@router.post("/add", response_model=ProductRead) 
def create_product(product: ProductCreate, session: Session = Depends(get_db),current_user: User = Depends(get_current_user)): 
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied. Only admins can create products.")
    existing_product = session.exec(select(Product).where(Product.sku == product.sku)).first()
    
    if existing_product:
        existing_product.quantity += product.quantity

        updated_fields = product.dict(exclude_unset=True)
        for key, value in updated_fields.items():
            if key != "quantity": 
                setattr(existing_product, key, value)

        session.add(existing_product)
        session.commit()
        session.refresh(existing_product)
        return existing_product
    else:
       
        print("✅ مقدار image دریافتی:", product.image)

        db_product = Product.from_orm(product)
        session.add(db_product)
        print("🎯 مقدار image قبل از commit:", db_product.image)
        session.commit()
        session.refresh(db_product)

        print("📦 محصول ذخیره‌شده:", db_product.dict())
        return db_product


