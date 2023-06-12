from time import sleep

import pytest


class TestWithDrawAccount:

    account = None
    value_account = 300

    @pytest.fixture(autouse=True)
    def setup_method_fixture(self, account_login):
        self.account = account_login
        self.account.click_menu_deposit()
        self.account.insert_value(self.value_account)
        self.account.click_menu_withdraw()

    @pytest.mark.suite1
    def test_withdraw_with_success(self):
        withdraw = 35
        balance = self.value_account - withdraw
        sleep(1)
        assert self.account.validate_label_withdraw(), "Não foi selecionado corretamente o Menu de WithDraw"
        self.account.insert_value(withdraw)
        assert self.account.has_message("Transaction successful")
        assert self.account.balance_money_is(balance), "O valor que tem no saldo não é correspondente"

    def test_withdraw_with_balance_insufficient(self):
        sleep(1)
        assert self.account.validate_label_withdraw(), "Não foi selecionado corretamente o Menu de WithDraw"
        withdraw = 500
        self.account.insert_value(withdraw)
        assert self.account.has_message("Transaction Failed. You can not withdraw amount more than the balance.")
        assert self.account.balance_money_is(self.value_account), "O valor que tem no saldo não é correspondente"
