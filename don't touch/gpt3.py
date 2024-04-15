from transformers import pipeline
import openai

def query_huggingface_model(file_path, model_name="gpt-3", api_token="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"):
    # Load the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        context = file.read()
    
    # Initialize a pipeline for the desired model
    generator = pipeline(model=model_name, api_key=api_token, use_auth_token=True)
    
    # Use the model to generate a response based on the file's content
    response = generator('what is ai?', max_length=50)
    
    return response

# Example usage
file_path = "professors_content.txt"
output = query_huggingface_model(file_path)
print(output)
