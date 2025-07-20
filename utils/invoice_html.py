def render_invoice_html(data):
    items_html = "".join([
        f"<tr><td>{item.name}</td><td>{item.quantity}</td><td>{item.price:,}tomans</td></tr>"
        for item in data.items
    ])
    total = sum(item.price * item.quantity for item in data.items)

    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <style>
        body { direction: rtl; font-family: sans-serif; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid black; padding: 8px; text-align: center; }
      </style>
    </head>
    <body>
      <h2>sale receipt</h2>
      <p>customer name:{data.customer_name}</p>
      <p>order number: {data.order_number}</p>
      <p>date: {data.order_date}</p>
      <table>
        <tr><th>کالا</th><th>quantity</th><th>price/th></tr>
        {items_html}
      </table>
      <p><strong>total price: {total:,} tomans/strong></p>
    </body>
    </html>
    """
    return html