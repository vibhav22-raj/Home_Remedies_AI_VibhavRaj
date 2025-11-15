# 🪴 Home Remedies AI - TinyLlama PDF Q&A System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-orange.svg)](https://langchain.com/)
[![TinyLlama](https://img.shields.io/badge/TinyLlama-1.1B-purple.svg)](https://huggingface.co/TinyLlama)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent **AI-powered Question-Answering system** that extracts knowledge from PDF documents using **TinyLlama** language model and **LangChain** framework. Get instant answers about home remedies from your PDF knowledge base!

> 🤖 **Powered by TinyLlama 1.1B** - A compact yet powerful language model running locally via LM Studio
> 
> 📚 **RAG Architecture** - Retrieval-Augmented Generation for accurate, context-aware answers

---

## 🌟 Features

### 🧠 AI-Powered Intelligence
- **TinyLlama Language Model** - Efficient 1.1B parameter model
- **LM Studio Integration** - Run LLM locally without cloud APIs
- **Retrieval-Augmented Generation (RAG)** - Combines retrieval with generation
- **Semantic Search** - Find relevant information intelligently
- **Context-Aware Answers** - Answers grounded in your PDF content

### 📄 PDF Processing
- **Automatic PDF Loading** - Process any PDF document
- **Semantic Chunking** - Intelligent document splitting
- **Vector Embeddings** - HuggingFace sentence transformers
- **FAISS Vector Store** - Fast similarity search
- **Persistent Storage** - Cache vector store for faster loading

### 🎨 Web Interface
- **FastAPI Backend** - High-performance async framework
- **Clean UI** - Simple, intuitive question-answering interface
- **Real-time Processing** - Instant answer generation
- **Source Citations** - View source documents used

### 🔧 Modular Architecture
- **Separated Components** - PDF processor, vector store, QA chain
- **Easy Configuration** - Customize model and parameters
- **Extensible Design** - Add new features easily
- **Caching Support** - Optional vector store persistence

---

## 📸 Screenshots

### Home Page
*Ask your health and home remedy questions*

### Results Page
*Get AI-powered answers with context*

---

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Usage Guide](#-usage-guide)
- [Architecture](#-architecture)
- [API Endpoints](#-api-endpoints)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Quick Start

### 📋 Prerequisites

Before you begin, ensure you have:

- ✅ **Python 3.8+** installed
- ✅ **pip** package manager
- ✅ **LM Studio** installed and running ([Download here](https://lmstudio.ai/))
- ✅ **TinyLlama model** loaded in LM Studio
- ✅ **Git** for cloning the repository
- ✅ **PDF document** (Basic_Home_Remedies.pdf or your own)

---

## ⚡ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Home_Remedies_AI_VibhavRaj.git
cd Home_Remedies_AI_VibhavRaj
```

### 2️⃣ Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Core Dependencies:**
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `langchain` - LLM framework
- `langchain-community` - Community integrations
- `langchain-openai` - OpenAI-compatible API
- `sentence-transformers` - Embeddings
- `faiss-cpu` - Vector database
- `pdfplumber` - PDF processing
- `jinja2` - Template engine

### 4️⃣ Setup LM Studio

1. **Download and Install** [LM Studio](https://lmstudio.ai/)
2. **Load TinyLlama Model:**
   - Open LM Studio
   - Search for "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
   - Download the model
   - Load the model in the server
3. **Start Local Server:**
   - Go to "Local Server" tab
   - Click "Start Server"
   - Default: `http://127.0.0.1:1234/v1`

### 5️⃣ Add Your PDF Document

Place your PDF file in the root directory:
```bash
# Use provided file or add your own
Basic_Home_Remedies.pdf
```

### 6️⃣ Run the Application

**Option A: FastAPI Web Interface**
```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

**Option B: Command Line Interface**
```bash
python main.py
```

### 7️⃣ Access the Application

**Web Interface:** Navigate to `http://127.0.0.1:8000`

**CLI:** Follow the prompts in your terminal

🎉 **Start asking questions about home remedies!**

---

## 📁 Project Structure

```
Home_Remedies_AI_VibhavRaj/
│
├── app.py                              # FastAPI web application
├── main.py                             # CLI interface
├── Basic_Home_Remedies.pdf             # Knowledge base PDF
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
├── .gitattributes                      # Git attributes
│
├── qa_engine/                          # Core QA engine modules
│   ├── __init__.py                     # Main QA system interface
│   ├── pdf_processor.py                # PDF loading and chunking
│   ├── vector_store.py                 # FAISS vector store manager
│   └── qa_chain.py                     # LangChain QA chain
│
├── templates/                          # HTML templates
│   ├── index.html                      # Home page (question form)
│   └── result.html                     # Answer display page
│
├── static/                             # Static assets
│   └── style.css                       # Custom styling
│
├── models/                             # Cached models (auto-generated)
│   └── faiss_index/                    # Persistent vector store
│
├── venv/                               # Virtual environment (gitignored)
└── __pycache__/                        # Python cache (gitignored)
```

---

## 💻 Usage Guide

### 🌐 Web Interface Usage

#### 🔹 Step 1: Start the Server

```bash
# Make sure LM Studio is running first!
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

#### 🔹 Step 2: Ask a Question

1. Open browser to `http://127.0.0.1:8000`
2. You'll see the **Home Remedies AI** interface
3. Type your question in the input box
4. Click "Ask" button

**Example Questions:**
- "What are natural remedies for headache?"
- "How to treat cold naturally?"
- "What herbs help with digestion?"
- "Natural remedies for sleep problems?"

#### 🔹 Step 3: View the Answer

- AI processes your question
- Retrieves relevant context from PDF
- Generates answer using TinyLlama
- Displays answer on results page
- Click "Ask another question" to continue

### 🖥️ Command Line Usage

```bash
python main.py
```

**Interactive CLI:**
```
🤖 TinyLlama + LangChain PDF Q&A (Direct HuggingFace)
🏠 Initializing Home Remedies QA System
====================================================================
📄 Loading PDF...
✅ 50 pages loaded
🧩 Split into 120 chunks
📊 Creating vector store...
✅ Vector store created
🤖 Loading tinyllama-1.1b-chat-v1.0...
✅ LLM loaded
🔗 Building QA chain...
✅ QA chain created
====================================================================
✅ System Ready! TinyLlama is loaded and ready to answer questions.
====================================================================

❓ Question: What helps with fever?

🧠 Answer: Natural remedies for fever include drinking plenty of fluids, 
resting adequately, and using cool compresses. Herbal teas like ginger 
or chamomile can also help reduce temperature naturally.
```

---

## 🏗️ Architecture

### 📐 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      User Interface                          │
│              (FastAPI Web App / CLI)                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   HomeRemedyQA System                        │
│              (qa_engine/__init__.py)                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
┌──────────────┐ ┌──────────┐ ┌─────────────┐
│ PDFProcessor │ │  Vector  │ │ QAChain     │
│              │ │  Store   │ │ Manager     │
│ - Load PDF   │ │ - FAISS  │ │ - TinyLlama │
│ - Chunk Text │ │ - Search │ │ - Prompt    │
│ - Embeddings │ │ - Cache  │ │ - Generate  │
└──────────────┘ └──────────┘ └─────────────┘
        │              │              │
        └──────────────┴──────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  LM Studio      │
              │  (TinyLlama)    │
              │  Local Server   │
              └─────────────────┘
```

### 🔄 RAG Pipeline

```
1. Question Input
         ↓
2. Embedding Generation (HuggingFace)
         ↓
3. Semantic Search (FAISS)
         ↓
4. Context Retrieval (Top K Documents)
         ↓
5. Prompt Construction (Question + Context)
         ↓
6. LLM Generation (TinyLlama via LM Studio)
         ↓
7. Answer Output (With Source Citations)
```

### 🧩 Component Details

#### 📄 **PDFProcessor** (`pdf_processor.py`)
- Loads PDF using PDFPlumber
- Extracts text content
- Creates semantic chunks using SemanticChunker
- Generates embeddings with HuggingFace transformers

#### 🗄️ **VectorStoreManager** (`vector_store.py`)
- Creates FAISS vector index
- Stores document embeddings
- Performs similarity search
- Supports persistence (save/load)

#### 🤖 **QAChainManager** (`qa_chain.py`)
- Connects to LM Studio API
- Creates LangChain RetrievalQA chain
- Manages prompts and generation
- Returns answers with sources

#### 🏠 **HomeRemedyQA** (`__init__.py`)
- Orchestrates all components
- Provides simple API interface
- Handles initialization
- Manages caching

---

## 🔌 API Endpoints

### Web Application Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Main page (index.html) |
| `POST` | `/ask` | Process question and generate answer |
| `GET` | `/result` | Display answer (result.html) |

### Request Examples

**Ask a Question:**
```bash
curl -X POST "http://127.0.0.1:8000/ask" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "question=What helps with headache?"
```

**Response Format:**
The result is rendered in `result.html` with:
```html
Question: {{ question }}
Answer: {{ answer }}
```

---

## ⚙️ Configuration

### 🔧 Environment Variables

Create a `.env` file (optional):

```env
# LM Studio Configuration
OPENAI_API_BASE=http://127.0.0.1:1234/v1
OPENAI_API_KEY=lm-studio

# Model Settings
MODEL_NAME=tinyllama-1.1b-chat-v1.0
TEMPERATURE=0.7
REQUEST_TIMEOUT=60

# Embedding Settings
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Vector Store Settings
VECTOR_STORE_PATH=models/faiss_index
USE_CACHE=True

# Retrieval Settings
SEARCH_TYPE=similarity
TOP_K_RESULTS=3
```

### 🛠️ Customizing the QA Engine

Edit `qa_engine/__init__.py`:

```python
# Initialize with custom settings
qa_system = HomeRemedyQA(
    pdf_path="your_document.pdf",
    use_cache=True  # Enable vector store caching
)

# Get relevant documents without asking
docs = qa_system.get_relevant_docs("your question", k=5)
```

Edit `qa_engine/qa_chain.py`:

```python
# Customize prompt template
prompt_template = """You are a helpful assistant.
Use the context below to answer the question.

Context:
{context}

Question:
{question}

Answer in a friendly, conversational tone:"""
```

### 📊 PDF Processing Settings

Edit `qa_engine/pdf_processor.py`:

```python
# Change embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"  # More powerful
)

# Adjust chunk size
splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_amount=0.5  # Controls chunk boundaries
)
```

### 🗄️ Vector Store Configuration

Edit `qa_engine/vector_store.py`:

```python
# Adjust retrieval parameters
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 5,  # Return top 5 results
        "fetch_k": 20,  # Fetch 20 candidates first
        "score_threshold": 0.7  # Minimum similarity score
    }
)
```

---

## 🐛 Troubleshooting

### ❌ Common Issues & Solutions

**Issue 1: LM Studio Connection Error**
```bash
# Error: "Connection refused to http://127.0.0.1:1234/v1"
# Solution:
1. Open LM Studio
2. Load TinyLlama model
3. Go to "Local Server" tab
4. Click "Start Server"
5. Verify server is running at http://127.0.0.1:1234
```

**Issue 2: Module Not Found**
```bash
# Error: "ModuleNotFoundError: No module named 'langchain'"
# Solution:
pip install -r requirements.txt --upgrade
pip install langchain langchain-community langchain-openai
```

**Issue 3: PDF Not Loading**
```bash
# Error: "FileNotFoundError: Basic_Home_Remedies.pdf"
# Solution:
# Ensure PDF is in root directory
ls Basic_Home_Remedies.pdf  # Check file exists

# Or specify custom path
qa_system = HomeRemedyQA(pdf_path="path/to/your/document.pdf")
```

**Issue 4: FAISS Installation Error (Windows)**
```bash
# For Windows users
pip install faiss-cpu
# If that fails, try:
conda install -c pytorch faiss-cpu
```

**Issue 5: Slow Response Times**
```bash
# Solution 1: Enable caching
qa_system = HomeRemedyQA(use_cache=True)

# Solution 2: Reduce retrieved documents
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# Solution 3: Use smaller embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

**Issue 6: Template Not Found**
```bash
# Error: "TemplateNotFound: index.html"
# Solution: Verify templates folder structure
templates/
├── index.html
└── result.html
```

**Issue 7: Out of Memory**
```bash
# Solution: Process PDF in smaller chunks
# Or use a smaller model in LM Studio
# Or reduce the number of retrieved documents
```

---

## 📦 Requirements

**Core Dependencies:**
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
langchain==0.1.0
langchain-community==0.0.10
langchain-openai==0.0.2
sentence-transformers==2.2.2
faiss-cpu==1.7.4
pdfplumber==0.10.3
jinja2==3.1.2
python-multipart==0.0.6
```

**Optional Dependencies:**
```txt
python-dotenv==1.0.0    # For environment variables
langchain-experimental==0.0.47  # For advanced features
```

---

## 🤝 Contributing

We welcome contributions to improve the Home Remedies AI system!

### 🔄 How to Contribute

1. **Fork** the repository
2. Create a **feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit** changes: `git commit -m "✨ Add: New feature"`
4. **Push** to branch: `git push origin feature/AmazingFeature`
5. Open a **Pull Request**

### 📝 Contribution Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions
- Include type hints where possible
- Write clear commit messages
- Update README for significant changes
- Test your changes thoroughly

### 🎯 Areas for Contribution

- [ ] Add support for multiple PDF documents
- [ ] Implement conversation history/memory
- [ ] Add source document highlighting
- [ ] Create API documentation (Swagger)
- [ ] Add unit tests
- [ ] Improve UI/UX design
- [ ] Add support for other document formats (DOCX, TXT)
- [ ] Implement streaming responses
- [ ] Add authentication system
- [ ] Create Docker containerization

---

## 🚀 Future Enhancements

### 🎯 Planned Features

#### 🧠 AI Improvements
- [ ] Support for larger language models (Llama 2, Mistral)
- [ ] Multi-turn conversation with memory
- [ ] Hybrid search (semantic + keyword)
- [ ] Query expansion and reformulation
- [ ] Answer confidence scoring

#### 📚 Document Processing
- [ ] Multi-document support
- [ ] Document upload via web interface
- [ ] Support for DOCX, TXT, HTML formats
- [ ] Automatic document categorization
- [ ] OCR for scanned PDFs

#### 🎨 User Interface
- [ ] Modern, responsive design
- [ ] Dark mode toggle
- [ ] Real-time typing animation
- [ ] Source document viewer
- [ ] Search history
- [ ] Bookmark favorite answers

#### 🔧 Technical Features
- [ ] REST API with authentication
- [ ] WebSocket for streaming responses
- [ ] Redis caching layer
- [ ] PostgreSQL for conversation history
- [ ] Docker deployment
- [ ] Kubernetes orchestration

#### 📊 Analytics
- [ ] Question analytics dashboard
- [ ] Most asked questions
- [ ] User feedback collection
- [ ] Answer quality metrics

---

## 👨‍💻 Author

**Vibhav Raj**  
🤖 AI/ML Engineer | 🏥 Healthcare Technology Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=social&logo=github)](https://github.com/vibhavraj)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=social&logo=linkedin)](https://linkedin.com/in/vibhavraj)


### 💼 About Me
- 🎓 Passionate about AI applications in healthcare
- 💻 Specializing in NLP and LLM applications
- 🌟 Building practical AI solutions for real-world problems
- 📚 Contributing to open-source AI projects

---

## 🙏 Acknowledgments

Special thanks to:

- **[LangChain](https://langchain.com/)** - For the powerful LLM framework
- **[TinyLlama Team](https://huggingface.co/TinyLlama)** - For the efficient language model
- **[LM Studio](https://lmstudio.ai/)** - For easy local LLM deployment
- **[HuggingFace](https://huggingface.co/)** - For embeddings and model hosting
- **[FastAPI Team](https://fastapi.tiangolo.com/)** - For the modern web framework
- **[FAISS](https://github.com/facebookresearch/faiss)** - For efficient similarity search
- **Open Source Community** - For tools and inspiration

---

## 📚 Resources & References

### 📖 Documentation
- [LangChain Documentation](https://python.langchain.com/)
- [TinyLlama Model Card](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FAISS Documentation](https://faiss.ai/)
- [LM Studio Guide](https://lmstudio.ai/docs)

### 🔬 Research Papers
- "TinyLlama: An Open-Source Small Language Model"
- "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
- "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"

### 🎓 Tutorials
- [Building a RAG System with LangChain](https://python.langchain.com/docs/use_cases/question_answering/)
- [FAISS Vector Database Tutorial](https://www.pinecone.io/learn/faiss/)
- [FastAPI for Beginners](https://fastapi.tiangolo.com/tutorial/)

---

## 📞 Support & Contact

### 🐛 Found a Bug?
Open an issue: [GitHub Issues](https://github.com/vibhavraj/Home_Remedies_AI_VibhavRaj/issues)

### 💬 Need Help?
- 📧 Email: vibhavraj@example.com
- 💬 Discord: [Join our AI community](#)
- 🐦 Twitter: [@vibhavraj](#)
- 💼 LinkedIn: [Vibhav Raj](#)

### 💰 Support the Project
If this project helped you:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://buymeacoffee.com/vibhavraj)
[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub-pink?style=for-the-badge&logo=github)](https://github.com/sponsors/vibhavraj)

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### 📄 MIT License Summary
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ❌ Liability
- ❌ Warranty

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/vibhavraj/Home_Remedies_AI_VibhavRaj?style=social)
![GitHub forks](https://img.shields.io/github/forks/vibhavraj/Home_Remedies_AI_VibhavRaj?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/vibhavraj/Home_Remedies_AI_VibhavRaj?style=social)
![GitHub issues](https://img.shields.io/github/issues/vibhavraj/Home_Remedies_AI_VibhavRaj)
![GitHub last commit](https://img.shields.io/github/last-commit/vibhavraj/Home_Remedies_AI_VibhavRaj)

---

## ⭐ Show Your Support

If you found this project useful, please consider:

1. ⭐ **Star** this repository
2. 🔀 **Fork** for your own experiments
3. 📢 **Share** with the AI community
4. 🐛 **Report** issues to help improve
5. 💡 **Contribute** new features

---

<div align="center">

### 🪴 Powered by AI | Built with ❤️ and Python

**Your Personal Health Assistant - Always Ready to Help** 🏥

[Documentation](#) | [Demo](#) | [Community](#) | [Blog](#)

---

*Bridging traditional wisdom with modern AI technology*

</div>
