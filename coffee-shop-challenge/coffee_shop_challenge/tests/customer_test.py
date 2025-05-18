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

def test_customer_name_setter():
    customer = Customer("John")
    customer.name = "Jane"
    assert customer.name == "Jane"
    
    with pytest.raises(TypeError):
        customer.name = 123
    
    with pytest.raises(ValueError):
        customer.name = ""

def test_customer_orders():
    customer = Customer("John")
    coffee = Coffee("Latte")
    order1 = Order(customer, coffee, 5.0)
    order2 = Order(customer, coffee, 6.0)
    
    assert len(customer.orders()) == 2
    assert order1 in customer.orders()
    assert order2 in customer.orders()

def test_customer_coffees():
    customer = Customer("John")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Cappuccino")
    
    Order(customer, coffee1, 5.0)
    Order(customer, coffee2, 6.0)
    Order(customer, coffee1, 5.5)  # Same coffee again
    
    coffees = customer.coffees()
    assert len(coffees) == 2
    assert coffee1 in coffees
    assert coffee2 in coffees

def test_customer_create_order():
    customer = Customer("John")
    coffee = Coffee("Latte")
    
    order = customer.create_order(coffee, 5.0)
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
