from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def go_to_product_page(self):
        self.browser.get(self.product_url)

    def should_be_add_to_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_success_message(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present"
        self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).click()

    def should_be_product_in_basket(self, product_name, product_price):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name in success_message, "Product name in success message does not match"
        assert product_price in success_message, "Product price in success message does not match"
        self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).click()
    def solve_quiz_and_get_code(self):
        super().solve_quiz_and_get_code()
