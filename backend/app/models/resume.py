# app/models/resume.py
from odmantic import Model
from typing import List

class Resume(Model):
    name: str
    email: str
    phone: str
    skills: List[str]
    experience: int  # in years
    tags: List[str]
