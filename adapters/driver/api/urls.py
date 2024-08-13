from django.urls import path
from .controllers.customer_controller import CustomerController
from .controllers.product_controller import ProductController
from .controllers.order_controller import OrderController

urlpatterns = [
    path('customers/', CustomerController.as_view(), name='customer-create-list'),  # GET para listar todos e POST para criar um novo
    path('customers/<str:cpf>/', CustomerController.as_view(), name='customer-detail'),  # GET para recuperar detalhes, PATCH para atualizar, DELETE para remover
    path('products/', ProductController.as_view(), name='product-create-list'),
    path('products/<str:category>/', ProductController.as_view(), name='product-category'),
    path('products/name/<str:name>/', ProductController.as_view(), name='product-name'),
    path('products/name/<str:name>/', ProductController.as_view(), name='product-delete'),
    path('orders/', OrderController.as_view(), name='order-create-list'),
    path('orders/<int:order_id>/', OrderController.as_view(), name='order-update-status'),
]
