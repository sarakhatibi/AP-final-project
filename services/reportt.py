from sqlmodel import select, func
from model.sales_order import OrderItem
from model.product import Product 
def get_top_products(session):
    stmt = (
        select(
            Product.name, 
            func.sum(OrderItem.quantity).label("total_sold")
        )
        .join(Product, Product.id == OrderItem.product_id)
        .group_by(Product.name)
        .order_by(func.sum(OrderItem.quantity).desc())
    )
    results = session.exec(stmt).all()
    
    return [{"product_name": name, "total_sold": total} for name, total in results]