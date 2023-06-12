
import pytest

from pages.AccountPage import AccountPage
from pages.CustomerLoginPage import CustomerLoginPage


def data_account_is_validate(account_bank, number_account, balance, currency):
    account_bank.select_account(number_account)
    return account_bank.number_account_is(number_account) \
        and account_bank.balance_money_is(balance) \
        and account_bank.currency_is(currency)


def create_account(account, currency):
    account.create_account(currency)
    account.close_alert()
    return account.numberAccount


def insert_balance_deposit(account_bank, number_account, value_deposit):
    account_bank.select_account(str(number_account))
    account_bank.click_menu_deposit()
    account_bank.insert_value(value_deposit)


class TestMoveAccountsCustomer:

    @pytest.mark.suite1
    def test_multiple_account_customer(self, create_account_customer):
        id_customer, account = create_account_customer
        balance_pound = 300
        balance_dollar = 100

        # Create Account = Dollar
        id_account_dollar = create_account(account, "Dollar")
        # Create Account = Pound
        id_account_pound = create_account(account, "Pound")

        loginAccount = CustomerLoginPage(account.driver)
        loginAccount.login_account(account.full_name)
        account_bank = AccountPage(account.driver)

        # Insert balance in Account = Pound
        insert_balance_deposit(account_bank, id_account_pound, balance_pound)
        # Insert balance in Account = Dollar
        insert_balance_deposit(account_bank, id_account_dollar, balance_dollar)

        # Validate Accounts Balance Pound and Dollar
        assert data_account_is_validate(account_bank, id_account_pound, balance_pound, "Pound")
        assert data_account_is_validate(account_bank, id_account_dollar, balance_dollar, "Dollar")
