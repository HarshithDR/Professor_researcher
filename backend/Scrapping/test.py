# #HuggingFace AccessToken :  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
# !pip install pypdf

# !pip install -q transformers einops accelerate langchain==0.1.15 bitsandbytes

# """#Embedding :
# !pip install sentence_transformers

# # 4 bits quantatization:
# bitsandbytes
# """

# !pip install sentence_transformers

# !pip install llama_index

# !pip install llama-index-llms-huggingface

# Commented out IPython magic to ensure Python compatibility.
# %pip install llama-index-embeddings-langchain
#!pip install accelerate
#!pip install -i https://pypi.org/simple/ bitsandbytes

from llama_index.core import VectorStoreIndex,SimpleDirectoryReader, ServiceContext
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.prompts.prompts import SimpleInputPrompt
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.core import ServiceContext
from llama_index.embeddings.langchain import LangchainEmbedding
import torch

# !huggingface-cli login

#Create a base folder 'Data' and store all the required documents
documents = SimpleDirectoryReader("backend/Scrapping/data").load_data()
print(documents)

#Prompt for LLM
system_prompt = """
You are a QA assistant.
Your goal is to answer the questions as accurately as possible based on the context and instruction provided
"""

#Default formate supportable by llama2
query_wrapper_prompt=SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")
print(query_wrapper_prompt)

#LLM model
llm = HuggingFaceLLM(
    context_window=4096,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.0, "do_sample": False},
    system_prompt=system_prompt,
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="meta-llama/Llama-2-7b-chat-hf",
    model_name="meta-llama/Llama-2-7b-chat-hf",
    device_map="auto",
    # uncomment this if using CUDA to reduce memory usage
    # model_kwargs={"torch_dtype": torch.float16 , "load_in_8bit":True}
)

embed_model=LangchainEmbedding(
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2"))

service_context=ServiceContext.from_defaults(
    chunk_size=1024,
    llm=llm,
    embed_model=embed_model
)

index=VectorStoreIndex.from_documents(documents,service_context=service_context)

query_engine=index.as_query_engine()

response=query_engine.query("what is neural network?")

print(response)