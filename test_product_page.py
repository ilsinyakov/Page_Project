from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # открываем страницу с регистрацией
        login_page = LoginPage(browser, browser.current_url) # создаем экземпляр класса LoginPage
        email = str(time.time()) + "@fakemail.org"
        password = '1a2fg34-_S'
        login_page.register_new_user(email, password)   # регистрируем нового юзера
        login_page.should_be_authorized_user() # проверяем регистрацию юзера
        
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207' # ссылка без промо
        #    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear' # ссылка с промо (!включить квиз)
        page = ProductPage(browser, link) # создаем объект класса ProductPage
        page.open() # открываем страницу по ссылке
        page.should_be_add_to_basket_button() # проверяем наличие кнопки "Добавить в корзину"
        page.add_product_to_basket() # проверяем добавление товара в корзину
        #    page.solve_quiz_and_get_code() # решаем квиз
        page.should_be_product_in_basket() # проверяем, та ли книга у нас в корзине
        page.should_be_basket_cost_same_product_price() # проверяем, совпадает ли стоимость корзины с ценой книги   
    
    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207' # ссылка без промо
        page = ProductPage(browser, link) # создаем объект класса ProductPage
        page.open() # открываем страницу по ссылке
        page.should_not_be_success_message() # проверяем отсутствие сообщения


'''
# параметризация (!передать link в функцию)                                 
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
'''

#@pytest.mark.skip(reason="no way of currently testing this") # пропускаем тест
def test_guest_can_add_product_to_basket(browser): # <- вставить link в атрибуты при включении параметризации!
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207' # ссылка без промо
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear' # ссылка с промо (!включить квиз)
    page = ProductPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.should_be_add_to_basket_button() # проверяем наличие кнопки "Добавить в корзину"
    page.add_product_to_basket() # проверяем добавление товара в корзину
    page.solve_quiz_and_get_code() # решаем квиз
    page.should_be_product_in_basket() # проверяем, та ли книга у нас в корзине
    page.should_be_basket_cost_same_product_price() # проверяем, совпадает ли стоимость корзины с ценой книги

@pytest.mark.xfail(reason="Testing success message locator") # проверка локатора перед негативным тестом
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207' # ссылка без промо
    page = ProductPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.add_product_to_basket() # добавляем товар в корзину
    page.should_not_be_success_message() # проверяем отсутствие сообщения
    
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207' # ссылка без промо
    page = ProductPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.should_not_be_success_message() # проверяем отсутствие сообщения

@pytest.mark.xfail(reason="Message should not be disappeared") # пропускаем тест    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207' # ссылка без промо
    page = ProductPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.add_product_to_basket() # добавляем товар в корзину
    page.should_be_disappeared_success_message() # сообщение о добавлении в корзину должно исчезнуть
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.go_to_login_page() # переходим на страницу логина
    
@pytest.mark.xfail(reason="Testing not empty basket locator") # проверка локатора перед негативным тестом
def test_guest_cant_see_product_in_basket_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.add_product_to_basket() # добавляем товар в корзину
    page.go_to_basket_on_header_button()
    page.should_be_nothing_in_basket()
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):    
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.go_to_basket_on_header_button()
    page.should_be_nothing_in_basket()
    page.should_be_text_empty_basket()
    