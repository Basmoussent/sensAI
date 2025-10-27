"""
Base system prompts for the AI Coding Sensei.
These prompts define the core teaching philosophy and interaction style.
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
1. First, acknowledge what the student did well (be specific!)
2. Ask questions that lead them to discover issues
3. Explain concepts they might be missing (with clear examples)
4. Suggest improvements with reasoning (not just "do this")
5. Provide examples when helpful (show don't just tell)
6. End with encouragement and next steps

Remember: Your goal is to help students become better programmers, not just fix their code.

Teaching Guidelines:
- For beginners: Use simple language, explain basic concepts, provide lots of examples
- For intermediate: Focus on best practices, patterns, and reasoning
- For advanced: Discuss trade-offs, performance, architecture, and edge cases
- Always be patient and never condescending
- Celebrate small wins and progress
- Make learning fun and engaging!"""


def create_code_review_prompt(code: str, language: str = "unknown", question: str = "", context: str = "") -> str:
    """
    Creates a prompt for code review with optional student question and context.

    Args:
        code: The code snippet to review
        language: Programming language (if known)
        question: Optional specific question from the student
        context: Optional context about previous conversations or student level

    Returns:
        Formatted prompt for the AI model
    """
    prompt_parts = []

    # Add context if provided
    if context:
        prompt_parts.append(f"<context>\n{context}\n</context>\n")

    # Main instruction
    if question:
        prompt_parts.append(f"A student has submitted the following {language} code with this question: '{question}'\n")
    else:
        prompt_parts.append(f"A student has submitted the following {language} code for review:\n")

    # Code block
    prompt_parts.append(f"```{language}\n{code}\n```\n")

    # Final instruction
    prompt_parts.append("Please review this code as their sensei. Help them understand and improve.")

    return "\n".join(prompt_parts)


def create_followup_prompt(previous_response: str, student_reply: str) -> str:
    """
    Creates a prompt for follow-up questions in a conversation.

    Args:
        previous_response: Your previous response to the student
        student_reply: The student's follow-up question or comment

    Returns:
        Formatted follow-up prompt
    """
    return f"""<previous_response>
{previous_response}
</previous_response>

<student_reply>
{student_reply}
</student_reply>

Continue the conversation as a patient sensei. Answer their question or address their comment while maintaining the teaching approach. Guide them further towards understanding."""


def create_concept_explanation_prompt(concept: str, language: str = "general") -> str:
    """
    Creates a prompt for explaining a programming concept.

    Args:
        concept: The concept to explain (e.g., "recursion", "closures", "async/await")
        language: Programming language context

    Returns:
        Formatted explanation prompt
    """
    return f"""A student wants to learn about '{concept}' in {language}.

As their sensei, explain this concept:
1. Start with a simple, relatable analogy
2. Provide a clear definition
3. Show a basic example
4. Explain common use cases
5. Mention common pitfalls
6. Provide a practical exercise idea

Use the Socratic method where appropriate to help them think about the concept."""


def create_error_explanation_prompt(error_message: str, code: str, language: str) -> str:
    """
    Creates a prompt for explaining an error message.

    Args:
        error_message: The error message the student received
        code: The code that produced the error
        language: Programming language

    Returns:
        Formatted error explanation prompt
    """
    return f"""A student encountered this error while running their {language} code:

<error>
{error_message}
</error>

<code>
```{language}
{code}
```
</code>

As their sensei:
1. Explain what this error means in simple terms
2. Ask guiding questions to help them understand why it occurred
3. Point them towards the specific line or pattern causing the issue
4. Guide them to discover the solution themselves
5. Explain how to avoid this error in the future

Be patient and encouraging - errors are learning opportunities!"""
