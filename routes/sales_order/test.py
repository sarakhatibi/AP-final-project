from xhtml2pdf import pisa
from io import BytesIO

html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { direction: rtl; font-family: Tahoma, sans-serif; }
    table { border-collapse: collapse; width: 100%; margin-top: 20px; }
    th, td { border: 1px solid black; padding: 8px; text-align: center; }
  </style>
</head>
<body>
  <h2>رسید فروش</h2>
  <p>مشتری: علی افشاری</p>
  <p>شماره سفارش: ۲</p>
  <p>تاریخ: ۲۰۲۵-۰۷-۲۰</p>
  <table>
    <tr><th>کالا</th><th>تعداد</th><th>قیمت</th></tr>
    <tr><td>مانیتور اپل</td><td>۱</td><td>۸۹,۹۰۰,۰۰۰ تومان</td></tr>
  </table>
  <p><strong>جمع کل: ۸۹,۹۰۰,۰۰۰ تومان</strong></p>
</body>
</html>
"""

pdf_stream = BytesIO()
pisa_status = pisa.CreatePDF(html, dest=pdf_stream)

if pisa_status.err:
    print("PDF ساختنش شکست خورد 😭")
else:
    with open("receipt.pdf", "wb") as f:
        f.write(pdf_stream.getvalue())
    print("🎉 رسید ساخته شد → receipt.pdf")