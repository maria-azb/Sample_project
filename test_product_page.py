﻿from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import pytest
import time

login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="some bug")),
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

@pytest.mark.skip		 
@pytest.mark.quiz # -m "not quiz"
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    product = page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_was_added(product['product_name'])
    page.check_basket_price(product['price'])

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message() 
		
@pytest.mark.xfail    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    product = page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail  	
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    product = page.add_to_basket()	
    page.should_disappear_success_message()

@pytest.mark.logincheck
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()
	
@pytest.mark.logincheck	
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()

@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_have_products()
    basket_page.is_basket_empty()

@pytest.mark.for_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = 'p'+str(time.time())
        page.register_new_user(email, password) 	
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message() 
		
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()
        product = page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_product_was_added(product['product_name'])
        page.check_basket_price(product['price'])
