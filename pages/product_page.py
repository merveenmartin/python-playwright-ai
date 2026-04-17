from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_btn = page.locator("button:has-text('Add to Cart')")
        self.cart_badge = page.locator("[aria-label='Cart items count']")
        self.product_title = page.locator("h1.product-title")

    def add_item_to_cart(self):
        self.add_to_cart_btn.click()
        self.cart_badge.wait_for(state="visible")

    def get_product_name(self) -> str:
        return self.product_title.text_content() or ""
