from rag_pipeline import load_website, create_vectorstore

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

text = load_website(url)

vectorstore = create_vectorstore(text)

print("Total chunks stored:", vectorstore._collection.count())