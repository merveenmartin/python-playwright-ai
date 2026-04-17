import pytest
import allure
from playwright.sync_api import Page, expect
from config import BASE_URL
from pages import ProductPage


@allure.feature("Shopping Cart")
class TestAddToCart:

    @allure.story("Add single item")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_single_item(self, page: Page):
        page.goto(BASE_URL)
        product_page = ProductPage(page)
        product_page.add_item_to_cart()
        expect(product_page.cart_badge).to_contain_text("1")

    @allure.story("Add multiple quantities")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("quantity", [1, 5, 10])
    def test_add_multiple_quantities(self, page: Page, quantity: int):
        page.goto(BASE_URL)
        product_page = ProductPage(page)
        for _ in range(quantity):
            product_page.add_item_to_cart()
        expect(product_page.cart_badge).to_contain_text(str(quantity))
