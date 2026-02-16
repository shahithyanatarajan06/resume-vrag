import os
from groq import Groq
from prompts import MATCH_PROMPT


def analyze_match(resume_chunks, job_desc):

    # Create Groq client INSIDE function
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    client = Groq(api_key=api_key)

    # Combine retrieved resume chunks
    context = "\n".join([doc.page_content for doc in resume_chunks])

    final_prompt = f"""
    {MATCH_PROMPT}

    Resume:
    {context}

    Job Description:
    {job_desc}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content