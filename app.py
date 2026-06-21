import streamlit as st

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


# -----------------------------
# Load Documents
# -----------------------------
leave_doc = TextLoader("leave_policy.txt").load()
travel_doc = TextLoader("travel_policy.txt").load()
wfh_doc = TextLoader("wfh_policy.txt").load()

documents = leave_doc + travel_doc + wfh_doc


# -----------------------------
# Chunk Documents
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = text_splitter.split_documents(documents)


# -----------------------------
# Create Embeddings
# -----------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------
# Create Vector Database
# -----------------------------
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model
)


# -----------------------------
# Retrieval Function
# -----------------------------
def retrieve_answer(question):

    results = db.similarity_search(
        question,
        k=1
    )

    return {
        "answer": results[0].page_content,
        "source": results[0].metadata["source"]
    }


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("TechNova Policy Assistant")

question = st.text_input("Ask a Question")

if st.button("Search"):

    if question:

        response = retrieve_answer(question)

        st.subheader("Retrieved Information")
        st.write(response["answer"])

        st.subheader("Source")
        st.write(response["source"])

    else:
        st.warning("Please enter a question.")