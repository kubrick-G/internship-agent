import os
import streamlit as st
import google.generativeai as genai

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
st.write("AI-powered internship fit scorer and application drafter")

api_key = st.text_input("Enter your Gemini API Key", type="password", placeholder="Get free key at aistudio.google.com")

job_desc = st.text_area("Job Description", height=200)

if st.button("Analyze & Draft"):
    if not api_key:
        st.warning("Please enter your Gemini API key first.")
    elif not job_desc:
        st.warning("Please paste a job description.")
    else:
        with st.spinner("Analyzing..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-2.0-flash")
                prompt = f"""
You are an internship application assistant.

Candidate Profile:
{profile}

Job Description:
{job_desc}

1. Score the fit out of 10 with reasoning
2. Draft a personalized application message highlighting matching skills and projects
"""
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")