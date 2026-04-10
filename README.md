# Website RAG Chatbot 🌐🤖

A Retrieval-Augmented Generation (RAG) chatbot that can read any website URL and answer questions based on the website content.

This project demonstrates how Large Language Models (LLMs) can retrieve relevant information from external data sources instead of relying only on pre-trained knowledge.

---

## 🚀 Features

- Extracts content directly from any website
- Converts text into embeddings
- Stores embeddings in vector database
- Retrieves relevant information based on user query
- Generates accurate answers using LLM
- Simple and interactive UI using Streamlit

---

## 🧠 Tech Stack

- Python
- LangChain
- Mistral LLM
- ChromaDB (Vector Database)
- Sentence Transformers (Embeddings)
- BeautifulSoup (Web Scraping)
- Streamlit (User Interface)

---

## 📂 Project Structure

website-rag-chatbot/
│
├── app.py                 # Streamlit UI
├── rag_pipeline.py        # RAG pipeline logic
├── requirements.txt       # dependencies
├── README.md              # project documentation
├── .gitignore
└── .env                   # API key (not uploaded)

---

## ⚙️ How it Works

1. User enters a website URL
2. Website content is extracted using BeautifulSoup
3. Text is split into smaller chunks
4. Chunks are converted into embeddings
5. Embeddings stored in Chroma vector database
6. User asks a question
7. Relevant content is retrieved from vector DB
8. LLM generates answer based on retrieved context

---

## 💻 Installation

Clone repository:

git clone https://github.com/yourusername/website-rag-chatbot.git

Go to project folder:

cd website-rag-chatbot

Create virtual environment:

python -m venv venv

Activate environment:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Add API key in .env file:

MISTRAL_API_KEY=your_api_key_here

Run project:

streamlit run app.py

---

## 📸 Example Use Case

Input website:
https://en.wikipedia.org/wiki/Artificial_intelligence

Example questions:
- What is artificial intelligence?
- Applications of AI
- Who is father of AI?

---

## 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- LangChain framework
- Vector databases
- Embeddings
- Prompt engineering
- Streamlit app development
- Git & GitHub workflow

---

## 🔮 Future Improvements

- Chat history memory
- Support multiple URLs
- Upload PDF documents
- Deploy online (Streamlit Cloud)
- Improve UI design

---

## 👨‍💻 Author

Abhijeet Anand

Aspiring Data Scientist | GenAI Enthusiast