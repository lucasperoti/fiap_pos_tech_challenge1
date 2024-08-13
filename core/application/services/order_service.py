from core.domain.entities.order import Order

class OrderService:
    def __init__(self, order_repository, customer_repository, product_repository):
        self.order_repository = order_repository
        self.customer_repository = customer_repository
        self.product_repository = product_repository

    def create_order(self, customer_cpf, product_names):
        customer = self.customer_repository.find_by_cpf(customer_cpf)
        products = [self.product_repository.find_by_name(name) for name in product_names]
        order = Order(customer, products, status='RECEIVED')
        self.order_repository.save(order)
        return order

    def list_orders(self):
        return self.order_repository.list_orders()

    def update_order_status(self, order_id, new_status):
        order = self.order_repository.find_by_id(order_id)
        if order:
            order.status = new_status
            self.order_repository.update(order)
            return order
        return None