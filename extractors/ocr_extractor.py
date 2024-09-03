import pytesseract
from pdf2image import convert_from_path
import os
import json

# Specify the path to the Tesseract executable (update if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_labels(pdf_path):
    # Ensure Poppler is correctly specified
    poppler_path = 'C:\\Program Files\\poppler-24.07.0\\Library\\bin'

    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return json.dumps({"error": "File not found"})

    try:
        # Convert PDF to images
        images = convert_from_path(pdf_path, poppler_path=poppler_path)
        print(f"Number of pages converted to images: {len(images)}")
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        return json.dumps({"error": "Error converting PDF to images"})

    labels = []
    for i, image in enumerate(images):
        try:
            # Perform OCR on each image
            ocr_text = pytesseract.image_to_string(image, config='--psm 6')
            print(f"Page {i+1} OCR text: {ocr_text[:100]}")  # Print first 100 characters for debugging
            if ocr_text.strip():
                labels.append({'page': i+1, 'text': ocr_text.strip()})
        except Exception as e:
            print(f"Error during OCR on page {i+1}: {e}")

    # Return the extracted information as a JSON object
    return json.dumps({"pages": labels}, indent=4)

# Example usage
if __name__ == "__main__":
    pdf_path = 'example.pdf'  # Replace with your PDF file path
    json_output = extract_labels(pdf_path)
    print(json_output)
