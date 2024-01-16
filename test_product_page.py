from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear' # /?promo=newYear
    page = ProductPage(browser, link) # создаем объект класса ProductPage
    page.open() # открываем страницу по ссылке
    page.should_be_add_to_basket_button() # проверяем наличие кнопки "Добавить в корзину"
    page.add_product_to_basket() # проверяем добавление товара в корзину
    page.solve_quiz_and_get_code() # решаем квиз
    page.should_be_product_in_basket() # проверяем, та ли книга у нас в корзине
    page.shoud_be_basket_cost_same_product_price() # проверяем, совпадает ли стоимость корзины с ценой книги
    