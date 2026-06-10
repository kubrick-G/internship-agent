import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

profile = {
    "name": "Gokula Krishnan J",
    "skills": ["C++", "Python", "Adobe Premiere Pro", "Linux", "DSA"],
    "projects": [
        {
            "name": "Accent Changer",
            "description": "Real-time accent changer using faster-whisper, Edge TTS, VB-Audio",
            "tech": ["Python", "faster-whisper", "TTS"]
        },
        {
            "name": "TANGEDCO Meter Reader",
            "description": "Civic tech concept for automating electricity meter reading using computer vision",
            "tech": ["Python", "Computer Vision"]
        }
    ],
    "education": "B.E. Computer Science, RMK Engineering College, Chennai (2025-2029)",
    "experience": ["Video editing with Adobe Premiere Pro", "DSA practice in C++ on LeetCode"],
    "interests": ["AI", "Agentic Systems", "Linux", "Open Source"]
}

st.title("🎯 Internship Agent")
st.write("Paste a job description below and I'll score your fit and draft an application message.")

job_desc = st.text_area("Job Description", height=200)

if st.button("Analyze & Draft"):
    if job_desc:
        with st.spinner("Analyzing..."):
            prompt = f"""
You are an internship application assistant.

Candidate Profile:
{profile}

Job Description:
{job_desc}

1. Score the fit out of 10 with reasoning
2. Draft a personalized application message highlighting matching skills and projects
"""
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown(response.choices[0].message.content)
    else:
        st.warning("Please paste a job description first.")