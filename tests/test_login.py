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
        login_page.login("standard_user", "secret_sauce")
        page.wait_for_url("**/inventory.html")
        expect(page.locator("[data-test='title']")).to_contain_text("Products")

    @allure.story("Login validation")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("email,password,expected_error", [
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ("standard_user", "wrongpass", "Epic sadface: Username and password do not match any user in this service"),
    ])
    def test_login_validation(self, page: Page, email: str, password: str, expected_error: str):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(email, password)
        assert expected_error.lower() in login_page.get_error_text().lower()
