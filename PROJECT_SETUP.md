# ResearchPilot AI - Beginner Setup

## 1. Install Python 3.12

Check:

py -3.12 --version

## 2. Create environment

py -3.12 -m venv .venv

## 3. Activate

.\.venv\Scripts\Activate.ps1

## 4. Install packages

pip install -r requirements.txt

## 5. Create secrets

Copy:

.streamlit/secrets.toml.example

to:

.streamlit/secrets.toml

Then put your real Groq API key inside.

## 6. Run

streamlit run app.py

Open:

http://localhost:8501

## 7. Test

Try:

Artificial intelligence in education

Then:

The impact of artificial intelligence on cybersecurity in 2026

## 8. GitHub

git init
git add .
git status
git commit -m "Initial ResearchPilot AI"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main

Before pushing, verify that `.streamlit/secrets.toml` is NOT listed by git status.

## 9. Streamlit Cloud

Create a new app from your GitHub repository.
Main file: app.py
Python: 3.12

Add these secrets in Streamlit Cloud:

GROQ_API_KEY = "your-key"
GROQ_MODEL = "openai/gpt-oss-120b"

The app caps generated output and retries the configured model after a
rate-limit window.
