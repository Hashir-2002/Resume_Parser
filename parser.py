import re
import spacy
import PyPDF2
import pandas as pd

nlp = spacy.load("en_core_web_sm")

false_positives = [
    'responses', 'parser', 'system', 'updates', 'video',
    'interactive', 'matrix', 'reports', 'datasets', 'real-time',
    'analysis', 'research', 'engineering', 'testing', 'sales'
]

def extract_clean_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def load_skills(csv_path):
    df = pd.read_csv(csv_path, header=0)
    skills = [col.strip().lower() for col in df.columns.tolist()]
    return skills

def extract_skills(text, skills_db):
    text_lower = text.lower()
    found = [skill for skill in skills_db
             if re.search(r'\b' + re.escape(skill) + r'\b', text_lower)
             and skill not in false_positives]
    return found

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group() if match else None

def extract_phone(text):
    match = re.search(r'(\+92|0)\d{10}', text)
    return match.group() if match else None

def get_resume_data(pdf_path):
    text = extract_clean_text(pdf_path)
    skills_db = load_skills("skills.csv")
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text, skills_db)
    }