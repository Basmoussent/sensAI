# 🎯 Prompts Library for sensAI

This directory contains all prompt templates used by the AI Coding Sensei.

## 📁 Structure

```
prompts/
├── __init__.py                    # Main exports
├── README.md                      # This file
├── base_prompts.py                # Core system prompts
├── language_specific.py           # Language-specific guidance
├── specialized_prompts.py         # Special-purpose prompts
└── examples/                      # Example usage (future)
```

## 🚀 Quick Start

```python
from backend.prompts import (
    SYSTEM_PROMPT,
    create_code_review_prompt,
    PYTHON_PROMPT,
    PERFORMANCE_ANALYSIS_PROMPT
)

# Basic code review
prompt = create_code_review_prompt(
    code=user_code,
    language="python",
    question="How can I make this faster?"
)

# With language-specific context
full_prompt = f"{SYSTEM_PROMPT}\n\n{PYTHON_PROMPT}\n\n{prompt}"
```

## 📋 Available Prompts

### Base Prompts (`base_prompts.py`)

#### `SYSTEM_PROMPT`
Core system prompt defining the sensei's teaching philosophy and approach.

**Usage:**
```python
from backend.prompts import SYSTEM_PROMPT
```

#### `create_code_review_prompt(code, language, question, context)`
Creates a formatted prompt for code review.

**Parameters:**
- `code` (str): The code to review
- `language` (str): Programming language
- `question` (str, optional): Student's specific question
- `context` (str, optional): Conversation context

**Usage:**
```python
prompt = create_code_review_prompt(
    code="def factorial(n):\n    return n * factorial(n-1)",
    language="python",
    question="Is this efficient?",
    context="Student is learning recursion"
)
```

#### `create_followup_prompt(previous_response, student_reply)`
Creates a prompt for follow-up questions.

#### `create_concept_explanation_prompt(concept, language)`
Creates a prompt for explaining programming concepts.

#### `create_error_explanation_prompt(error_message, code, language)`
Creates a prompt for explaining error messages.

---

### Language-Specific Prompts (`language_specific.py`)

These prompts provide language-specific guidance and best practices.

#### Available Languages:
- `PYTHON_PROMPT` - Pythonic code, PEP 8, common pitfalls
- `JAVASCRIPT_PROMPT` - ES6+, async/await, common patterns
- `TYPESCRIPT_PROMPT` - Type system, strict mode, best practices
- `JAVA_PROMPT` - OOP, SOLID principles, modern Java
- `CPP_PROMPT` - Memory management, modern C++, RAII
- `GO_PROMPT` - Go idioms, concurrency, error handling
- `RUST_PROMPT` - Ownership, borrowing, safety

**Usage:**
```python
from backend.prompts import PYTHON_PROMPT, JAVASCRIPT_PROMPT

# Combine with base prompt
full_prompt = f"{SYSTEM_PROMPT}\n\n{PYTHON_PROMPT}\n\n{user_prompt}"
```

**When to use:**
- Append to SYSTEM_PROMPT for language-specific reviews
- Helps the AI focus on language-specific best practices
- Provides context for common pitfalls

---

### Specialized Prompts (`specialized_prompts.py`)

These prompts focus on specific aspects of code review.

#### `PERFORMANCE_ANALYSIS_PROMPT`
Focus on time/space complexity and optimization.

**Use when:**
- Student asks about performance
- Code has obvious performance issues
- Discussing algorithm efficiency

#### `SECURITY_REVIEW_PROMPT`
Focus on security vulnerabilities and best practices.

**Use when:**
- Code handles user input
- Working with authentication/authorization
- Dealing with sensitive data

#### `BEST_PRACTICES_PROMPT`
Focus on code quality, maintainability, and standards.

**Use when:**
- General code review
- Teaching clean code principles
- Preparing code for production

#### `REFACTORING_PROMPT`
Focus on code smells and refactoring opportunities.

**Use when:**
- Code is messy or complex
- Student asks how to improve structure
- Teaching design patterns

#### `DEBUG_HELP_PROMPT`
Focus on debugging methodology and problem-solving.

**Use when:**
- Student has a bug
- Code doesn't work as expected
- Teaching debugging skills

#### `CODE_REVIEW_CHECKLIST_PROMPT`
Comprehensive checklist-based review.

**Use when:**
- Thorough review needed
- Preparing for production
- Teaching code review skills

#### `BEGINNER_FRIENDLY_PROMPT`
Adjust teaching style for beginners.

**Use when:**
- Detected beginner-level code
- Student is struggling
- Need to simplify explanations

#### `ADVANCED_DEVELOPER_PROMPT`
Adjust teaching style for advanced developers.

**Use when:**
- Detected advanced patterns
- Student shows expertise
- Can discuss advanced topics

---

## 🎨 Prompt Composition

### Basic Pattern
```python
from backend.prompts import SYSTEM_PROMPT, create_code_review_prompt

# Simple review
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": create_code_review_prompt(code, language)}
]
```

### With Language-Specific Context
```python
from backend.prompts import SYSTEM_PROMPT, PYTHON_PROMPT, create_code_review_prompt

# Python-specific review
system_prompt = f"{SYSTEM_PROMPT}\n\n{PYTHON_PROMPT}"
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": create_code_review_prompt(code, "python")}
]
```

