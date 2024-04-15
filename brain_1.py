import re
from io import BytesIO
from typing import Tuple, List
import pickle

from langchain.docstore.document import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from pypdf import PdfReader
import faiss

def parse_pdf(file: BytesIO, filename: str) -> Tuple[List[str], str]:
    pdf = PdfReader(file)
    output = []
    for page in pdf.pages:
        text = page.extract_text()
        if text:  # Ensure there's text to process
            text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", text)
            text = re.sub(r"(?<!\n\s)\n(?!\s\n)", " ", text.strip())
            text = re.sub(r"\n\s*\n", "\n\n", text)
            output.append(text)
    return output, filename

def text_to_docs(text: List[str], filename: str) -> List[Document]:
    page_docs = [Document(page_content=page, metadata={'filename': filename, 'page': i + 1}) for i, page in enumerate(text)]
    return page_docs

def create_index_from_docs(docs: List[Document], openai_api_key: str) -> FAISS:
    index = FAISS.from_documents(docs, OpenAIEmbeddings(openai_api_key=openai_api_key))
    return index

def get_index_for_single_pdf(pdf_file, pdf_name, openai_api_key):
    text, filename = parse_pdf(BytesIO(pdf_file), pdf_name)
    docs = text_to_docs(text, filename)
    index = create_index_from_docs(docs, openai_api_key)
    return index
