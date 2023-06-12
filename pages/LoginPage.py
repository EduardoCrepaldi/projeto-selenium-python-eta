from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    btn_home = "[ng-click='home()']"
    btn_customer_login = "[ng-click='customer()']"
    btn_bank_manager = "[ng-click='manager()']"

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.driver.get(self.url)

    def click_home(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_home).click()

    def click_customer_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_customer_login).click()

    def click_bank_manager(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_bank_manager).click()