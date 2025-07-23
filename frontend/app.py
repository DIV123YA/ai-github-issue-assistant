import streamlit as st
import requests

st.title("🧠 GitHub Issue Analyzer")

repo_url = st.text_input("GitHub Repository URL", "https://github.com/facebook/react")
issue_title = st.text_input("Issue Title", "Login error")
issue_body = st.text_area("Issue Body", "Clicking on the Google login button causes a 500 server error in production.")

if st.button("Analyze"):
    with st.spinner("Analyzing..."):
        try:
            res = requests.post("http://localhost:8000/analyze", json={
                "issue_title": issue_title,
                "issue_body": issue_body
            })
            res.raise_for_status()
            st.success("Analysis complete!")
            st.json(res.json())
        except requests.exceptions.RequestException as e:
            st.error(f"HTTP Error: {e}")
        except Exception as e:
            st.error(f"Unexpected Error: {e}")
