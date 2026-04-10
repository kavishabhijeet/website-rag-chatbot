import streamlit as st

from rag_pipeline import load_website
from rag_pipeline import create_vectorstore
from rag_pipeline import create_rag_chain


st.set_page_config(page_title="Website RAG Chatbot", page_icon="🤖")

st.title("🌐 Website RAG Chatbot")

st.write("Chat with any website content")


# store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# store rag pipeline
if "rag" not in st.session_state:
    st.session_state.rag = None


url = st.text_input("Enter Website URL")


if url and st.session_state.rag is None:

    with st.spinner("Reading website..."):

        text = load_website(url)

        vectorstore = create_vectorstore(text)

        st.session_state.rag = create_rag_chain(vectorstore)

    st.success("Website ready! Ask questions below.")



# display previous chat
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])



# user input
question = st.chat_input("Ask question")


if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)


    answer = st.session_state.rag(question)


    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)   