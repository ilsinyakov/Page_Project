from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Basket button isn't present"
        
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()        
        
    def should_be_product_in_basket(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        book_title_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_BASKET).text
        assert book_title == book_title_in_basket, "There isn't book in the basket"
    
    def should_be_basket_cost_same_product_price(self):
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert basket_cost == book_price, "Book's price isn't same basket cost"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
    
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is not disappeared, but should be"