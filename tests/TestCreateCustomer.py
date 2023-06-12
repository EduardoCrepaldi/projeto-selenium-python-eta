
import pytest

from pages.CustomersListPage import CustomersListPage


class TestCreateCustomer:

    @pytest.mark.suite1
    def test_create_customer(self, create_customer):
        name = "Eduardo"
        lastName = "Crepaldi"
        postalCode = "1234567"
        customer = create_customer
        customer.add_customer(name, lastName, postalCode)
        assert customer.has_alert_success_message()

        # Validate customer in page list
        customersListPage = CustomersListPage(customer.driver)
        customersListPage.search_customer(name)
        assert customersListPage.validateDataCustomerPrimaryLine(name, lastName, postalCode)
