# PDF Field and Label Extraction Service

## Overview

The PDF Field and Label Extraction Service is an educational project developed by Yi Lin. This project demonstrates advanced techniques for extracting fields and labels from PDF documents using OCR technology. It provides a web-based interface where users can upload PDF files and receive structured data in JSON format.

## Features

- **Field Extraction**: Identifies and extracts field names and values from PDF documents.
- **Label Extraction**: Uses OCR to detect and extract text near the fields that acts as labels.
- **JSON Output**: Provides extracted information in a structured JSON format.
- **File Export**: Allows users to download the extracted data as a JSON file.

## Technologies Used

- **Python**: Programming language used for developing the extraction service.
- **Flask**: Web framework for creating the web application.
- **PyMuPDF**: Library for handling PDF files and extracting data.
- **pdf2image**: Converts PDF pages to images for OCR processing.
- **Tesseract OCR**: Optical Character Recognition tool for text extraction from images.
- **JavaScript**: Used for handling file downloads on the web interface.

## Installation

### Prerequisites

- Python 3.7 or higher
- Poppler (for `pdf2image` library)
- Tesseract OCR (for `pytesseract` library)