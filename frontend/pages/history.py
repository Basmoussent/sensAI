import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="History - sensAI",
    page_icon="📜",
    layout="wide"
)

# Modern header
st.markdown("""
    <style>
    .history-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    .history-item {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="history-header"><h1>📜 History</h1><p>Your previous code reviews</p></div>', unsafe_allow_html=True)

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = []

# Search and Filter
col1, col2 = st.columns([2, 1])

with col1:
    search_term = st.text_input("🔍 Search history", placeholder="Search by language, question, or code...")

with col2:
    languages_filter = st.multiselect(
        "🌐 Filter by Language",
        options=["python", "javascript", "typescript", "java", "cpp", "go", "rust", "unknown"],
        default=[]
    )

# History Items
filtered_responses = st.session_state.responses

# Apply language filter
if languages_filter:
    filtered_responses = [r for r in filtered_responses if r.get('language') in languages_filter]

# Apply search filter
if search_term:
    search_term = search_term.lower()
    filtered_responses = [
        r for r in filtered_responses
        if search_term in r.get('code', '').lower()
        or search_term in r.get('question', '').lower()
        or search_term in r.get('language', '').lower()
    ]

# Display history
if filtered_responses:
    st.markdown(f"### Found {len(filtered_responses)} review(s)")
    
    for idx, review in enumerate(reversed(filtered_responses)):
        with st.container():
            st.markdown('<div class="history-item">', unsafe_allow_html=True)
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"#### Review #{len(filtered_responses) - idx} - {review['language'].upper()}")
                if review.get('question'):
                    st.info(f"💡 **Question:** {review['question']}")
            
            with col2:
                if review.get('timestamp'):
                    try:
                        dt = datetime.fromisoformat(review['timestamp'])
                        st.caption(f"📅 {dt.strftime('%Y-%m-%d %H:%M')}")
                    except:
                        pass
            
            # Code preview
            st.code(review['code'], language=review['language'])
            
            # Response
            with st.expander("🧘‍♂️ View Sensei's Response"):
                st.markdown(review['response'])
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")
            
elif st.session_state.responses:
    st.warning("🔍 No reviews match your search criteria")
else:
    st.info("📚 No history yet. Start reviewing code to build your history!")
    
    # Sample code suggestions
    st.markdown("### 💡 Get Started")
    st.code("""
# Example Python code to review
def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)
""", language="python")
