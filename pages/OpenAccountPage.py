
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.ManagerPage import ManagerPage


class OpenAccountPage(ManagerPage):

    userSelect = 'userSelect'
    currency = 'currency'
    btn_submit = "button[type='submit']"
    expected_messageAlert = "Account created successfully with account Number :"

    def __init__(self, driver, full_name):
        super().__init__(driver=driver)
        self.click_open_account()
        self.alert = Alert(self.driver)
        self.full_name = full_name
        self.numberAccount = 0

    def create_account(self, currency):
        self.select_customer(self.full_name)
        self.select_currency(currency)
        self.click_submit()

        try:
            self.numberAccount = self.alert.text.split(':', 1)[1]
        except:
            raise Exception("Account não foi criado com sucesso para ", self.full_name)


    def select_customer(self, nameComplete):
        select = Select(self.driver.find_element(By.ID, self.userSelect))
        select.select_by_visible_text(nameComplete)

    def select_currency(self, currency):
        select = Select(self.driver.find_element(By.ID, self.currency))
        select.select_by_visible_text(currency)

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_submit).click()

    def has_alert_success_message(self):
        alert_text = self.alert.text
        self.close_alert()
        return self.expected_messageAlert in alert_text

    def close_alert(self):
        self.alert.accept()