def fetch_issue_details(repo_url, issue_number):
    import requests

    if not repo_url.startswith("https://github.com/"):
        raise ValueError("Invalid GitHub repo URL")

    parts = repo_url.strip().split("/")
    if len(parts) < 5:
        raise ValueError("GitHub URL must be in format https://github.com/owner/repo")

    owner, repo = parts[3], parts[4]

    issue_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    comments_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"

    headers = {"Accept": "application/vnd.github.v3+json"}

    issue_response = requests.get(issue_url, headers=headers)
    if issue_response.status_code != 200:
        raise ValueError(f"Issue not found: {issue_response.status_code} - {issue_response.text}")

    issue_data = issue_response.json()
    title = issue_data.get("title", "")
    body = issue_data.get("body", "")

    comments_response = requests.get(comments_url, headers=headers)
    comments_data = comments_response.json() if comments_response.status_code == 200 else []

    comments = [comment["body"] for comment in comments_data]

    return title, body, comments
