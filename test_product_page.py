from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest


# параметризация (!передать link в функцию)                                 
'''@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])'''

@pytest.mark.skip(reason="no way of currently testing this") # пропускаем тест
def test_guest_can_add_product_to_basket(browser): # <- вставить link в атрибуты при включении параметризации!
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207' # ссылка без промо
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear' # ссылка с промо (!включить квиз)
    page = ProductPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.should_be_add_to_basket_button() # проверяем наличие кнопки "Добавить в корзину"
    page.add_product_to_basket() # проверяем добавление товара в корзину
#    page.solve_quiz_and_get_code() # решаем квиз
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
    