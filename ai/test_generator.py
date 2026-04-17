import json
from config import client, MODEL, MAX_TOKENS


_SYSTEM_TEXT = (
    "You generate pytest test functions for Playwright in Python. "
    "Return only valid JSON with key \"tests\" (array of objects with "
    "\"function_name\", \"description\", and \"steps\" as plain English actions). "
    "No Gherkin, no extra text."
)


def generate_test_cases(feature_description: str) -> dict[str, object]:
    """Uses Claude to generate test cases from a feature description."""
    message = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=_SYSTEM_TEXT,
        messages=[{
            "role": "user",
            "content": (
                "Generate test cases for this feature covering happy path, "
                "error handling, edge cases, and performance considerations:\n\n"
                f"Feature: {feature_description}"
            ),
        }],
    )
    response_text = next(b.text for b in message.content if b.type == "text")
    print(f"\nGenerated Test Cases:\n{response_text}")
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {"raw_response": response_text}
