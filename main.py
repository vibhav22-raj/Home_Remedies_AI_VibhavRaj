"""
🤖 TinyLlama + LangChain PDF Q&A (No LM Studio)
🏠 Home Remedies AI - Command Line Interface
"""

from qa_engine import HomeRemedyQA


def print_header():
    """Print a nice header"""
    print("\n" + "=" * 70)
    print("🤖 TinyLlama + LangChain PDF Q&A (No LM Studio)")
    print("🏠 HOME REMEDIES AI - COMMAND LINE INTERFACE")
    print("=" * 70)


def print_separator():
    """Print a separator line"""
    print("-" * 70)


def main():
    """Main CLI function"""
    print_header()
    
    # Initialize the QA system with TinyLlama
    print("\n⏳ Loading TinyLlama model and initializing system...")
    print("   (This may take a minute on first run...)")
    qa_system = HomeRemedyQA(use_cache=True)
    
    print("\n💬 Ask me anything about home remedies!")
    print("📝 Commands: 'exit', 'quit', or 'q' to stop")
    print_separator()
    
    # Example questions
    print("\n💡 Example questions you can ask:")
    print("   - What are home remedies for common cold?")
    print("   - How to treat a headache naturally?")
    print("   - What herbs are good for digestion?")
    print("   - Natural remedies for sore throat?")
    print_separator()
    
    question_count = 0
    
    while True:
        try:
            # Get user input
            question = input("\n❓ Your question: ").strip()
            
            # Check for exit commands
            if question.lower() in ['exit', 'quit', 'q']:
                print("\n" + "=" * 70)
                print(f"👋 Thank you for using Home Remedies AI!")
                print(f"📊 You asked {question_count} question(s) today.")
                print("=" * 70)
                break
            
            if not question:
                print("⚠️ Please enter a question.")
                continue
            
            # Get answer from TinyLlama
            print("\n🤔 TinyLlama is thinking...")
            result = qa_system.ask(question)
            question_count += 1
            
            # Display answer
            print("\n" + "=" * 70)
            print("💡 ANSWER FROM TINYLLAMA:")
            print_separator()
            print(result["answer"])
            print("=" * 70)
            
            # Show number of sources used
            num_sources = len(result.get("source_documents", []))
            print(f"\n📚 Answer based on {num_sources} source document(s)")
            
        except KeyboardInterrupt:
            print("\n\n" + "=" * 70)
            print("👋 Goodbye!")
            print(f"📊 You asked {question_count} question(s) today.")
            print("=" * 70)
            break
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try asking your question differently.\n")


if __name__ == "__main__":
    main()