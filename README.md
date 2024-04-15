Certainly! Below is a README file for the provided code:

---

# RAG Enhanced Chatbot with Streamlit

This repository contains code for a Streamlit app implementing an enhanced chatbot capable of answering questions based on the context provided in a PDF document. The chatbot utilizes OpenAI's GPT model for generating responses and FAISS for efficient similarity search over document embeddings.

## Features

- **Scraping**: our server will scrape the professors data from the college website and stores it vectorized form for further rag model.
- **Response Generation**: The chatbot generates concise responses based on the context provided in the PDF.
- **Metadata Handling**: Responses include metadata such as the filename and page number for citation purposes.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HarshithDR/Scarlet-hacks
   ```


2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Upload a PDF document using the file uploader.
3. Ask questions related to the content of the PDF in the provided text input.
4. View the generated responses from the chatbot.

## Implementation Details

- **Backend**: Python code utilizing Streamlit for the web interface.
- **OpenAI API**: Integration with OpenAI's GPT model for response generation.
- **Document Processing**: PDF parsing and document embedding using FAISS for efficient similarity search.
- **Frontend**: Streamlit's UI components for file upload and text input.

## Contributors

- Harshit Deshalli
- Sachin Shivanna
- Nishchal
- Uday Venkatesha


Feel free to customize this README file with additional information or instructions specific to your project.