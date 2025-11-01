"""
Vector Store Module
Handles FAISS vector store creation and retrieval
"""

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


class VectorStoreManager:
    def __init__(self):
        self.vector_store = None
        self.retriever = None
    
    def create_vector_store(self, documents, embeddings):
        """Create FAISS vector store from documents"""
        print("🔄 Creating vector store...")
        self.vector_store = FAISS.from_documents(documents, embeddings)
        print("✅ Vector store created")
        return self.vector_store
    
    def get_retriever(self, search_type="similarity", k=3):
        """Get retriever from vector store"""
        if not self.vector_store:
            raise ValueError("Vector store not created. Call create_vector_store first.")
        
        self.retriever = self.vector_store.as_retriever(
            search_type=search_type,
            search_kwargs={"k": k}
        )
        print(f"✅ Retriever configured (search_type={search_type}, k={k})")
        return self.retriever
    
    def save_local(self, path="models/faiss_index"):
        """Save vector store locally"""
        if self.vector_store:
            self.vector_store.save_local(path)
            print(f"✅ Vector store saved to {path}")
    
    def load_local(self, path="models/faiss_index", embeddings=None):
        """Load vector store from local path"""
        if embeddings is None:
            raise ValueError("Embeddings required to load vector store")
        
        print(f"🔄 Loading vector store from {path}...")
        self.vector_store = FAISS.load_local(
            path, 
            embeddings,
            allow_dangerous_deserialization=True
        )
        print("✅ Vector store loaded")
        return self.vector_store