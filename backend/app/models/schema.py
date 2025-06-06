from sqlmodel import SQLModel, Field
from typing import Optional

class Resume(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    skills: Optional[str]
    experience: Optional[str]
    education: Optional[str]
    certifications: Optional[str]
    projects: Optional[str]
    internships: Optional[str]
    strengths: Optional[str]
    weaknesses: Optional[str]
    github: Optional[str]
    linkedin: Optional[str]
    portfolio: Optional[str]
    about: Optional[str]

