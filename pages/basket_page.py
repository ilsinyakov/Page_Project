from .base_page import BasePage
# from .main_page import MainPage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_nothing_in_basket(self):    
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "Basket is not empty"
    
    def should_be_text_empty_basket(self):
        message_empty_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET) # ищем поле с текстом о пустой корзине
        
        assert 'Your basket is empty.' in message_empty_basket.text, "Text 'Your basket is empty.' is not present"
            