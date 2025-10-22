🧠 RAG Chatbot – Yapay Zeka Destekli Bilgi Asistanı
🚀 Proje Amacı

Bu proje, Retrieval-Augmented Generation (RAG) mimarisi kullanılarak geliştirilmiş bir akıllı chatbot uygulamasıdır.
Amaç, bir veri kümesi içerisinden en alakalı bilgileri vektör veritabanı yardımıyla bulup, OpenAI modeliyle anlamlı ve kaynaklı cevaplar üretmektir.
Kısacası: chatbot hem ezbere değil, hem de bilgiye dayalı cevap verir.

🧩 Kullanılan Teknolojiler
Katman	Teknoloji
Framework	LangChain
LLM (Language Model)	OpenAI GPT-3.5 Turbo
Embedding	OpenAI Embeddings
Vektör Veritabanı	Chroma DB
Backend	FastAPI
Frontend	Streamlit
Ortam Yönetimi	Python Virtual Env (venv)
🗂️ Veri Seti Hakkında

Proje, kullanıcı tarafından hazırlanan veya dışarıdan yüklenen metin verilerini işler.
Bu veriler, app/ingest.py dosyası aracılığıyla küçük parçalara bölünür (chunk edilir) ve Chroma veritabanına embedding olarak kaydedilir.
Chatbot, kullanıcı soru sorduğunda önce bu veritabanında en benzer içerikleri bulur, ardından LLM modeliyle anlamlı bir yanıt oluşturur.

⚙️ Kurulum ve Çalıştırma Adımları
1️⃣ Sanal Ortam Kurulumu
python -m venv venv
venv\Scripts\activate  # Windows için
pip install -r requirements.txt

2️⃣ Veriyi Sisteme Ekle
python app/ingest.py

3️⃣ Backend (API) Çalıştır
uvicorn app.chatbot_api:app --reload

4️⃣ Arayüzü Başlat
streamlit run ui/chat_ui.py


✅ Tarayıcı otomatik açılacaktır:
http://localhost:8501
 adresinden chatbot’a erişebilirsin.

🧱 RAG Mimarisi Özeti

RAG (Retrieval-Augmented Generation), iki temel adımdan oluşur:

Retrieval (Bilgi Getirme):
Kullanıcının sorusuna göre vektör veritabanından en alakalı bilgi parçaları çekilir.

Generation (Cevap Üretme):
Bu bilgiler, GPT-3.5 modeline iletilerek doğal dilde akıcı bir cevap oluşturulur.

Bu sayede chatbot, yalnızca eğitim verisine değil, gerçek ve güncel kaynaklara dayalı yanıtlar üretir.

🖥️ Web Arayüzü

Arayüz Streamlit ile oluşturulmuştur.
Kullanıcı:

Sorusunu girer

Sohbet geçmişi tutulur

Her cevap RAG pipeline’ından geçer

💬 Modern, minimal ve kullanıcı dostu tasarım.

📊 Çözümün Katkısı

Bu proje;

Kurumsal dokümanlar, teknik belgeler veya PDF verileriyle konuşan chatbot’lar geliştirmek için temel oluşturur.

RAG mimarisiyle bilgiye dayalı yapay zekâ geliştirmenin örnek bir uygulamasıdır.
