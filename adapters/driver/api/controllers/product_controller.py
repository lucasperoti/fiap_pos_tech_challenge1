from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.application.services.product_service import ProductService
from adapters.driven.infra.database.repositories.product_repository import DjangoProductRepository
from adapters.driver.api.serializers.product_serializer import ProductSerializer

class ProductController(APIView):
    serializer_class = ProductSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_service = ProductService(DjangoProductRepository())

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = self.product_service.create_product(
                name=serializer.validated_data['name'],
                category=serializer.validated_data['category'],
                price=serializer.validated_data['price']
            )
            return Response({"name": product.name, "category": product.category, "price": product.price}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, category=None, name=None):
        if category:
            products = self.product_service.get_products_by_category(category)
        elif name:
            product = self.product_service.get_product_by_name(name)
            if product:
                serializer = self.serializer_class(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            products = self.product_service.get_all_products()

        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, name):
        product = self.product_service.get_product_by_name(name)
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            updated_product = self.product_service.update_product(
                name=serializer.validated_data['name'],
                category=serializer.validated_data['category'],
                price=serializer.validated_data['price']
            )
            return Response({"name": updated_product.name, "category": updated_product.category, "price": updated_product.price}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name=None):
        if not name:
            return Response({"error": "Product name is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        product = self.product_service.get_product_by_name(name)
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        self.product_service.delete_product(name)
        return Response(status=status.HTTP_204_NO_CONTENT)
