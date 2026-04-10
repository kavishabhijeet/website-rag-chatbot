from rag_pipeline import load_website

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

text = load_website(url)

print(text[:500])