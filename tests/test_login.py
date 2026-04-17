import pytest
import allure
from playwright.sync_api import Page, expect
from pages import LoginPage


@allure.feature("Authentication")
class TestLoginFlow:

    @allure.story("Successful login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, page: Page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("tomsmith", "SuperSecretPassword!")
        page.wait_for_url("**/secure")
        expect(page.locator("h2")).to_contain_text("Secure Area")

    @allure.story("Login validation")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("email,password,expected_error", [
        ("wronguser", "wrongpass", "Your username is invalid"),
        ("tomsmith", "wrongpass", "Your password is invalid"),
    ])
    def test_login_validation(self, page: Page, email: str, password: str, expected_error: str):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(email, password)
        assert expected_error.lower() in login_page.get_error_text().lower()
