"""
Educational prompt templates for the AI Coding Sensei.
Uses Socratic method to guide students rather than giving direct answers.

DEPRECATED: This file is kept for backward compatibility.
Please use the new prompts module: backend.prompts
"""

import warnings

# Import from new location
from backend.prompts import (
    SYSTEM_PROMPT,
    create_code_review_prompt,
    PYTHON_PROMPT,
    JAVASCRIPT_PROMPT,
    TYPESCRIPT_PROMPT,
    JAVA_PROMPT,
    CPP_PROMPT,
    GO_PROMPT,
    RUST_PROMPT,
)

warnings.warn(
    "backend.prompts.py is deprecated. Use 'from backend.prompts import ...' instead.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = [
    "SYSTEM_PROMPT",
    "create_code_review_prompt",
    "PYTHON_PROMPT",
    "JAVASCRIPT_PROMPT",
    "TYPESCRIPT_PROMPT",
    "JAVA_PROMPT",
    "CPP_PROMPT",
    "GO_PROMPT",
    "RUST_PROMPT",
]

