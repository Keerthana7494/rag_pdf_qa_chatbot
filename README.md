# rag_pdf_qa_chatbot
# PDF RAG Question Answering

A simple Retrieval-Augmented Generation (RAG) project built to understand how applications can answer questions from uploaded documents.

The idea behind this project is simple: upload a PDF, ask a question about it, retrieve the relevant parts of the document, and use an LLM to generate an answer based on that information.

I built this as a learning project to understand the fundamentals of RAG before moving to more advanced implementations with databases, authentication, APIs, and Docker.

## What the project does

The application allows you to:

* Upload a PDF document
* Extract text from the PDF
* Split the text into smaller chunks
* Convert the chunks into embeddings
* Store the embeddings using FAISS
* Ask questions about the uploaded document
* Retrieve the most relevant chunks
* Send the retrieved information along with the question to Gemini
* Generate an answer based on the document

## RAG Flow

```text
PDF
 |
 v
Text Extraction
 |
 v
Text Chunking
 |
 v
Embeddings
 |
 v
FAISS Vector Store
 |
 v
User Question
 |
 v
Question Embedding
 |
 v
Similarity Search
 |
 v
Relevant Chunks
 |
 v
Gemini
 |
 v
Answer
```

## Technologies Used

* Python
* Streamlit
* LangChain
* PyPDF
* Sentence Transformers
* FAISS
* Google Gemini

## Project Structure

```text
pdf-rag-v1/
│
├── app.py
├── rag.py
├── embeddings.py
├── pdf_loader.py
├── vector_store.py
├── requirements.txt
├── .env
├── .gitignore
│
└── data/
```

## How It Works

### 1. Upload a PDF

The user uploads a PDF through the Streamlit interface.

### 2. Extract Text

PyPDF is used to read the PDF and extract its text.

### 3. Split the Text

Large documents are divided into smaller chunks using LangChain's `RecursiveCharacterTextSplitter`.

For example:

```text
Large Document
     |
     +-- Chunk 1
     +-- Chunk 2
     +-- Chunk 3
     +-- Chunk 4
```

This makes it easier to search for relevant information.

### 4. Create Embeddings

Each chunk is converted into a numerical vector using the Sentence Transformers model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

The embedding represents the meaning of the text as numbers.

### 5. Store Embeddings

The embeddings are stored in a FAISS vector store.

FAISS is used to perform similarity searches between the user's question and the document chunks.

### 6. Retrieve Relevant Information

When the user asks a question, the question is also converted into an embedding.

FAISS compares the question with the stored document embeddings and returns the most relevant chunks.

### 7. Generate the Answer

The retrieved chunks are added to the prompt along with the user's question.

Gemini then generates the final answer using the retrieved document information.

## Example

Suppose the uploaded PDF contains information about Java.

The user asks:

```text
What is the difference between HashMap and Hashtable?
```

The application does not simply send the question to the LLM.

Instead:

```text
Question
   |
   v
Question Embedding
   |
   v
FAISS Similarity Search
   |
   v
Relevant PDF Chunks
   |
   v
Question + Retrieved Context
   |
   v
Gemini
   |
   v
Answer
```

This is the basic idea behind Retrieval-Augmented Generation.

## Why I Built This

I wanted to understand RAG from the fundamentals instead of directly using a complete RAG framework and treating it as a black box.
The purpose is to understand the core RAG pipeline first.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Keerthana_07/pdf-rag-v1.git
```

```bash
cd pdf-rag-v1
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Replace the value with your Gemini API key.

Do not commit the `.env` file to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in the browser.

## Current Limitations

This is the first version of the project, so the vector store is maintained in memory.

When the application is stopped, the stored vectors are lost.

It currently focuses on a single uploaded PDF and basic question answering.

## Future Improvements

I plan to improve this project step by step by adding:

* PostgreSQL with pgvector
* Multiple document support
* Document metadata
* Firebase authentication
* User-specific documents
* FastAPI backend
* Docker
* Better retrieval and prompt handling
* Source/document references in answers

## What I Learned

While building this project, I got a better understanding of:

* Document loading
* Text chunking
* Embeddings
* Vector stores
* Similarity search
* Retrieval
* Context construction
* LLM-based answer generation
* The overall RAG architecture

The main takeaway for me was that RAG is not just about calling an LLM. The retrieval step is what allows the application to bring relevant information from an external document into the generation process.

## Author

Keerthana

Software Trainer | AI & Software Mentor

This project is part of my learning journey toward AI backend development.
