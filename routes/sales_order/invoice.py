
from fastapi import APIRouter, Response
from xhtml2pdf import pisa
from io import BytesIO
from schemas.invoice import InvoiceRequest  

router = APIRouter()

def render_invoice_html(data) -> str:
    items_html = "".join([
        f"<tr><td>{item.name}</td><td>{item.quantity}</td><td>{item.price}</td></tr>"
        for item in data.items
    ])
    total = sum(item.price * item.quantity for item in data.items)

    return f"""
    <html>
    <head>
      <meta charset="UTF-8">
      <style>
        body {{
          font-family: Arial, sans-serif;
        }}
        table {{
          border-collapse: collapse;
          width: 100%;
          margin-top: 20px;
        }}
        th, td {{
          border: 1px solid black;
          padding: 8px;
          text-align: center;
        }}
      </style>
    </head>
    <body>
      <h2>Invoice</h2>
      <p>Customer: {data.customer_name}</p>
      <p>Order : {data.order_number}</p>
      <p>Date: {data.order_date}</p>
      <table>
        <tr><th>Item</th><th>Quantity</th><th>Price</th></tr>
        {items_html}
      </table>
      <p><strong>Total: {total}</strong></p>
    </body>
    </html>
    """

@router.post("/invoice/download")
def download_invoice(data: InvoiceRequest):
    html = render_invoice_html(data)
    pdf_stream = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf_stream)

    if pisa_status.err:
        return Response(content="❌ PDF generation failed", status_code=500)

    return Response(
        content=pdf_stream.getvalue(),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=invoice.pdf"}
    )