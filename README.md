# AI Resume Parser 🤖

An NLP-powered resume parser that extracts key information from PDF resumes automatically — built with spaCy, PyPDF2, and Streamlit.

🔗 **Live Demo:** [resumeparser-gjafxggpdukeqnhrdvo3wx.streamlit.app](https://resumeparser-gjafxggpdukeqnhrdvo3wx.streamlit.app/)

---

## What it does

Upload any PDF resume and it instantly extracts:

- **Name** — detected using spaCy's Named Entity Recognition (NER)
- **Email** — extracted using regex pattern matching
- **Phone Number** — extracted using regex pattern matching
- **Skills** — matched against a curated dataset of 500+ technical and professional skills

---

## Tech Stack

- **spaCy** — NLP and Named Entity Recognition
- **PyPDF2** — PDF text extraction
- **Streamlit** — Web UI
- **Pandas** — Skills dataset processing
- **Regex** — Email and phone extraction

---

## How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/hashir-2002/ai-resume-parser.git
cd ai-resume-parser
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## Project Structure

```
ai-resume-parser/
├── app.py          # Streamlit UI
├── parser.py       # Core NLP extraction logic
├── skills.csv      # Skills database (500+ skills)
├── requirements.txt
└── README.md
```

---

## Author

**Muhammad Hashir** — BS Computer Science, Superior University Lahore

[GitHub](https://github.com/hashir-2002)
