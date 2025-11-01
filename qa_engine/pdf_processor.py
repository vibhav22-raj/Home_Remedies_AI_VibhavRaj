"""
PDF Processor Module
Handles PDF loading and chunking
"""

from langchain_community.document_loaders import PDFPlumberLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings


class PDFProcessor:
    """Process PDF documents for the QA system"""
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.embeddings = None
        self.documents = None
    
    def process(self):
        """Load and split PDF into semantic chunks"""
        print("📄 Loading PDF...")
        loader = PDFPlumberLoader(self.pdf_path)
        docs = loader.load()
        print(f"✅ {len(docs)} pages loaded")

        # Initialize embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        # Split into semantic chunks
        splitter = SemanticChunker(self.embeddings)
        self.documents = splitter.split_documents(docs)
        print(f"🧩 Split into {len(self.documents)} chunks")
        
        return self.documents, self.embeddings


# Legacy function for backward compatibility
def load_pdf(pdf_path: str):
    """Load and split PDF into semantic chunks (legacy function)"""
    processor = PDFProcessor(pdf_path)
    documents, embeddings = processor.process()
    return documents