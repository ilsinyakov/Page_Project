from .pages.product_page import ProductPage
import pytest

                                 
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
                                  
def test_guest_can_add_product_to_basket(browser, link):
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear' # /?promo=newYear
    page = ProductPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.should_be_add_to_basket_button() # проверяем наличие кнопки "Добавить в корзину"
    page.add_product_to_basket() # проверяем добавление товара в корзину
    page.solve_quiz_and_get_code() # решаем квиз
    page.should_be_product_in_basket() # проверяем, та ли книга у нас в корзине
    page.shoud_be_basket_cost_same_product_price() # проверяем, совпадает ли стоимость корзины с ценой книги
    