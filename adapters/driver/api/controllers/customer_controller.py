from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.application.services.customer_service import CustomerService
from adapters.driven.infra.database.repositories.customer_repository import DjangoCustomerRepository
from adapters.driver.api.serializers.customer_serializer import CustomerSerializer

class CustomerController(APIView):
    serializer_class = CustomerSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.customer_service = CustomerService(DjangoCustomerRepository())

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            customer = self.customer_service.create_customer(
                cpf=serializer.validated_data['cpf'],
                name=serializer.validated_data['name'],
                email=serializer.validated_data['email']
            )
            return Response(
                {"cpf": customer.cpf, "name": customer.name, "email": customer.email}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, cpf=None):
        if cpf:
            customer = self.customer_service.get_customer_by_cpf(cpf)
            if customer:
                return Response(
                    {"cpf": customer.cpf, "name": customer.name, "email": customer.email}, 
                    status=status.HTTP_200_OK
                )
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            customers = self.customer_service.list_customers()
            serializer = self.serializer_class(customers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
