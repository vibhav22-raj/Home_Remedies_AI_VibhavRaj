"""
QA Chain Module
Handles the question-answering chain with TinyLlama
"""

import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain


class QAChainManager:
    """Manages the QA chain with TinyLlama"""
    
    def __init__(self, model_name="tinyllama-1.1b-chat-v1.0"):
        self.model_name = model_name
        self.llm = None
        self.qa_chain = None
    
    def _initialize_llm(self):
        """Initialize the ChatOpenAI LLM (LM Studio connection)"""
        print(f"🤖 Loading {self.model_name}...")
        
        self.llm = ChatOpenAI(
            model=self.model_name,
            temperature=0.7,
            openai_api_base=os.environ.get("OPENAI_API_BASE", "http://127.0.0.1:1234/v1"),
            openai_api_key=os.environ.get("OPENAI_API_KEY", "lm-studio"),
            request_timeout=60,
            verbose=True
        )
        print("✅ LLM loaded")
    
    def create_qa_chain(self, retriever):
        """Create Retrieval-QA chain using TinyLlama via LM Studio"""
        if not self.llm:
            self._initialize_llm()
        
        print("🔗 Building QA chain...")
        
        # Define the prompt template
        prompt_template = """You are a domain expert assistant.
Use the provided context to answer accurately in 3–4 sentences.
If the answer is not found, say: "The information is not available in the provided context."

Context:
{context}

Question:
{question}

Answer:"""
        
        qa_prompt = PromptTemplate.from_template(prompt_template)
        llm_chain = LLMChain(llm=self.llm, prompt=qa_prompt, verbose=True)

        doc_prompt = PromptTemplate(
            input_variables=["page_content", "source"],
            template="Context:\n{page_content}\nSource: {source}"
        )

        combine_chain = StuffDocumentsChain(
            llm_chain=llm_chain,
            document_variable_name="context",
            document_prompt=doc_prompt
        )

        self.qa_chain = RetrievalQA(
            combine_documents_chain=combine_chain,
            retriever=retriever,
            return_source_documents=True,
            verbose=True
        )
        
        print("✅ QA chain created")
        return self.qa_chain
    
    def ask(self, question):
        """
        Ask a question and get an answer
        
        Args:
            question (str): The question to ask
            
        Returns:
            dict: Contains 'question', 'answer', and 'source_documents'
        """
        if not self.qa_chain:
            raise ValueError("QA chain not created. Call create_qa_chain first.")
        
        print(f"\n❓ Question: {question}")
        result = self.qa_chain.invoke({"query": question})
        
        return {
            "question": question,
            "answer": result.get("result", "No answer generated"),
            "source_documents": result.get("source_documents", [])
        }


# Legacy function for backward compatibility
def build_qa_chain(retriever):
    """Create Retrieval-QA chain using TinyLlama via LM Studio (legacy function)"""
    manager = QAChainManager()
    return manager.create_qa_chain(retriever)