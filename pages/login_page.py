from playwright.sync_api import Page
from config import BASE_URL


class LoginPage:
    URL = BASE_URL

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input[id='user-name']")
        self.password_input = page.locator("input[id='password']")
        self.login_button = page.locator("input[type='submit']")
        self.error_message = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto(self.URL)

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self) -> str:
        return self.error_message.text_content() or ""
