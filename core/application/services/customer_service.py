from core.domain.entities.customer import Customer

class CustomerService:
    def __init__(self, customer_repository):
        self.customer_repository = customer_repository

    def create_customer(self, cpf, name, email):
        customer = Customer(cpf, name, email)
        self.customer_repository.save(customer)
        return customer

    def get_customer_by_cpf(self, cpf):
        return self.customer_repository.find_by_cpf(cpf)

    def update_customer(self, cpf, name, email):
        customer = Customer(cpf, name, email)
        self.customer_repository.update(customer)
        return customer

    def delete_customer(self, cpf):
        return self.customer_repository.delete(cpf)

    def list_customers(self):
        return self.customer_repository.list_all()
