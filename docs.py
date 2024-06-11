import os
import PyPDF2
from langchain.docstore.document import Document

def load_documents(folder_paths):
    documents = []
    for folder_path in folder_paths:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith(".txt"):
                    with open(file_path, "r", encoding="utf-8") as f:
                        text = f.read()
                    documents.append(Document(page_content=text, metadata={"source": file_path}))
                elif file.endswith(".pdf"):
                    with open(file_path, "rb") as f:
                        pdf_reader = PyPDF2.PdfReader(f)
                        text = ""
                        for page in range(len(pdf_reader.pages)):
                            text += pdf_reader.pages[page].extract_text()
                    documents.append(Document(page_content=text, metadata={"source": file_path}))
    return documents