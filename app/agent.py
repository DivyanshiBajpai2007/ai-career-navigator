import os
import random
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models.lite_llm import LiteLlm

def score_resume(resume_text: str) -> str:
    """Scores a resume for ATS compatibility.
    Args:
        resume_text: The resume content to analyze
    Returns:
        A detailed score and improvement suggestions
    """
    score = 75
    feedback = []
    if "python" in resume_text.lower():
        score += 5
        feedback.append("Good: Python mentioned")
    else:
        feedback.append("Missing: Add Python skills")
    if "project" in resume_text.lower():
        score += 5
        feedback.append("Good: Projects mentioned")
    else:
        feedback.append("Missing: Add projects section")
    if "github" in resume_text.lower():
        score += 5
        feedback.append("Good: GitHub mentioned")
    else:
        feedback.append("Missing: Add GitHub profile")
    if "internship" in resume_text.lower():
        score += 5
        feedback.append("Good: Internship experience mentioned")
    else:
        feedback.append("Missing: Add internship experience")
    if "ai" in resume_text.lower() or "machine learning" in resume_text.lower():
        score += 5
        feedback.append("Good: AI/ML skills mentioned")
    else:
        feedback.append("Missing: Add AI/ML skills")
    result = f"Resume ATS Score: {score}/100\n\n"
    result += "Detailed Feedback:\n"
    for f in feedback:
        result += f"- {f}\n"
    if score >= 90:
        result += "\nExcellent! Your resume is ATS ready!"
    elif score >= 75:
        result += "\nGood! A few improvements needed."
    else:
        result += "\nNeeds work. Follow the suggestions above."
    return result

def get_internships() -> str:
    """Gets list of AI/ML internships.
    Returns:
        List of top internships for CSE students
    """
    result = "Top AI/ML Internships for CSE Students:\n\n"
    result += "1. Generative AI Intern at Google India\n"
    result += "   Stipend: 25000/month, Remote\n"
    result += "   Skills: Python, LLMs, GenAI\n"
    result += "   Apply: careers.google.com\n\n"
    result += "2. ML Engineer Intern at Microsoft India\n"
    result += "   Stipend: 20000/month, Hybrid\n"
    result += "   Skills: Python, ML, Azure\n"
    result += "   Apply: careers.microsoft.com\n\n"
    result += "3. AI Research Intern at TechCorp India\n"
    result += "   Stipend: 15000/month, Remote\n"
    result += "   Skills: Python, Deep Learning\n"
    result += "   Apply: internshala.com\n\n"
    result += "4. Data Science Intern at Analytics Pro\n"
    result += "   Stipend: 12000/month, Remote\n"
    result += "   Skills: Python, Pandas, ML\n"
    result += "   Apply: internshala.com\n\n"
    result += "5. Python Developer Intern at StartupXYZ\n"
    result += "   Stipend: 10000/month, Delhi Hybrid\n"
    result += "   Skills: Python, FastAPI, SQL\n"
    result += "   Apply: internshala.com\n\n"
    result += "Tip: Apply to at least 5 internships daily!"
    return result

def get_interview_question() -> str:
    """Gets a random technical interview question.
    Returns:
        An interview question with answering tips
    """
    questions = [
        "What is the difference between AI, ML and Deep Learning?",
        "Explain how a Large Language Model works.",
        "What is RAG and why is it important?",
        "What is the difference between a list and tuple in Python?",
        "Explain what an API is with a real world example.",
        "What is the bias-variance tradeoff in Machine Learning?",
        "How does a neural network learn from data?",
        "What is prompt engineering and why does it matter?",
        "Explain the difference between supervised and unsupervised learning.",
        "What is transfer learning and when would you use it?",
        "What is Docker and why is it important for AI deployment?",
        "Explain what a vector database is and its use in AI.",
    ]
    question = random.choice(questions)
    result = "Technical Interview Question:\n\n"
    result += f"Q: {question}\n\n"
    result += "How to Answer:\n"
    result += "- Start with a clear simple definition (30 seconds)\n"
    result += "- Give a real example from your projects (60 seconds)\n"
    result += "- Explain why it matters in industry (30 seconds)\n"
    result += "- Keep total answer under 2 minutes\n\n"
    result += "Practice tip: Record yourself answering!"
    return result

