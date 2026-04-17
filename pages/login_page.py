from playwright.sync_api import Page
from config import BASE_URL


class LoginPage:
    URL = f"{BASE_URL}/login"

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")
        self.error_message = page.locator("#flash")

    def goto(self):
        self.page.goto(self.URL)

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self) -> str:
        return self.error_message.text_content() or ""
