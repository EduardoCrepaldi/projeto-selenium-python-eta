import pytest

from pages.CustomersListPage import CustomersListPage


class TestCreateAccount:

    @pytest.mark.suite1
    @pytest.mark.parametrize("currency", ["Dollar", "Pound", "Rupee"])
    def test_create_account(self, currency, create_account_customer):
        id_customer, account = create_account_customer
        account.create_account(currency=currency)

        assert account.has_alert_success_message()

        # Validate customer in page list
        customersListPage = CustomersListPage(account.driver)
        customersListPage.search_customer(account.numberAccount)
        assert customersListPage.validateNumberAccountOnTable(account.numberAccount)
