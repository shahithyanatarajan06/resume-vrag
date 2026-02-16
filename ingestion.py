import pytesseract
from PIL import Image
from langchain_community.document_loaders import PyPDFLoader
from docx import Document
import tempfile

# 🔥 Correct path for YOUR install
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\91890\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def load_pdf(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name

    loader = PyPDFLoader(tmp_path)
    pages = loader.load()

    return " ".join([page.page_content for page in pages])


def load_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


def load_image(file):
    image = Image.open(file)
    return pytesseract.image_to_string(image)


def load_txt(file):
    return file.read().decode("utf-8")