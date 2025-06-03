# Import required libraries
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
    # Text input for user question
    user_input = st.text_input("Enter your question:", key="user_input")
    # Two-column layout for buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        submit = st.form_submit_button("Submit")
    with col2:
        clear = st.form_submit_button("Clear")

    # If Clear button is pressed, reset input and rerun
    if clear:
        st.session_state.chat_history = []
        # st.session_state.clear()
        st.rerun()

# Initialize Ollama LLM with Llama3 model
llm = OllamaLLM(model="llama3.2", temperature=0)

# Initialize chat history in session state if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# If Submit is pressed and input exists, process the prompt
if submit and user_input:
    prompt = f"Answer the question: {user_input}"
    response = llm.invoke(prompt)
    # Append user input and response to chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display conversation history
st.markdown("### Conversation")
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")
