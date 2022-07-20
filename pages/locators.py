from selenium.webdriver.common.by import By


#class MainPageLocators():
 #   LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form')
    REG_LOGIN = (By.ID, 'id_registration-email')
    REG_PASSWORD1 = (By.ID, 'id_registration-password1')
    REG_PASSWORD2 = (By.ID, 'id_registration-password2')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name^="registration_submit"]')
    
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BOOK_NAME_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    BOOK_PRICE_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")
