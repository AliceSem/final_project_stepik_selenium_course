from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form > button")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form > button")
    REGISTR_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTR_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTR_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTR_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info strong') 

class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
