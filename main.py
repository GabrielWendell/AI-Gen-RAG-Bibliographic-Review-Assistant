import argparse
from modules.data_fetch import fetch_arxiv_papers
from modules.dashboard import launch_dashboard

def main():
    parser = argparse.ArgumentParser(description = "Choose the summarization method")
    parser.add_argument("--method", choices = ["bart", "openai"], default = "bart", help = "Summarization method (bart or openai)")
    args = parser.parse_args()

    print(f"\n🔍 Using the summarization method: {args.method}")

    if args.method == "bart":
        from modules.text_summarization import summarize_text
    elif args.method == "openai":
        from modules.text_summarization_openai import summarize_text

    print("\n🔍 Searching for articles...")
    papers = fetch_arxiv_papers("quantum computing")
    print(f"\n✅ {len(papers)} articles found.")

    print("📝 Generating summaries...")
    summaries = [summarize_text(paper['abstract']) for paper in papers]
    
    print("\n📊 Launching dashboard...")
    launch_dashboard(papers, summaries)

if __name__ == "__main__":
    main()