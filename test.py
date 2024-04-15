from transformers import pipeline
import torch

def read_context_file(filename, encoding="utf-8"):
  """Reads the contents of a text file and returns the text, handling potential encoding issues.

  Args:
      filename (str): Name of the context file.
      encoding (str, optional): Encoding of the text file. Defaults to "utf-8".

  Returns:
      str: The text content of the file.
  """
  try:
    with open(filename, "r", encoding=encoding) as f:
      context_text = f.read().strip()
    return context_text
  except UnicodeDecodeError:
    print("Error: The file encoding might be incorrect. Trying common encodings...")
    encodings = ["utf-8", "latin-1", "windows-1252"]
    for enc in encodings:
      try:
        with open(filename, "r", encoding=enc) as f:
          context_text = f.read().strip()
        print(f"Success! Using encoding: {enc}")
        return context_text
      except UnicodeDecodeError:
        pass  # Try the next encoding if this one fails
    print("Couldn't determine the correct encoding. Please check your file manually.")
    return ""  # Return an empty string if all encodings fail

# Replace 'model_id' with the actual ID of your chosen model from Hugging Face Hub
# (e.g., "openai/gpt-3")
model_id = "meta-llama/Llama-2-7b-chat-hf"

# Task type (e.g., question-answering, summarization, sentiment-analysis)
task = "question-answering"  # Adjust based on your model's capabilities

# Load the pipeline for your chosen task
nlp = pipeline(task, model=model_id, device=0 if torch.cuda.is_available() else -1)  # Use GPU if available

context_filename = "professors_content.txt"

# Handle potential encoding issues with the context file
context = read_context_file(context_filename)

user_question = input("Ask your question: ")

if task == "question-answering":
  # This approach combines context and user input for question-answering tasks.
# # Adjust for other task types accordingly.
    combined_text = context + "\n" + user_question
    # answer = nlp(combined_text, question=user_question)["answer"]
    # print(f"Answer: {answer}")
    input_data = {
    "question": user_question,
    "context": combined_text}
    answer = nlp(**input_data)["answer"]  # Use double asterisk (**) to unpack the dictionary
    print(f"Answer: {answer}")
    
else:
  # Modify this based on your chosen task (e.g., nlp(context_text) for summarization)
  output = nlp(combined_text)
  print(f"Output: {output}")

# Clarification: The `.weight']` message you might have seen earlier is likely unrelated
# and might be from a different part of your code (potentially model weights). You can
# safely ignore it for now.
