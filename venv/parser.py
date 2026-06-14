import re
import spacy
from pdfminer.high_level import extract_text
import PyPDF2
import pandas as pd
import json

nlp=spacy.load("en_core_web_sm")


import pandas as pd



def extract_clean_text(pdf_path):
    text=""
    with open(pdf_path,'rb') as f:
        reader=PyPDF2.PdfReader(f)
        for each in reader.pages:
            text+=each.extract_text()
        text=re.sub(r'\s+',' ',text)
        return text.strip()
def extract_entites(text):
    doc=nlp(text)
    entites={}
    for ent in doc.ents:
        if ent.label not in entites:
            entites[ent.label_]=[]
        entites[ent.label_].append(ent.text)
    return entites
text=extract_clean_text("C:\\Users\\muham\\Downloads\\cv.pdf")
text = extract_clean_text("C:\\Users\\muham\\Downloads\\cv.pdf")

false_positives = [
    'responses', 'parser', 'system', 'updates', 'video',
    'interactive', 'matrix', 'reports', 'datasets', 'real-time',
    'analysis', 'research', 'engineering', 'testing', 'sales'
]

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
    doc=nlp(text)
    for ent in doc.ents:
        if ent.label_=="PERSON":
            return ent.text
        return None
def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group() if match else None

def extract_phone(text):
    match = re.search(r'(\+92|0)\d{10}', text)
    return match.group() if match else None





# Load skills
skills_db = load_skills("C:\\Users\\muham\\Downloads\\skills.csv")

# Extract
print("Skills:", extract_skills(text, skills_db))

def get_resume_data(pdf_path):
    text = extract_clean_text(pdf_path)
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text, skills_db)
    }
result = get_resume_data("C:\\Users\\muham\\Downloads\\cv.pdf")
print(json.dumps(result, indent=2))
#print(text)
entities=extract_entites(text)
#for label,values in entities.items():
    #print(label,"-->",values)

