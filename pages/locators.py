from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form')
    REG_LOGIN = (By.ID, 'id_registration-email')
    REG_PASSWORD1 = (By.ID, 'id_registration-password1')
    REG_PASSWORD2 = (By.ID, 'id_registration-password2')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name^="registration_submit"]')