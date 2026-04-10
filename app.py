import streamlit as st
from rag_pipeline import load_website,create_rag_chain,create_vectorstore

st.title("Website RAG Chatbot 🌐🤖")
st.write("Enter any website URL and ask questions from its content")

url = st.text_input("Enter Wesite URL")

if url:
    with st.spinner("Reading Website...."):
        text = load_website(url)
        vectorstore = create_vectorstore(text)
        rag = create_rag_chain(vectorstore)

    st.success("Website Loaded Successfully") 

    question = st.text_input("Ask a question")

    if question:
        answer = rag(question)

        st.write("### answer : ")
        st.write(answer)   