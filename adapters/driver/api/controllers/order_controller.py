from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.application.services.order_service import OrderService
from adapters.driven.infra.database.repositories.order_repository import DjangoOrderRepository
from adapters.driven.infra.database.repositories.customer_repository import DjangoCustomerRepository
from adapters.driven.infra.database.repositories.product_repository import DjangoProductRepository
from adapters.driver.api.serializers.order_serializer import OrderSerializer

class OrderController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.order_service = OrderService(
            DjangoOrderRepository(),
            DjangoCustomerRepository(),
            DjangoProductRepository()
        )

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = self.order_service.create_order(
                customer_cpf=serializer.validated_data['customer']['cpf'],
                product_names=[p['name'] for p in serializer.validated_data['products']]
            )
            return Response({"message": "Order created", "order_id": order.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        orders = self.order_service.list_orders()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, order_id):
        new_status = request.data.get('status')
        if new_status:
            order = self.order_service.update_order_status(order_id, new_status)
            if order:
                return Response({"message": "Order status updated", "order_id": order.id}, status=status.HTTP_200_OK)
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)