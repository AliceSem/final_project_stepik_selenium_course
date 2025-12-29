from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    product_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, product_url)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message()
