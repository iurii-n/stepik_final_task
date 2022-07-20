from .pages.product_page import ProductPage
#from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import random
import time


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}?promo=offer{no}" if no != "???"
        else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    
    product_page.should_be_book_name()
    product_page.should_be_book_price()
