# ResearchPilot AI

An AI-powered research agent built with Streamlit, CrewAI, DuckDuckGo, and Groq.

## Features

- Single CrewAI research agent
- Free DuckDuckGo web search
- Groq LLM
- Structured Markdown research reports
- Downloadable research report
- Enterprise-style Streamlit interface
- Ready for GitHub and Streamlit Community Cloud

## Recommended Python

Python 3.12

## Local setup

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.streamlit/secrets.toml.example` to:

```text
.streamlit/secrets.toml
```

Then add your Groq API key.

Run:

```powershell
streamlit run app.py
```

## Deployment

Push the project to GitHub. On Streamlit Community Cloud, select `app.py` as the main file and add:

```toml
GROQ_API_KEY = "your-key"
GROQ_MODEL = "openai/gpt-oss-120b"
```

The app limits report generation to reduce Groq token-per-minute errors. If
`openai/gpt-oss-120b` is temporarily rate-limited, it waits for the reported
window and retries the same model up to two times.

Do not commit `.streamlit/secrets.toml`.
