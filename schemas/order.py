
from typing import Optional
from sqlmodel import SQLModel
from datetime import datetime

class OrderUpdate(SQLModel):
    customer_name: Optional[str] = None
    order_type: Optional[str] = None
    status: Optional[str] = None
    order_date: Optional[datetime] = None
    provider_id: Optional[int] = None


class OrderCreate(SQLModel):
    customer_name: str
    order_type: str
    status: str
    provider_id: int

class OrderRead(SQLModel):
    id: int
    customer_name: str
    order_type: str
    status: str
    order_date: datetime
    provider_id: int

