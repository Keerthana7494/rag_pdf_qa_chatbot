from langchain_google_genai import ChatGoogleGenerativeAI
from embeddings import(split_text,get_embedding_model)
from vector_store import(create_vector_store,search_documents)
from pdf_loader import extract_text_from_pdf
from dotenv import load_dotenv
import os

load_dotenv()

#Embedding Model
embedding_model = get_embedding_model()

#LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

# Global vector store
vector_store = None

#Process PDF
def process_pdf(pdf_file):
    global vector_store

    #step 1:Extract text
    text = extract_text_from_pdf(pdf_file)

    if not text.strip():
        raise ValueError("Could not extract text from PDF.")

    #Step 2:
    chunks = split_text(text)

    #Step 3:
    vector_store = create_vector_store(chunks,embedding_model)

    return len(chunks)


#Ask Question
def ask_questions(question):

    if vector_store is None:
        raise ValueError(
            "Please upload and process a PDF first."
        )

    # ---------------------------------------
    # Retrieve relevant chunks
    # ---------------------------------------

    documents = search_documents(
        vector_store,
        question,
        k=4
    )

    # ---------------------------------------
    # Create context
    # ---------------------------------------

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # ---------------------------------------
    # Prompt
    # ---------------------------------------

    prompt = f"""
You are a document question-answering assistant.

Answer the question using ONLY the information
provided in the context.

If the answer cannot be found in the context,
say:

"I could not find the answer in the uploaded document."

Do not make up information.

Context:
------------------------
{context}
------------------------

Question:
{question}

Answer:
"""

    # ---------------------------------------
    # Call Gemini
    # ---------------------------------------

    response = llm.invoke(prompt)

    # ---------------------------------------
    # Extract answer
    # ---------------------------------------

    if isinstance(response.content, str):

        answer = response.content

    else:

        answer = ""

        for item in response.content:

            if isinstance(item, dict):

                if item.get("type") == "text":
                    answer += item.get("text", "")

            else:

                answer += str(item)

    # ---------------------------------------
    # IMPORTANT
    # ---------------------------------------

    return answer, documents
