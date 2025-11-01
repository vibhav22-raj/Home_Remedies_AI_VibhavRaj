"""
🤖 TinyLlama + LangChain PDF Q&A (Direct HuggingFace)
Home Remedies QA Engine - Main interface for the question-answering system
"""

from .pdf_processor import PDFProcessor
from .vector_store import VectorStoreManager
from .qa_chain import QAChainManager


class HomeRemedyQA:
    """
    🏠 Home Remedies AI powered by TinyLlama
    Complete QA system running directly via HuggingFace
    """
    def __init__(self, pdf_path="Basic_Home_Remedies.pdf", use_cache=False):
        self.pdf_path = pdf_path
        self.use_cache = use_cache
        
        # Initialize components
        self.pdf_processor = PDFProcessor(pdf_path)
        self.vector_manager = VectorStoreManager()
        self.qa_manager = QAChainManager(model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
        
        # Initialize the system
        self._initialize()
    
    def _initialize(self):
        """Initialize the complete QA system with TinyLlama"""
        print("\n" + "=" * 70)
        print("🤖 TinyLlama + LangChain PDF Q&A (Direct HuggingFace)")
        print("🏠 Initializing Home Remedies QA System")
        print("=" * 70)
        
        # Step 1: Process PDF
        documents, embeddings = self.pdf_processor.process()
        
        # Step 2: Create or load vector store
        if self.use_cache:
            try:
                self.vector_manager.load_local(embeddings=embeddings)
            except Exception as e:
                print(f"⚠️ Could not load cached vector store: {e}")
                print("Creating new vector store...")
                self.vector_manager.create_vector_store(documents, embeddings)
                self.vector_manager.save_local()
        else:
            self.vector_manager.create_vector_store(documents, embeddings)
        
        retriever = self.vector_manager.get_retriever()
        
        # Step 3: Load TinyLlama and create QA chain
        self.qa_manager.create_qa_chain(retriever)
        
        print("=" * 70)
        print("✅ System Ready! TinyLlama is loaded and ready to answer questions.")
        print("=" * 70 + "\n")
    
    def ask(self, question):
        """
        Ask a question and get an answer from TinyLlama
        
        Args:
            question (str): The question to ask
            
        Returns:
            dict: Contains 'question', 'answer', and 'source_documents'
        """
        return self.qa_manager.ask(question)
    
    def get_relevant_docs(self, question, k=3):
        """
        Get relevant documents for a question without generating an answer
        
        Args:
            question (str): The question
            k (int): Number of documents to retrieve
            
        Returns:
            list: List of relevant documents
        """
        retriever = self.vector_manager.get_retriever(k=k)
        return retriever.get_relevant_documents(question)


# Make it easy to import
__all__ = ['HomeRemedyQA', 'PDFProcessor', 'VectorStoreManager', 'QAChainManager']