from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_vectorstore(text, embeddings):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    docs = splitter.create_documents([text])

    vectordb = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    return vectordb