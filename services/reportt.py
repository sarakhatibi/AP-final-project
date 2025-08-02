from sqlmodel import select, func
from datetime import datetime
from model.sales_order import OrderItem 

def get_top_products(start: datetime, end: datetime, session):
    stmt = (
        select(
            OrderItem.product_name,
            func.sum(OrderItem.quantity).label("total_sold")
        )
        .where(OrderItem.order_date.between(start, end))
        .group_by(OrderItem.product_name)
        .order_by(func.sum(OrderItem.quantity).desc())
    )
    return session.exec(stmt).all()