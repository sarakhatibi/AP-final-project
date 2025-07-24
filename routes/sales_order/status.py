from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from database.connection import get_db
from model.order import OrderItem, OrderStatus
from schemas.sales_order import StatusUpdate

router = APIRouter()

@router.put("/status/{order_id}")
def update_order_status(order_id: int, data: StatusUpdate, db: Session = Depends(get_db)):
    try:
        order = db.exec(select(OrderItem).where(OrderItem.id == order_id)).first()
        if not order:
            raise HTTPException(status_code=404, detail="سفارش پیدا نشد.")

        print("🧪 Enum فعلی:", [e.value for e in OrderStatus])

        print("✅ مقدار جدید status: ", data.new_status)

        order.status = data.new_status

        db.add(order)
        db.commit()
        db.refresh(order)

        return {
            "message": f"وضعیت سفارش با موفقیت به '{order.status}' تغییر کرد",
            "order_id": order.id,
            "new_status": order.status
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ خطای داخلی: {str(e)}")