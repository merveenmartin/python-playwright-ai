from ai.debugger import optimize_test_code

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

if __name__ == "__main__":
    result = optimize_test_code(test_code)
    print(result)
