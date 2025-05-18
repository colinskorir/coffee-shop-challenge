import pytest
from coffee_shop_challenge.customer import Customer
from coffee_shop_challenge.coffee import Coffee
from coffee_shop_challenge.order import Order

def test_customer_init():
    customer = Customer("John")
    assert customer.name == "John"

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    
    with pytest.raises(ValueError):
        Customer("")
    
    with pytest.raises(ValueError):
        Customer("ThisNameIsTooLongForACustomer")
