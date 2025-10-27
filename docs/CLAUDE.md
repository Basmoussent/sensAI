# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

sensAI is a self-hostable AI-powered coding sensei that helps students learn programming through Socratic questioning. The application uses Mistral-7B-Instruct-v0.3 via vLLM for AI inference, with a FastAPI backend and Streamlit frontend.

## Development Commands

### Docker Operations
```bash
make              # Build and start all services (default)
make re           # Restart all services
make clean        # Stop services and prune Docker system
make logs         # Follow service logs
```

### Development Setup
```bash
make setup-dev    # Setup virtual environment and install dependencies
make dev          # Run in development mode (Streamlit + FastAPI)

# Manual setup:
python3 -m venv venv
source venv/bin/activate
pip install -e .
pip install -e ".[dev]"  # Install dev dependencies (pytest, black, isort, flake8, mypy)
```

### Running the Application
- **Frontend**: Streamlit runs on port 8501 (http://localhost:8501)
- **Backend**: FastAPI runs on port 8000 (http://localhost:8000)
- **Health Check**: http://localhost:8000/health

### Testing & Code Quality
```bash
pytest                # Run tests
pytest -v            # Verbose test output
black .              # Format code (line length: 88)
isort .              # Sort imports
flake8               # Lint code
mypy .               # Type checking (strict mode enabled)
```

## Architecture

### Frontend (Streamlit)

**Entry Point**: `frontend/app.py` - Main Streamlit application with chat interface

**Structure**:
- `pages/` - Individual page modules (dashboard, history)
- `components/` - Reusable UI components (ui.py, code_input.py)
- `services/` - Business logic layer
  - `api_client.py` - HTTP client for backend API communication
- `utils/` - Helper functions (helpers.py for validation and formatting)

**Key Patterns**:
- Uses `st.session_state` for conversation history management
- Implements chat interface with suggestion pills for new users
- Streams responses from backend API in real-time
- History tracking limited to last 5 messages (HISTORY_LENGTH constant)
- Prompt building includes system instructions, recent messages, and user question

**State Management**:
- `st.session_state.messages` - Chat history array with role/content
- `st.session_state.initial_question` - First user query
- `st.session_state.selected_suggestion` - Selected suggestion pill

### Backend (FastAPI)

**Current State**: Backend directory only contains `prompts.py` - suggests backend implementation is planned or incomplete

**Prompt System** (`backend/prompts.py`):
- `SYSTEM_PROMPT` - Defines AI sensei teaching philosophy (Socratic method)
- `create_code_review_prompt()` - Generates prompts for code review with language and optional question

**Teaching Philosophy**:
1. Acknowledge what student did well
2. Ask guiding questions to discover issues
3. Explain missing concepts
4. Suggest improvements with reasoning
5. Provide examples when helpful

### AI Integration

**Model**: Mistral-7B-Instruct-v0.3
- **Size**: ~13GB (7 billion parameters)
- **Requirements**: 8GB+ RAM, NVIDIA GPU recommended
- **Framework**: vLLM for high-performance inference
- **Prompt Management**: LangChain for prompt templates

### API Communication

**Endpoint**: POST `/api/review`
**Request**:
```json
{
  "code": "string",
  "language": "string",
  "question": "string (optional)"
}
```
**Response**: Server-Sent Events (SSE) stream
- Format: `data: <text>\n\n`
- Termination: `data: [DONE]\n\n`

### Configuration

**API URL**: Hardcoded to `http://localhost:8000` in `frontend/app.py:14`

**Python Requirements**:
- Python >= 3.10
- Core: fastapi, uvicorn, vllm, pydantic, streamlit, htbuilder
- AI: langchain, langchain-community, langchain-core
- Dev: pytest, pytest-asyncio, black, isort, flake8, mypy

**Code Style** (pyproject.toml):
- Black formatting: 88 character line length
- isort profile: black-compatible
- mypy: Strict type checking enabled
- pytest: Auto async mode, verbose output with short tracebacks

### Streamlit Best Practices (from .cursor/rules)

**Key Architectural Principles**:
- Separate business logic into `services/` directory
- Build reusable UI components in `components/`
- Use `@st.cache_data` and `@st.cache_resource` for expensive operations
- Initialize session state with conditional checks to prevent overwrites
- Implement comprehensive error handling with `try/except` blocks

**Anti-patterns to Avoid**:
- Do not perform expensive computations in main app loop
- Do not store large datasets in `st.session_state`
- Avoid global variables
- Do not forget to cache expensive operations

**Performance**:
- Use caching for expensive computations
- Debounce user interactions to reduce reruns
- Implement lazy loading for heavy components
- Minimize external dependencies

## Important Notes

1. **Backend Status**: The backend directory appears minimal - only prompt templates exist. FastAPI server implementation may be elsewhere or not yet implemented.

2. **Docker Deployment**: Primary deployment method is Docker Compose (`make` command), but docker-compose.yml and Dockerfiles were not found in the repository.

3. **Prompt Context**: Frontend builds prompts with 3 sections:
   - `<instructions>` - System instructions for AI behavior
   - `<recent_messages>` - Last 5 messages from conversation history
   - `<question>` - Current user query

4. **Supported Languages**: Python, JavaScript, TypeScript, Java, C++, Go, Rust (as documented in README)

5. **Type Safety**: Project uses strict mypy configuration - all functions should have type annotations.

6. **Code Quality**: Use black (line 88) and isort for formatting before committing.
