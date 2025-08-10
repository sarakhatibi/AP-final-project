from sqlmodel import select, func
from model.sales_order import OrderItem
from model.product import Product 
def get_top_products(session):
    stmt = (
        select(
            Product.name,
            Product.sku,
            func.sum(OrderItem.quantity).label("sales_count")
        )
        .join(Product, Product.id == OrderItem.product_id)
        .group_by(Product.id)
        .order_by(func.sum(OrderItem.quantity).desc())
    )
    results = session.exec(stmt).all()

    return [
        {"name": name, "sku": sku, "sales_count": count}
        for name, sku, count in results
    ]