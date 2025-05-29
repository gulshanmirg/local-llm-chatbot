# 🤖 Local Web-Based Chatbot with Llama3 + Streamlit

Build your own **local chatbot** using **Meta's Llama3**, **Streamlit**, and **LangChain** with this beginner-friendly project. This chatbot runs entirely on your machine using **Ollama** to load and interact with the LLM (no internet or API key required).

---

## 📌 Features
- Simple Streamlit web interface
- Powered by LangChain and Llama3
- Fully local (privacy-friendly)
- Tracks chat history
- Clean layout and customizable UI

---

## 🧰 Requirements
- Python 3.8+
- [Streamlit](https://streamlit.io)
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com) (must have Llama3 model installed)

---

## 🔧 Installation

1. **Clone the repo**
```bash
git clone https://github.com/gulshanmirg/local-llm-chatbot.git
cd local-llm-chatbot
```

2. **Create and activate a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install the required packages**
```bash
pip install -r requirements.txt
```

4. **Start Ollama and pull the Llama3 model**
```bash
ollama run llama3
```

5. **Run the chatbot app**
```bash
streamlit run chatbot_app.py
```

---

## 🧪 Project Exercises (Step-by-Step)
1. Create a Streamlit interface
2. Connect the Llama3 model with LangChain
3. Add input validation and a Clear button
4. Implement chat history with `session_state`
5. Enhance layout and styling with Streamlit columns

---

## 📁 Project Structure
```
local-llm-chatbot/
│
├── chatbot_app.py        # Main chatbot application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🛠️ Powered By
- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com)
- [Streamlit](https://streamlit.io)

---

## 📬 Feedback & Contributions
Feel free to fork the repo, submit issues, or create pull requests to improve or expand the chatbot. Happy coding!

---

## 📄 License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute this software, including in closed-source projects. See the LICENSE file for details.
