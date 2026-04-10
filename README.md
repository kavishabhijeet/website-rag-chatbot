# Website RAG Chatbot

This project is a Retrieval-Augmented Generation (RAG) chatbot that can read any website URL and answer questions based on its content.

## Tech Stack

- Python
- LangChain
- Mistral LLM
- Chroma Vector Database
- Sentence Transformers
- BeautifulSoup (web scraping)
- Streamlit (UI)

## Features

- Extracts website content
- Converts text into embeddings
- Stores embeddings in vector database
- Answers user questions from website data

## Project Structure

website-rag-chatbot/
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
├── README.md
└── .env

## How to Run

1. Install dependencies
pip install -r requirements.txt

2. Run project
streamlit run app.py

## Future Improvements

- Chat history memory
- Multiple website support
- PDF upload
- Deploy online