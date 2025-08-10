from sqlmodel import Session, select
from model.order import Order, OrderStatus

def calculate_provider_score(provider_id: int, session: Session) -> float:
    orders = session.exec(
        select(Order).where(Order.provider_id == provider_id)
    ).all()

    if not orders:
        return None

    total_orders = len(orders)
    on_time_deliveries = 0
    correct_deliveries = 0

    for order in orders:
        
        if order.status == OrderStatus.received:
            correct_deliveries += 1

            # بررسی سرعت تحویل
            if order.delivery_date and order.expected_date:
                if order.delivery_date <= order.expected_date:
                    on_time_deliveries += 1

    accuracy_score = correct_deliveries / total_orders
    speed_score = on_time_deliveries / total_orders

    final_score = round((accuracy_score * 0.6 + speed_score * 0.4) * 5, 2)
    return final_score