import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

st.set_page_config(
    page_title="Dashboard - sensAI",
    page_icon="📊",
    layout="wide"
)

# Modern header
st.markdown("""
    <style>
    .dashboard-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="dashboard-header"><h1>📊 Dashboard</h1><p>Your coding journey insights</p></div>', unsafe_allow_html=True)

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = []

# Stats Overview
col1, col2, col3, col4 = st.columns(4)

total_reviews = len(st.session_state.responses)
languages_used = len(set([r.get('language', 'unknown') for r in st.session_state.responses]))
unique_sessions = len(st.session_state.responses)
avg_length = sum([len(r.get('code', '')) for r in st.session_state.responses]) / max(total_reviews, 1)

with col1:
    st.metric("Total Reviews", total_reviews, "📈")
with col2:
    st.metric("Languages Used", languages_used, "🌐")
with col3:
    st.metric("Unique Sessions", unique_sessions, "🔥")
with col4:
    st.metric("Avg Code Length", f"{avg_length:.0f} chars", "📏")

# Language Distribution
if st.session_state.responses:
    st.markdown("---")
    st.subheader("📊 Language Distribution")
    
    language_dist = {}
    for review in st.session_state.responses:
        lang = review.get('language', 'unknown')
        language_dist[lang] = language_dist.get(lang, 0) + 1
    
    df_langs = pd.DataFrame(list(language_dist.items()), columns=['Language', 'Count'])
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.bar_chart(df_langs.set_index('Language'))
    with col2:
        st.dataframe(df_langs, use_container_width=True)
else:
    st.info("📊 Start reviewing code to see your dashboard analytics!")

# Recent Activity
if st.session_state.responses:
    st.markdown("---")
    st.subheader("🎯 Recent Activity")
    
    for idx, review in enumerate(reversed(st.session_state.responses[-5:])):
        with st.expander(f"{review['language']} - {review.get('timestamp', 'N/A')[:10]}"):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.code(review['code'], language=review['language'])
            with col2:
                st.metric("Code Length", f"{len(review['code'])} chars")
