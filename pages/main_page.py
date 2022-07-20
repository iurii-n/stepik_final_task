from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): #класс MainPage имеет доступ ко всем атрибутам и методам класса BasePage
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    """def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"    
        """
   """ def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_enter_basket()
    page2 = BasketPage(browser, browser.current_url)
    page2.is_basket_empty()
    page2.should_be_basket_empty_message()"""