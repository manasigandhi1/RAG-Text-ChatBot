# 🔍 RAG Document Retrieval System

A Retrieval-Augmented Generation (RAG) prototype that demonstrates the core retrieval layer of a GenAI application using document chunking, embeddings, vector storage, and semantic search.

---

## 📌 Project Overview

Large Language Models can only provide useful answers when they have access to relevant information. Retrieval-Augmented Generation (RAG) solves this problem by retrieving the most relevant content from a knowledge base before generating a response.

This project focuses on building and validating the **retrieval component** of a RAG pipeline.

The system successfully:

✅ Loads document data

✅ Splits documents into meaningful chunks

✅ Converts chunks into vector embeddings

✅ Stores embeddings in a vector database

✅ Performs semantic similarity search

✅ Retrieves the most relevant chunks for a user query

✅ Displays results through a simple user interface

---

## 🎯 Objective

The goal of this project was to understand and implement the foundational components of a RAG architecture.

Instead of relying on keyword matching, the system uses vector embeddings and semantic search to identify the most relevant information related to a user's query.

---

## 🏗️ Architecture

```text
Document
    ↓
Document Loading
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
Chroma Vector Database
    ↓
Similarity Search
    ↓
Relevant Chunks Retrieved
    ↓
Displayed to User
```

---

## ⚙️ Technologies Used

* Python
* LangChain
* ChromaDB
* Text Embeddings
* Semantic Search
* Vector Databases

---

## 🔄 Workflow

### 1️⃣ Load Document

The application reads document content and prepares it for processing.

### 2️⃣ Chunk the Text

Large text is divided into smaller chunks to improve retrieval accuracy and context relevance.

### 3️⃣ Generate Embeddings

Each chunk is converted into a numerical vector representation that captures semantic meaning.

### 4️⃣ Store in ChromaDB

The generated embeddings are stored in a vector database for efficient retrieval.

### 5️⃣ Query Processing

When a user enters a question, the query is converted into an embedding.

### 6️⃣ Similarity Search

The system compares the query embedding with stored document embeddings.

### 7️⃣ Retrieve Relevant Content

The most semantically similar chunks are returned and displayed to the user.

---

## 💡 Example Queries

* What is Retrieval-Augmented Generation?
* Explain vector databases.
* What is semantic search?
* How are embeddings used in AI applications?
* What are the benefits of chunking?

---

## 📊 Key Learnings

Through this project, I gained practical experience with:

* RAG architecture fundamentals
* Document chunking strategies
* Embedding generation
* Vector databases
* Semantic similarity search
* LangChain workflow design
* Retrieval pipelines used in modern GenAI systems

---

## 🚀 Current Scope

This project successfully demonstrates the retrieval layer of a RAG system.

The retrieved document chunks can be used as contextual input for a Large Language Model (LLM) in a complete end-to-end RAG application.

Future iterations can extend this implementation by integrating response generation and conversational capabilities on top of the existing retrieval pipeline.

---

## 📂 Project Structure

```text
rag-document-retrieval/

│
├── app.py
├── requirements.txt
├── README.md
│
├── sample_data/
│   └── sample_document.txt
│
├── screenshots/
│   ├── ui.png
│   └── retrieval_results.png
│
└── architecture.png
```

---

## 📸 Screenshots

### User Interface
<img width="1279" height="601" alt="image" src="https://github.com/user-attachments/assets/98a718b3-e477-45ce-8897-8c014c882b8e" />

### Retrieval Results

<img width="1274" height="664" alt="image" src="https://github.com/user-attachments/assets/ba8a3811-2fba-4fcc-a526-be5374b10eee" />


---

## 🎓 Resume Highlights

**RAG Document Retrieval System**

* Developed a retrieval pipeline using LangChain and ChromaDB to perform semantic document search.
* Implemented document loading, chunking, embedding generation, and vector storage workflows.
* Built a user interface for querying documents and retrieving contextually relevant information.
* Demonstrated practical understanding of vector databases, embeddings, and Retrieval-Augmented Generation (RAG) concepts.
* Established a foundation for extending the system into a complete end-to-end GenAI application.

---

## 👩‍💻 Author

[Manasi Gandhi](https://manasigandhiportfolio.lovable.app/)

**Data Analyst | Generative AI Learner | Tableau | SQL | Excel | Dashboard Development**

 

---

⭐ If you found this project interesting, feel free to explore the code and share feedback.
