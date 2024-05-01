from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader, CSVLoader, Docx2txtLoader
import pathlib

def load_documents(temp_dir):
    """
    Load documents from the specified temporary directory.
    Supports txt, pdf, CSV, and docx formats.
    """
    temp_dir = pathlib.Path(temp_dir)
    documents = []

    # Setup for different document types
    txt_loader = DirectoryLoader(temp_dir.as_posix(), glob="**/*.txt", loader_cls=TextLoader, show_progress=True)
    documents.extend(txt_loader.load())

    pdf_loader = DirectoryLoader(temp_dir.as_posix(), glob="**/*.pdf", loader_cls=PyPDFLoader, show_progress=True)
    documents.extend(pdf_loader.load())

    csv_loader = DirectoryLoader(temp_dir.as_posix(), glob="**/*.csv", loader_cls=CSVLoader, show_progress=True, loader_kwargs={"encoding": "utf8"})
    documents.extend(csv_loader.load())

    docx_loader = DirectoryLoader(temp_dir.as_posix(), glob="**/*.docx", loader_cls=Docx2txtLoader, show_progress=True)
    documents.extend(docx_loader.load())

    return documents

if __name__ == "__main__":
    # Example usage
    loaded_docs = load_documents("/Users/livlucas/rag-projects/rag-chatbot-langchain/temp-data")
    print(loaded_docs)
