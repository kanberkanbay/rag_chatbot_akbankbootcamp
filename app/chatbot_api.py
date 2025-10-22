from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv
import json

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
vectordb = Chroma(collection_name="ai_docs", embedding_function=embeddings)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectordb.as_retriever(),
    memory=memory,
)

@app.post("/query")
async def chat(request: Request):
    data = await request.json()
    question = data.get("question", "")

    if not question:
        return {"error": "Soru boş olamaz."}

    print(f"\n🟡 Soru: {question}")

    try:
        result = qa_chain.invoke({"question": question})
        print("🟢 Ham sonuç:", result)
    except Exception as e:
        print("🔴 Hata:", str(e))
        return {"answer": f"Hata oluştu: {str(e)}"}

    # LangChain result bazen HumanMessage nesneleri içerir -> JSON’a çevrilebilir hale getiriyoruz
    def make_json_safe(obj):
        if isinstance(obj, (dict, list, str, int, float, type(None))):
            return obj
        return str(obj)

    safe_result = json.loads(json.dumps(result, default=make_json_safe))

    # Yanıt metnini bul
    answer_text = (
        safe_result.get("answer")
        or safe_result.get("result")
        or safe_result.get("output_text")
        or safe_result.get("response")
        or "Cevap alınamadı."
    )

    print("💬 Bot cevabı:", answer_text)
    return {"answer": answer_text}
