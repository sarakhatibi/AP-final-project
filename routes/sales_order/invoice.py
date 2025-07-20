from fastapi import APIRouter, Response
from schemas.invoice import InvoiceRequest
import pdfkit
from utils.invoice_html import render_invoice_html

router = APIRouter()

@router.post("/invoice/download")
def download_invoice(data: InvoiceRequest):
    html = render_invoice_html(data)
    pdf = pdfkit.from_string(html, False)
    
    return Response(content=pdf, media_type="application/pdf", headers={
        "Content-Disposition": "attachment; filename=invoice.pdf"
    })