from .pages.product_page import ProductPage
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

@pytest.mark.xfail(reason="Test success message locator") # пропускаем тест
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
    