import streamlit as st
from htbuilder import div
from htbuilder.units import rem
from htbuilder import styles
from services.api_client import review_code, get_response_text
from utils.helpers import format_response
from datetime import datetime

st.set_page_config(page_title="sensAI", page_icon="🧘‍♂️")

# -----------------------------------------------------------------------------
# Configuration

API_URL = "http://localhost:8000"
HISTORY_LENGTH = 5

SUGGESTIONS = {
    ":blue[:material/code:] Review my Python code": (
        "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)"
    ),
    ":green[:material/bug_report:] Find bugs in my code": (
        "How can I improve this code?"
    ),
    ":orange[:material/lightbulb:] Learn best practices": (
        "What are best practices for error handling?"
    ),
}

INSTRUCTIONS = """
You are a helpful AI coding sensei. You help students learn programming through Socratic questioning.

Key principles:
- Ask guiding questions rather than giving direct answers
- Help students discover solutions themselves
- Explain concepts clearly with examples
- Identify what's wrong and why, with clear reasoning
- Encourage good coding practices
- Be encouraging and supportive
- Adapt explanations to student level

Remember: Your goal is to help students become better programmers, not just fix their code.
"""

# -----------------------------------------------------------------------------
# Helper Functions

def history_to_text(chat_history):
    """Convert chat history into a string."""
    return "\n".join(f"[{h['role']}]: {h['content']}" for h in chat_history)

def build_prompt(question, recent_messages=None):
    """Build a prompt string with context."""
    prompt_parts = [f"<instructions>\n{INSTRUCTIONS}\n</instructions>"]
    
    if recent_messages:
        prompt_parts.append(f"<recent_messages>\n{recent_messages}\n</recent_messages>")
    
    prompt_parts.append(f"<question>\n{question}\n</question>")
    
    return "\n".join(prompt_parts)

# -----------------------------------------------------------------------------
# UI

st.html(div(style=styles(font_size=rem(4), line_height=1))["❉"])

title_row = st.container(horizontal=True, vertical_alignment="bottom")

with title_row:
    st.title("sensAI - Your AI Coding Sensei", anchor=False, width="stretch")

user_just_asked_initial_question = (
    "initial_question" in st.session_state and st.session_state.initial_question
)

user_just_clicked_suggestion = (
    "selected_suggestion" in st.session_state and st.session_state.selected_suggestion
)

user_first_interaction = (
    user_just_asked_initial_question or user_just_clicked_suggestion
)

has_message_history = (
    "messages" in st.session_state and len(st.session_state.messages) > 0
)

# Show initial UI when user hasn't asked a question yet
if not user_first_interaction and not has_message_history:
    st.session_state.messages = []
    
    with st.container():
        st.chat_input("Ask a question about your code...", key="initial_question")
        st.pills(
            label="Examples",
            label_visibility="collapsed",
            options=list(SUGGESTIONS.keys()),
            key="selected_suggestion",
        )
    
    st.stop()

# Show chat input at the bottom when a question has been asked
user_message = st.chat_input("Ask a follow-up...")

if not user_message:
    if user_just_asked_initial_question:
        user_message = st.session_state.initial_question
    if user_just_clicked_suggestion:
        user_message = SUGGESTIONS[st.session_state.selected_suggestion]

with title_row:
    def clear_conversation():
        st.session_state.messages = []
        st.session_state.initial_question = None
        st.session_state.selected_suggestion = None
    
    st.button(
        "Restart",
        icon=":material/refresh:",
        on_click=clear_conversation,
    )

# Display chat messages from history
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            st.container()  # Fix ghost message bug
        
        st.markdown(message["content"])

if user_message:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_message)
    
    # Display assistant response
    with st.chat_message("assistant"):
        with st.container():
            # Get recent history
            recent_messages = None
            if len(st.session_state.messages) >= 2:
                recent_messages = history_to_text(st.session_state.messages[-HISTORY_LENGTH:])
            
            with st.spinner("Analyzing your code..."):
                # Build prompt
                full_prompt = build_prompt(user_message, recent_messages)
                
                # Get response from API
                try:
                    response = review_code(user_message, "python", None, API_URL)
                    
                    if response and response.status_code == 200:
                        response_text = get_response_text(response)
                        formatted_text = format_response(response_text)
                        
                        st.markdown(formatted_text)
                        
                        # Add to history
                        st.session_state.messages.append({"role": "user", "content": user_message})
                        st.session_state.messages.append({"role": "assistant", "content": formatted_text})
                    else:
                        st.error("❌ Failed to get response from API. Make sure the backend is running.")
                        st.session_state.messages.append({"role": "user", "content": user_message})
                        st.session_state.messages.append({"role": "assistant", "content": "I apologize, but I'm having trouble connecting to the backend service. Please make sure the backend is running."})
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.session_state.messages.append({"role": "user", "content": user_message})
                    st.session_state.messages.append({"role": "assistant", "content": f"I encountered an error: {str(e)}. Please check the backend connection."})