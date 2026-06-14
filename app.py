import streamlit as st
import json
from parser import get_resume_data, load_skills

skills_db = load_skills("C:\\Users\\muham\\Downloads\\skills.csv")

st.title("AI Resume Parser")
st.write("Upload a resume PDF and extract key information instantly.")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

if uploaded_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    result = get_resume_data("temp_resume.pdf")

    st.subheader("Extracted Information")
    st.write("**Name:**", result["name"])
    st.write("**Email:**", result["email"])
    st.write("**Phone:**", result["phone"])

    st.subheader("Skills Found")
    st.write(result["skills"])