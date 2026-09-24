
import faiss
from langchain_community.vectorstores import FAISS

def create_vector_store(chunks,embedding_model):

    vector_store = FAISS.from_texts(
        chunks,
        embedding_model
    )
    return vector_store


def search_documents(vector_store,question,k=4):

    documents = vector_store.similarity_search(question,k=k)

    return documents
    