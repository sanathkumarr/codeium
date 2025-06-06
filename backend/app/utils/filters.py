import re

def extract_email(text: str):
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else ""

def extract_phone(text: str):
    match = re.search(r"\+?\d[\d -]{8,}\d", text)
    return match.group(0) if match else ""

def filter_tech_skills(skills_block: str):
    tech_keywords = {"python", "java", "sql", "html", "css", "javascript", "react", "node", "aws", "docker", "kubernetes", "tensorflow", "pytorch"}
    found = []
    for word in re.split(r"[,\n]", skills_block.lower()):
        word = word.strip()
        if word in tech_keywords:
            found.append(word)
    return list(set(found))

def filter_education(edu_block: str):
    degrees = []
    lines = edu_block.split("\n")
    for line in lines:
        if any(key in line.lower() for key in ["b.tech", "bachelor", "intermediate", "ssc", "10th", "12th", "high school"]):
            degrees.append(line.strip())
    return degrees

def extract_links(text: str):
    urls = re.findall(r'(https?://[^\s]+)', text)
    github = [url for url in urls if "github.com" in url]
    linkedin = [url for url in urls if "linkedin.com" in url]
    portfolio = [url for url in urls if "portfolio" in url or "personal" in url]
    return {
        "all": urls,
        "github": github,
        "linkedin": linkedin,
        "portfolio": portfolio
    }
