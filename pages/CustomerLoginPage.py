from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class CustomerLoginPage(PageObject):
    # locators
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
    id_userSelect = 'userSelect'
    btn_login = "button[type='submit']"


    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver.get(self.url)

    def select_customer(self, nameComplete):
        sleep(1)
        select = Select(self.driver.find_element(By.ID, self.id_userSelect))
        select.select_by_visible_text(nameComplete)
        sleep(1)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_login).click()

    def login_account(self, name_complete):
        self.select_customer(name_complete)
        self.click_login()