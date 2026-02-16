import streamlit as st
from dotenv import load_dotenv
from ingestion import load_pdf, load_docx, load_image, load_txt
from embeddings import get_embeddings
from vectorstore import create_vectorstore
from retriever import retrieve
from matcher import analyze_match
from utils import calculate_match_score

load_dotenv()

st.title("🚀 Resume + Job Matching Bot (VRAG)")

# Upload Resume
resume_file = st.file_uploader(
    "Upload Resume (PDF/DOCX/Image)",
    type=["pdf", "docx", "png", "jpg", "jpeg"]
)

# Upload Job Description
job_file = st.file_uploader(
    "Upload Job Description (TXT)",
    type=["txt"]
)

if resume_file and job_file:

    # Load resume
    if resume_file.type == "application/pdf":
        resume_text = load_pdf(resume_file)
    elif "word" in resume_file.type:
        resume_text = load_docx(resume_file)
    else:
        resume_text = load_image(resume_file)

    job_text = load_txt(job_file)

    embeddings = get_embeddings()
    vectordb = create_vectorstore(resume_text, embeddings)

    resume_chunks = retrieve(vectordb, job_text)

    result = analyze_match(resume_chunks, job_text)

    score = calculate_match_score(resume_text, job_text)

    st.subheader("📊 Match Score")
    st.write(score, "%")

    st.subheader("🧠 AI Analysis")
    st.write(result)