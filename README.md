# 🚀 Resume VRAG – Intelligent Resume + Job Matching Bot

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-green)

An AI-powered Resume + Job Matching system built using **Vector Retrieval-Augmented Generation (VRAG)** that intelligently analyzes resumes against job descriptions, calculates match scores, identifies skill gaps, and provides improvement suggestions.

---

## 📑 Table of Contents

- [Motivation](#-motivation)
- [Key Features](#-key-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#️-configuration)
- [Architecture](#-architecture)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Acknowledgements](#-acknowledgements)

---

## ✨ Motivation

Recruiters and applicants often struggle to evaluate resume-job compatibility objectively.  
Traditional keyword matching fails to capture semantic meaning and context.

This project solves that using:

- Semantic vector embeddings
- Intelligent retrieval
- LLM-based reasoning
- Structured skill gap analysis

Result: **Accurate, explainable, AI-driven job suitability analysis.**

---

## 🔥 Key Features

- 📄 Resume ingestion (PDF, DOCX, Image with OCR)
- 📑 Job Description ingestion (TXT)
- 🧠 HuggingFace embeddings for semantic understanding
- 🗂 Chroma Vector Database for retrieval
- ⚡ Groq LLM for intelligent reasoning
- 📊 Match score calculation
- 🔎 Skill gap analysis
- 🧾 Resume rewriting tailored to job description
- 🏆 Multi-job ranking comparison
- 📋 ATS keyword compatibility checker


---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Embeddings | HuggingFace (all-MiniLM-L6-v2) |
| Vector DB | Chroma |
| LLM | Groq (Llama 3.3 70B Versatile) |
| OCR | Tesseract |
| Framework | LangChain |

---

## 📦 Installation

### 1️⃣ Clone the repository

git clone https://github.com/yourusername/resume-vrag.git
cd resume-vrag

2️⃣ Create virtual environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Install Tesseract (for image OCR)

Download from:
https://github.com/UB-Mannheim/tesseract/wiki

If not added to PATH, configure manually in ingestion.py:

pytesseract.pytesseract.tesseract_cmd = r"C:\Path\To\Tesseract-OCR\tesseract.exe"
🚀 Usage

Run the Streamlit app:

streamlit run app.py
In the Web Interface:

Upload Resume (PDF/DOCX/Image)

Upload Job Description (TXT)

View:

Match Score

Matching Skills

Missing Skills

Suitability Score (0–100)

Improvement Suggestions

Resume Rewrite (Optional)

ATS Compatibility Analysis

⚙️ Configuration

Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here

Make sure load_dotenv() is called before initializing Groq client.

📊 Architecture
Resume Upload
     ↓
Text Extraction (PDF/DOCX/OCR)
     ↓
Chunking
     ↓
HuggingFace Embeddings
     ↓
Chroma Vector Store
     ↓
Semantic Retrieval
     ↓
Groq LLM Analysis
     ↓
Match Score + Suggestions

This is a full Vector Retrieval-Augmented Generation (VRAG) pipeline.

🛣 Roadmap

Deploy on Streamlit Cloud

Add LinkedIn profile ingestion

Add recruiter dashboard

Hybrid RAG (Vector + Knowledge Graph)

SaaS version with authentication

Resume formatting optimizer
