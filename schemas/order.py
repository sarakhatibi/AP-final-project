
from typing import Optional
from sqlmodel import SQLModel
from datetime import datetime

class OrderUpdate(SQLModel):
    customer_name: Optional[str] = None
    order_type: Optional[str] = None
    status: Optional[str] = None
    order_date: Optional[datetime] = None
    provider_id: Optional[int] = None
