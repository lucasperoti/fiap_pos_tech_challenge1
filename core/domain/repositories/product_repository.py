from abc import ABC, abstractmethod
from ..entities.product import Product

class ProductRepository(ABC):

    @abstractmethod
    def save(self, product: Product):
        pass

    @abstractmethod
    def find_by_category(self, category: str):
        pass

    @abstractmethod
    def update(self, product: Product):
        pass

    @abstractmethod
    def delete(self, name: str):
        pass