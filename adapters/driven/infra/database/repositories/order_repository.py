from core.domain.repositories.order_repository import OrderRepository
from core.domain.entities.order import Order
from core.domain.entities.customer import Customer
from core.domain.entities.product import Product
from adapters.driven.infra.database.models.order import DjangoOrder
from adapters.driven.infra.database.models.customer import DjangoCustomer
from adapters.driven.infra.database.models.product import DjangoProduct


class DjangoOrderRepository(OrderRepository):
    
    def save(self, order: Order):
        django_order = DjangoOrder.objects.create(
            customer=DjangoCustomer.objects.get(cpf=order.customer.cpf),
            status=order.status
        )
        for product in order.products:
            django_order.products.add(DjangoProduct.objects.get(name=product.name))
        return django_order

    def list_orders(self):
        django_orders = DjangoOrder.objects.all().order_by('created_at')
        orders = []
        for django_order in django_orders:
            customer = Customer(
                cpf=django_order.customer.cpf,
                name=django_order.customer.name,
                email=django_order.customer.email
            )
            products = [
                Product(name=p.name, category=p.category, price=p.price)
                for p in django_order.products.all()
            ]
            orders.append(Order(customer=customer, products=products, status=django_order.status))
        return orders

    def update(self, order: Order):
        django_order = DjangoOrder.objects.filter(id=order.id).first()
        if django_order:
            django_order.status = order.status
            django_order.save()
            return django_order
        return None

    def find_by_id(self, order_id: int) -> Order:
        django_order = DjangoOrder.objects.filter(id=order_id).first()
        if django_order:
            customer = Customer(
                cpf=django_order.customer.cpf,
                name=django_order.customer.name,
                email=django_order.customer.email
            )
            products = [
                Product(name=p.name, category=p.category, price=p.price)
                for p in django_order.products.all()
            ]
            return Order(customer=customer, products=products, status=django_order.status)
        return None

    def delete(self, order_id: int) -> bool:
        django_order = DjangoOrder.objects.filter(id=order_id).first()
        if django_order:
            django_order.delete()
            return True
        return False
