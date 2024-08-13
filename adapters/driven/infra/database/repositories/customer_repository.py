from core.domain.repositories.customer_repository import CustomerRepository
from core.domain.entities.customer import Customer
from adapters.driven.infra.database.models.customer import DjangoCustomer


class DjangoCustomerRepository(CustomerRepository):
    
    def save(self, customer: Customer):
        django_customer = DjangoCustomer.objects.create(
            cpf=customer.cpf,
            name=customer.name,
            email=customer.email
        )
        return django_customer

    def find_by_cpf(self, cpf: str) -> Customer:
        django_customer = DjangoCustomer.objects.filter(cpf=cpf).first()
        if django_customer:
            return Customer(cpf=django_customer.cpf, name=django_customer.name, email=django_customer.email)
        return None

    def list_all(self) -> list[Customer]:
        django_customers = DjangoCustomer.objects.all()
        customers = [
            Customer(cpf=customer.cpf, name=customer.name, email=customer.email)
            for customer in django_customers
        ]
        return customers

    def update(self, customer: Customer):
        django_customer = DjangoCustomer.objects.filter(cpf=customer.cpf).first()
        if django_customer:
            django_customer.name = customer.name
            django_customer.email = customer.email
            django_customer.save()
            return django_customer
        return None

    def delete(self, cpf: str):
        django_customer = DjangoCustomer.objects.filter(cpf=cpf).first()
        if django_customer:
            django_customer.delete()
            return True
        return False
