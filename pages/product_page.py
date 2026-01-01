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

    def should_be_product_in_basket(self, product_name, product_price):
        strong_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert strong_text == product_name, (f"Expected product name '{product_name}', "f"but got '{strong_text}' in success message")

        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text.replace('\xa0', ' ')
        assert basket_total == product_price, (f"Basket total ({basket_total}) does not match product price ({product_price})")

    def solve_quiz_and_get_code(self):
        super().solve_quiz_and_get_code()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not disappeared, but should be"
    