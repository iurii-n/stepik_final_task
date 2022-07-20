class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self): 
        #метод открывающий нужную страницу в браузере
        self.browser.get(self.url)