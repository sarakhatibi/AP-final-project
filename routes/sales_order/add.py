from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database.connection import get_db
from model.product import Product
from model.user import Userwallet
from model.order import OrderItem, OrderStatus
from schemas.sales_order import OrdersalesCreate
from datetime import datetime

router = APIRouter()

@router.post("/add")
def create_order(
    order_data: OrdersalesCreate,  
    db: Session = Depends(get_db)
):
   
    product = db.exec(select(Product).where(Product.id == order_data.product_id)).first()
    if not product:
        raise HTTPException(status_code=404, detail="محصول پیدا نشد.")

   
    if product.quantity < order_data.quantity:
        raise HTTPException(status_code=400, detail="موجودی محصول کافی نیست.")

    
    user_wallet = db.exec(select(Userwallet).where(Userwallet.id == order_data.user_id)).first()
    if not user_wallet or user_wallet.userwallet < (order_data.quantity * product.price):
        raise HTTPException(status_code=400, detail="موجودی کیف پول کافی نیست.")


    total_price = order_data.quantity * product.price

   
    product.quantity -= order_data.quantity
    db.add(product)

  
    user_wallet.userwallet -= total_price
    db.add(user_wallet)

   
    new_order = OrderItem(
        order_id=order_data.order_id,
        product_id=product.id,
        product_name=product.name,
        quantity=order_data.quantity,
        unit_price=product.price,
        status=OrderStatus.draf,
        order_date=datetime.utcnow()
    )
    db.add(new_order)

    db.commit()
    db.refresh(new_order)

    return {"message": "سفارش با موفقیت ثبت شد.", "order": new_order}