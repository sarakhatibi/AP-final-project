from database.connection import get_db
from pydantic import BaseModel



class OrderCreate(BaseModel):
    order_id: int
    product_id: int
    user_id: int
    quantity: int