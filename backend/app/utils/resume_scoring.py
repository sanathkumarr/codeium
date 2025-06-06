# app/utils/resume_scoring.py
def compute_match_score(resume_skills, jd_skills):
    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)
    matched_skills = resume_set & jd_set
    score = len(matched_skills) / len(jd_set) * 100 if jd_set else 0
    return round(score, 2), list(matched_skills)
