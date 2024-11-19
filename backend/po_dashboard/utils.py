import pdfplumber
from .models import PurchaseOrder

def process_po_file(file):
    # Extract text from the uploaded PDF file
    with pdfplumber.open(file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    # Extract relevant fields (adjust parsing logic as needed)
    po_number = extract_field(text, "P.O. #")
    order_date = extract_field(text, "Order Date")
    delivery_date = extract_field(text, "Delivery Date")
    total_amount = extract_field(text, "TOTAL")

    # Save the extracted data to the database
    PurchaseOrder.objects.create(
        po_number=po_number,
        order_date=order_date,
        delivery_date=delivery_date,
        total_amount=total_amount,
        status='OPEN',  # Default status
    )

def extract_field(text, label):
    # Simple extraction logic for labeled fields
    start = text.find(label) + len(label)
    end = text.find("\n", start)
    return text[start:end].strip()
