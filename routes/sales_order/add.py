from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.connection import get_db
from model.product import Product
from model.user import Userwallet, User
from model.order import OrderStatus
from model.sales_order import OrderItem
from schemas.sales_order import OrdersalesCreate
from datetime import datetime
from security.auth import get_current_user 


router = APIRouter()

@router.post("/add")
def create_order( 
    order_data: OrdersalesCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.exec(select(User).where(User.id == current_user.id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="کاربر پیدا نشد.")
   
    product = db.exec(select(Product).where(Product.id == order_data.product_id)).first()
    if not product:
        raise HTTPException(status_code=404, detail="محصول پیدا نشد.")

   
    if product.quantity < order_data.quantity:
        raise HTTPException(status_code=400, detail="موجودی محصول کافی نیست.")

    
    user_wallet = db.exec(select(Userwallet).where(Userwallet.id == current_user.id)).first()
    if not user_wallet:
        raise HTTPException(status_code=400, detail="کیف پول برای این کاربر یافت نشد.")
    
    if user_wallet.userwallet < (order_data.quantity * product.price):
        raise HTTPException(status_code=400, detail="موجودی کیف پول کافی نیست.")


    total_price = order_data.quantity * product.price

   
    product.quantity -= order_data.quantity
    db.add(product)

  
    user_wallet.userwallet -= total_price
    db.add(user_wallet)

   
    new_order = OrderItem(
        user_id=current_user.id,
        product_id=product.id,
        quantity=order_data.quantity,
        unit_price=product.price,
        status=OrderStatus.draft,
        
    )
    db.add(new_order)
    try:
        
        db.commit()
        db.refresh(new_order)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"خطا در ثبت سفارش: {str(e)}")

    return {"message": "سفارش با موفقیت ثبت شد.", "order": new_order}