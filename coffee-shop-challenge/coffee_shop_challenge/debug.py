from coffee_shop_challenge import Customer, Coffee, Order

def main():
    john = Customer("John")
    jane = Customer("Jane")
    
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    
    john.create_order(latte, 5.0)
    john.create_order(cappuccino, 6.0)
    jane.create_order(latte, 5.5)
    jane.create_order(latte, 6.0)
    