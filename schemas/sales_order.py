from database.connection import get_db
from pydantic import BaseModel, validator

from typing import Optional
from model.order import OrderStatus

class StatusUpdate(BaseModel):
    new_status: OrderStatus

    @validator("new_status", pre=True)
    def normalize_status(cls, v: str) -> str:
        v = v.strip().capitalize()
        valid_values = [e.value for e in OrderStatus]
        if v not in valid_values:
            raise ValueError(f"مقدار '{v}' معتبر نیست. فقط مقادیر مجاز: {valid_values}")
        return v

class  OrdersalesCreate(BaseModel):

    product_id: int
    user_id: int
    quantity: int