from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class ManagerPage(PageObject):
    btn_add_customer = "[ng-click='addCust()']"
    btn_open_account = "[ng-click='openAccount()']"
    btn_customers = "[ng-click='showCust()']"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_add_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_add_customer).click()

    def click_open_account(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_open_account).click()

    def click_customers(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_customers).click()