# backend/app/utils/patterns.py
EMAIL_PATTERN = r"[\w\.-]+@[\w\.-]+"
PHONE_PATTERN = r"(?:\+91[-\s]?)?[6-9]\d{9}"
URL_PATTERN = r"https?://[\w\.-]+"
TECH_KEYWORDS = [
    "Python", "Java", "C++", "React", "Node.js", "Machine Learning", "Deep Learning",
    "NLP", "Flask", "Django", "MongoDB", "SQL", "TensorFlow", "PyTorch", "FastAPI"
]
COMPANY_KEYWORDS = ["Technologies", "Pvt", "Private", "Inc", "Solutions", "LLC", "Ltd"]
DEGREE_KEYWORDS = ["B.Tech", "Bachelor", "Intermediate", "12th", "10th", "SSC"]
