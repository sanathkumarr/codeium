
# backend/app/storage.py
import os
import json

STORE_PATH = "data/resumes.json"

def save_resume(data):
    os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)
    resumes = load_all()
    resumes.append(data)
    with open(STORE_PATH, "w") as f:
        json.dump(resumes, f, indent=2)

def load_all():
    if not os.path.exists(STORE_PATH):
        return []
    with open(STORE_PATH) as f:
        return json.load(f)