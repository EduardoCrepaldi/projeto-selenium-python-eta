
import pytest

from pages.AccountPage import AccountPage
from pages.CustomerLoginPage import CustomerLoginPage
from pages.CustumerPage import CustomerPage
from pages.LoginPage import LoginPage
from pages.OpenAccountPage import OpenAccountPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox", help="Set browser")


@pytest.fixture()
def choose_browser(request):
    selected_browser = request.config.getoption("--browser").lower()
    yield selected_browser


@pytest.fixture()
def open_login(choose_browser):
    print('open page Bank Manager Login')
    login_page = LoginPage(browser=choose_browser)
    yield login_page
    print('Close Browser')
    login_page.close()


@pytest.fixture()
def create_customer(open_login):
    print('open-addCustomer')
    open_login.click_bank_manager()
    customer = CustomerPage(open_login.driver)
    yield customer


@pytest.fixture()
def create_account_customer(create_customer):
    print('Create customer')
    id_customer = create_customer.add_customer(name='Eduardo', lastName='Crepaldi', postalCode='12345678')
    create_customer.close_alert()
    print('open-account')
    account = OpenAccountPage(driver=create_customer.driver, full_name=create_customer.full_name)
    yield id_customer, account


@pytest.fixture()
def create_account_customer_complete(create_account_customer):
    id_customer, account = create_account_customer
    print('create-account')
    account.create_account("Dollar")
    account.close_alert()
    yield id_customer, account


@pytest.fixture()
def account_login(create_account_customer_complete):
    id_customer, account = create_account_customer_complete
    loginAccount = CustomerLoginPage(account.driver)
    loginAccount.login_account(account.full_name)
    account = AccountPage(account.driver)
    yield account
