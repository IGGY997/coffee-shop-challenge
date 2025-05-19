from order import all_orders

class Coffee:
    # ... (previous code)

    def orders(self):
        return [order for order in all_orders if order.coffee == self]

    def customers(self):
        customers_set = {order.customer for order in self.orders()}
        return list(customers_set)

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)

#class customer:
class Customer:
    def __init__(self, name):
        self._name = None  # private attribute
        self.name = name   # call setter to validate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1-15 characters long")
        self._name = value

from order import Order, all_orders  # We'll create all_orders list in order.py

class Customer:
    # ... (previous code)
    
    def orders(self):
        # return list of Orders belonging to this customer
        return [order for order in all_orders if order.customer == self]

    def coffees(self):
        # return unique list of Coffees ordered by this customer
        coffees_set = {order.coffee for order in self.orders()}
        return list(coffees_set)

    def create_order(self, coffee, price):
        # create new Order linking this customer and the coffee
        order = Order(self, coffee, price)
        all_orders.append(order)
        return order


#class oder:
class Customer:
    def __init__(self, name):
        self._name = None  # private attribute
        self.name = name   # call setter to validate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1-15 characters long")
        self._name = value

from order import Order, all_orders  # We'll create all_orders list in order.py

class Customer:
    # ... (previous code)
    
    def orders(self):
        # return list of Orders belonging to this customer
        return [order for order in all_orders if order.customer == self]

    def coffees(self):
        # return unique list of Coffees ordered by this customer
        coffees_set = {order.coffee for order in self.orders()}
        return list(coffees_set)

    def create_order(self, coffee, price):
        # create new Order linking this customer and the coffee
        order = Order(self, coffee, price)
        all_orders.append(order)
        return order



class Customer:
    def __init__(self, name):
        self._name = None  # private attribute
        self.name = name   # call setter to validate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1-15 characters long")
        self._name = value

from order import Order, all_orders  # We'll create all_orders list in order.py

class Customer:
    # ... (previous code)
    
    def orders(self):
        # return list of Orders belonging to this customer
        return [order for order in all_orders if order.customer == self]

    def coffees(self):
        # return unique list of Coffees ordered by this customer
        coffees_set = {order.coffee for order in self.orders()}
        return list(coffees_set)

    def create_order(self, coffee, price):
        # create new Order linking this customer and the coffee
        order = Order(self, coffee, price)
        all_orders.append(order)
        return order
