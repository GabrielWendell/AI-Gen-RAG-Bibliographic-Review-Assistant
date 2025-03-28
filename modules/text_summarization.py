from transformers import pipeline

# Initializes the summarization pipeline
summarizer = pipeline("summarization", model = "facebook/bart-large-cnn")

def summarize_text(text):
    try:
        # Generate the summary using BART
        summary = summarizer(text, max_length = 700, min_length = 300, do_sample = False)[0]['summary_text']
        return summary
    except Exception as e:
        print(f"Error generating abstract: {e}")
        return "Abstract unavailable."