### With Specialized Focus
```python
from backend.prompts import (
    SYSTEM_PROMPT,
    PYTHON_PROMPT,
    PERFORMANCE_ANALYSIS_PROMPT,
    create_code_review_prompt
)

# Performance-focused Python review
system_prompt = f"{SYSTEM_PROMPT}\n\n{PYTHON_PROMPT}\n\n{PERFORMANCE_ANALYSIS_PROMPT}"
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": create_code_review_prompt(
        code=code,
        language="python",
        question="How can I optimize this?"
    )}
]
```

### With Conversation Context
```python
from backend.prompts import create_followup_prompt

# Follow-up in conversation
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": previous_code_prompt},
    {"role": "assistant", "content": previous_response},
    {"role": "user", "content": "Can you explain recursion more?"},
]
```

---

## 🧠 Prompt Engineering Best Practices

### 1. **Be Specific**
```python
# ❌ Vague
"Review this code"

# ✅ Specific
"Review this Python code for performance issues, focusing on the nested loops"
```

### 2. **Provide Context**
```python
# ❌ No context
create_code_review_prompt(code, "python")

# ✅ With context
create_code_review_prompt(
    code=code,
    language="python",
    question="Is this efficient for large datasets?",
    context="Student is building a data processing pipeline for 1M+ records"
)
```

### 3. **Use Appropriate Prompts**
```python
# For beginners
system_prompt = f"{SYSTEM_PROMPT}\n\n{BEGINNER_FRIENDLY_PROMPT}"

# For security-critical code
system_prompt = f"{SYSTEM_PROMPT}\n\n{SECURITY_REVIEW_PROMPT}"

# For performance issues
system_prompt = f"{SYSTEM_PROMPT}\n\n{PERFORMANCE_ANALYSIS_PROMPT}"
```

### 4. **Maintain Conversation History**
```python
# Keep last 5 messages for context
recent_messages = conversation_history[-5:]
```

### 5. **Adjust Temperature**
```python
# More creative/varied responses
temperature = 0.8

# More focused/consistent responses
temperature = 0.6
```

---

## 📊 Prompt Selection Decision Tree

```
Is it a code review?
├─ Yes
│  ├─ What's the student level?
│  │  ├─ Beginner → Use BEGINNER_FRIENDLY_PROMPT
│  │  ├─ Advanced → Use ADVANCED_DEVELOPER_PROMPT
│  │  └─ Unknown → Use base SYSTEM_PROMPT
│  │
│  ├─ What's the focus?
│  │  ├─ Performance → Add PERFORMANCE_ANALYSIS_PROMPT
│  │  ├─ Security → Add SECURITY_REVIEW_PROMPT
│  │  ├─ Refactoring → Add REFACTORING_PROMPT
│  │  ├─ Best Practices → Add BEST_PRACTICES_PROMPT
│  │  └─ General → Use base prompts only
│  │
│  └─ What's the language?
│     ├─ Python → Add PYTHON_PROMPT
│     ├─ JavaScript → Add JAVASCRIPT_PROMPT
│     ├─ TypeScript → Add TYPESCRIPT_PROMPT
│     └─ etc...
│
├─ Is it debugging help?
│  └─ Use DEBUG_HELP_PROMPT
│
├─ Is it a concept explanation?
│  └─ Use create_concept_explanation_prompt()
│
└─ Is it an error explanation?
   └─ Use create_error_explanation_prompt()
```

---

## 🔧 Configuration

### Recommended Model Parameters

```python
# For Mistral-7B-Instruct-v0.3
model_params = {
    "temperature": 0.7,      # Balance creativity and consistency
    "top_p": 0.9,            # Nucleus sampling
    "max_tokens": 2048,      # Sufficient for detailed explanations
    "frequency_penalty": 0.1, # Reduce repetition
    "presence_penalty": 0.1,  # Encourage diversity
}
```

### Context Window Management

```python
# Mistral-7B has 8192 token context
# Reserve space for:
# - System prompt: ~500 tokens
# - Language prompt: ~300 tokens
# - Specialized prompt: ~300 tokens
# - Code + question: ~2000 tokens
# - Conversation history: ~2000 tokens
# - Response: ~2048 tokens
# Total: ~7148 tokens (safe margin)
```

---

## 🧪 Testing Prompts

```python
# Test different prompts
test_cases = [
    {
        "code": "def fib(n): return fib(n-1) + fib(n-2)",
        "language": "python",
        "expected_topics": ["base case", "recursion", "performance"]
    },
    {
        "code": "eval(user_input)",
        "language": "python",
        "expected_topics": ["security", "injection", "dangerous"]
    },
]

for test in test_cases:
    prompt = create_code_review_prompt(test["code"], test["language"])
    response = llm.generate(prompt)
    # Assert expected topics are covered
```

---

## 📚 Examples

See `examples/` directory for complete usage examples:
- `basic_review.py` - Simple code review
- `conversation_flow.py` - Multi-turn conversation
- `specialized_review.py` - Using specialized prompts
- `language_specific.py` - Language-specific reviews

---

## 🔄 Version History

- **v1.0.0** (2025-10-27): Initial prompt library
  - Base prompts
  - 7 language-specific prompts
  - 8 specialized prompts

---

## 🤝 Contributing

When adding new prompts:
1. Follow the existing structure
2. Document parameters and usage
3. Add examples
4. Test with various code samples
5. Update this README

---

## 📖 References

- [LangChain Prompting Guide](https://python.langchain.com/docs/modules/model_io/prompts/)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Mistral AI Documentation](https://docs.mistral.ai/)
- [Socratic Teaching Method](https://en.wikipedia.org/wiki/Socratic_method)

---

**Last Updated:** 2025-10-27
