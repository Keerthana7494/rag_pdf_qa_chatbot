import streamlit as st

from rag import(process_pdf,ask_questions)

# Page configuration
st.set_page_config(
    page_title="PDF RAG Chatbot",
    layout="centered"
)

#Title
st.title("📄 Chat with Your PDF")
st.write("Upload a pdf and ask questions using Retrieval-Augumented Generation.")

#Upload PDF
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

#Process PDF
if uploaded_file:
    st.info(f"Selected file:{uploaded_file}")

    if st.button("Process PDF"):
        with st.spinner("Processing PDF..."):
            try:
                chunk_count = process_pdf(uploaded_file)
                st.session_state["pdf_processed"]=True
                st.success(f"PDF processed successfully!")
                st.write(f"Created {chunk_count} text chunks.")

            except Exception as e:
                st.error(f"Error:{e}")

 #Question
st.divider()
st.subheader("Ask a Question")
question = st.text_input("Enter your question")

#Ask
if st.button("Ask Question"):
    if not uploaded_file:
        st.warning("Please upload a pdf first.")
    elif not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching document..."):

            try:
                answer,documents = ask_questions(question)

                #Answer
                st.subheader("Answer")
                st.write(answer)    

                #Retrived context
                with st.expander(" View Retrieved Chunks"):

                    for index,document in enumerate(
                        documents, start = 1
                    ):

                        st.markdown(f"### Chunk {index}")
                        st.write(document.page_content)

            except Exception as e:
                st.error(f"Error: {e}")        


               



