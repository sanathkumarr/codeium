# backend/app/api/routes.py
from fastapi import APIRouter, UploadFile, File
from app.services.extractor import process_resume
from app.storage import load_all

router = APIRouter()

@router.post("/extract")
async def extract_resume(file: UploadFile = File(...)):
    resume_data = await process_resume(file)
    return {"message": "Resume processed successfully", "data": resume_data}

@router.get("/resumes")
def get_all_resumes():
    return {"resumes": load_all()}