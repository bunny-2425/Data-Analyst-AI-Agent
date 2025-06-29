import os
import pandas as pd
from docx import Document
import fitz  # PyMuPDF
from PIL import Image
import pytesseract

def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        return pd.read_csv(file_path)
    elif ext in [".xlsx", ".xls"]:
        return pd.read_excel(file_path)
    elif ext == ".txt":
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif ext == ".docx":
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    elif ext == ".pdf":
        text = ""
        pdf = fitz.open(file_path)
        for page in pdf:
            text += page.get_text()
        return text
    elif ext in [".png", ".jpg", ".jpeg"]:
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)
    else:
        return "Unsupported file type"