def get_career_roadmap() -> str:
    """Gets complete AI Engineering career roadmap.
    Returns:
        Step by step roadmap for becoming AI Engineer
    """
    result = "Complete AI Engineering Roadmap:\n\n"
    result += "PHASE 1 Foundation Month 1-2:\n"
    result += "- Master Python via Kaggle Python Course\n"
    result += "- Learn Git and GitHub basics\n"
    result += "- Build 1 small project per week\n"
    result += "- Complete Python certification\n\n"
    result += "PHASE 2 AI Basics Month 3-4:\n"
    result += "- Learn Machine Learning via Kaggle ML Course\n"
    result += "- Study LLMs and Prompt Engineering\n"
    result += "- Learn Streamlit for quick apps\n"
    result += "- Complete AI-900 Microsoft certification\n\n"
    result += "PHASE 3 Advanced Month 5-6:\n"
    result += "- Learn LangChain and RAG systems\n"
    result += "- Study Azure AI or Google Cloud\n"
    result += "- Learn FastAPI for building APIs\n"
    result += "- Complete AZ-900 certification\n\n"
    result += "PHASE 4 Production Month 7-8:\n"
    result += "- Learn Docker and deployment\n"
    result += "- Build and deploy 3 real projects\n"
    result += "- Contribute to open source\n"
    result += "- Apply for AI internships daily!\n\n"
    result += "Remember: Build in public on LinkedIn and GitHub!"
    return result

def get_linkedin_tips() -> str:
    """Gets LinkedIn profile optimization tips.
    Returns:
        Complete tips to improve LinkedIn profile
    """
    result = "LinkedIn Profile Optimization Guide:\n\n"
    result += "HEADLINE OPTIONS:\n"
    result += "Option 1: AI Engineer in Making | Python | LLMs | Google ADK | Open to Internships\n"
    result += "Option 2: CSE-AI Student | Building AI Agents | Google ADK | Seeking Internships\n"
    result += "Option 3: Aspiring AI Engineer | Python, GenAI, RAG | Interning at Venura Tech\n\n"
    result += "SUMMARY TIPS:\n"
    result += "- Start with your goal as AI Engineer at top tech company\n"
    result += "- Mention your best 2-3 projects\n"
    result += "- List your certifications\n"
    result += "- End with call to action\n\n"
    result += "PROFILE CHECKLIST:\n"
    result += "- Add Open to Work badge\n"
    result += "- Upload professional photo\n"
    result += "- Add all certifications\n"
    result += "- List all technical skills\n"
    result += "- Add location: Kanpur, Uttar Pradesh\n"
    result += "- Connect with 5 AI engineers per week\n"
    result += "- Post weekly about AI learning journey\n\n"
    result += "Consistency beats perfection on LinkedIn!"
    return result

root_agent = Agent(
    name="career_craft_ai",
    model=LiteLlm(model="groq/meta-llama/llama-4-scout-17b-16e-instruct"),
    instruction="""You are CareerCraft AI, a friendly and 
    encouraging career navigation assistant specifically 
    built for Indian CSE students who want to become 
    AI Engineers at top tech companies like Google and Microsoft.

    You have access to these tools:
    - score_resume: Score and review a resume for ATS
    - get_internships: Find AI/ML internships
    - get_interview_question: Practice interview questions
    - get_career_roadmap: Get complete learning roadmap
    - get_linkedin_tips: Optimize LinkedIn profile

    Always use tools when relevant to the user's question.
    For general questions, answer from your own knowledge.
    
    Always be encouraging, warm and practical.
    You understand Indian tech landscape and tier-2 city 
    student challenges perfectly.
    Always end responses with a motivating message!
    
    Start by warmly greeting the student and asking 
    what career challenge they need help with today.""",
    tools=[
        score_resume,
        get_internships,
        get_interview_question,
        get_career_roadmap,
        get_linkedin_tips,
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)