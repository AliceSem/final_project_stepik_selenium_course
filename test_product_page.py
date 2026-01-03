import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage 
import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

urls = [
    f"{product_base_link}/?promo=offer{no}"
    if no != 7
    else pytest.param(
        f"{product_base_link}/?promo=offer{no}",
        marks=pytest.mark.xfail(reason="Bug", strict=True))
    for no in range(10)]

@pytest.mark.parametrize('urls', urls)
def test_guest_can_add_product_to_basket_promo(browser, urls):
    product_page = ProductPage(browser, urls)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message()
    product_page.should_be_product_in_basket(product_name, product_price) 

product_link  = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9" 

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message()
    product_page.should_be_product_in_basket(product_name, product_price)

@pytest.mark.xfail(reason="Bug", strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message() 

@pytest.mark.xfail(reason="Bug", strict=True) 
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_disappeared() 

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message()
    basket_page.should_not_be_items_in_basket() 

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def test_setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "hXT14I9fP"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_not_be_success_message() 

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_be_add_to_basket_button()
        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_success_message()
        product_page.should_be_product_in_basket(product_name, product_price) 
