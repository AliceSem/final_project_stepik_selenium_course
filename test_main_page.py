from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    main_page.open()                      # открываем страницу
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)  # инициализируем Page Object для страницы логина  
    login_page.should_be_login_page()        # выполняем метод страницы — переходим на страницу логина

def test_should_be_login_url(browser): 
    main_page = MainPage(browser, link)  
    main_page.open()                      
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)                      
    login_page.should_be_login_url()
    
def test_should_be_login_form(browser):
    main_page = MainPage(browser, link)  
    main_page.open()                      
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)                        
    login_page.should_be_login_form()
    
def test_should_be_register_form(browser):
    main_page = MainPage(browser, link)  
    main_page.open()                      
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)                       
    login_page.should_be_register_form()
