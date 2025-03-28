import argparse
from modules.data_fetch import fetch_arxiv_papers
from modules.dashboard import launch_dashboard

def main():
    print("📚 Welcome to the AI Gen and RAG Bibliographic Review Assistant!")

    # Interaction to choose the topic
    topic = input("📝 Enter the topic you want to search for: ").strip()
    
    # Interaction to choose the method
    print("\nChoose the summarization method:")
    print("1 - BART (local)")
    print("2 - OpenAI GPT (API)")
    method_choice = input("Enter the number of your choice: ").strip()
    
    # Choice verification
    if method_choice == "1":
        from modules.text_summarization import summarize_text
        print("🔍 Using the summarization method: BART (local)")
    elif method_choice == "2":
        from modules.text_summarization_openai import summarize_text
        print("🔍 Using the summarization method: OpenAI GPT (API)")
    else:
        print("❌ Invalid choice! Using BART (local) by default.")
        from modules.text_summarization import summarize_text

    print(f"\n🔍 Searching for articles about: {topic}...")
    papers = fetch_arxiv_papers(topic)
    print(f"✅ {len(papers)} articles found.")

    print("📝 Generating abstracts...")
    summaries = [summarize_text(paper['abstract']) for paper in papers]
    
    print("📊 Launching dashboard...")
    launch_dashboard(papers, summaries)

if __name__ == "__main__":
    main()
