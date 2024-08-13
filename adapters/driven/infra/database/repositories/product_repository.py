from core.domain.entities.product import Product
from core.domain.repositories.product_repository import ProductRepository
from adapters.driven.infra.database.models.product import DjangoProduct as ProductModel


class DjangoProductRepository(ProductRepository):
    def save(self, product: Product) -> None:
        product_model = ProductModel(name=product.name, category=product.category, price=product.price)
        product_model.save()

    def find_by_category(self, category: str) -> list[Product]:
        products = ProductModel.objects.filter(category=category)
        return [Product(name=p.name, category=p.category, price=p.price) for p in products]

    def find_by_name(self, name: str) -> Product:
        try:
            product = ProductModel.objects.get(name=name)
            return Product(name=product.name, category=product.category, price=product.price)
        except ProductModel.DoesNotExist:
            return None

    def find_all(self) -> list[Product]:
        products = ProductModel.objects.all()
        return [Product(name=p.name, category=p.category, price=p.price) for p in products]

    def update(self, product: Product) -> None:
        product_model = ProductModel.objects.get(name=product.name)
        product_model.category = product.category
        product_model.price = product.price
        product_model.save()

    def delete(self, name: str) -> None:
        ProductModel.objects.filter(name=name).delete()

    def find_all(self):
        return ProductModel.objects.all()