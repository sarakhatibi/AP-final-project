def render_invoice_html(data):
    items_html = "".join([
        f"<tr><td>{item.name}</td><td>{item.quantity}</td><td>{item.price:,} تومان</td></tr>"
        for item in data.items
    ])
    total = sum(item.price * item.quantity for item in data.items)

    return f"""
    <html>
    <head><meta charset="utf-8">
    <style>
      table, td, th {{ border: 1px solid black; border-collapse: collapse; padding: 8px; }}
    </style></head>
    <body>
      <h2>رسید فروش</h2>
      <p>مشتری: {data.customer_name}</p>
      <p>شماره سفارش: {data.order_number}</p>
      <p>تاریخ: {data.order_date}</p>
      <table>
        <tr><th>کالا</th><th>تعداد</th><th>قیمت</th></tr>
        {items_html}
      </table>
      <p><strong>جمع کل: {total:,} تومان</strong></p>
    </body>
    </html>
    """