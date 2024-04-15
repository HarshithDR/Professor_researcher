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
import requests
import streamlit as st

def main():
    st.title(" Chicago Universities information")
    st.markdown("---")

    # Initialize conversation list
    session_state = st.session_state
    if "conversation" not in session_state:
        session_state.conversation = []

    # Display conversation
    for idx, (user, response) in enumerate(session_state.conversation):
        if user == 'You':
            st.text_area(f"{user}:", value=response, height=100, key=f"user_{idx}")
        else:
            st.text_area(f"{user}:", value=response, height=100, key=f"bot_{idx}")

    # Text input from the user
    user_input = st.text_input("Type a message...")

    if st.button("Send"):
        # Add user input to conversation
        session_state.conversation.append(('You', user_input))

        # Send the text to the Flask server
        response = requests.get("http://127.0.0.1:5000/chat", json={"text": user_input}).json()['response']
        print(ImportError(response))

        # Add bot response to conversation
        session_state.conversation.append(('Bot', response))

if __name__ == "__main__":
    main()
