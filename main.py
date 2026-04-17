from ai import generate_test_cases, analyze_test_failure, optimize_test_code


def demonstrate_ai_capabilities() -> None:
    """Runs all three AI capabilities without a real browser."""

    # ── Edit these to match your scenario ─────────────────────────────────────
    feature = "User login with email and password, including error handling"

    test_code = """\
def test_login():
    page.goto("https://example.com")
    time.sleep(2)
    page.fill("input[name='email']", "user@test.com")
    page.fill("input[name='password']", "pass")
    page.click("button")
    time.sleep(3)
    assert "Dashboard" in page.title()
"""

    test_name     = "test_add_to_cart"
    error_message = "Timeout waiting for element"
    log_snippet   = "Element not found after 30s, DOM shows cart button disabled"
    # ──────────────────────────────────────────────────────────────────────────

    sep = "=" * 70
    print(f"\n{sep}\nAI-DRIVEN QA DEMONSTRATION\n{sep}")

    # print("\n1  TEST CASE GENERATION — login feature\n" + "-" * 70)
    # generate_test_cases(feature)

    # print("\n2  TEST CASE GENERATION — add 1 item\n" + "-" * 70)
    # generate_test_cases("User adds 1 item in cart")

    # print("\n3  TEST CASE GENERATION — add 3 items\n" + "-" * 70)
    # generate_test_cases("User adds 3 items in cart")

    print("\n4  CODE OPTIMIZATION\n" + "-" * 70)
    print(optimize_test_code(test_code))

    print("\n5  INTELLIGENT DEBUGGING\n" + "-" * 70)
    print(analyze_test_failure(test_name, error_message, log_snippet))


if __name__ == "__main__":
    demonstrate_ai_capabilities()
