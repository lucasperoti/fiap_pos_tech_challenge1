from abc import ABC, abstractmethod
from ..entities.order import Order

class OrderRepository(ABC):

    @abstractmethod
    def save(self, order: Order):
        pass

    @abstractmethod
    def list_orders(self):
        pass

    @abstractmethod
    def update(self, order: Order):
        pass

    @abstractmethod
    def delete(self, order_id: int):
        pass