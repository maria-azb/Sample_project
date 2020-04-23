from .main_page import MainPage
from .locators import ProductPageLocators


class ProductPage(MainPage):
# добавление в корзину
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