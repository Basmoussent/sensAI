"""
Prompt templates for the AI Coding Sensei.
Organized by language and use case.
"""

from .base_prompts import SYSTEM_PROMPT, create_code_review_prompt
from .language_specific import (
    PYTHON_PROMPT,
    JAVASCRIPT_PROMPT,
    TYPESCRIPT_PROMPT,
    JAVA_PROMPT,
    CPP_PROMPT,
    GO_PROMPT,
    RUST_PROMPT,
)
from .specialized_prompts import (
    PERFORMANCE_ANALYSIS_PROMPT,
    SECURITY_REVIEW_PROMPT,
    BEST_PRACTICES_PROMPT,
    REFACTORING_PROMPT,
    DEBUG_HELP_PROMPT,
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
    "PERFORMANCE_ANALYSIS_PROMPT",
    "SECURITY_REVIEW_PROMPT",
    "BEST_PRACTICES_PROMPT",
    "REFACTORING_PROMPT",
    "DEBUG_HELP_PROMPT",
]
