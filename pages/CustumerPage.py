from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from pages.ManagerPage import ManagerPage


class CustomerPage(ManagerPage):
    # locators
    input_name = "input[ng-model='fName']"
    input_lastName = "input[ng-model='lName']"
    input_postalCode = "input[ng-model='postCd']"
    btn_submit = "button[type='submit']"
    expected_messageAlert = "Customer added successfully with customer id"
    full_name = ""

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.click_add_customer()
        self.alert = Alert(self.driver)

    def add_customer(self, name="Eduardo", lastName="Cristiane", postalCode="18011321"):
        self.driver.find_element(By.CSS_SELECTOR, self.input_name).send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, self.input_lastName).send_keys(lastName)
        self.driver.find_element(By.CSS_SELECTOR, self.input_postalCode).send_keys(postalCode)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_submit).click()
        try:
            self.full_name = name + " " + lastName
            return self.alert.text.split(':', 1)[1]
        except:
            raise Exception("Customer não foi criado com sucesso!")

    def has_alert_success_message(self):
        alert_text = self.alert.text
        self.close_alert()
        return self.expected_messageAlert in alert_text

    def close_alert(self):
        self.alert.accept()