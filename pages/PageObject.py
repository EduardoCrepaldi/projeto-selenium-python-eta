from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:

    class_title = 'title'

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            else:
                raise Exception('Browser não supportado!!')
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def is_page(self, url, title):
        is_url = self.driver.current_url == url
        is_title = self.driver.find_element(By.CLASS_NAME, self.class_title).text == title
        return is_url and is_title



