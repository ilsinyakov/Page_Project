from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail(reason="Testing not empty basket locator") # проверка локатора перед негативным тестом
def test_guest_cant_see_product_in_basket_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.add_product_to_basket() # добавляем товар в корзину
    page.go_to_basket_on_header_button()
    page.should_be_nothing_in_basket()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_on_header_button()
    page.should_be_nothing_in_basket()
    page.should_be_text_empty_basket()
    