from transformers import pipeline

def extract_data_from_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()  # Read the entire file as a single string
    return text

def run_chatbot(user_question):
    file_path = 'professors_content.txt'  # Update with your file path
    context = extract_data_from_text_file(file_path)
    # context = "Shouvik Roy | Shouvik Roy Assistant Teaching Professor of Computer Science Tags: Faculty Computer Science Home Office and Department Directory Directory Shouvik Roy Education Ph.D. Computer Science, Stony Brook University M.E. Computer Science and Engineering, Jadavpur University Research Interests Artificial Intelligence and Machine Learning Theory Systems Contact Information sroy20@iit.edu Website SB 206A Learn more... Illinois Tech welcomes you to join our community of people who discover, create, and solve. Apply today, visit us in Chicago, and contact us for more information.  Contact 10 West 35th Street Chicago, IL 60616 312.567.3000 Contact Us Social Media Links Facebook Instagram LinkedIn Twitter YouTube Campus Emergency Information Employment Alumni Access Illinois Tech Web Links Privacy Copyright Concerns IBHE Online Complaint System Student Complaint Information Student Non-Discrimination Policy"
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-large-squad2")
    answer = qa_pipeline({
        'question': user_question,
        'context': context
    })
    return answer['answer']

result = run_chatbot("who is shouvik?")
print(result)
