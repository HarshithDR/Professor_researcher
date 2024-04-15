# import requests
# import streamlit as st

# def main():
#     st.title("Chat Bot")

#     # Text input from the user
#     user_input = st.text_area("Enter your text here:")

#     if st.button("Submit"):
#         # Send the text to the Flask server
#         response = requests.get("http://127.0.0.1:5000/chat", json={"text": user_input})
#         print(ImportError(response))
#         if response.status_code == 200:
#             # Display the response from the Flask server
#             st.text_area("Response:", value=response.json()['response'], height=200)

# if __name__ == "__main__":
#     main()


# import requests
# import streamlit as st

# def main():
#     st.title("ChatGPT UI")
#     st.markdown("---")

#     # Initialize conversation list
#     conversation = []

#     # Text input from the user
#     user_input = st.text_input("You", "")

#     if st.button("Send"):
#         # Add user input to conversation
#         conversation.append(('You', user_input))

#         # Send the text to the Flask server
#         response = requests.get("http://127.0.0.1:5000/chat", json={"text": user_input}).json()['response']
#         print(ImportError(response))

#         # Add bot response to conversation
#         conversation.append(('Bot', response))

#     # Display conversation
#     for idx, (user, response) in enumerate(conversation):
#         if user == 'You':
#             st.text_area(f"{user}:", value=response, height=100, key=f"user_{idx}")
#         else:
#             st.text_area(f"{user}:", value=response, height=100, key=f"bot_{idx}")

# if __name__ == "__main__":
#     main()


# import requests
# import streamlit as st

# def main():
#     st.title("Chicago Universities Information")
#     st.markdown(
#         """
#         <style>
#         html, body, [class*="css"] {
#             font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; /* Change font style */
#             background-color: #f0f2f6; /* Light grey background */
#             color: #333333; /* Adjust text color for better contrast */
#         }
#         .stButton>button {
#             color: white; /* Button text color */
#             background-color: #0078d7; /* Button background color */
#             border: none;
#             border-radius: 5px;
#             padding: 10px 24px;
#         }
#         .stTextInput>div>div>input {
#             color: #4a4a4a; /* Input field text color */
#             border-radius: 5px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown("---")

#     # Initialize conversation list
#     session_state = st.session_state
#     if "conversation" not in session_state:
#         session_state.conversation = []

#     # Display conversation
#     for idx, (user, response) in enumerate(session_state.conversation):
#         if user == 'You':
#             st.text_area(f"{user}:", value=response, height=100, key=f"user_{idx}")
#         else:
#             st.text_area(f"{user}:", value=response, height=100, key=f"bot_{idx}")

#     # Text input from the user
#     user_input = st.text_input("Type a message...", key="user_input")

#     if st.button("Send"):
#         # Add user input to conversation
#         session_state.conversation.append(('You', user_input))

#         # Send the text to the Flask server
#         response = requests.get("http://127.0.0.1:5000/chat", json={"text": user_input})
#         response= response.json()['response']
#         print(ImportError(response))
        
#         # Add bot response to conversation
#         session_state.conversation.append(('Bot', response))

# if __name__ == "__main__":
#     main()



# import requests
# import streamlit as st

# def main():
#     st.title("Chicago Universities information")
    
#     # Initialize a container for the response before the input
#     response_container = st.empty()

#     # Text input from the user
#     user_input = st.text_area("Enter the topics you want to work on",placeholder="Eg : AI , Machine Learning, NLP, etc")

#     if st.button("Find"):
#         # Send the text to the Flask server
#         response = requests.get("http://127.0.0.1:5000/chat", json={"text": user_input})
        
#         if response.status_code == 200:
#             # Display the response from the Flask server using the container
#             response_container.text_area("Response:", value=response.json()['response'], height=200)
#         else:
#             response_container.text("Error: Failed to get a response from the server.")

# if __name__ == "__main__":
#     main()


import requests
import streamlit as st

def main():
    st.title("Chicago Universities Information")

    # Custom CSS to inject for styling
    st.markdown("""
        <style>
        /* Set the overall background color and text color */
        body {
            color: #fff;
            background-color: #263238;
        }
        /* Customize text area */
        .stTextArea > div > div > textarea {
            background-color: #546e7a;
            color: #eceff1;
        }
        /* Customize buttons */
        .stButton > button {
            background-color: #b2dfdb;
            color: #004d40;
        }
        /* Response text area style */
        .stTextInput > div > div > input {
            background-color: #546e7a;
            color: #eceff1;
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize a container for the response before the input
    response_container = st.empty()

    # Text input from the user
    user_input = st.text_area("Enter the topics you want to work on",
                              placeholder="E.g., AI, Machine Learning, NLP, etc")

    if st.button("Find"):
        # Send the text to the Flask server
        response = requests.get("http://127.0.0.1:5000/chat", json={"text": user_input})
        
        if response.status_code == 200:
            # Display the response from the Flask server using the container
            response_container.text_area("Response:", value=response.json()['response'], height=200)
        else:
            response_container.text("Error: Failed to get a response from the server.")

if __name__ == "__main__":
    main()
