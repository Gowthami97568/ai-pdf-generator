import os
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


# ==============================
# 📘 REPORT (AI + FALLBACK)
# ==============================
def generate_report(topic):
    prompt = f"""
Write a very detailed academic report on {topic}.

Requirements:
- Long paragraphs
- Minimum 1500 words
- Sections: Introduction, Definition, Explanation, Working, Applications, Advantages, Disadvantages, Future Scope, Conclusion
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except:
        # fallback (your existing improved content)
        return f"""
{topic.upper()} REPORT

INTRODUCTION:
{topic} is a highly important concept in modern technology that improves efficiency and innovation.

DETAILED EXPLANATION:
It involves intelligent systems, automation, and advanced data processing techniques.

APPLICATIONS:
Used in healthcare, education, business, and industry.

CONCLUSION:
{topic} plays a major role in future technological development.
"""


# ==============================
# 📝 NOTES (AI + CLEAN STRUCTURE)
# ==============================
def generate_notes(topic):
    prompt = f"""
Create well-structured, detailed notes on {topic}.

Requirements:
- Clear headings
- Bullet points
- Easy to study
- Detailed explanation
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except:
        return f"""
NOTES ON {topic.upper()}

INTRODUCTION:
{topic} is an important concept in modern systems.

KEY POINTS:
- Improves efficiency
- Reduces errors
- Used in many industries

CONCLUSION:
{topic} is essential in modern development.
"""


# ==============================
# 🧾 RESUME (REAL AI FORMAT)
# ==============================
def generate_resume(topic):
    prompt = f"""
Create a professional resume for a candidate skilled in {topic}.

Include:
- Full Name
- Contact details
- Career Objective
- Education
- Skills
- Projects
- Internship
- Strengths
- Declaration

Make it look like a real modern resume with proper formatting.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except:
        return f"""
RESUME

Name: Your Name
Skills: {topic}
Projects: {topic} based project
Summary: Interested in {topic}
"""