import pytest

from pages.CustomersListPage import CustomersListPage

class TestDeleteCustomerAccount:

    @pytest.mark.suite1
    def test_delete_account_customer(self, create_account_customer_complete):
        id_customer, account = create_account_customer_complete
        # Validate customer in page list and delete
        customersListPage = CustomersListPage(account.driver)
        customersListPage.search_customer(account.numberAccount)
        assert customersListPage.validateNumberAccountOnTable(account.numberAccount)
        customersListPage.deleteCustomer(account.numberAccount)
        assert customersListPage.validateTableIsEmpty()

