from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): #класс MainPage имеет доступ ко всем атрибутам и методам класса BasePage
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
