import requests
import streamlit as st

def review_code(code, language, question=None, api_url="http://localhost:8000"):
    try:
        response = requests.post(
            f"{api_url}/api/review",
            json={
                "code": code,
                "language": language,
                "question": question
            },
            stream=True,
            timeout=60
        )
        
        if response.status_code == 200:
            return response
        else:
            return None
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to API. Make sure the backend is running.")
        return None
    except requests.exceptions.Timeout:
        st.error("Request timed out. Please try again.")
        return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

def get_response_text(response):
    full_response = ""
    for line in response.iter_lines():
        if line:
            line_text = line.decode('utf-8')
            if line_text.startswith('data: '):
                data = line_text[6:]
                if data != '[DONE]' and data:
                    full_response += data
    return full_response
