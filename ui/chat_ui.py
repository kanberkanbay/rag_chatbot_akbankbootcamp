import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background: transparent;
        }
        h1 {
            text-align: center;
            color: #00d9ff;
            font-weight: 800;
            text-shadow: 0px 0px 10px rgba(0, 217, 255, 0.4);
        }
        .chat-bubble {
            padding: 12px 18px;
            border-radius: 18px;
            margin: 8px 0;
            max-width: 75%;
            line-height: 1.4;
            word-wrap: break-word;
            font-size: 16px;
        }
        .user {
            background-color: #0078ff;
            color: white;
            margin-left: auto;
            border-top-right-radius: 5px;
        }
        .bot {
            background-color: #303f9f;
            color: #e3f2fd;
            margin-right: auto;
            border-top-left-radius: 5px;
        }
        .stTextInput>div>div>input {
            border: 2px solid #00d9ff;
            border-radius: 12px;
            padding: 10px;
            background-color: #111;
            color: white;
        }
        .stButton>button {
            width: 100%;
            border-radius: 12px;
            background: linear-gradient(45deg, #00d9ff, #0078ff);
            border: none;
            color: white;
            font-weight: bold;
            padding: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #0078ff, #00d9ff);
            box-shadow: 0 0 15px #00d9ff;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 RAG Chatbot - Yapay Zeka Kaynaklı")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat history display
for role, msg in st.session_state.chat_history:
    bubble_class = "user" if role == "Sen" else "bot"
    st.markdown(f"<div class='chat-bubble {bubble_class}'><b>{role}:</b> {msg}</div>", unsafe_allow_html=True)

# User input
user_input = st.text_input("Sorunu yaz:", placeholder="Yapay zeka nedir?")

# Send button
if st.button("🚀 Gönder"):
    if user_input.strip():
        st.session_state.chat_history.append(("Sen", user_input))
        try:
            res = requests.post("http://127.0.0.1:8000/query", json={"question": user_input})
            res.raise_for_status()
            data = res.json()
            bot_reply = data.get("answer", "Cevap alınamadı.")
        except Exception as e:
            bot_reply = f"Hata oluştu: {e}"
        st.session_state.chat_history.append(("Bot", bot_reply))
        st.rerun()
