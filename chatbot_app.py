# =======================
# Exercise 1: Basic Streamlit Interface
# =======================
import streamlit as st

st.title("Web-based Local ChatBOT")
user_input = st.text_input("Enter your question:")
if user_input:
    st.write(f"You entered: {user_input}")

# =======================
# Exercise 2: Integrate OllamaLLM
# =======================
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2", temperature=0)
if user_input:
    prompt = f"Answer the question: {user_input}"
    response = llm.invoke(prompt)
    # Display the response on the screen
    st.write(f"Response:\n{response}")
# =======================
# =======================
# Exercise 3: Add Input Validation and Clear Button
# =======================
if st.button("Clear"):
    st.experimental_rerun()
if user_input == "":
    st.warning("Please enter a question to continue.")

# =======================

# =======================
# Exercise 4: Chat History
# =======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if user_input:
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for speaker, message in st.session_state.chat_history:
    st.write(f"**{speaker}:** {message}")
# =======================

