import os
import streamlit as st
from mistralai import Mistral, UserMessage

# Load API key from environment variable
os.environ["MISTRAL_API_KEY"] = "CZ54uDhpNVIrfJTvnjflHs4LuiSU4XHr"
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize Mistral client
def mistral(user_message, model="mistral-large-latest", is_json=False):
    client = Mistral(api_key=api_key)
    messages = [UserMessage(content=user_message)]
    
    chat_response = client.chat.complete(
        model=model,
        messages=messages,
    )
    return chat_response.choices[0].message.content

# Streamlit page configuration
st.set_page_config(page_title="Mistral AI Tasks", page_icon=":guardsman:", layout="wide")

# Custom CSS to remove circles and add hover effect
st.markdown("""
    <style>
        /* Remove the radio button circles and custom styles for sidebar */
        .css-1g6z4f8 {
            display: none;
        }
        
        .css-1h2w6u8 {
            padding: 10px;
            font-size: 16px;
            background-color: transparent;
            transition: background-color 0.3s ease;
        }

        /* Apply hover effect to sidebar items */
        .css-1h2w6u8:hover {
            background-color: #f4f4f4;
            cursor: pointer;
        }

        /* Sidebar background */
        .css-1b1a2qz {
            background-color: #f7f7f7;
        }
        
        /* Apply hover effect on sidebar section labels */
        .css-1d391kg {
            padding: 5px 15px;
            font-size: 18px;
            color: #333;
        }
        
        .css-1d391kg:hover {
            background-color: #e2e2e2;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Page Header
st.title("Mistral AI Task Selector")
st.markdown("""
    **Explore various AI capabilities** like Classification, Information Extraction, Personalization, and Summarization with Mistral.
    Use the sidebar to select your task and interact with the powerful language model.
""")

# Sidebar options with a fresh design
st.sidebar.title("Select a Task")
task = st.sidebar.radio("Choose an option", [
    "Classification",
    "Information Extraction",
    "Personalization",
    "Summarization"
])

# Task: Classification
if task == "Classification":
    st.subheader("Customer Service Classification")
    st.markdown("""
        You are a **bank customer service bot**. Your task is to assess customer intent and categorize their inquiry into one of the following predefined categories:
        * Card Arrival
        * Change PIN
        * Exchange Rate
        * Country Support
        * Cancel Transfer
        * Charge Dispute
        If the text doesn't fit into any of the above categories, classify it as: **Customer Service**.
    """)
    
    inquiry = st.text_area("Enter your inquiry here")
    if st.button("Classify Inquiry"):
        if inquiry:
            response = mistral(f"Please classify the inquiry: {inquiry}")
            st.success(f"Category: {response}")
        else:
            st.error("Please enter an inquiry to classify.")

# Task: Information Extraction
elif task == "Information Extraction":
    st.subheader("Information Extraction from Medical Notes")
    st.markdown("""
        **Extract structured information** from medical notes. 
        Use the model to extract relevant details such as age, gender, diagnosis, weight, and smoking status from the provided text.
    """)
    
    medical_notes = """
    A 60-year-old male patient, Mr. Johnson, presented with symptoms of increased thirst, frequent urination, fatigue, and unexplained weight loss. 
    He was diagnosed with diabetes and prescribed Metformin.
    """
    
    prompt = f"""
    Extract information from the following medical notes:
    {medical_notes}
    Return json format with the following schema:
    {{
        "age": {{ "type": "integer" }},
        "gender": {{ "type": "string", "enum": ["male", "female", "other"] }},
        "diagnosis": {{ "type": "string", "enum": ["migraine", "diabetes", "arthritis", "acne"] }},
        "weight": {{ "type": "integer" }},
        "smoking": {{ "type": "string", "enum": ["yes", "no"] }}
    }}
    """
    
    if st.button("Extract Information"):
        response = mistral(prompt, is_json=True)
        if response:
            st.json(response)
        else:
            st.error("Error extracting information. Try again.")

# Task: Personalization
elif task == "Personalization":
    st.subheader("Personalized Email Response")
    st.markdown("""
        **Generate personalized email responses** for mortgage inquiries. The model will use the provided facts to craft a professional and tailored email.
    """)
    
    email = """
    Dear mortgage lender,
    What's your 30-year fixed-rate APR, and how does it compare to the 15-year fixed rate?
    Regards,
    Anna
    """
    
    prompt = f"""
    You are a mortgage lender customer service bot, and your task is to create personalized email responses.
    Answer the customer's inquiry using the provided facts below. Ensure that your response is clear, concise, and addresses the question.
    # Email
    {email}
    """
    
    if st.button("Generate Email Response"):
        response = mistral(prompt)
        if response:
            st.success(f"Response: {response}")
        else:
            st.error("Error generating response. Try again.")

# Task: Summarization
elif task == "Summarization":
    st.subheader("Summarization of Newsletter")
    st.markdown("""
        **Summarize the key points** of the newsletter using the model. 
        It will generate interesting questions and provide answers, followed by a full markdown report.
    """)
    
    newsletter = """
    Mistral AI introduced new models, formed an alliance with Microsoft, and made waves in the AI industry with impressive results. 
    The partnership promises new AI applications and significant advancements in language models.
    """
    
    prompt = f"""
    You are a commentator. Your task is to summarize the following newsletter.
    Combine key points, questions, and answers into a comprehensive markdown report.
    # Newsletter:
    {newsletter}
    """
    
    if st.button("Generate Report"):
        response = mistral(prompt)
        if response:
            st.write(f"### Summary and Analysis Report: \n{response}")
        else:
            st.error("Error generating summary. Try again.")
