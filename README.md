# Mistral AI Task Selector

This project uses the **Mistral AI API** to demonstrate various tasks that can be performed with AI, including text classification, information extraction, personalization, and summarization. Users can select a task from the sidebar and interact with the model.

## Features

- **Customer Service Classification**: Classify customer inquiries into predefined categories.
- **Information Extraction**: Extract structured information from medical notes.
- **Personalized Email Response**: Generate personalized responses for mortgage inquiries.
- **Newsletter Summarization**: Summarize the key points of a newsletter and generate a markdown report.

## Requirements

Before running the app, make sure you have the following dependencies installed:

- Python 3.7+
- Streamlit
- Mistral AI API client

## Installation

Follow these steps to set up the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/your-username/mistral-ai-task-selector.git
cd mistral-ai-task-selector
```

### 2. Install the required libraries
Create a virtual environment (recommended) and install the dependencies.

```bash
python -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

Alternatively, if you don't use a virtual environment, install the dependencies directly:

```bash
pip install streamlit mistralai
```

### 3. Set up the API key
Ensure you have an API key from Mistral AI. You can set it as an environment variable by running the following command:

```bash
export MISTRAL_API_KEY="your-api-key-here"  # For Windows use: set MISTRAL_API_KEY=your-api-key-here
```

Alternatively, you can hardcode the key in the app.py file (not recommended for production).

### 4. Run the app
After installing the dependencies and setting up the API key, you can start the app with the following command:

```bash
streamlit run app.py
```

This will open a new tab in your browser, where you can interact with the app.

## How to Use
Once the app is running, you can:

1. **Select a task**: Choose from the options in the sidebar (Classification, Information Extraction, Personalization, or Summarization).
2. **Input your data**: Based on the selected task, you will be prompted to enter text data (e.g., customer inquiry, medical notes, email, or newsletter).
3. **Submit**: Click on the corresponding button to process the data. The app will then interact with the Mistral AI model and display the results.

## Available Tasks
- **Customer Service Classification**: Enter a customer inquiry, and the AI will classify it into one of the following categories:
  - Card Arrival
  - Change PIN
  - Exchange Rate
  - Country Support
  - Cancel Transfer
  - Charge Dispute
  - Customer Service (if it doesn't match any of the predefined categories)

- **Information Extraction**: Enter medical notes, and the AI will extract information such as age, gender, diagnosis, weight, and smoking status in a structured JSON format.

- **Personalized Email Response**: Provide a mortgage inquiry email, and the AI will generate a personalized response using the provided facts about mortgage rates.

- **Newsletter Summarization**: Input a newsletter, and the AI will generate a concise summary, interesting questions, and a markdown report based on the content.

## Customization
You can customize the app by modifying the CSS styles, updating the API key, or adding new tasks. The layout and appearance can be customized by modifying the Streamlit widgets and CSS classes.

### Example Customizations
- Change sidebar colors: Modify the background and hover effects in the CSS section.
- Add more tasks: Add new tasks by creating new sections in the code and linking them to the sidebar options.

## Troubleshooting
- If you encounter issues related to the Mistral API key, make sure the key is correctly set in the environment variables or hardcoded in app.py.
- If you experience performance issues, check if the server hosting the application has sufficient resources.
