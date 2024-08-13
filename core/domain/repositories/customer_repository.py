from abc import ABC, abstractmethod
from ..entities.customer import Customer

class CustomerRepository(ABC):
    
    @abstractmethod
    def save(self, customer: Customer):
        pass

    @abstractmethod
    def find_by_cpf(self, cpf: str) -> Customer:
        pass

    @abstractmethod
    def update(self, customer: Customer):
        pass

    @abstractmethod
    def delete(self, cpf: str):
        pass

    @abstractmethod
    def list_all(self) -> list[Customer]:
        pass
