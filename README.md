# RAG Chatbot - Yapay Zeka Kaynaklı

## Kurulum

1. Sanal ortam oluştur:
```bash
python -m venv venv
source venv/bin/activate  # windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. `.env.example` dosyasını `.env` olarak kopyalayıp OpenAI API keyinizi ekleyin:
```
OPENAI_API_KEY="buraya_senin_api_key"
```

3. Metni ingest et:
```bash
python app/ingest.py
```

4. FastAPI backend’i çalıştır:
```bash
uvicorn app.chatbot_api:app --reload
```

5. Streamlit chat arayüzünü çalıştır:
```bash
streamlit run ui/chat_ui.py
```

Tarayıcıda aç: `http://localhost:8501`
