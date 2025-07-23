from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import llm_utils  # Import your summarizer

app = FastAPI()

class AnalyzeRequest(BaseModel):
    issue_title: str
    issue_body: str

@app.post("/analyze")
def analyze_issue(req: AnalyzeRequest):
    try:
        response = llm_utils.analyze_github_issue(req.issue_title, req.issue_body)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
