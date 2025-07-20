from sqlmodel import Session, select
from model.order import Order, OrderStatus

def calculate_provider_score(provider_id: int, session: Session) -> float:
    orders = session.exec(
        select(Order)
        .where(Order.provider_id == provider_id)
        .where(Order.status == OrderStatus.recived) 
    ).all()

    if not orders:
        return 0.0

    on_time_count = 0
    for order in orders:
        if order.delivery_date and order.expected_date:
            if order.delivery_date <= order.expected_date:
                on_time_count += 1

    score = (on_time_count / len(orders)) * 100
    return round(score, 2)