"""
🚀 Home Remedies AI – TinyLlama + LangChain (LM Studio)
FastAPI Web Application
"""

import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Set LM Studio configuration BEFORE imports
os.environ["OPENAI_API_BASE"] = "http://127.0.0.1:1234/v1"
os.environ["OPENAI_API_KEY"] = "lm-studio"

# ✅ Import the main QA system
from qa_engine import HomeRemedyQA

# =====================================================
# Initialize FastAPI
# =====================================================
app = FastAPI(
    title="Home Remedies AI - TinyLlama (LM Studio)",
    description="Ask questions about natural home remedies using TinyLlama and LangChain",
    version="1.0.0"
)

# Load Jinja2 HTML templates
templates = Jinja2Templates(directory="templates")

# =====================================================
# Initialize QA System (runs once at startup)
# =====================================================
print("📘 Initializing Home Remedies QA System...")

qa_system = None

try:
    qa_system = HomeRemedyQA(
        pdf_path="Basic_Home_Remedies.pdf",
        use_cache=False  # Set to True after first run to use cached vectors
    )
    print("✅ Home Remedies QA system ready!")
except Exception as e:
    print(f"❌ Error during initialization: {e}")
    import traceback
    traceback.print_exc()

# =====================================================
# Routes
# =====================================================
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Display home page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask", response_class=HTMLResponse)
async def ask_question(request: Request, question: str = Form(...)):
    """Handle user question and return AI-generated answer"""
    if qa_system is None:
        answer = "⚠️ The model is still initializing or failed to load. Please try again later."
    else:
        try:
            result = qa_system.ask(question)
            answer = result["answer"]
        except Exception as e:
            answer = f"❌ Error: {str(e)}"
            import traceback
            traceback.print_exc()
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "question": question,
        "answer": answer
    })

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy" if qa_system is not None else "initializing",
        "message": "QA system ready" if qa_system else "QA system not ready"
    }

# =====================================================
# Entry point (if run directly)
# =====================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)