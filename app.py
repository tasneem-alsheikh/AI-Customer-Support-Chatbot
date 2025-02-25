import os
import streamlit as st
from mistralai import Mistral, UserMessage

# Set API Key (you can also set it through environment variables)
os.environ["MISTRAL_API_KEY"] = "CZ54uDhpNVIrfJTvnjflHs4LuiSU4XHr"
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize Mistral instance
client = Mistral(api_key=api_key)

# Streamlit UI
st.title("💬 AI Customer Support Chatbot")

# User input
user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input:
        # Prepare the request
        messages = [UserMessage(content=user_input)]
        
        # Call the Mistral API for a chat completion
        response = client.chat.complete(model="mistral-small-latest", messages=messages)
        
        # Display the chatbot response
        st.write("🤖 **Chatbot:**", response.choices[0].message.content)
    else:
        st.warning("Please enter a message.")
