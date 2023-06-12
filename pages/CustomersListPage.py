from time import sleep

from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CustomersListPage(PageObject):

    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    input_searchcustomer = "input[ng-model='searchCustomer']"
    all_elementsSearchPrimaryLine = "td.ng-binding"
    btn_deleteUserPrimaryLine = "td > button"
    tbody_tr = 'tbody > tr'

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver.get(self.url)

    def search_customer(self, value):
        self.driver.find_element(By.CSS_SELECTOR, self.input_searchcustomer).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.input_searchcustomer).send_keys(value)

    def validateDataCustomerPrimaryLine(self, name, lastName, postalCode):
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.all_elementsSearchPrimaryLine)
        return elements[0].text == name and elements[1].text == lastName and elements[2].text == postalCode

    def validateNumberAccountOnTable(self, numberAccount):
        xpath = "//span[text()='" + numberAccount + " ']"
        return self.driver.find_element(By.XPATH, xpath).is_displayed()

    def validateTableIsEmpty(self):
        isEmpty = self.driver.find_elements(By.CSS_SELECTOR, self.tbody_tr)
        return len(isEmpty) == 0

    def deleteCustomer(self, value):
        self.search_customer(value)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_deleteUserPrimaryLine).click()