import pytest
from pages.product_page import ProductPage
import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

urls = [
    f"{product_base_link}/?promo=offer{no}"
    if no != 7
    else pytest.param(
        f"{product_base_link}/?promo=offer{no}",
        marks=pytest.mark.xfail(reason="Bug", strict=True)
    )
    for no in range(10)
]

@pytest.mark.parametrize('urls', urls)
def test_guest_can_add_product_to_basket(browser, urls):
    product_page = ProductPage(browser, urls)
    product_page.open()

    product_page.should_be_add_to_basket_button()

    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()

    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()

    product_page.should_be_success_message()
    product_page.should_be_product_in_basket(product_name, product_price) 
