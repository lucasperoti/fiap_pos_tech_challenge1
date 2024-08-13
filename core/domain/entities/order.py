class Order:
    def __init__(self, customer, products, status='RECEIVED'):
        self.customer = customer
        self.products = products
        self.status = status
