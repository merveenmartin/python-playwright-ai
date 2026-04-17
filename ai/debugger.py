from config import client, MODEL, MAX_TOKENS


_FAILURE_SYSTEM = (
    "You analyze Playwright test failures. For each failure determine: "
    "root cause (code/test/environment), whether it is a race condition or flaky, "
    "a specific fix, and a prevention strategy. Be concise and actionable."
)

_OPTIMIZE_SYSTEM = (
    "You review Playwright test code and provide: specific issues "
    "(duplication, flaky patterns, inefficiency), a refactored snippet, "
    "best practices applied, and performance improvements. "
    "Focus on stability, maintainability, and readability."
)


def analyze_test_failure(test_name: str, error_message: str, log_snippet: str) -> str:
    """Claude analyzes a test failure and suggests a fix."""
    message = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=_FAILURE_SYSTEM,
        messages=[{
            "role": "user",
            "content": f"Test Name: {test_name}\nError: {error_message}\nLogs: {log_snippet}",
        }],
    )
    return next(b.text for b in message.content if b.type == "text")


def optimize_test_code(test_code: str) -> str:
    """Claude reviews test code and returns optimization suggestions."""
    message = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=_OPTIMIZE_SYSTEM,
        messages=[{
            "role": "user",
            "content": f"Review this test code:\n\n```python\n{test_code}\n```",
        }],
    )
    return next(b.text for b in message.content if b.type == "text")
