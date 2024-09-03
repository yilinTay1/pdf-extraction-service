import fitz  # PyMuPDF

def extract_form_fields(pdf_path):
    doc = fitz.open(pdf_path)
    fields = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        for widget in page.widgets():
            if widget.field_type == fitz.PDF_WIDGET_TYPE_TEXT:
                field_name = widget.field_name
                field_value = widget.field_value
                rect = widget.rect
                fields.append({'name': field_name, 'value': field_value, 'rect': rect, 'page': page_num})
    return fields
