Local LLM Chatbot

This project is part of the Udemy course:Getting Started with Gen AI: LangChain, LLAMA3 & Ollama 
https://www.udemy.com/course/getting-started-with-gen-ai-langchain-llama3-ollama/

🔍 Overview

This project demonstrates how to build your own web-based chatbot using local large language models (LLMs). It uses:

LangChain for chaining prompts and tools

LLAMA3 models running locally through Ollama

A simple Streamlit web interface

Perfect for learners who want hands-on experience building and running local LLM-powered applications.

📁 Project Structure

local-llm-chatbot/
  - chatbot_app.py             # Streamlit chatbot interface
  - requirements.txt          # Python dependencies
  - README.md                 # Project instructions

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/gulshanmirg/local-llm-chatbot.git
cd local-llm-chatbot

2. Install Requirements

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Then install dependencies (streamlit and langchain_ollama):
pip install -r requirements.txt

or 

install streamlit and langchain_ollama manually: 
pip install streamlit  
pip install langchain_ollama

3. Install and Run Ollama

Install Ollama:👉 https://ollama.com/download

Pull a LLaMA3 model:

ollama pull llama3

Start the model:

ollama run llama3

4. Run the Chatbot

streamlit run chatbot_app.py

📘 Project Requirements

To complete this project, you should:

Set up a Python environment with LangChain, Streamlit, and Ollama

Pull and run an LLM locally (LLAMA3 or similar)

Build a user interface using Streamlit (chatbot_app.py)

Test end-to-end chatbot functionality

✅ Project: Local Chatbot Web App with Local LLM

This exercise guides you to build a complete, user-friendly chatbot webpage that runs entirely on your computer using a local LLM (Llama3 via Ollama), using Python, Streamlit, and the langchain_ollama library. The layout is clean and modern, with the following key features:

A warm title and welcome message

A light-colored screen with a bordered layout and rounded corners for neatness

An input box with a light yellow background where users can type their questions

Two buttons placed side-by-side: one for submitting the question and one for clearing the conversation history

When a user presses Enter or clicks Submit, the app sends the question to the local chatbot model and shows the response

Below the input, a conversation history section displays both the user's and the chatbot's messages

If the Clear button is pressed, it clears only the chat history but keeps the typed question in place

# Python Code
import streamlit as st
from langchain_ollama import OllamaLLM

# Set up Streamlit page config and custom styling
st.set_page_config(page_title="Local ChatBOT", layout="wide")
st.markdown("""
    <style>
        .main {
            background-color: #f0f4f8;
        }
        .stColumn > div {
            border: 1px solid #ccc;
            padding: 1rem;
            border-radius: 8px;
            background-color: white;
        }
        input[type="text"] {
            background-color: #fff9db !important;
        }
        .form-buttons-container button {
            margin-right: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Display the app title and introduction
st.title("🤖 Web-based Local ChatBOT")
st.markdown("Welcome to your local chatbot powered by Llama3.")

# Create input form with Submit and Clear buttons
with st.form(key="chat_form"):
    user_input = st.text_input("Enter your question:", key="user_input")
    col1, col2 = st.columns([1, 1])
    with col1:
        submit = st.form_submit_button("Submit")
    with col2:
        clear = st.form_submit_button("Clear")

    if clear:
        st.session_state.chat_history = []
        st.rerun()

# Initialize LLM
llm = OllamaLLM(model="llama3.2", temperature=0)

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Process input on submit
if submit and user_input:
    prompt = f"Answer the question: {user_input}"
    response = llm.invoke(prompt)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display conversation history
st.markdown("### Conversation")
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")


# 💬 LLM Prompt to Recreate the Chatbot UI

Use the following prompt in ChatGPT or another LLM to regenerate the Python code for this chatbot project:

Prompt:

I want to create a simple web page where users can ask questions and get answers from a chatbot that runs on my computer. The page should look clean, with a light background and a clear layout.
It should have:
- A title and welcome message at the top
- A box for typing a question
- Two buttons side by side: one to submit the question and one to clear the conversation history
- When someone submits a question (by pressing Enter or clicking Submit), the chatbot should give a reply using the Llama3 model through Ollama
- Below that, a chat window should show both the user’s questions and the bot’s responses
- If the Clear button is clicked, it should clear the conversation (but keep the typed question)
- The input box should have a light yellow background, and the layout should use bordered sections with rounded corners to look neat

📄 License

This project is licensed under the MIT License – you are free to use, modify, and distribute the code for personal or commercial purposes.


