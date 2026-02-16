# 🚀 Resume-VRAG: AI Resume + Job Matching System

An intelligent **Vector RAG (VRAG)** powered Resume + Job Matching system that analyzes resumes against job descriptions using embeddings, semantic retrieval, and LLM reasoning.

---

## 📑 Table of Contents

- [Motivation](#-motivation)
- [Features](#-features)
- [Architecture](#-architecture)
- [Demo](#-demo)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Acknowledgements](#-acknowledgements)

---

## 💡 Motivation

Job seekers often struggle to understand:

- Whether they are a good fit for a role
- What skills they are missing
- How to tailor their resume for ATS systems

This project solves that problem using:

- Semantic embeddings
- Vector similarity search (Chroma)
- LLM reasoning (Groq LLaMA models)
- Structured skill extraction
- Match scoring logic

---

## ✨ Features

### 📄 Multi-Format Resume Ingestion
- PDF
- DOCX
- Image (OCR powered)

### 📑 Job Description Matching
- Upload `.txt` job descriptions
- Semantic similarity retrieval

### 🧠 Vector RAG Pipeline
- HuggingFace embeddings
- Chroma vector database
- Retrieval-Augmented Generation

### 📊 Match Score Engine
- Keyword overlap scoring
- Skill gap detection
- Suitability score (0–100)

### 🚀 Advanced Add-ons
- Multi-job comparison ranking
- Skill gap learning roadmap
- ATS keyword compatibility checker
- Resume rewriting tailored to job description

---

## 🏗 Architecture


Resume Upload
↓
Text Extraction (PDF/DOCX/OCR)
↓
Chunking + Embeddings (HuggingFace)
↓
Chroma Vector Store
↓
Job Description Embedding
↓
Similarity Retrieval
↓
Groq LLM Analysis
↓
Match Score + Suggestions


---

## 🛠 Prerequisites

- Python 3.10+
- Tesseract OCR (for image resumes)
- Git
- Groq API Key

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/resume-vrag.git
cd resume-vrag
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Install Tesseract OCR (Windows Only)

Download from:
https://github.com/UB-Mannheim/tesseract/wiki

Ensure path is configured properly.

🚀 Usage

Run the Streamlit app:

streamlit run app.py

Then:

Upload resume (PDF/DOCX/Image)

Upload job description (.txt)

View match score and AI analysis

⚙️ Configuration

Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here


🧠 Example Analysis Output
Match Score: 82%

Matching Skills:
- Python
- SQL
- Machine Learning

Missing Skills:
- Docker
- Kubernetes

Recommendation:
Strong candidate. Apply after adding containerization experience.
