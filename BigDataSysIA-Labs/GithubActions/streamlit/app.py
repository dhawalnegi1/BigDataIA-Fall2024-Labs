import streamlit as st
import requests
import json

st.title("Chat with OpenAI through FastAPI")

user_message = st.text_input("Enter your message:")

if st.button("Send"):
    if user_message:
        try:
            # Prepare the request payload
            payload = json.dumps({"message": user_message})
            
            # Set the headers
            headers = {
                "Content-Type": "application/json"
            }
            
            # Make the POST request to the FastAPI endpoint
            response = requests.post("http://fastapi:8000/chat", data=payload, headers=headers)
        
            if response.status_code == 200:
                st.write("OpenAI Response:", response.json().get("response"))
            else:
                st.error(f"Error: {response.json().get('detail')}")
        except Exception as e:
            st.error(f"Error: {e}")
