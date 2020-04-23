from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	 
class ProductPageLocators():	 
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_WAS_ADDED = (By.CSS_SELECTOR, "div.alertinner:nth-child(2) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")