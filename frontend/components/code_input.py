import streamlit as st

def language_selector():
    """Language selector with icons."""
    languages = {
        "python": "🐍 Python",
        "javascript": "🟨 JavaScript",
        "typescript": "📘 TypeScript",
        "java": "☕ Java",
        "cpp": "⚙️ C++",
        "go": "🐹 Go",
        "rust": "🦀 Rust",
        "unknown": "❓ Unknown"
    }
    
    language_values = list(languages.keys())
    language_options = list(languages.values())
    
    selected = st.selectbox(
        "Select Language",
        options=language_options,
        key="language_selector"
    )
    
    return language_values[language_options.index(selected)]