import requests
import time

def fetch_arxiv_papers(query, max_retries = 3, retry_delay = 5):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"
    retries = 0

    while retries < max_retries:
        try:
            print(f"\n🕵️ Trying to fetch articles... (Attempt {retries + 1})")
            response = requests.get(url, timeout = 10)
            response.raise_for_status()
            entries = response.text.split("<entry>")
            papers = []

            for entry in entries[1:]:
                title = entry.split("<title>")[1].split("</title>")[0].strip()
                summary = entry.split("<summary>")[1].split("</summary>")[0].strip()
                papers.append({"title": title, "abstract": summary})

            return papers
        
        except (requests.ConnectionError, requests.Timeout) as e:
            print(f"\n⚠️ Connection error: {e}")
            retries += 1
            print(f"\n⏳ Waiting {retry_delay} seconds before trying again...")
            time.sleep(retry_delay)

        except requests.RequestException as e:
            print(f"\n❌ Error fetching articles: {e}")
            break

    print("\n🚫 Failed to get items after multiple attempts.")
    return []