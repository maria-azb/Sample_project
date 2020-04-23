from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"		

    def should_not_have_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Basket has products"
		
