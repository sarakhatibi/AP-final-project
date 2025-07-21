from database.connection import get_db
from pydantic import BaseModel
from typing import Optional
from model.order import OrderStatus

class StatusUpdate(BaseModel):
    new_status: OrderStatus



class  OrdersalesCreate(BaseModel):
    order_id: Optional[int] = None
    product_id: int
    user_id: int
    quantity: int