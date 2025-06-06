# app/utils/ocr.py
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text
