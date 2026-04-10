from rag_pipeline import load_website, create_vectorstore, create_rag_chain

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

text = load_website(url)

vectorstore = create_vectorstore(text)

rag = create_rag_chain(vectorstore)

question = "What is Artificial Intelligence"

answer = rag(question)

print("\nAnswer:\n", answer)