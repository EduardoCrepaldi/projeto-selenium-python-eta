import random
import pytest

class TestDepositAccount:

    @pytest.mark.suite1
    def test_depositAccount(self, account_login):
        account = account_login

        account.click_menu_deposit()
        assert account.validate_label_deposit(), "Não foi selecionado corretamente o Menu de Deposito"
        account.insert_value("400")
        assert account.has_message("Deposit Successful")
        assert account.balance_money_is("400"), "O valor que tem no saldo não é correspondente ao teste"

    def test_multipleDepositAccount(self, account_login):
        account = account_login
        account.click_menu_deposit()
        assert account.validate_label_deposit(), "Não foi selecionado corretamente o Menu de Deposito"
        balance = 0

        for seq in range(5):
            value = random.randint(1, 10)
            balance = balance + value
            print("Valor ===> ", value)
            account.insert_value(value)
            assert account.has_message("Deposit Successful")

        assert account.balance_money_is(str(balance)), ("O valor que tem no saldo " + str(balance) + " não é correspondente ao teste")
