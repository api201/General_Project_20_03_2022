import pytest
import time

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

#link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'

def test_guest_can_add_product_to_basket(browser): #, link
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_product_to_message()
    page.should_be_price_product_to_message()