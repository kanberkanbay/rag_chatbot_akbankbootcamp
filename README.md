# RAG Chatbot - Yapay Zeka Kaynaklı

## Kurulum

1. Sanal ortam oluştur:
python -m venv venv
venv/bin/activate
pip install -r requirements.txt

2. Metni ingest et:
python app/ingest.py

3. FastAPI backend’i çalıştır:
uvicorn app.chatbot_api:app --reload

4. Streamlit chat arayüzünü çalıştır:
streamlit run ui/chat_ui.py

Otomatik tarayıcı açılır.
