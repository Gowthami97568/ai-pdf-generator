# 🤖 AI PDF Generator

An AI-powered PDF Generator built using Python that creates **Reports, Notes, and Resumes** dynamically using AI and converts them into well-structured PDF documents.

---

## 📌 Overview

This project uses **Google Gemini AI API** to generate intelligent content and **ReportLab** to convert that content into PDF format. It supports multiple document types and ensures clean formatting and readability.

---

## ✨ Features

- 📘 Generate detailed **Reports**
- 📝 Create structured **Notes**
- 🧾 Build professional **Resumes**
- 📄 Convert content into **PDF format**
- 🤖 Uses AI for dynamic content generation
- 🔄 Fallback system when AI limit is reached

---

## 🧠 How It Works

1. User selects document type (Report / Notes / Resume)
2. User enters a topic
3. AI generates content based on the topic
4. Content is formatted and converted into PDF
5. PDF is automatically generated and opened

---

## 🛠️ Technologies Used

### Core Technologies
- Python – Programming language
- ReportLab – PDF generation
- Google Gemini API – AI content generation

### Libraries
- `google-generativeai`
- `reportlab`

---

## 📂 Project Structure
ai-pdf-generator/
│
├── app.py # Main application file
├── generator.py # AI content generation logic
├── pdf.py # PDF creation logic
├── .gitignore
└── README.md


---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Gowthami97568/ai-pdf-generator.git
cd ai-pdf-generator
---

### 2️⃣ Install Dependencies

```bash
pip install reportlab google-generativeai

Set API Key
set GEMINI_API_KEY=your_api_key   # Windows

Run Application
python app.py
