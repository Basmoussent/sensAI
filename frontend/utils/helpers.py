import streamlit as st

def validate_code(code):
    if not code or not code.strip():
        return False, "Please enter some code to review"
    return True, None

def format_response(text):
    return text
