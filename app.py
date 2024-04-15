import streamlit as st
import openai
from io import BytesIO
from brain_1 import get_index_for_single_pdf
import os

# Set the title for the Streamlit app
st.title("RAG enhanced Chatbot")

# Initialize OpenAI client with API key from environment variable
# For security, never hardcode your API keys in the source code. Use environment variables or secrets management instead.
client = openai.OpenAI(api_key="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")

# Function to create a vectordb for a single PDF file
@st.cache_resource
def create_vectordb(file, filename):
    with st.spinner("Creating vector database..."):
        vectordb = get_index_for_single_pdf(file.getvalue(), filename, client.api_key)
    return vectordb

# Upload PDF file using Streamlit's file uploader
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

# If a PDF file is uploaded, create the vectordb and store it in the session state
if pdf_file:
    st.session_state["vectordb"] = create_vectordb(pdf_file, pdf_file.name)

# Define the template for the chatbot prompt
prompt_template = """
    You are a helpful Assistant who answers users' questions based on the PDF context provided.

    Keep your answer concise.

    Focus on the metadata 'filename' and 'page' when citing sources.

    Reply "Not applicable" if the text is irrelevant.
    
    PDF content:
    {pdf_extract}
"""

# Get the user's question using Streamlit's chat input
question = st.text_input("Ask anything")

# Handle the user's question
if question and "vectordb" in st.session_state:
    vectordb = st.session_state["vectordb"]
    search_results = vectordb.similarity_search(question, k=3)
    pdf_extract = "\n".join([result.page_content for result in search_results])

    # Prepare the full prompt for the ChatGPT
    full_prompt = prompt_template.format(pdf_extract=pdf_extract)

    try:
        # Generate response using OpenAI's GPT model via the new client
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": full_prompt},
                {"role": "user", "content": question}
            ],
            model="gpt-3.5-turbo"
        )

        # Display the generated response, properly accessing the content
        if chat_completion.choices:
            st.write(chat_completion.choices[0].message.content)
        else:
            st.error("Failed to generate a response. Please try again.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    if question:  # If a question is asked but no PDF is loaded
        st.error("Please upload a PDF to proceed.")
