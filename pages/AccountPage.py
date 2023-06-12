from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class AccountPage(PageObject):
    text_name = "span[class='fontBig ng-binding']"
    select_number_account = "accountSelect"
    btn_menu_deposit = "button[ng-click='deposit()']"
    btn_menu_withdraw = "button[ng-click='withdrawl()']"
    btn_menu_transaction = "button[ng-click='transactions()']"
    details_account = "strong[class='ng-binding']"
    input_value = "input[ng-model='amount']"
    btn_submit = "button[type='submit']"
    message_text = "span[ng-show='message']"
    label_validate = "div > label"
    message_deposit = "Amount to be Deposited :"
    message_withdraw = "Amount to be Withdrawn :"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_menu_deposit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_menu_deposit).click()

    def click_menu_withdraw(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_menu_withdraw).click()

    def click_menu_transaction(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_menu_transaction).click()

    def number_account_is(self, number_account):
        return self.driver.find_elements(By.CSS_SELECTOR, self.details_account)[0].text == str(number_account)

    def balance_money_is(self, money):
        return self.driver.find_elements(By.CSS_SELECTOR, self.details_account)[1].text == str(money)

    def currency_is(self, currency):
        return self.driver.find_elements(By.CSS_SELECTOR, self.details_account)[2].text == str(currency)

    def has_text_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.text_name).text

    def insert_value(self, value):
        self.driver.find_element(By.CSS_SELECTOR, self.input_value).send_keys(value)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_submit).click()

    def has_message(self, message):
        return self.driver.find_element(By.CSS_SELECTOR, self.message_text).text == message

    def validate_label_deposit(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.label_validate).text == self.message_deposit

    def validate_label_withdraw(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.label_validate).text == self.message_withdraw

    def select_account(self, number_account):
        select = Select(self.driver.find_element(By.NAME, self.select_number_account))
        select.select_by_visible_text(number_account)