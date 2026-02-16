import re

def calculate_match_score(resume_text, job_text):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_text.lower().split())

    overlap = resume_words.intersection(job_words)
    score = (len(overlap) / len(job_words)) * 100

    return round(score, 2)