# backend/app/services/extractor.py
import fitz  # PyMuPDF
from app.utils.resume_parser import extract_fields
from app.storage import save_resume

async def process_resume(file):
    contents = await file.read()
    with fitz.open(stream=contents, filetype="pdf") as doc:
        text = "\n".join(page.get_text() for page in doc)
    data = extract_fields(text)
    save_resume(data)
    return data

