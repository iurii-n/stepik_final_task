import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


class TestProductPage:
    
    def test_guest_can_go_to_login_page(self, browser):
        """Тест проверяет, что страница товара
         содержит кнопку добавления в корзину
        """
        # Открываем страницу товара
        browser.get(link)
       
        # Установлено время принудительной задержки браузера
        # после открытия страницы, для визуальной проверки языка открытой страницы
        #time.sleep(30)
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

        # Проверяем наличие кнопки добавления товара в корзину
        #button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket") 
        #assert button, "кнопка не найдена"
