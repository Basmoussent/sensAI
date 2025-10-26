import streamlit as st
from htbuilder import div, styles
from htbuilder.units import rem

def render_page_header(title, icon="🧘‍♂️"):
    """Render a modern page header with gradient background."""
    st.markdown(f"""
        <style>
        .page-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            text-align: center;
            color: white;
        }}
        .page-header h1 {{
            color: white;
            margin: 0;
            font-size: 3rem;
        }}
        .page-header p {{
            color: rgba(255, 255, 255, 0.9);
            margin: 0.5rem 0 0 0;
        }}
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="page-header">
            <h1>{icon} {title}</h1>
        </div>
    """, unsafe_allow_html=True)

def render_decorative_divider():
    """Render a decorative divider."""
    st.html(div(style=styles(font_size=rem(4), line_height=1))["❉"])

def create_title_row(title_text, button_label="Restart", button_icon=":material/refresh:", on_click=None):
    """Create a title row with optional button."""
    title_row = st.container(horizontal=True, vertical_alignment="bottom")
    
    with title_row:
        st.title(title_text, anchor=False, width="stretch")
        
        if on_click:
            st.button(
                button_label,
                icon=button_icon,
                on_click=on_click,
            )
    
    return title_row

def show_suggestions_pills(suggestions_dict, key="selected_suggestion"):
    """Show clickable suggestion pills."""
    return st.pills(
        label="Examples",
        label_visibility="collapsed",
        options=list(suggestions_dict.keys()),
        key=key,
    )

def create_chat_input(placeholder="Ask a question...", key="chat_input"):
    """Create a chat input with consistent styling."""
    return st.chat_input(placeholder, key=key)

def show_feedback_controls(message_index):
    """Show feedback controls for assistant messages."""
    with st.popover("How did I do?"):
        with st.form(key=f"feedback-{message_index}", border=False):
            rating = st.feedback(options="stars")
            details = st.text_area("More information (optional)")
            
            if st.form_submit_button("Send feedback"):
                st.toast("Thanks for your feedback!", icon="✅")
                # TODO: Implement feedback submission

def render_status_with_spinner(label, container=None):
    """Render a status with spinner."""
    if container:
        return st.status(label)
    else:
        return st.spinner(label)

def clear_messages():
    """Clear conversation messages."""
    st.session_state.messages = []
    st.session_state.initial_question = None
    st.session_state.selected_suggestion = None

