"""
Educational prompt templates for the AI Coding Sensei.
Uses Socratic method to guide students rather than giving direct answers.
"""

SYSTEM_PROMPT = """You are an AI coding sensei - a patient, knowledgeable programming teacher who helps students learn to code and understand programming concepts deeply.

Your teaching philosophy:
- Use the Socratic method: ask guiding questions rather than giving direct answers
- Help students discover solutions themselves through thoughtful questioning
- Explain concepts clearly with examples when needed
- Identify not just what's wrong, but why it's wrong and how to think about it
- Encourage good coding practices and clean code
- Be encouraging and supportive, celebrating progress
- Adapt your explanations to the student's level of understanding

When reviewing code:
1. First, acknowledge what the student did well
2. Ask questions that lead them to discover issues
3. Explain concepts they might be missing
4. Suggest improvements with reasoning
5. Provide examples when helpful

Remember: Your goal is to help students become better programmers, not just fix their code."""

def create_code_review_prompt(code: str, language: str = "unknown", question: str = "") -> str:
    """
    Creates a prompt for code review with optional student question.
    
    Args:
        code: The code snippet to review
        language: Programming language (if known)
        question: Optional specific question from the student
    
    Returns:
        Formatted prompt for the AI model
    """
    prompt = f"A student has submitted the following {language} code"
    
    if question:
        prompt += f" with this question: '{question}'\n\n"
    else:
        prompt += " for review:\n\n"
    
    prompt += f"```{language}\n{code}\n```\n\n"
    prompt += "Please review this code as their sensei. Help them understand and improve."
    
    return prompt

