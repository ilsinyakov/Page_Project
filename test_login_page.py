from .pages.login_page import LoginPage


def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес     
    page.should_be_login_page()          # выполняем метод страницы — переходим на страницу логина    
    