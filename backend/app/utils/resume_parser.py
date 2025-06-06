# backend/app/utils/resume_parser.py
import re
from app.utils.patterns import EMAIL_PATTERN, PHONE_PATTERN, URL_PATTERN, TECH_KEYWORDS, COMPANY_KEYWORDS, DEGREE_KEYWORDS

def extract_section(text: str, keywords: str) -> str | None:
    """
    Extracts a section from the resume text based on given keywords.
    Returns the content of that section or None if not found.
    """
    pattern = rf"{keywords}\s*[:\-]?\s*(.*?)(?=\n[A-Z][a-zA-Z ]{2,}:|\Z|\n\n)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    
    if match and match.group(1):
        return match.group(1).strip()
    
    return None
def extract_fields(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "github": extract_url(text, "github"),
        "linkedin": extract_url(text, "linkedin"),
        "portfolio": extract_url(text, "portfolio"),
        "about": extract_section(text, "about me|about"),
        "skills": extract_skills(text),
        "experience": extract_experience(text),
        "internships": extract_internships(text),
        "education": extract_education(text),
        "certifications": extract_section(text, "certifications?|achievements"),
        "projects": extract_section(text, "projects?|personal projects"),
        "strengths": extract_section(text, "strengths"),
        "weaknesses": extract_section(text, "weaknesses")
    }

def extract_name(text):
    lines = text.splitlines()
    for line in lines[:5]:
        if re.search(EMAIL_PATTERN, line):
            continue
        return line.strip()
    return None

def extract_email(text):
    match = re.search(EMAIL_PATTERN, text)
    return match.group() if match else None

def extract_phone(text):
    match = re.search(PHONE_PATTERN, text)
    return match.group() if match else None

def extract_url(text, keyword):
    urls = re.findall(URL_PATTERN, text)
    for url in urls:
        if keyword in url.lower():
            return url
    return None

def extract_skills(text):
    found = [kw for kw in TECH_KEYWORDS if kw.lower() in text.lower()]
    return list(set(found)) if found else None

def extract_experience(text):
    matches = re.findall(r"(?i)([^\n]*?(?:Pvt\.? Ltd\.?|Technologies|Inc|Solutions|Company|Corporation).*?\n.*?)", text)
    return matches if matches else None

def extract_internships(text):
    matches = re.findall(r"(?i)(intern|internship).*?\n(.*?)(?=\n[A-Z])", text, re.DOTALL)
    return [f"{m[0]} - {m[1].strip()}" for m in matches] if matches else None

def extract_education(text):
    edu = []
    for degree in DEGREE_KEYWORDS:
        pattern = rf"(?i)({degree}.*?)(\n\n|\n[A-Z][a-z])"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            edu.append(match.group(1).strip())
    return edu if edu else None

