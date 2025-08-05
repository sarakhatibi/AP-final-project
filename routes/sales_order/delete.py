from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from model.order import OrderItem
from database.connection import get_db
from model.user import User
from security.auth import get_current_user

router = APIRouter()

@router.delete("/delete/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # پیدا کردن سفارش
    order = db.exec(
        select(OrderItem).where(
            OrderItem.id == order_id,
            OrderItem.user_id == current_user.id  # فقط سفارش‌های مربوط به کاربر فعلی
        )
    ).first()

    if not order:
        raise HTTPException(status_code=404, detail="سفارشی با این مشخصات پیدا نشد.")

    try:
        db.delete(order)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"خطا در حذف سفارش: {str(e)}")

    return {"message": "سفارش با موفقیت حذف شد."}