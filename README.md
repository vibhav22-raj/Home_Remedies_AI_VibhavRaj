# Home_Remedies_AI_VibhavRaj

# 🏠 Home Remedies AI — TinyLlama + LangChain (FastAPI Dashboard)

A **FastAPI-powered AI web application** that answers questions about **natural home remedies** using the **TinyLlama** model through **LM Studio** and **LangChain**.  
This project connects a **local LLM (TinyLlama in LM Studio)** to a **custom FastAPI dashboard**, creating a seamless local AI experience 💡.

---

# 🏠 Home Remedies AI — TinyLlama + LangChain (FastAPI Dashboard)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Enabled-8A2BE2?logo=chainlink)](https://www.langchain.com/)
[![LM Studio](https://img.shields.io/badge/LM%20Studio-TinyLlama-orange?logo=openai)](https://lmstudio.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellowgreen.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](#)
[![Bootstrap](https://img.shields.io/badge/UI-Bootstrap%205-blueviolet?logo=bootstrap)](https://getbootstrap.com/)
[![Chart.js](https://img.shields.io/badge/Charts-Chart.js-red?logo=chartdotjs)](https://www.chartjs.org/)


## 🌟 Features

### 💬 Ask About Any Home Remedy
- Example: _“How can I cure cold naturally?”_ 🌿  
- Uses **TinyLlama** through **LM Studio** to generate accurate, context-based answers.
- References your own **PDF knowledge base** (`Basic_Home_Remedies.pdf`).

### 📊 Professional Dashboard
- 🔐 **Admin login** with access token  
- 📈 **Live metrics** (total questions, errors, response time)  
- 🗂️ **Recent queries table**  
- 🔄 Clear logs and reload system cache

### 🧠 Intelligent Backend
- Uses **LangChain** to manage retrieval + generation.
- Embeds your PDF into a **vector store (FAISS)** for fast context-based retrieval.
- Works fully **offline** after LM Studio setup.

---

## 🧩 Project Structure

Home_Remedies_AI/
│
├── app.py # Main FastAPI app (Frontend + Dashboard)
├── main.py # Optional runner (if needed)
├── Basic_Home_Remedies.pdf # Knowledge base used for QA
├── requirements.txt # Dependencies list
├── README.md # Project documentation
│
├── qa_engine/ # Core AI logic (LangChain + LM Studio)
│ ├── init.py
│ ├── pdf_loader.py # Loads and splits PDF text
│ ├── vector_store.py # Embedding + FAISS vector DB
│ └── qa.py / qa_core.py # Main Q&A pipeline
│
├── models/ # (Optional) model cache or embedding store
│
├── static/ # Frontend static assets
│ ├── style.css
│ └── dashboard.js
│
├── templates/ # Frontend pages
│ ├── index.html # User interface
│ ├── result.html # AI answer page
│ └── dashboard.html # Admin dashboard
│
├── venv/ # Python virtual environment (ignored by git)
└── pycache/ # Cached files (ignored)

markdown
Copy code

---

## 🧠 LM Studio Configuration & Setup

You’ve already set up **LM Studio**, and that’s the key engine behind this project.  
Here’s what you did (and others should do) to make it work:

### ⚙️ Steps You Did in LM Studio

1. **Installed LM Studio** — from [https://lmstudio.ai](https://lmstudio.ai)  
2. **Downloaded the TinyLlama Model**  
   - Example: `TinyLlama-1.1B-Chat-v1.0` or any compatible instruction-tuned model  
   - Loaded it in LM Studio’s local model runner.  
3. **Started the Local Server (API Mode)**  
   - Open LM Studio → Go to the **Server** tab  
   - Enabled **Local Inference Server**  
   - Confirm it runs on → `http://127.0.0.1:1234/v1`  
4. **Verified it works**  
   - Open a browser and visit: [http://127.0.0.1:1234/v1/models](http://127.0.0.1:1234/v1/models)  
   - It should show your model name like `TinyLlama-1.1B-Chat`.

✅ **This FastAPI project automatically connects to that LM Studio endpoint** using:
```python
os.environ["OPENAI_API_BASE"] = "http://127.0.0.1:1234/v1"
os.environ["OPENAI_API_KEY"] = "lm-studio"


🖥️ **How the System Works (Flow Diagram)**

sql
Copy code
          +---------------------------+
          |  Basic_Home_Remedies.pdf  |
          +-------------+-------------+
                        |
                        v
                [LangChain Loader]
                        |
                        v
                 [Vector Store - FAISS]
                        |
                        v
       +-------------------------------------+
       |   User Asks Question via Web App    |
       +-------------------------------------+
                        |
                        v
         [LangChain Retriever + TinyLlama]
                        |
                        v
           💡 AI Answer Displayed in UI



## ⚙️ Installation & Running the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Home_Remedies_AI.git
cd Home_Remedies_AI



### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate   # On macOS/Linux


### 3️⃣ Install Dependencies
pip install -r requirements.txt



### 4️⃣ Start LM Studio Server

**Make sure LM Studio is running locally on**
👉 http://127.0.0.1:1234

with the TinyLlama model loaded.



🧠 **Inside LM Studio:**

Open LM Studio

Go to the Models tab

Download and load TinyLlama-1.1B-Chat-v1.0

Start the Local Server

Confirm API live at http://127.0.0.1:1234/v1/models



### 5️⃣ Run the FastAPI App
uvicorn app:app --reload


Visit:
🌐 User Interface: http://127.0.0.1:8000

🧭 Admin Dashboard: http://127.0.0.1:8000/admin/dashboard

Default Admin Token: dev-token-please-change

🔑 ### Environment Variables
Variable	Description	Default
OPENAI_API_BASE	LM Studio endpoint	http://127.0.0.1:1234/v1
OPENAI_API_KEY	Fake API key for LM Studio	lm-studio
HOME_REMEDIES_ADMIN_TOKEN	Dashboard access token	dev-token-please-change


🧠### How It Works Internally

PDF Loading – The app reads Basic_Home_Remedies.pdf and extracts text.

Embedding Creation – LangChain converts each text chunk into numerical vectors.

Vector Search – When you ask a question, it finds the most relevant chunks.

TinyLlama Response – LM Studio (TinyLlama) generates a natural language answer.

Response Display – The answer and metadata appear in the frontend.



📊 ### API Endpoints
Endpoint	Method	Description
/	GET	Main user interface
/ask	POST	Ask a question via HTML form
/api/ask	POST	API endpoint for JSON queries
/health	GET	Health check
/admin/dashboard	GET	Dashboard page
/admin/api/metrics	GET	Metrics API
/admin/api/clear-history	POST	Clear logs


🧰 ### Troubleshooting
Problem	Possible Solution
❌ QA system not ready	Start LM Studio with TinyLlama loaded
⚠️ ModuleNotFoundError: qa_engine	Check folder structure & __init__.py
🔒 Dashboard unauthorized	Use correct admin token
🖼️ Static/Template not loading	Verify paths to static/ & templates/
🧑‍💻 Tech Stack
Layer	Technology
Frontend	HTML + CSS + JS + Jinja2
Backend	FastAPI
AI Engine	TinyLlama (via LM Studio)
Framework	LangChain
Storage	FAISS (Vector Store)
Charts	Chart.js
UI Styling	Bootstrap 5


📸 Preview


🏠 User Interface


📊 Admin Dashboard

🚀 Future Enhancements

🔄 Live answer streaming via WebSocket

💾 Persistent metrics with SQLite

🧭 Multi-PDF knowledge base

🌙 Dark mode for dashboard

🤖 Support for other local models in LM Studio

🧭 Multi-PDF knowledge base

🌙 Dark mode for dashboard

🤖 Support for other local models in LM Studio
