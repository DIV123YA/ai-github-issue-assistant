ai-github-issue-assistant/
│
├── main.py                 # FastAPI backend API for issue analysis
├── model.py                # Uses Hugging Face Transformers to summarize issues
├── utils.py                # Fetches issue data from GitHub
├── requirements.txt        # Python dependencies
├── frontend/
│   └── app.py              # Streamlit app UI


How It Works
Frontend (Streamlit): Takes GitHub repo URL and issue number from the user.

Backend (FastAPI):

Fetches the issue details (title, body, comments).

Uses a transformer model to generate a summary.

Model: A Hugging Face Transformer like distilbart-cnn is used for summarization.

1. Clone the Repository
git clone https://github.com/DIV123YA/ai-github-issue-assistant
cd ai-github-issue-assistant


3. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


5. Install Dependencies
pip install -r requirements.txt

1. Start the FastAPI Backend
uvicorn main:app --reload
This starts the backend at http://127.0.0.1:8000

2. Start the Streamlit Frontend
cd frontend
streamlit run app.py
This opens the frontend in your browser.
