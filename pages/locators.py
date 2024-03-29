from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini.pull-right .btn-default[href="/en-gb/basket/"]')
    USER_ICON = (By.CLASS_NAME, "icon-user")    

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL_FIELD = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD_CONFIRM_FIELD = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_TITLE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_COST = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div') # сообщение, подтверждающее добавление в корзину
        
class BasketPageLocators():
    NOT_EMPTY_BASKET = (By.CLASS_NAME, 'basket-title') # локатор заголовка непустой корзины
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    