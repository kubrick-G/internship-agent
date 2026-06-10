# 🎯 Internship Agent

An AI-powered tool that helps students score their fit for a job description and drafts a personalized application message in seconds.

## What it does
- Paste any job description
- AI scores your fit out of 10 with reasoning
- Drafts a personalized application message highlighting your matching skills and projects

## Tech Stack
- Python + Streamlit (web interface)
- Google Gemini API (AI reasoning)
- MongoDB Atlas (profile storage)

## How to run locally

1. Clone the repo
```bash
git clone https://github.com/kubrick-G/internship-agent.git
cd internship-agent
```

2. Install dependencies
```bash
pip install streamlit google-generativeai python-dotenv
```

3. Run the app
```bash
python -m streamlit run app.py
```

4. Enter your free Gemini API key from [aistudio.google.com](https://aistudio.google.com)

## License
MIT
