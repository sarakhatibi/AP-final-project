from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    quantity: int
    price: int

class InvoiceRequest(BaseModel):
    customer_name: str
    order_number: str
    order_date: str
    items: List[Item]