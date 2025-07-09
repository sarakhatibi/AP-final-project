
from typing import Optional
from sqlmodel import SQLModel
from datetime import datetime
from model.order import OrderStatus, OrderType


class OrderUpdate(SQLModel):
    customer_name: Optional[str] = None
    order_type: Optional[OrderType] = None
    status: Optional[OrderStatus] = None
    order_date: Optional[datetime] = None
    provider_id: Optional[int] = None


class OrderCreate(SQLModel):
    customer_name: str
    order_type:OrderType
    status: OrderStatus
    provider_id: int

class OrderRead(SQLModel):
    id: int
    customer_name: str
    order_type:OrderType 
    status: OrderStatus
    order_date: datetime
    provider_id: int

