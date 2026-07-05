# CareerCraft AI 🚀

### Smart Career Agent for Indian CSE Students

> From Kanpur to Google — a 5-agent ADK system that finds
> internships, scores resumes and preps Indian CSE students
> for AI Engineering roles

---

## 🎯 Problem Statement

As a 3rd year CSE-AI student from Kanpur actively
applying for AI internships, I struggled with:
- Finding relevant AI internships on Internshala
- Getting resume ATS optimized for top companies
- Preparing for technical interviews
- Building a proper learning roadmap
- Optimizing LinkedIn profile for recruiters

So I built the solution myself!

---

## 🤖 5 Career Agents

| Agent | What It Does |
|-------|-------------|
| Resume ATS Scorer | Scores resume out of 100 with detailed feedback |
| Internship Finder | Finds top AI/ML internships |
| Interview Simulator | Asks real technical interview questions |
| Career Roadmap Builder | 8-month AI Engineer learning roadmap |
| LinkedIn Optimizer | Complete profile optimization guide |

---

## 🏗️ Architecture

User Input
    ↓
Orchestrator Agent (Google ADK 2.0)
    ↓
5 Specialized Career Tools
    ↓
Personalized Career Action Plan

---

## 🛠️ Tech Stack

- Google Agent Development Kit (ADK) 2.0
- Google Agents CLI 0.5.0
- Groq API with meta-llama/llama-4-scout-17b
- Python 3.13
- LiteLLM
- uv package manager

---

## 🚀 How To Run

### Prerequisites
- Python 3.11+
- uv package manager
- Groq API key — free at console.groq.com

### Setup

Clone the repo
git clone https://github.com/DivyanshiBajpai2007/ai-career-navigator.git
cd ai-career-navigator

Install dependencies
agents-cli install

Set API keys on Windows
set GROQ_API_KEY=your_groq_key_here
set GOOGLE_GENAI_USE_VERTEXAI=0

Run the agent
uv run adk web app

Open browser at http://127.0.0.1:8000

---

## 💬 Example Conversations

Resume Scoring:
You: Score my resume: Python developer,
     3 AI projects, GitHub profile,
     interning at Venura Tech
Agent: Resume ATS Score: 90/100
       Excellent! Your resume is ATS ready!

Finding Internships:
You: Find me AI internships
Agent: Top AI/ML Internships:
       1. Generative AI Intern at Google India
          Stipend: 25000/month, Remote
       2. ML Engineer Intern at Microsoft India
          Stipend: 20000/month, Hybrid

Interview Practice:
You: Ask me an interview question on AI
Agent: Q: What is the difference between
          AI, ML and Deep Learning?
       Tips: Start with clear definition...

Career Roadmap:
You: Give me career roadmap to become AI Engineer
Agent: Phase 1 Foundation Month 1-2:
       Master Python via Kaggle
       Learn Git and GitHub basics...

---

## ✅ Course Concepts Demonstrated

1. Multi-agent system using Google ADK 2.0
2. Agent Skills with progressive disclosure
3. LiteLLM model integration
4. Tool calling with 5 specialized functions
5. Vibe Coding workflow throughout development
6. Security features with API key management

---

## 👩‍💻 About The Builder

Divyanshi Bajpai
3rd Year CSE-AI Student
Maharana Pratap Engineering College, Kanpur
Interning at Venura Tech as AI Engineer Intern
Goal: Azure AI Engineer at Microsoft or Google

Skills: Python, Java, Streamlit, Groq API,
Git/GitHub, Prompt Engineering, REST API,
Generative AI, LLM Evaluation

Certifications:
- AWS GenAI Business Strategy
- Google Cloud GenAI and LLMs
- Microsoft AI Skills Fest 2026
- AWS Summit 2026

GitHub: github.com/DivyanshiBajpai2007

---

## 🏆 Kaggle Capstone

Built for: Google and Kaggle 5-Day AI Agents
Intensive Vibe Coding Course 2026
Track: Concierge Agents
Submission Deadline: July 6, 2026

---

Give this repo a star if it helped you! ⭐