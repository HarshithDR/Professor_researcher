import requests
import streamlit as st

def main():
    st.title("Chat Bot")

    # Text input from the user
    user_input = st.text_area("Enter your text here:")

    if st.button("Submit"):
        # Send the text to the Flask server
        response = requests.post("http://127.0.0.1:5000/process_text", json={"text": user_input})
        if response.status_code == 200:
            # Display the response from the Flask server
            st.text_area("Response:", value=response.json()['response'], height=200)

if __name__ == "__main__":
    main()
