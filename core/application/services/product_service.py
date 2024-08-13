from core.domain.entities.product import Product

class ProductService:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def create_product(self, name, category, price):
        product = Product(name, category, price)
        self.product_repository.save(product)
        return product

    def get_products_by_category(self, category):
        return self.product_repository.find_by_category(category)

    def get_product_by_name(self, name):
        return self.product_repository.find_by_name(name)

    def update_product(self, name, category, price):
        product = Product(name, category, price)
        self.product_repository.update(product)
        return product

    def delete_product(self, name):
        return self.product_repository.delete(name)
    
    def get_all_products(self):
        return self.product_repository.find_all()