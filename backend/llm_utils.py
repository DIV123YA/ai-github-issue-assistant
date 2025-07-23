from transformers import pipeline

print("🔧 Loading summarization model...")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
print("✅ Model loaded.")

def analyze_github_issue(title: str, body: str) -> dict:
    combined = f"{title}. {body}"
    summary = summarizer(combined, max_length=60, min_length=15, do_sample=False)
    return {"response": summary[0]["summary_text"]}
