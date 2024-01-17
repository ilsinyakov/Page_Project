from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_TITLE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_COST = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div') # сообщение, подтверждающее добавление в корзину
        