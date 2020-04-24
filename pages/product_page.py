from .base_page import BasePage
from .locators import ProductPageLocators
import time 

class ProductPage(BasePage):

    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button 'add to basket' is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        return {'product_name':product_name, 'price':price}

    def check_product_was_added(self, product):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_WAS_ADDED).text == product, "Product was not added"

    def check_basket_price(self, price):
        assert self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text == price, "Price in basket is wrong"		
		
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented"
		
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented"